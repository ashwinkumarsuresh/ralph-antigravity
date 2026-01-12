---
description: Brainstorm different options and create an Idea Bank before committing to a PRD
---

# Aura Ideation Workflow (Phase 0)

This workflow is for divergent thinking. Use it to explore the "What" and "How" before you are ready to write a structured `prd.md`.

## Workflow Phases

### 1. Vision Setting
- Ask the user for the "North Star" of the project.
- What is the ultimate goal? What problem are we solving?
- Document this in `IDEAS.md` under the **Vision** header.

### 2. The Idea Dump
- Discuss different features, tech stacks, or UI concepts.
- Proactively suggest alternatives or "crazy ideas" to expand the user's thinking.
- Categorize ideas into:
    - **High Priority**: Desired for the first PRD.
    - **Maybe/Later**: Interesting but out of scope for now.
    - **Exploratory**: Needs research before decided.

### 3. Comparison & Trade-offs
- If there are multiple ways to solve a problem (e.g., Auth0 vs Custom JWT), create a comparison matrix.
- Discuss the pros, cons, and consequences (ADR-style thinking).

### 4. Export to Idea Bank
- Write the results to `IDEAS.md` in the current project root.
- The file should be human-readable and act as a "scratchpad" for the project's future.

## Instructions for Antigravity

- **Be a Creative Partner**: In this phase, your goal is to help the user explore. Don't worry about "implementation feasibility" too much yet.
- **Divergent Thinking**: If the user suggests one way, ask if they've considered another.
- **Structure the Chaos**: Turn the chat into a organized `IDEAS.md`.
- **Vertical Alignment**: Ensure ideas align with the "North Star" defined in Phase 1.

## Transition to PRD
Once the user feels confident about a set of ideas, recommend running `/prd-brainstorm` to turn those ideas into actionable tasks.
