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

def create_github_issue(title, body):
    """Create a new GitHub issue."""
    output = run_command(["gh", "issue", "create", "--title", title, "--body", body])
    if output:
        print(f"Created issue: {output}")
        return output
    return None

def parse_prd(filepath):
    """Parse the local prd.md for task items."""
    if not os.path.exists(filepath):
        print(f"PRD file not found: {filepath}")
        return []
    
    tasks = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        # Match markdown checkboxes: - [ ] Task Title OR - [x] Task Title
        match = re.match(r'^\s*-\s*\[([ xX])\]\s*(.*)', line)
        if match:
            status = match.group(1).lower() == 'x'
            title = match.group(2).split('(')[0].strip() # Strip existing links/IDs
            tasks.append({"title": title, "completed": status, "raw": line.strip()})
            
    return tasks

def sync_prd_to_github(prd_path):
    """Sync local PRD tasks to GitHub issues."""
    local_tasks = parse_prd(prd_path)
    github_issues = get_github_issues()
    
    gh_titles = {issue['title'] for issue in github_issues}
    
    for task in local_tasks:
        if not task['completed'] and task['title'] not in gh_titles:
            print(f"Syncing new task to GitHub: {task['title']}")
            create_github_issue(task['title'], "Created automatically by Ralph-Antigravity-Git-Issues")

if __name__ == "__main__":
    # Example usage
    PRD_PATH = "prd.md"
    if len(sys.argv) > 1:
        PRD_PATH = sys.argv[1]
        
    sync_prd_to_github(PRD_PATH)
