# Go Technical Documentation English Reading AI Tutor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a workspace environment in Antigravity for a Go technical documentation English reading tutor with persistent session tracking, difficulty scaling, flashcards, and an updated `go.dev` curriculum.

**Architecture:** Antigravity workspace rules (`AGENTS.md` / `GEMINI.md`) drive an interactive 5-step tutoring agent that operates on a fresh-chat-per-session basis. Progress, vocabulary cards, and difficulty states are persisted into markdown repositories (`sessions/` and `vocabulary/flashcards.md`) guided by a modernized `curriculum/roadmap.md`.

**Tech Stack:** Markdown, Git, Python 3 (verification test), Antigravity CLI customization rules (`AGENTS.md`/`GEMINI.md`).

**Spec:** [docs/superpowers/specs/2026-11-03-go-reading-tutor-design.md](file:///home/hseongh/Documents/dev/english/docs/superpowers/specs/2026-11-03-go-reading-tutor-design.md)

## Global Constraints

- All system prompts, instructions, configuration files, curriculum definitions, and templates must be authored in clear, professional English.
- The tutor persona must use Korean for explanations, pedagogical structure analysis, and guidance, while keeping source text, technical citations, examples, and learner output strictly in English.
- Each conversation turn during tutoring must strictly wait for the learner's response for each step (no multi-step bundling).
- Each tutoring session must represent one section (15–20 min), conclude with Step 5 logging, and explicitly prompt the user to start a fresh chat conversation for the next session.
- The system must read the most recent file in `sessions/` on startup to resume difficulty tiers and streak counters seamlessly.

## Review Focus

- Missing YAML frontmatter keys in session logs breaking difficulty state tracking on fresh chat restarts.
- Failure of `AGENTS.md` to enforce single-step turn-taking, causing the agent to dump steps 1 through 3 all at once.
- Misalignment in the curriculum using archived or obsolete Go 1.0 patterns without modern style pointers.
- Incorrect relative file links or directory layout causing flashcard updates to fail.
- Ambiguity in difficulty scaling thresholds causing premature tier jumps or reductions.

---

### Task 1: Git and Workspace Scaffolding

**Files:**
- Create: `.gitignore`
- Create: `sessions/.gitkeep`

**Interfaces:**
- Consumes: None
- Produces: Git repository initialized with directories `curriculum/`, `templates/`, `vocabulary/`, `sessions/`, `docs/`.

- [ ] **Step 1: Initialize Git Repository**

Run: `git init` in `/home/hseongh/Documents/dev/english`
Expected: `Initialized empty Git repository`

- [ ] **Step 2: Create directory structure and .gitignore**

Create `.gitignore` containing:
```gitignore
.DS_Store
Thumbs.db
__pycache__/
*.pyc
.gemini/
```
Create `sessions/.gitkeep` so git tracks the empty session log directory.

- [ ] **Step 3: Verify git status and commit scaffolding**

Run:
```bash
git add .gitignore sessions/.gitkeep docs/
git commit -m "chore: initialize repository and workspace scaffolding"
```
Expected: Clean git working tree with initial commit.

---

### Task 2: Modernized go.dev Curriculum Roadmap

**Files:**
- Create: `curriculum/roadmap.md`

**Interfaces:**
- Consumes: Spec Section 5.2
- Produces: Complete technical syllabus with 5 stages, section breakdown, official go.dev URLs, rationale, and estimated completion times.

- [ ] **Step 1: Write `curriculum/roadmap.md`**

Author the curriculum covering:
1. Stage 1: Foundations & Fundamentals (Tour of Go, Tutorials: Getting started, Create module, Workspaces)
2. Stage 2: Modern Features & Tooling (Generics, Fuzzing, Go Modules Reference: go.mod, versioning, replace, workspace)
3. Stage 3: Idiomatic Go & Style Guidelines (Code Review Comments, Google Go Style Decisions, Effective Go selected contemporary sections with historical notes)
4. Stage 4: Deep Systems & Standard Library Prose (Standard Library: `io`, `errors`, `context`, `sync`; Go Blog classic guides; The Go Memory Model; Diagnostics; Go Language Specification selected clauses)
5. Stage 5: Practical API Development (Developing a RESTful API with Go and Gin)

Each entry must specify:
- Topic name and canonical URL
- Key technical vocabulary to anticipate
- Recommended reading breakdown (approx. 150–250 words per 15–20 min session)

- [ ] **Step 2: Verify links and structure**

Verify that all URLs point to valid domains (`go.dev`, `pkg.go.dev`, `google.github.io/styleguide/go/`).

- [ ] **Step 3: Commit curriculum**

Run:
```bash
git add curriculum/roadmap.md
git commit -m "feat(curriculum): add modernized go.dev reading syllabus"
```

---

### Task 3: Session Logging and Flashcard Templates

**Files:**
- Create: `templates/session_template.md`
- Create: `vocabulary/flashcards.md`

**Interfaces:**
- Consumes: Spec Sections 5.1, 5.3, 5.4
- Produces: Standardized schema for daily session logs and cumulative flashcards.

- [ ] **Step 1: Create `templates/session_template.md`**

Define markdown template with YAML frontmatter:
```markdown
---
session_id: "YYYY-MM-DD_NN"
date: "YYYY-MM-DD"
curriculum_stage: 1
topic: "A Tour of Go: Packages, variables, and functions"
doc_url: "https://go.dev/tour/basics/1"
difficulty_tier: "Normal" # "Normal" | "Advanced" (no vocab preview, +50% length) | "Assisted" (halved length, sentence-by-sentence)
streak_accurate: 0
miss_counter: 0
next_recommended_section: "A Tour of Go: Flow control statements"
---

# Session Summary: [Topic]

## 1. Excerpt Studied
[Excerpt]

## 2. Learner Synthesis & Summary
- **Learner English Summary:** [Summary]
- **Feedback & Structural Analysis:** [Analysis]

## 3. Idiomatic Expressions Analyzed
- **Expression 1:** [Notes]
- **Expression 2:** [Notes]

## 4. Production Exercise
- **Exercise Type:** [Peer Explanation | Technical Q&A | Git Commit/Docstring]
- **Learner Submission:** [Submission]
- **Tutor Feedback:** [Before -> After Feedback]

## 5. Review Cards Added
- **Words (5):**
  1. ...
- **Expressions (2):**
  1. ...
```

- [ ] **Step 2: Create `vocabulary/flashcards.md`**

Initialize cumulative flashcards repository with table formats:
- Technical Terms Bank (Term, Part of Speech, English Definition, Korean Meaning, First Encountered Date/Session)
- Technical Idioms & Phrasal Patterns (Pattern, Nuance / Pragmatic Meaning, Example in Technical Docs, Session)
- Spaced Review Checklist

- [ ] **Step 3: Commit templates and flashcards**

Run:
```bash
git add templates/session_template.md vocabulary/flashcards.md
git commit -m "feat(templates): add session logging template and flashcard deck"
```

---

### Task 4: Antigravity Primary System Prompts and Rules (`AGENTS.md` and `GEMINI.md`)

**Files:**
- Create: `AGENTS.md`
- Create: `GEMINI.md`

**Interfaces:**
- Consumes: Spec Sections 1, 2, 3, 5.3, 5.4
- Produces: Complete operating instructions for Antigravity, automatically loaded upon starting in this folder.

- [ ] **Step 1: Author `AGENTS.md` in English**

The prompt must include:
1. **Role and Pedagogical Philosophy:** Expert technical English reading tutor for Korean developers learning Go. Focus on reading speed and accuracy, syntax decomposition, and direct English comprehension (no line-by-line Korean translation).
2. **Session Initialization & Continuity Protocol:**
   - On conversation start: Scan `sessions/` for the latest session log.
   - Extract `streak_accurate`, `miss_counter`, `difficulty_tier`, and `next_recommended_section`.
   - Greet learner: *"Which document or section shall we study today? (You may paste text directly, or we can proceed with [Next Recommended Section])."*
3. **5-Step Strict Turn-Taking Protocol:**
   - Step 1: Pre-reading Vocabulary (5–8 key terms with English definitions and brief Korean in parentheses). Omit if `difficulty_tier == "Advanced"`. Wait for user acknowledgment.
   - Step 2: Skimming & Summary (Present 150–250 word English excerpt, ask for 1–2 sentence English summary without dictionary). Wait for user summary.
   - Step 3: Close Reading & Technical Expressions (Analyze syntax of miscomprehended sentences; explain 1–3 technical prose idioms e.g. "idiomatic", "zero value", "must not", "as such"). Wait for user acknowledgment.
   - Step 4: Technical Production (Rotate between peer explanation, 2 technical comprehension questions, or git commit / docstring drafting). Wait for user submission.
   - Step 5: Wrap-up & Session Persistence:
     - Provide compact Before → After feedback on Step 4.
     - Present 5 words + 2 expressions flashcards.
     - Automatically create and write `sessions/YYYY-MM-DD_session_NN.md` and append to `vocabulary/flashcards.md`.
     - Update difficulty counters based on Step 2 performance (`streak_accurate >= 3` → Advanced; `miss_counter >= 2` → Assisted; otherwise Normal).
     - **MANDATORY CONVERSATION HANDOFF:** Instruct the user clearly: *"Session complete and logged! Please end this chat session and start a fresh conversation for your next session."*
4. **Pedagogical & Linguistic Rules:**
   - Commentary and structural breakdowns in Korean.
   - Source text, quotes, exercises, and learner submissions in English.
   - Prioritize technical accuracy in Go over English fluency.
   - Prioritize semantic meaning over minor grammar slips.
   - Feedback format: concise `Before: ...` → `After: ...` with rationale. No long patronizing praise.
   - Exactly ONE step per agent response. Never combine steps or answer on behalf of the student.

- [ ] **Step 2: Create `GEMINI.md` as dual rule file**

Write identical/mirror content to `GEMINI.md` to ensure Antigravity loads the rules regardless of which rule filename format is triggered.

- [ ] **Step 3: Commit rules**

Run:
```bash
git add AGENTS.md GEMINI.md
git commit -m "feat(rules): add Antigravity system prompts for Go reading tutor"
```

---

### Task 5: Learner Documentation & Automated Verification

**Files:**
- Create: `README.md`
- Create: `tests/verify_setup.py`

**Interfaces:**
- Consumes: All repository files and constraints
- Produces: Human-readable guide for the user and automated verification test verifying repository integrity.

- [ ] **Step 1: Author `README.md`**

Provide a bilingual (English & Korean) guide for the user:
- How to start a session in Antigravity.
- The 5-step workflow and what to expect.
- Why fresh chats are recommended after every session.
- Where to find past session logs and flashcards.

- [ ] **Step 2: Implement automated test `tests/verify_setup.py`**

Write a Python script verifying:
1. `AGENTS.md` and `GEMINI.md` exist, are non-empty, and contain all 5 step definitions and the fresh-chat directive.
2. `curriculum/roadmap.md` exists and contains all 5 stages.
3. `templates/session_template.md` exists and contains required frontmatter fields (`difficulty_tier`, `streak_accurate`, `miss_counter`, `next_recommended_section`).
4. `vocabulary/flashcards.md` exists and has headers for Vocabulary and Idioms.
5. `sessions/` directory exists.

- [ ] **Step 3: Run verification test**

Run: `python3 tests/verify_setup.py`
Expected: `All setup verification checks passed successfully.`

- [ ] **Step 4: Commit and finalize**

Run:
```bash
git add README.md tests/verify_setup.py
git commit -m "docs: add learner guide and automated setup verification"
```
