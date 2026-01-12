# 🤖 Aura-Antigravity: Your AI Developer 🚀

**Aura-Antigravity** is like having a robot developer who works on your project while you sleep (or have a coffee! ☕). It takes your "Idea List" and turns it into real code, one small piece at a time.

---

## 👋 What is this? (The Simple Version)

Imagine you are building a website. You have a list of things to do:
1. "Add a logo"
2. "Change the background color"
3. "Add a 'Contact Us' button"

Usually, you would have to write all that code yourself. **Aura-Antigravity** does the hard work for you. It reads your list, writes the code, tests it to make sure it works, and then tells you it's finished.

## ✨ Why even use this?

*   **No Overwhelm**: It works on ONE thing at a time. No more getting lost in thousands of lines of code.
*   **Proof of Work**: Everything it does is saved on GitHub, so you (and your teacher!) can see exactly how it solved each problem.
*   **Smart Testing**: It checks its own work! If it mentions "UI", it can even take a screenshot to show you how it looks.

---

## 🚀 How to set it up (Easy Mode)

### 1. Get the files
Copy the folders from this repository into your project folder. You need:
*   `.agent/workflows/` (The instructions for the AI)
*   `src/` (The "brain" of the loop)

### 2. Connect to GitHub
You need the **GitHub CLI** (a tool that lets the AI talk to GitHub).
*   Download it here: [cli.github.com](https://cli.github.com/)
*   In your terminal, type: `gh auth login` and follow the steps in your browser.

### 3. Initialize
Tell Antigravity (your AI assistant):
*"Antigravity, initialize aura-antigravity for this project."*

---

## 📖 How to use it step-by-step

### Phase 0: Ideate & Explore 🧠
If you have a rough idea but aren't ready for a technical list yet, type:
```bash
/aura-ideate
```
I will help you explore different options and create an `IDEAS.md` "Bank" for your project.

### Step 1: Brainstorm your PRD 📝
Once your vision is clear, type:
```bash
/prd-brainstorm
```
I will chat with you about your idea (reading your `IDEAS.md` if it exists) and create a file called `prd.md`.

### Step 2: Upload your tasks ☁️
Once your `prd.md` list is ready, type:
```bash
/aura-sync
```
This sends your list to GitHub as "Issues" (a fancy word for a To-Do list on the web).

### Step 3: Start the robot! 🤖
Type:
```bash
/aura-antigravity start
```
**Now watch the magic happen!** I will pick the first task, write the code, and close the task when it's done.

### Step 4: Scaling to Big Projects (Architecture 3.0) 🏗️
Aura-Antigravity is built for multi-app monorepos. You can have a `prd.md` in *every* folder:
- `apps/backend/prd.md`
- `apps/frontend/prd.md`

1. **Sync All**: Running `/aura-sync` will find them all and apply `scope:backend` and `scope:frontend` labels on GitHub.
2. **Targeted Loop**: Focus on one app at a time:
   ```bash
   /aura-antigravity start --scope backend
   ```

Check out our **[Junior Dev Guide to Complex Projects](docs/COMPLEX_PROJECTS.md)** for deep-dive examples on dependencies, milestones, and monorepo management. 

For developers, see:
*   📜 **[Technical Architecture](docs/ARCHITECTURE.md)**
*   🖥️ **[API Reference](docs/API_REFERENCE.md)**
*   🚀 **[CI/CD Integration](docs/CICD.md)**
*   🏛️ **[ADR Guide (Decisions)](docs/ADR_GUIDE.md)**
*   🛠️ **[Troubleshooting Guide](docs/TROUBLESHOOTING.md)**
*   📖 **[System Glossary](docs/GLOSSARY.md)**
*   🤝 **[Contributing Guide](docs/CONTRIBUTING.md)**

---

## 🆘 Troubleshooting (If things go wrong)

*   **"gh command not found"**: This means you need to install the GitHub CLI. Ask me "How do I install gh CLI on [my OS]?" and I'll help!
*   **"No prd.md found"**: Make sure you have a file named `prd.md` in your main project folder.
*   **The AI gets stuck**: Just send a message! I'm here to help you get back on track.

## 📜 Legal Stuff
This project is under the **MIT License**. That means it's free for everyone to use and learn from!

Happy Coding! 🎉
