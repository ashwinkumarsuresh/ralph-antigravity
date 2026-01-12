# Contributing to Aura-Antigravity 🤝

Thank you for your interest in improving Aura-Antigravity! As an autonomous development loop, we have specific standards for how code should be contributed.

## 1. Branching Strategy
We strictly follow the **Architecture 7.0** branching rules:
- **Feature Branches**: All changes must be made in a branch following the format `feat/your-feature-name` or `fix/issue-id`.
- **Primary Branch**: The `main` branch is protected. All contributions must come via Pull Request.

## 2. The Aura Quality Bar
Every contribution must be "Aura-Ready." This means:
*   **Small & Atomic**: Don't submit giant PRs. If a feature is large, break it into smaller commits.
*   **Documentation First**: Every new feature must include an update to the relevant `.md` file in the `docs/` folder.
*   **Diagrams**: If adding a new phase to the loop, update the Mermaid diagrams in `docs/ARCHITECTURE.md`.

## 3. Development Setup
To test your changes locally:
1. Clone the repository.
2. Initialize a local mock project.
3. Run `python src/github_sync.py [mock-path]` to verify synchronization logic.
4. Run `python src/aura_controller.py next` to verify task selection and branching logic.

## 4. Coding Standards
*   **Python**: Use PEP 8 standards. Keep functions small and documented.
*   **Workflows**: Workflow files in `.agent/workflows/` should be consultative, not just a list of commands. Use the **INVEST** principles for all task templates.

## 5. Security & Privacy
*   **Never** commit API keys or environment secrets.
*   Ensure that any `gh` CLI commands handle authentication failures gracefully.

Happy contributing! 🚀
