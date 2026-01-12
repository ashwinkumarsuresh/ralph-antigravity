import subprocess
import json
import re
import sys
import os

def run_command(command):
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command {' '.join(command)}: {e.stderr}", file=sys.stderr)
        return None

def get_github_issues():
    """Fetch all open issues from the current repository."""
    output = run_command(["gh", "issue", "list", "--json", "number,title,url,body,labels"])
    if output:
        return json.loads(output)
    return []

def ensure_label_exists(name, color="EDEDED"):
    """Check if a label exists, and create it if not."""
    labels = run_command(["gh", "label", "list", "--json", "name"])
    if labels:
        label_names = [l['name'] for l in json.loads(labels)]
        if name in label_names:
            return True
    
    print(f"Creating label: {name}")
    run_command(["gh", "label", "create", name, "--color", color])
    return True

def create_github_issue(title, body, labels=None):
    """Create a new GitHub issue."""
    cmd = ["gh", "issue", "create", "--title", title, "--body", body]
    if labels:
        for label in labels:
            ensure_label_exists(label)
        cmd.extend(["--label", ",".join(labels)])
        
    output = run_command(cmd)
    if output:
        print(f"Created issue: {output}")
        return output
    return None

def parse_prd(filepath):
    """Parse the local prd.md for detailed US blocks."""
    if not os.path.exists(filepath):
        print(f"PRD file not found: {filepath}")
        return []
    
    with open(filepath, 'r') as f:
        content = f.read()

    # Split by User Story markers
    story_blocks = re.split(r'\n### (US-\d+:.*)', content)
    
    tasks = []
    # story_blocks[0] is everything before the first ### US
    for i in range(1, len(story_blocks), 2):
        header = story_blocks[i]
        body = story_blocks[i+1] if i+1 < len(story_blocks) else ""
        
        # Parse Header (ID and Title)
        header_match = re.match(r'(US-\d+):\s*(.*)', header)
        us_id = header_match.group(1) if header_match else "US-UNKNOWN"
        title = header_match.group(2).strip() if header_match else header.strip()
        
        # Clean title from dependencies for comparison
        clean_title = title.split('(')[0].strip()
        
        # Parse Description
        desc_match = re.search(r'\*\*Description:\*\*\s*(.*)', body)
        description = desc_match.group(1).strip() if desc_match else ""
        
        # Parse Acceptance Criteria
        ac_section = re.split(r'\*\*Acceptance Criteria:\*\*', body)
        ac_text = ac_section[1] if len(ac_section) > 1 else ""
        
        # Find all checkboxes in the AC
        # - [ ] or - [x]
        ac_items = re.findall(r'^\s*-\s*\[([ xX])\]\s*(.*)', ac_text, re.MULTILINE)
        
        # A task is completed ONLY if all its ACs are checked
        completed = all(status.lower() == 'x' for status, text in ac_items) if ac_items else False
        
        # Detect dependencies
        dep_match = re.search(r'\(requires\s*#(\d+)\)', title)
        dependency = dep_match.group(1) if dep_match else None
        
        # Detect UI flag
        is_ui = "ui-verification" in body.lower() or "verify in browser" in body.lower()
        
        tasks.append({
            "id": us_id,
            "title": f"[{us_id}] {clean_title}",
            "full_title": title,
            "description": description,
            "ac_items": ac_items,
            "completed": completed,
            "dependency": dependency,
            "is_ui": is_ui,
            "raw_body": body.strip()
        })
            
    return tasks

def sync_prd_to_github(root_dir="."):
    """Recursively find all PRDs and sync them to GitHub."""
    import glob
    
    # Find all prd.md files recursively, excluding top-level or specific patterns if needed
    prd_files = glob.glob(os.path.join(root_dir, "**/prd.md"), recursive=True)
    
    if not prd_files:
        print("No prd.md files found.")
        return

    github_issues = get_github_issues()
    gh_titles = {issue['title'] for issue in github_issues}
    
    for prd_path in prd_files:
        print(f"--- Syncing {prd_path} ---")
        rel_path = os.path.relpath(prd_path, root_dir)
        path_parts = os.path.dirname(rel_path).split(os.sep)
        
        # Generate labels from all parent directories (Vertical Slicing)
        labels = ["aura-autonomous"]
        ignore_names = ["apps", "features", "src", "packages", "prd.md", "."]
        
        for part in path_parts:
            if part and part not in ignore_names:
                # Detect if it's a scope (first level after apps) or a feature
                if "apps" in path_parts and path_parts.index(part) > path_parts.index("apps"):
                    # If it's the first thing after apps, it's a scope
                    if path_parts.index(part) == path_parts.index("apps") + 1:
                        labels.append(f"scope:{part}")
                    else:
                        labels.append(f"feature:{part}")
                else:
                    labels.append(f"scope:{part}")
            
        local_tasks = parse_prd(prd_path)
        
        for task in local_tasks:
            if not task['completed'] and task['title'] not in gh_titles:
                print(f"Syncing new task to GitHub: {task['title']}")
                
                body = f"## {task['title']}\n"
                body += f"**Description:** {task['description']}\n\n"
                body += "**Acceptance Criteria:**\n"
                for status, ac_text in task['ac_items']:
                    checkbox = "[ ]" if status.lower() != 'x' else "[x]"
                    body += f"- {checkbox} {ac_text}\n"
                
                body += f"\n---\nCreated automatically by Aura-Antigravity\nSource: `{rel_path}`"
                
                if task['dependency']:
                    body += f"\n\n**Dependency:** Requires #{task['dependency']}"
                
                task_labels = list(set(labels)) # Unique labels
                if task['is_ui']:
                    task_labels.append("ui-verification")
                    
                create_github_issue(task['title'], body, task_labels)

if __name__ == "__main__":
    # Example usage
    ROOT_DIR = "."
    if len(sys.argv) > 1:
        ROOT_DIR = sys.argv[1]
        
    sync_prd_to_github(ROOT_DIR)
