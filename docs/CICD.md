# 🤖 Ralph in CI/CD (GitHub Actions)

Ralph-Antigravity is designed to be automation-friendly. You can run the controller inside a GitHub Action to create a "Self-Healing Backlog" or Automated Onboarding.

---

## 1. Automated Syncing
Run this action on every push to `main` to ensure your GitHub Issues always reflect your local `prd.md`.

```yaml
name: Ralph Sync
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
You can trigger a "Ralph Run" whenever a new issue is opened or labeled `ralph-run`.

```yaml
name: Ralph Worker
on:
  issues:
    types: [labeled]

jobs:
  implement:
    if: github.event.label.name == 'ralph-run'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Start Ralph Loop
        run: python src/ralph_controller.py next
        env:
          GH_TOKEN: ${{ secrets.PAT_WITH_REPO_SCOPE }}
```
> [!IMPORTANT]
> To allow Ralph to create branches and push code, you must use a **Personal Access Token (PAT)** with `repo` scope, as the default `GITHUB_TOKEN` may have restricted permissions on protected branches.

---

## 3. Integration with PR Environments
Ralph's **Architecture 7.0** branching strategy is perfect for PR environments:
1. Ralph creates a branch `ralph/issue-123`.
2. A GitHub Action detects the branch and deploys a preview environment.
3. You review the code and the live preview.
4. On Merge, the GitHub Issue is closed.

---

*Looking for deployment troubleshooting? See [TROUBLESHOOTING.md](TROUBLESHOOTING.md).* 🚀
