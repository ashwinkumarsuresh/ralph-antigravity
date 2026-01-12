# 📖 Aura-Antigravity Glossary

This glossary defines the specific terminology used throughout the Aura-Antigravity system.

---

### **A**
*   **Acceptance Criteria (AC)**: A set of verifiable conditions that a User Story must meet to be considered complete. Aura checks these locally before closing a task.
*   **Architecture 7.1**: The current technical version of Aura, featuring task-specific branching, INVEST slicing, and 5-attempt retry resilience.
*   **Artifacts**: Structured Markdown files (`implementation_plan.md`, `walkthrough.md`, `task.md`) used by the AI to track progress and document decisions.

### **C**
*   **Context Anchors**: Persistent rulebooks (`ARCH.md` or `LEARNINGS.md`) located in directory hierarchies. Aura inherits these rules recursively to understand local project conventions.
*   **Controller**: The `aura_controller.py` script that manages the Git lifecycle, task selection, and retry logic.

### **D**
*   **Discovery Scan**: A heuristic search phase where Aura identifies the most relevant files for a task based on keywords, reducing noise in large codebases.

### **G**
*   **GitHub Sync**: The process of converting local `prd.md` blocks into GitHub Issues using `github_sync.py`.

### **I**
*   **INVEST**: A framework for task atomization: **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, and **T**estable.

### **P**
*   **PRD (Product Requirements Document)**: The root source of truth for your project features, usually stored in `prd.md`.

### **Q**
*   **Quarantine Strategy**: Isolating legacy or messy codebases in specific subdirectories so the AI doesn't "learn" bad habits from them.

### **S**
*   **Scope**: A label applied to GitHub issues (e.g., `scope:api`) to filter which module the AI loop should work on.

### **V**
*   **Vertical Slicing**: Breaking tasks into functional increments that touch all layers (DB + API + UI) rather than horizontal technology layers.

---

*Think we missed a term? Check the [ARCHITECTURE.md](ARCHITECTURE.md) for deeper technical context.* 🚀
