---
description: Start the autonomous Ralph development loop for the current project
---

# Ralph-Antigravity-Git-Issues Workflow

This workflow executes a tight, iterative development loop using Gemini (Antigravity) and GitHub Issues.

## Usage

1. **Initialize**
   - Copy `prd_template.md` to `prd.md`.
   - Run `python src/github_sync.py` to push tasks to GitHub.

2. **Loop Iteration**
   - Run `python src/ralph_controller.py next` to pick the next task.
   - Antigravity analyzes the fetched task and creates a local `implementation_plan.md`.

3. **Execution**
   - Perform the code changes specified in the plan.
   - Run project-specific tests.

4. **Closure**
   - Run `python src/ralph_controller.py finish "Implementation Summary Here"` to close the GitHub issue and post the summary.

## Workflow Logic (Internal)

1. **Verify State**
   - Read local `prd.md`.
   - Sync with GitHub Issues using `python src/github_sync.py`.

2. **Select Task**
   - Pick the highest priority open issue using `python src/ralph_controller.py next`.

3. **Plan & Execute**
   - Execute Implementation Plan for that task.

4. **Verify**
   - Run verification (tests/screenshots).

5. **Finalize**
   - Commit changes referencing the issue ID.
   - Close the GitHub issue using `python src/ralph_controller.py finish [SUMMARY]`.
