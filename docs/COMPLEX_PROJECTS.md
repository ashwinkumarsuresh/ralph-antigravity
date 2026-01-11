# 🏗️ Managing Complex Projects with Ralph-Antigravity
## A Guide for Junior Developers

So you've graduated from a single-file script to a complex application with multiple modules? Welcome to the big leagues! Ralph-Antigravity is designed to scale with you. This guide explains how to use the **Architecture 6.0** (Detailed Stories) features in real-world multi-app environments.

---

### 1. The Monorepo Structure
In a professional environment, you often have a "Monorepo" (one repository with many applications). 

**Example Project Layout:**
```text
my-cool-app/
├── apps/
│   ├── api/             # Backend (Node/Python)
│   │   └── prd.md       # Backend Tasks (Detailed Format)
│   ├── web/             # Frontend (React/Next.js)
│   │   └── prd.md       # Frontend Tasks (Detailed Format)
├── packages/
│   └── shared-types/    # Shared code between both
└── LEARNINGS.md         # Global project engineering rules
```

### 2. The Detailed PRD Format (Architecture 6.0) 💎
Ralph now expects tasks to be structured as professional **User Stories**. This makes the AI much more accurate because it understands the *why* and the *how* before it starts.

**Example in `apps/api/prd.md`:**
```markdown
### US-001: Create User Login API
**Description:** As a developer, I want a secure login endpoint so that users can authenticate.

**Acceptance Criteria:**
- [ ] POST /api/login endpoint exists
- [ ] Returns JWT on success
- [ ] Returns 401 on invalid credentials
- [ ] Typecheck/lint passes
```

### 3. Scoped Synchronization
You don't want your backend tasks mixed up with your frontend tasks. Ralph handles this automatically.

**How to sync:**
1. Put a `prd.md` in each folder.
2. Run `/ralph-sync`.
3. **The Result**: Ralph creates GitHub Issues but adds a `scope:api` or `scope:web` label automatically based on the folder name. 

### 4. Running a "Targeted" Loop
If you are a Frontend Developer today, you don't want the AI accidentally touching the Backend.

**Command:**
```bash
/ralph-antigravity start --scope web
```
Ralph will now only look for issues labeled `scope:web`. This keeps the AI focused and prevents it from breaking other modules.

### 5. Handling Cross-App Dependencies
Sometimes the Web app needs the API to be finished first. You can communicate this to Ralph using issue numbers.

**In `apps/web/prd.md`:**
```markdown
### US-002: Add Login Screen (requires #12)
**Description:** As a user, I want a login screen so I can access my account.

**Acceptance Criteria:**
- [ ] Login form with Email/Password
- [ ] Calls the login API
- [ ] Redirects to dashboard on success
```
*(Assuming #12 is the "API: Create User Login API" issue)*

### 6. The Artifact Lifecycle (Your Work Diary)
As a Junior Dev, your biggest value is documenting *how* you solved a problem. Ralph makes this mandatory:

1.  **`implementation_plan.md`**: Before writing code, Ralph drafts a plan. Review this! It's your chance to play "Tech Lead" and correct the AI's approach.
2.  **`walkthrough.md`**: Once the task is done, a walkthrough is generated. This is automatically posted to the GitHub Issue.

### 7. Adopting Ralph in an Existing Project 🛫
Don't worry, you don't have to start from zero! You can bring Ralph into a project you've already been working on for months.

#### How to Onboard:
1. **Copy the Files**: Copy the `src/` folder and the `.agent/workflows/` folder into your project.
2. **Run the Onboarder**: Type: `/ralph-onboard`
3. **What I will do**: I'll scan your code for formatting patterns and technical debt (`TODO` comments) to build your first `prd.md`.

---

### 💡 Pro-Tip for Junior Devs:
Keep your tasks **Small**. If a task takes more than 1 hour for a human, it's too big for a single Ralph iteration. Break it down! 

*Good Task*: "Add 'Email' field to Login Form"
*Bad Task*: "Implement the entire User Authentication system"

Happy Scaling! 🚀
