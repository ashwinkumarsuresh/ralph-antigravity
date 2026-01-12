# 🆘 Aura-Antigravity Troubleshooting Guide

Encountering issues with the autonomous loop? Most problems are related to environment setup or permissioning.

---

## 1. GitHub Integration Issues

### **Error: `gh command not found`**
*   **Cause**: The GitHub CLI is not installed or not in your system's PATH.
*   **Fix**: Install it via `brew install gh` (macOS) or download from [cli.github.com](https://cli.github.com/).

### **Error: `Authentication failed`**
*   **Cause**: Your `gh` CLI session has expired or is not authorized for the current repository.
*   **Fix**: Run `gh auth login` and follow the prompts to re-authenticate.

### **Error: `Label 'scope:...' not found`**
*   **Cause**: You are trying to sync or filter by a label that doesn't exist yet.
*   **Fix**: `github_sync.py` should create them automatically, but you can also create them manually on GitHub or via `gh label create [name]`.

---

## 2. Controller & Git Issues

### **Error: `Git checkout failed (uncommitted changes)`**
*   **Cause**: Aura cannot switch to a task branch because your `main` branch has uncommitted local changes.
*   **Fix**: Commit or stash your local changes before starting the Aura loop.

### **Error: `Task #X has failed 5 times`**
*   **Cause**: The AI is stuck in a loop where it cannot pass its own verification steps.
*   **Fix**: 
    1.  Check the GitHub Issue comment to see the last failure error.
    2.  Manually fix the code on the task branch.
    3.  Manually close the issue or reset the attempt counter in `aura_status.json`.

---

## 3. Context & Accuracy Issues

### **Issue: The AI is editing the wrong files**
*   **Cause**: The **Discovery Scan** might be picking up too much noise or missing the target.
*   **Fix**: Improve your User Story title in `prd.md` to include more specific keywords related to the filenames you want it to find.

### **Issue: The AI is ignoring project conventions**
*   **Cause**: Missing **Context Anchors**.
*   **Fix**: Create an `ARCH.md` file in the specific directory containing the rules (e.g., "Use functional components for React").

---

*Still stuck? Try running with `python src/aura_controller.py --help` or check the logs.* 🚀
