---
description: Brainstorm and generate a PRD file with Antigravity
---

# PRD Brainstorming Workflow

This workflow helps you go from an initial idea to a structured `prd.md` file that can be used with the Ralph-Antigravity loop.

## Workflow Phases

### 1. Discovery
- Ask the user for the high-level objective of the project.
- Determine the target audience and technology stack.
- Identify the core "Must-Have" features.

### 2. Refinement
- Suggest technical constraints (e.g., API limits, security requirements).
- Surface potential edge cases or UX considerations.
- Discuss testing and verification strategies.

### 3. Structuring
- Organize the gathered information into discrete, checkboxed tasks.
- Prioritize tasks based on user feedback.

### 4. Export
- Write the final content to `prd.md` in the current project root.
- Validate that the format is compatible with the `github_sync.py` script.

## Instructions for Antigravity

- Be proactive but consultative.
- Don't just list features; ask *why* they are needed to ensure better design.
- Each task in the final `prd.md` should be concise enough to be solved in a single Ralph iteration.
