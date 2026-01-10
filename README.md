# Ralph-Antigravity-Git-Issues

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Ralph-Antigravity-Git-Issues** is an autonomous, iterative development workflow for [Antigravity](https://deepmind.google/technologies/gemini/) (Gemini-based AI agent). 

Inspired by the "Ralph" pattern originally conceived by Geoffrey Huntley for [AMP](https://github.com/snarktank/ralph) and later adapted for [Claude Code](https://github.com/frankbria/ralph-claude-code), this implementation brings tight, verifiable iteration cycles to the Gemini ecosystem with first-class **GitHub Issues** integration for a multi-layered audit trail.

## 🚀 Core Philosophy

1.  **Iterative Atomicity**: Tasks are broken down into small, verifiable "stories".
2.  **GitHub as Source of Truth**: GitHub Issues act as the master task list and historical audit record.
3.  **Clean Context Cycles**: The agent implements one story at a time, ensuring maximum accuracy and minimal "context rot".
4.  **Automatic Verification**: Every cycle includes mandatory tests/linting and optional multimodal (screenshot) validation.

## 🛠 Features

-   **Autonomous Loop**: Automatically picks the next open GitHub issue and solves it.
-   **GitHub Sync**: Bidirectional sync between local `prd.md` and GitHub Issues.
-   **Detailed Audit Trail**: Every closure includes a "Summary of Work" comment on GitHub with linked commits.
-   **Safety First**: "Wait for User" policy on any synchronization failure or API error.
-   **Multimodal Ready**: Support for Gemini vision-based UI verification.

## 📦 Installation

To use this workflow in your project:

1.  **Clone this repository** or copy the `.agent/workflows/` and `scripts/` directories to your project.
2.  **Initialize GitHub CLI**: Ensure you have [`gh`](https://cli.github.com/) installed and authenticated (`gh auth login`).
3.  **Bootstrap**:
    ```bash
    antigravity initialize ralph-antigravity-git-issues
    ```

## 📖 Usage Guide

### Step 0: Brainstorm your PRD (New!)
If you're starting from scratch, use the brainstorming workflow:
```bash
/prd-brainstorm
```
I will chat with you to define your goals and automatically generate your `prd.md`.

### Step 1: Define your PRD
If you already have requirements, create or edit your `prd.md`:
```markdown
# Product Requirements Document
- [ ] Feature: Add user authentication
- [ ] Bug: Fix navigation overflow on mobile
```

### Step 2: Sync to GitHub
```bash
/ralph-antigravity-git-issues sync
```
This will turn your checklist into GitHub Issues.

### Step 3: Run the Autonomous Loop
```bash
/ralph-antigravity-git-issues start
```
Antigravity will now:
1.  Fetch the next issue from GitHub.
2.  Plan the implementation.
3.  Write the code.
4.  Run tests.
5.  Commit with the issue number (e.g., `fixes #1`).
6.  Close the issue with a summary comment.

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
