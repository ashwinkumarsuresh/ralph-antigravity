# 🏛️ ADR: Architecture Decision Records (Guide)

In Aura-Antigravity, we use **Architecture Decision Records (ADRs)** to capture the "Why" behind our technical choices. This is especially important for autonomous agents, so their decisions are transparent and defensible.

---

## 📅 When to write an ADR?
Aura is instructed to automatically include an ADR section in the `implementation_plan.md` when it detects a **Major Change**. These include:
- Adding or removing a library (dependency).
- Changing a database schema or file storage pattern.
- Modifying a core security/authentication flow.
- Significant refactoring of shared code or parent context anchors.

---

## 📝 The ADR Structure
A good ADR consists of three critical sections:

### 1. Context
What is the technical problem we are trying to solve? Why can't we keep the current implementation?
> *Example: "The current local JSON storage is causing file lock issues during concurrent runs."*

### 2. Decision
What specific technical change are we making?
> *Example: "Switching to a SQLite database for task state management."*

### 3. Consequences
What are the trade-offs?
- ✅ **Pros**: Better concurrency, ACID compliance.
- ⚠️ **Cons**: Adds a binary dependency, requires migration scripts.

---

## 🤖 Aura's Role
During the **Planning Phase (Phase 3)**, Aura will:
1. Scan the prompt and existing code.
2. If it meets the "Major" criteria, it will generate the ADR section.
3. You should review this section carefully in the `implementation_plan.md` before approving implementation.

---

*For high-level system overview, see [ARCHITECTURE.md](ARCHITECTURE.md).* 🚀
