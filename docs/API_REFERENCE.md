# 📟 Aura-Antigravity API Reference

This document provides a technical reference for the Python scripts that power the Aura-Antigravity loop.

---

## 1. `aura_controller.py`
The central manager for task selection, branching, and retry logic.

### Commands
| Command | Arguments | Description |
| :--- | :--- | :--- |
| `next` | `--scope`, `--milestone` | Picks the next task from GitHub, creates a task-branch, and increments the attempt counter. |
| `finish` | `summary` (optional) | Reads `walkthrough.md`, posts it to GitHub, closes the issue, and pushes the local branch. |
| `discover` | `task_title` | Heuristic scan that identifies the top 10 most relevant files for a task. |
| `fail` | `task_id` | Manually increments the retry counter for a specific task. |
| `verify-ui` | N/A | Prints instructions for multimodal UI verification. |

### Core Methods
*   **`gather_context_anchors(start_dir)`**: Recursively crawls parent directories to find `ARCH.md` and `LEARNINGS.md`. Returns a list of paths in root-first order.
*   **`discovery_scan(task_title)`**: Uses keywords from the title to find relevant files in the project tree, skipping `.git` and `node_modules`.

---

## 2. `github_sync.py`
The synchronization engine between local PRDs and GitHub.

### CLI Usage
```bash
python src/github_sync.py [root_directory]
```
If no directory is provided, it defaults to `.`.

### Core Functional Logic
*   **`parse_prd(filepath)`**: Uses regular expressions to split a `prd.md` into User Story blocks (ID, Title, Description, Acceptance Criteria). It detected dependencies via `(requires #ID)` and UI flags.
*   **`sync_prd_to_github(root_dir)`**: 
    1.  Recursively finds all `prd.md` files.
    2.  Generates labels (e.g., `scope:api`) based on directory hierarchy.
    3.  Fetches existing GitHub issues to avoid duplication.
    4.  Creates new issues for non-completed local tasks.

---

## 3. Internal State (`aura_status.json`)
The controller maintains a local JSON file to track persistence across agent turns.

| Field | Type | Description |
| :--- | :--- | :--- |
| `iterations` | Integer | Total tasks started in this project session. |
| `current_task` | Object | Contains `id`, `title`, and `branch` of the active task. |
| `task_attempts` | Object | Map of `task_id` -> `attempt_count` (0-5). |

---

*For high-level project guides, see [COMPLEX_PROJECTS.md](COMPLEX_PROJECTS.md).* 🚀
