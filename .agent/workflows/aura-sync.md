---
description: Sync local tasks from prd.md to GitHub Issues
---

# Aura Sync Workflow

This workflow synchronizes your local `prd.md` checklist with GitHub Issues.

## Steps

1. **Safety Check**
   - Verify that `prd.md` exists in the project root.
   - Verify that `gh` CLI is installed and authenticated.

2. **Execute Sync**
   - Run the sync script: `python src/github_sync.py`
   - This script will:
     - Identification: Parse `prd.md` for `[ ]` uncompleted tasks.
     - Pushing: Create a new GitHub Issue for any task that doesn't already exist on GitHub.

3. **Confirmation**
   - Report how many new issues were created.
   - Remind the user they can now start the loop using `/aura-antigravity`.
