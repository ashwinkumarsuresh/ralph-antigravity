# 🤖 Aura in CI/CD (GitHub Actions)

Aura-Antigravity is designed to be automation-friendly. You can run the controller inside a GitHub Action to create a "Self-Healing Backlog" or Automated Onboarding.

---

## 1. Automated Syncing
Run this action on every push to `main` to ensure your GitHub Issues always reflect your local `prd.md`.

```yaml
name: Aura Sync
on:
  push:
    branches: [main]
    paths: ['**/prd.md']

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Sync PRD to Issues
        run: python src/github_sync.py .
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

## 2. Autonomous Task Worker (Beta)
You can trigger a "Aura Run" whenever a new issue is opened or labeled `aura-run`.

```yaml
name: Aura Worker
on:
  issues:
    types: [labeled]

jobs:
  implement:
    if: github.event.label.name == 'aura-run'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Start Aura Loop
        run: python src/aura_controller.py next
        env:
          GH_TOKEN: ${{ secrets.PAT_WITH_REPO_SCOPE }}
```
> [!IMPORTANT]
> To allow Aura to create branches and push code, you must use a **Personal Access Token (PAT)** with `repo` scope, as the default `GITHUB_TOKEN` may have restricted permissions on protected branches.

---

## 3. Integration with PR Environments
Aura's **Architecture 7.0** branching strategy is perfect for PR environments:
1. Aura creates a branch `aura/issue-123`.
2. A GitHub Action detects the branch and deploys a preview environment.
3. You review the code and the live preview.
4. On Merge, the GitHub Issue is closed.

---

*Looking for deployment troubleshooting? See [TROUBLESHOOTING.md](TROUBLESHOOTING.md).* 🚀
