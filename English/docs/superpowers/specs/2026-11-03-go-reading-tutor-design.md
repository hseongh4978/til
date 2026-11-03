# Go Technical Documentation English Reading AI Tutor - Design Document

- **Date:** 2026-11-03
- **Topic:** Go Technical Reading Tutor Environment for Antigravity
- **Status:** Draft (Pending Review & Approval)

---

## 1. Intent and Why

The goal of this project is to set up a dedicated workspace environment inside `/home/hseongh/Documents/dev/english` for an AI-powered technical English reading tutor. 
The learner is a Korean developer who is new to Go and wants to simultaneously learn Go language fundamentals and dramatically improve English technical reading comprehension (speed and accuracy without sentence-by-sentence Korean translation).

By using the official Go documentation (`go.dev`), standard library references, and modern Go style guides as reading materials, the tutor trains the learner to parse technical syntax, internalize idiomatic Go prose, and express technical concepts in English.

Each learning session is designed to last 15–20 minutes and cover one coherent document section. To prevent context window bloat and maintain fresh focus, each session is run in a fresh conversation, with continuity preserved through persistent session log files in the repository.

---

## 2. Goals, Non-Goals, Anti-Goals

### Goals
- Provide an automated, high-fidelity AI tutoring environment natively supported by Antigravity CLI via workspace rules (`AGENTS.md` and `GEMINI.md`).
- Implement an updated, modern `go.dev` curriculum reflecting contemporary Go practices (including modern Go modules, Generics, Go Style Decisions, and Standard Library architecture).
- Execute a strict 5-step tutoring methodology per session (Vocabulary Preview → Skimming Summary → Close Reading & Idiomatic Expressions → Technical Output → Wrap-up & Persistent Logging).
- Track learning state (difficulty adjustments, streak counters, and flashcard repository) across sessions via markdown files.
- Enable clean session restarts: each session concludes by writing state to `sessions/` and `vocabulary/flashcards.md`, instructing the learner to start a new chat turn for the next session.
- Write all system prompts, rules, curriculum maps, and template files in clear, professional English.

### Non-Goals
- Building an external web application, mobile app, or GUI.
- Writing code execution sandboxes or interactive Go compilers (reading comprehension and technical commentary are the focus).
- Providing verbatim machine translation from English to Korean (the explicit pedagogical goal is direct comprehension in English).

### Anti-Goals
- Long rambling conversations that fill context memory across days.
- Over-correcting minor conversational grammar at the expense of technical meaning and sentence structure comprehension.
- Presenting deprecated Go 1.0 conventions (e.g. legacy GOPATH, deprecated `How to Write Go Code`) without contextual warnings.

---

## 3. Constraints

- **Language of Settings:** All configuration files (`AGENTS.md`, `GEMINI.md`), prompt templates, curriculum definitions, and internal documentation must be written in English.
- **Language of Interaction during Tutoring:**
  - Explanations and structural breakdown: Korean (to facilitate rapid comprehension for the Korean learner).
  - Source text, technical citations, examples, and learner outputs: English.
- **Environment:** Antigravity CLI workspace (`/home/hseongh/Documents/dev/english`). Antigravity automatically loads `AGENTS.md` and `GEMINI.md` at workspace root.
- **Single-Session Conversations:** One session per conversation. State persistence must rely entirely on repository files (`sessions/` and `vocabulary/flashcards.md`).

---

## 4. Approaches Considered

1. **Approach 1: Minimal Rules-Only Setup (Lightweight)**
   - Single `AGENTS.md` containing prompt, curriculum, and rules.
   - *Trade-off:* Context-free sessions cannot track consecutive success/difficulty scaling, and vocabulary cards are lost between chat resets.
   - *Result:* Rejected.

2. **Approach 2: Structured Workspace with Active Session Logging & Flashcard Repository (Selected)**
   - Root rules (`AGENTS.md`, `GEMINI.md`) defining the tutor persona and workflow.
   - Dedicated `curriculum/roadmap.md` mapping modern `go.dev` resources.
   - `sessions/` directory storing completed session logs with difficulty streak metadata.
   - `vocabulary/flashcards.md` storing cumulative 5-word + 2-idiom review cards.
   - `templates/session_template.md` establishing standardized output structures.
   - Clear protocol for terminating conversations after Step 5 and resuming seamlessly in a new conversation.
   - *Result:* Selected by user.

---

## 5. Detailed Design & Architecture

### 5.1 Repository File Layout

```
/home/hseongh/Documents/dev/english/
├── AGENTS.md                  # Primary system prompt & operating instructions for Antigravity
├── GEMINI.md                  # Symlink or mirror to AGENTS.md for complete platform compatibility
├── README.md                  # Quickstart guide for the learner on how to start sessions
├── curriculum/
│   └── roadmap.md             # Modernized go.dev reading syllabus with URLs and rationale
├── templates/
│   └── session_template.md    # Template for recording each 15-20 min session
├── vocabulary/
│   └── flashcards.md          # Cumulative vocabulary (5 words) and idiom (2 expressions) deck
└── sessions/
    └── .gitkeep               # Directory where YYYY-MM-DD_session_NN.md files are saved
```

### 5.2 Curated go.dev Curriculum (Modernized)

The curriculum improves upon the original prompt by replacing deprecated articles and inserting high-yield official documentation:

1. **Stage 1: Foundations & Fundamentals**
   - *A Tour of Go* (`go.dev/tour/`): Basics, Flow control, More types (structs, slices, maps), Methods and interfaces.
   - *Tutorial: Get started with Go* (`go.dev/doc/tutorial/getting-started`)
   - *Tutorial: Create a Go module* (`go.dev/doc/tutorial/create-module`)
   - *Tutorial: Multi-module workspaces* (`go.dev/doc/tutorial/workspaces`)
