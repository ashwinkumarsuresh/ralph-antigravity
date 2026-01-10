# 🏗️ Managing Complex Projects with Ralph-Antigravity
## A Guide for Junior Developers

So you've graduated from a single-file script to a complex application with multiple modules? Welcome to the big leagues! Ralph-Antigravity is designed to scale with you. This guide explains how to use the **Architecture 3.0** features in a real-world multi-app environment.

---

### 1. The Monorepo Structure
In a professional environment, you often have a "Monorepo" (one repository with many applications). 

**Example Project Layout:**
```text
my-cool-app/
├── apps/
│   ├── api/             # Backend (Node/Python)
│   │   └── prd.md       # Backend Tasks
│   ├── web/             # Frontend (React/Next.js)
│   │   └── prd.md       # Frontend Tasks
├── packages/
│   └── shared-types/    # Shared code between both
└── LEARNINGS.md         # Global project engineering rules
```

### 2. Scoped Synchronization
You don't want your backend tasks mixed up with your frontend tasks. Ralph handles this automatically.

**How to sync:**
1. Put a `prd.md` in each folder.
2. Run `/ralph-sync`.
3. **The Result**: Ralph creates GitHub Issues but adds a `scope:api` or `scope:web` label automatically based on the folder name. 

### 3. Running a "Targeted" Loop
If you are a Frontend Developer today, you don't want the AI accidentally touching the Backend.

**Command:**
```bash
/ralph-antigravity start --scope web
```
Ralph will now only look for issues labeled `scope:web`. This keeps the AI focused and prevents it from breaking other modules.

### 4. Handling Cross-App Dependencies
Sometimes the Web app needs the API to be finished first. You can communicate this to Ralph using issue numbers.

**In `apps/web/prd.md`:**
```markdown
- [ ] UI: Add Login Screen (requires #12)
```
*(Assuming #12 is the "API: Create Login Endpoint" issue)*

**What Ralph Does:**
- It sees issue #12 is a dependency.
- Before starting "Add Login Screen", Ralph checks GitHub.
- If #12 is still **Open**, Ralph skips the UI task and looks for the next non-blocked task.
- This ensures your project is built in the correct logical order! 🧱

### 5. The Artifact Lifecycle (Your Work Diary)
As a Junior Dev, your biggest value is documenting *how* you solved a problem. Ralph makes this mandatory:

1.  **`implementation_plan.md`**: Before writing code, Ralph drafts a plan. Review this! It's your chance to play "Tech Lead" and correct the AI's approach.
2.  **`walkthrough.md`**: Once the task is done, a walkthrough is generated. This is automatically posted to the GitHub Issue.
    - **Tip**: Add a screenshot to the walkthrough for UI tasks. It creates a beautiful visual history of your progress.

### 6. Using Milestones for Sprints
Working in a 2-week Sprint? Use GitHub Milestones.

**Command:**
```bash
/ralph-antigravity start --milestone "v1.0-Alpha"
```
This tells Ralph to ignore the "backlog" and only focus on the tasks you've promised for this release.

---

### 💡 Pro-Tip for Junior Devs:
Keep your tasks **Small**. If a task takes more than 1 hour for a human, it's too big for a single Ralph iteration. Break it down! 

*Good Task*: "Add 'Email' field to Login Form"
*Bad Task*: "Implement the entire User Authentication system"

Happy Scaling! 🚀
