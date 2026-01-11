# 🏗️ Ralph-Antigravity System Architecture

This document provides a deep dive into the technical design, data flows, and state management of the Ralph-Antigravity system.

---

## 1. High-Level System Overview
Ralph-Antigravity follows an **Event-Driven Loop** architecture, where the state is distributed between the local file system and GitHub.

```mermaid
graph TD
    A["User Requirement (prd.md)"] --> B["GitHub Sync (github_sync.py)"]
    B --> C["GitHub Issues (Source of Truth)"]
    C --> D["Controller (ralph_controller.py)"]
    D --> E["Antigravity Agent (Gemini)"]
    E --> F["Implementation Plan"]
    F --> G["Execution & Implementation"]
    G --> H["Walkthrough Artifact"]
    H --> I["Verification & Testing"]
    I --> J["GitHub Issue (Closure & Audit)"]
    J --> D
```

---

## 2. The Resilient Execution Flow (Architecture 7.1)
The loop is designed to be atomic and failure-resilient. If a task fails verification, it enters a retry-loop (max 5 attempts) before alerting the user.

```mermaid
sequenceDiagram
    participant C as Controller
    participant G as GitHub API
    participant A as Agent (Antigravity)
    participant V as Verification Logic

    C->>G: Fetch Next Open Issue
    G-->>C: US-123 Payload
    C->>C: Create Task Branch (ralph/issue-123)
    C->>A: Start Implementation Task
    A->>A: Create implementation_plan.md
    A->>A: Execute Code Changes
    A->>V: Run Tests / UI Screenshots
    V-->>A: Result (Success/Fail)
    alt Success
        A->>C: Generate walkthrough.md
        C->>G: Post Walkthrough & Close Issue
        C->>G: Push Feature Branch
    else Failure (Attempt < 5)
        A->>C: Report Failure (python fail 123)
        C->>C: Increment Attempt Counter
        C-->>A: Retry Loop Start
    else Failure (Attempt >= 5)
        C->>G: Label: ralph-blocked
        C->>G: Notify User
    end
```

---

## 3. Task State Transition
The lifecycle of a requirement from inception to production.

```mermaid
stateDiagram-v2
    [*] --> LocalTask: prd.md entry
    LocalTask --> GitHubIssue: /ralph-sync
    GitHubIssue --> InProgress: /ralph-antigravity start
    InProgress --> BranchCreated: controller.next()
    BranchCreated --> Implementing: architecture logic
    Implementing --> Verifying: tests/UI checks
    Verifying --> Implementing: failure (retry < 5)
    Verifying --> Blocked: failure (retry >= 5)
    Verifying --> Closed: success
    Closed --> [*]: Issue comment + Audit
```

---

## 3. Data & State Management

### A. Local State (`ralph_status.json`)
Tracks the current session status and internal retry counters.
```json
{
  "iterations": 1,
  "current_task": { "id": "123", "branch": "ralph/issue-123" },
  "task_attempts": { "123": 1 }
}
```

### B. Context Anchors (`ARCH.md` / `LEARNINGS.md`)
Used for recursive context gathering. The controller crawls the directory tree upwards to merge rules:
- **Project Root**: Global conventions.
- **App Root**: Backend/Frontend specific rules.
- **Feature Root**: Atomic component rules.

---

## 4. Component Breakdown

| Component | Responsibility | Technical Stack |
| :--- | :--- | :--- |
| **`github_sync.py`** | Parses `prd.md` blocks; Syncs to GitHub Issues. | Python3, `gh` CLI |
| **`ralph_controller.py`** | Manages the task loop, branching, and retries. | Python3, `subprocess` |
| **Antigravity Workflows** | Orchestrates the AI's step-by-step logic. | Markdown-driven LLM instructions |
| **Artifacts** | Planning and post-implementation audit trails. | Markdown (`.md`) |

---

## 5. Evolution of Ralph

- **Architecture 1.0**: Simple local `prd.md` list.
- **Architecture 3.0**: GitHub Issues integration & Monorepo labels.
- **Architecture 4.0**: Context Discovery Scan & Parent Inheritance.
- **Architecture 6.0**: Professional User Stories & Acceptance Criteria.
- **Architecture 7.1**: Resilient Branching & INVEST Task Atomization.

---

*This architecture ensures that Ralph remains focused, verifiable, and safe for enterprise-scale projects.* 🚀
