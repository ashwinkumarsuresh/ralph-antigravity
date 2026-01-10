import json
import subprocess
import sys
import os
from github_sync import get_github_issues, run_command

class RalphController:
    def __init__(self, project_dir="."):
        self.project_dir = project_dir
        self.status_file = os.path.join(project_dir, "ralph_status.json")
        self.load_status()

    def load_status(self):
        """Load internal state from ralph_status.json."""
        if os.path.exists(self.status_file):
            with open(self.status_file, 'r') as f:
                self.state = json.load(f)
        else:
            self.state = {"iterations": 0, "current_task": None}

    def save_status(self):
        """Save internal state to ralph_status.json."""
        with open(self.status_file, 'w') as f:
            json.dump(self.state, f, indent=2)

    def get_next_task(self):
        """Fetch the next task from GitHub Issues (Master)."""
        issues = get_github_issues()
        if not issues:
            return None
        
        # Sort by number to maintain priority
        issues.sort(key=lambda x: x['number'])
        return issues[0]

    def start_iteration(self):
        """Prepare for the next iteration."""
        task = self.get_next_task()
        if not task:
            print("No more tasks found on GitHub. Workflow Complete!")
            return None
        
        self.state["current_task"] = {
            "id": task["number"],
            "title": task["title"],
            "url": task["url"]
        }
        self.state["iterations"] += 1
        self.save_status()
        
        print(f"--- Iteration {self.state['iterations']} ---")
        print(f"Active Task: #{task['number']} - {task['title']}")
        return task

    def finish_task(self, summary, commit_hash=None):
        """Close the task on GitHub and update state."""
        if not self.state["current_task"]:
            print("No active task to finish.")
            return

        task_id = self.state["current_task"]["id"]
        
        # 1. Post final summary as comment
        full_comment = f"### ✅ Task Complete\n\n**Summary:** {summary}\n"
        if commit_hash:
            full_comment += f"\n**Commit:** {commit_hash}"
        
        run_command(["gh", "issue", "comment", str(task_id), "--body", full_comment])
        
        # 2. Close issue
        run_command(["gh", "issue", "close", str(task_id)])
        
        print(f"Task #{task_id} closed on GitHub.")
        
        # 3. Cleanup local state
        self.state["current_task"] = None
        self.save_status()

if __name__ == "__main__":
    controller = RalphController()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "next":
            controller.start_iteration()
        elif cmd == "finish":
            if len(sys.argv) > 2:
                controller.finish_task(sys.argv[2])
            else:
                print("Usage: finish [summary]")
