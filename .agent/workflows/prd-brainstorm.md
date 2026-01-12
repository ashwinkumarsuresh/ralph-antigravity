---
description: Brainstorm and generate a PRD file with Antigravity
---

# PRD Brainstorming Workflow

This workflow helps you go from an initial idea to a structured `prd.md` file that can be used with the Aura-Antigravity loop.

## Workflow Phases

### 1. Discovery
- **Check for Ideation**: If `IDEAS.md` exists, read it first to understand the project's "North Star" and "Idea Bank".
- Ask the user for the high-level objective (or pull it from `IDEAS.md`).
- Determine the target audience and technology stack.
- Identify the core "Must-Have" features.

### 2. Refinement
- Suggest technical constraints (e.g., API limits, security requirements).
- Surface potential edge cases or UX considerations.
- Discuss testing and verification strategies.

### 3. Structuring (INVEST Framework)
- Organize the gathered information into discrete, checkboxed tasks.
- **Apply the INVEST Model**:
  - **Independent**: Minimize dependencies between tasks.
  - **Small**: Each task must be solvable in under 1 hour by a human.
  - **Testable**: Every story must have concrete Acceptance Criteria.
- **Vertical Slicing**: Ensure each task delivers a functional slice (e.g., DB + API for a specific feature).
- Prioritize tasks based on user feedback.

### 4. Export
- Write the final content to `prd.md` in the current project root.
- Validate that the format is compatible with the `github_sync.py` script.

## Instructions for Antigravity

- Be proactive but consultative.
- Don't just list features; ask *why* they are needed to ensure better design.
- **Atomization Strategy**: If a feature sounds large (e.g., "User Profile"), force the user to break it down. Ask: *"Should we start with the basic profile fields first, then do the image upload in a separate story?"*
- **Detailed Story Format**: Each task in the final `prd.md` MUST follow this structure:
  ```markdown
  ### US-001: [Title]
  **Description:** As a [user], I want [feature] so that [benefit].

  **Acceptance Criteria:**
  - [ ] Specific verifiable criterion
  - [ ] Another criterion
  - [ ] Typecheck/lint passes
  - [ ] **[UI stories only]** Verify in browser using dev-browser skill
  ```
- Each task should be concise enough to be solved in a single Aura iteration.