2. **Stage 2: Modern Language Features & Tooling**
   - *Tutorial: Getting started with generics* (`go.dev/doc/tutorial/generics`)
   - *Tutorial: Getting started with fuzzing* (`go.dev/doc/tutorial/fuzz`)
   - *Go Modules Reference* (`go.dev/ref/mod`): `go.mod` syntax, version queries, `replace` directives, workspace files.
3. **Stage 3: Idiomatic Go & Style Guidelines**
   - *Go Wiki: Code Review Comments* (`go.dev/wiki/CodeReviewComments`): Core items (Contexts, Declaring Empty Slices, Indent Error Flow, Receiver Names, etc.).
   - *Google Go Style Guide / Style Decisions* (`google.github.io/styleguide/go/`): Modern replacement for legacy styling notes.
   - *Effective Go (Selected Historical Sections)* (`go.dev/doc/effective_go`): Names, Control structures, Concurrency (with modern notes acknowledging superseded parts).
4. **Stage 4: Deep Systems & Standard Library Prose**
   - *Standard Library Documentation:* `io` (Reader/Writer contracts), `errors` (Join, Unwrap, As, Is), `context` (cancellation & timeouts), `sync` (Mutex, WaitGroup).
   - *Go Blog Classic Guides:* "Error handling and Go", "Go Slices: usage and internals", "Go Concurrency Patterns: Pipelines and cancellation".
   - *The Go Memory Model* (`go.dev/ref/mem`): Happens-before relationships, synchronization mechanisms.
   - *Diagnostics* (`go.dev/doc/diagnostics`): Profiling, tracing, runtime metrics.
   - *Go Language Specification (Selected Key Clauses)* (`go.dev/ref/spec`): Types, Type assertions, Channel operations.
5. **Stage 5: Practical API Development**
   - *Tutorial: Developing a RESTful API with Go and Gin* (`go.dev/doc/tutorial/web-service-gin`)

### 5.3 Five-Step Pedagogical Workflow

Each session corresponds to one section (15–20 min) and progresses strictly one step at a time:

- **Session Initialization:**
  - The tutor checks `sessions/` for the most recent log.
  - It extracts the current difficulty level, streak counter, and next target section.
  - Initial greeting: *"Which document or section shall we study today? (You may paste text directly, or I can provide the excerpt from [Next Scheduled Section])."*
- **Step 1: Pre-reading Vocabulary (사전 어휘)**
  - Present 5–8 critical technical terms from the section with English definitions.
  - Short Korean translation provided in parentheses.
  - (Omitted if the learner is at an advanced difficulty tier).
- **Step 2: Skimming & Synthesis (통독 및 영문 요약)**
  - Present the excerpt in English (with notice if approximate).
  - Ask learner to write a 1–2 sentence summary in English without using a dictionary.
  - Wait for response.
- **Step 3: Close Reading & Technical Expressions (정밀 독해 및 표현 해설)**
  - Review learner's summary. If misunderstood, dissect the exact sentence's syntactic structure (Subject/Verb/Modifiers/Clauses).
  - Highlight 1–3 technical prose idioms (e.g., *"idiomatic"*, *"zero value"*, *"must not"*, *"is said to"*, *"as such"*, *"predicated on"*, *"opt-in"*), explaining nuance and cross-document patterns.
  - Wait for learner acknowledgement.
- **Step 4: Active Technical Production (산출 연습)**
  - Rotate dynamically among 3 output exercises:
    1. Explain section concepts to a colleague in 3–5 English sentences.
    2. Answer 2 technical comprehension questions in English.
    3. Draft an English code docstring or Git commit message explaining the change/concept.
  - Wait for response.
- **Step 5: Review, Logging & Fresh Conversation Prompt (마무리 및 세션 영구 저장)**
  - Deliver feedback on Step 4.
  - Output Flashcard Deck: 5 vocabulary words + 2 idiomatic expressions.
  - Automatically create/write the session log to `sessions/YYYY-MM-DD_session_NN.md`.
  - Append the flashcard entries to `vocabulary/flashcards.md`.
  - Preview the next session's topic.
  - **Explicit Handoff Prompt:** *"Session completed and logged! Please end this chat and start a new conversation for your next session."*

### 5.4 Feedback & Difficulty Adjustment Logic

- **Feedback Rules:**
  - Technical Go correctness takes priority over English nuances.
  - Semantic accuracy takes priority over minor grammar slips.
  - Format corrections compactly: `Before: [learner text]` → `After: [idiomatic revision]` with brief rationale.
  - Positive reinforcement is kept concise without conversational fluff.
  - Explanations in Korean, all exercises and excerpts in English.
- **Difficulty State Progression:**
  - `streak_accurate`: +1 if Step 2 summary is accurate without conceptual misunderstandings; reset to 0 if misread.
  - `miss_counter`: +1 if core points are missed twice in a row.
  - *Tier Scaling:*
    - If `streak_accurate >= 3`: Increase excerpt length by 50% and omit Step 1 vocabulary preview.
    - If `miss_counter >= 2`: Halve excerpt length and guide sentence-by-sentence.
    - Normal tier otherwise.

---

## 6. What's Left to the Builder

- Creating the actual markdown files (`AGENTS.md`, `GEMINI.md`, `README.md`, `curriculum/roadmap.md`, `templates/session_template.md`, `vocabulary/flashcards.md`).
- Ensuring `sessions/` directory is created and properly structured.
- Reviewing that all system prompts are written in professional English and fulfill the user's constraints.
