---
description: Start the autonomous Ralph development loop for the current project
---

# Ralph-Antigravity Workflow

This workflow executes a tight, iterative development loop using Gemini (Antigravity).

## Workflow Logic (Artifact-Driven Loop)

1. **Phase 1: Sync & Select**
   - Run `python src/github_sync.py` to sync local `prd.md` files (recursive).
   - Run `python src/ralph_controller.py next` to pick the next task.
   - Use `--scope` or `--milestone` for targeted development.

2. **Phase 2: Context Discovery (New in 4.0)**
   - Run `python src/ralph_controller.py discover "[Task Title]"` to identify relevant files.
   - Antigravity gathers "Context Anchors" (`ARCH.md` / `LEARNINGS.md`) from the task's parent directories.
   - Antigravity *must* update the technical implementation plan using these specific anchors.

3. **Phase 3: Planning (Required)**
   - Antigravity *must* analyze the fetched task and create an `implementation_plan.md` (Artifact).
   - If in "Strict Mode", wait for user approval of the plan.

4. **Phase 3: Implementation**
   - Execute the code changes specified in the `implementation_plan.md`.
   - Update `task.md` to reflect progress.

4. **Phase 4: Verification & Walkthrough (Required)**
   - Run project-specific tests (Verify via logs/output).
   - **Multimodal Check**: If the task involves UI, run `browser_subagent` to capture a screenshot for vision-based verification.
   - Antigravity *must* create a `walkthrough.md` (Artifact) summarizing the changes and verification results.

5. **Phase 5: Automated Audit & Closure**
   - Commit changes referencing the issue ID.
   - Run `python src/ralph_controller.py finish` (This script will automatically read the `walkthrough.md` and post it to GitHub before closing the issue).

6. **Iterate**
   - Return to Phase 1.
