---
description: Onboard an existing project to the Ralph-Antigravity loop
---

# 🛫 Ralph-Antigravity Onboarding Workflow

Use this workflow to bridge an existing (legacy) project into the Ralph autonomous loop.

## Phase 1: Landscape Discovery
1. **Context Scan**: Antigravity, scan the current project structure and identify the tech stack (e.g., Python, React, Go).
2. **Architecture Mapping**: Identify key directories (apps, packages, docs) and their roles.
3. **Existing Docs**: Read any existing `README.md` or design documents to understand high-level goals.

## Phase 2: Foundation Setup
1. **Convention Extraction**: Analyze 2-3 core source files to detect code styles (naming, formatting, structure).
2. **Create Context Anchors**:
   - Create a root `LEARNINGS.md` with global project rules.
   - Create folder-specific `ARCH.md` anchors for each identified module.
3. **Status Check**: Ensure GitHub CLI is logged in and the repository is pushed.

## Phase 3: Task Generation (Build the PRD)
1. **Debt Discovery**: Scan the codebase for `TODO` or `FIXME` comments.
2. **Issue Synthesis**: Create a `prd.md` using the **Architecture 7.1 INVEST Format**:
   - **Break down large TODOs**: If a `TODO` is complex, split it into multiple US blocks.
   - **Apply Vertical Slicing**: Ensure each story is a functional increment.
   ```markdown
   ### US-001: [Title]
   **Description:** [Context from original TODO]
   **Acceptance Criteria:**
   - [ ] [Specific fix]
   - [ ] Typecheck/lint passes
   ```

## Phase 4: Ready for Loop
1. Run `/ralph-sync` to upload the new tasks to GitHub.
2. Run `/ralph-antigravity start` to begin the first autonomous iteration!

---
> [!TIP]
> **Incremental adoption is best.** Start by onboarding a single module (a "Scope") rather than the whole project.
