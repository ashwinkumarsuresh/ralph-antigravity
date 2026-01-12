import json
import subprocess
import sys
import os
import argparse
import re
from github_sync import get_github_issues, run_command

class AuraController:
    def __init__(self, project_dir="."):
        self.project_dir = os.path.abspath(project_dir)
        self.status_file = os.path.join(self.project_dir, "aura_status.json")
        self.load_status()

    def gather_context_anchors(self, start_dir):
        """Recursively collect ARCH.md and LEARNINGS.md from start_dir up to root."""
        anchors = []
        current = os.path.abspath(start_dir)
        
        while True:
            for name in ["ARCH.md", "LEARNINGS.md", "README.md"]:
                p = os.path.join(current, name)
                if os.path.exists(p):
                    anchors.append(p)
            
            if current == self.project_dir or current == "/":
                break
            current = os.path.dirname(current)
            
        return list(reversed(anchors)) # Root-first order

    def discovery_scan(self, task_title, search_dir=None):
        """Heuristic scan to identify relevant files for a task."""
        root = search_dir or self.project_dir
        print(f"--- Discovery Scan: '{task_title}' ---")
        
        # Simple keywords extraction
        keywords = re.findall(r'\w+', task_title.lower())
        relevant_files = []
        
        for dirpath, _, filenames in os.walk(root):
            # Skip hidden and node_modules
            if ".git" in dirpath or "node_modules" in dirpath:
                continue
                
            for f in filenames:
                full_p = os.path.join(dirpath, f)
                if any(kw in full_p.lower() for kw in keywords):
                    relevant_files.append(full_p)
        
        return relevant_files[:10] # Cap at 10 for focus

    def load_status(self):
        """Load internal state from aura_status.json."""
        if os.path.exists(self.status_file):
            with open(self.status_file, 'r') as f:
                self.state = json.load(f)
        else:
            self.state = {"iterations": 0, "current_task": None, "task_attempts": {}}

    def save_status(self):
        """Save internal state to aura_status.json."""
        with open(self.status_file, 'w') as f:
            json.dump(self.state, f, indent=2)

    def get_next_task(self, scope=None, milestone=None):
        """Fetch the next task from GitHub Issues with filtering."""
        issues = get_github_issues()
        if not issues:
            return None
        
        # Filter by Scope (Label)
        if scope:
            label_name = f"scope:{scope}" if not scope.startswith("scope:") else scope
            issues = [i for i in issues if any(l['name'] == label_name for l in i.get('labels', []))]
            
        # Filter by Milestone
        if milestone:
            issues = [i for i in issues if i.get('milestone') and i['milestone'].get('title') == milestone]

        if not issues:
            return None

        # Sort by number to maintain priority
        issues.sort(key=lambda x: x['number'])
        
        # Dependency & Failure Check
        for issue in issues:
            task_id = str(issue['number'])
            
            # Skip if failed 5 times
            if self.state.get("task_attempts", {}).get(task_id, 0) >= 5:
                print(f"Skipping Task #{task_id}: Maximum attempts reached.")
                continue

            body = issue.get('body', '')
            dep_match = re.search(r'Requires\s*#(\d+)', body)
            if dep_match:
                dep_id = dep_match.group(1)
                dep_status = run_command(["gh", "issue", "view", dep_id, "--json", "state"])
                if dep_status:
                    state = json.loads(dep_status).get('state')
                    if state == "OPEN":
                        print(f"Skipping Task #{issue['number']}: Blocked by #{dep_id}")
                        continue
            
            return issue # Return the first non-blocked, non-failed issue
            
        return None

    def start_iteration(self, scope=None, milestone=None):
        """Prepare for the next iteration with optional scope/milestone."""
        task = self.get_next_task(scope, milestone)
        if not task:
            print("No more tasks found matching criteria. Workflow Idle.")
            return None
        
        task_id = str(task["number"])
        attempts = self.state.get("task_attempts", {}).get(task_id, 0)
        
        if attempts >= 5:
            print(f"!!! Task #{task_id} has failed 5 times. Marking as blocked.")
            # Ensure label exists (import if needed or use gh directly)
            run_command(["gh", "label", "create", "aura-blocked", "--color", "ff0000"]) 
            run_command(["gh", "issue", "edit", task_id, "--add-label", "aura-blocked"])
            run_command(["gh", "issue", "comment", task_id, "--body", "### ❌ Autonomous Failure\nAura has attempted this task 5 times and failed to verify. Manual review required."])
            return self.start_iteration(scope, milestone) # Now get_next_task will skip it

        # Create task-specific branch
        clean_title = re.sub(r'[^a-zA-Z0-9-]', '-', task["title"].lower())[:30]
        branch_name = f"aura/issue-{task_id}-{clean_title}"
        print(f"Creating/Switching to branch: {branch_name}")
        run_command(["git", "checkout", "-b", branch_name])
        
        self.state["current_task"] = {
            "id": task_id,
            "title": task["title"],
            "url": task["url"],
            "branch": branch_name
        }
        self.state["iterations"] += 1
        self.state.setdefault("task_attempts", {})[task_id] = attempts + 1
        self.save_status()
        
        print(f"--- Iteration {self.state['iterations']} (Attempt {attempts + 1}/5) ---")
        print(f"Active Task: #{task['number']} - {task['title']}")
        return task

    def report_failure(self, task_id):
        """Manually trigger an attempt increment if a task fails without finishing."""
        self.load_status()
        tid = str(task_id)
        self.state.setdefault("task_attempts", {})[tid] = self.state.get("task_attempts", {}).get(tid, 0) + 1
        self.save_status()
        print(f"Failure recorded for Task #{tid}. Attempt count: {self.state['task_attempts'][tid]}")

    def finish_task(self, summary=None):
        """Close the task on GitHub and update state using walkthrough artifact."""
        if not self.state["current_task"]:
            print("No active task to finish.")
            return

        self.load_status() # Ensure we have latest attempts
        task_id = self.state["current_task"]["id"]
        branch_name = self.state["current_task"].get("branch", "main")
        
        # 1. Prefer walkthrough.md for the summary
        walkthrough_path = os.path.join(self.project_dir, "walkthrough.md")
        if os.path.exists(walkthrough_path):
            with open(walkthrough_path, 'r') as f:
                walkthrough_content = f.read()
            full_comment = f"### ✅ Task Complete (via Antigravity Walkthrough)\n\n{walkthrough_content}\n"
        elif summary:
            full_comment = f"### ✅ Task Complete\n\n**Summary:** {summary}\n"
        else:
            print("Error: No walkthrough.md found and no summary provided.")
            return

        # 2. Post final summary as comment
        run_command(["gh", "issue", "comment", str(task_id), "--body", full_comment])
        
        # 3. Close issue
        run_command(["gh", "issue", "close", str(task_id)])
        
        print(f"Task #{task_id} closed on GitHub.")
        
        # 4. Git Push Branch
        print(f"Pushing branch {branch_name} to remote...")
        run_command(["git", "push", "origin", branch_name])

        # 5. Cleanup local state
        self.state["current_task"] = None
        # Reset attempts on success
        if str(task_id) in self.state.get("task_attempts", {}):
            del self.state["task_attempts"][str(task_id)]
        self.save_status()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aura-Antigravity Controller")
    parser.add_argument("command", choices=["next", "finish", "verify-ui", "discover", "fail"])
    parser.add_argument("summary", nargs="?", help="Summary for finish command")
    parser.add_argument("--scope", help="Filter by project scope (label)")
    parser.add_argument("--milestone", help="Filter by GitHub milestone")
    
    args = parser.parse_args()
    
    controller = AuraController()
    
    if args.command == "next":
        controller.start_iteration(scope=args.scope, milestone=args.milestone)
    elif args.command == "finish":
        controller.finish_task(args.summary)
    elif args.command == "verify-ui":
         print("UI Verification mode enabled. Please capture a screenshot and provide it to the agent.")
    elif args.command == "fail":
        if args.summary: # Using summary arg as task_id for this command
            ctrl = AuraController()
            ctrl.report_failure(args.summary)
        else:
            print("Usage: fail [task_id]")
    elif args.command == "discover":
        if args.summary:
            ctrl = AuraController()
            files = ctrl.discovery_scan(args.summary)
            print("Found relevant files:")
            for f in files:
                print(f"- {os.path.relpath(f, ctrl.project_dir)}")
        else:
            print("Usage: discover [task_title]")
