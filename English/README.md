# Go Technical Documentation English Reading Tutor Workspace

An AI-driven technical English reading tutoring environment built inside Antigravity, using official Go documentation (`go.dev`) as reading material.

Go 언어 공식 문서(`go.dev`)를 교재로 삼아 기술 문서 영어 독해력(속도와 정확도, 직독직해)을 기르기 위한 Antigravity 기반 AI 튜터 환경입니다.

---

## 🚀 Quickstart Guide (빠른 시작 가이드)

### 1. How to Start a Session (세션 시작 방법)
1. Open this directory (`/home/hseongh/Documents/dev/english`) in your Antigravity IDE or terminal.
2. Open a new chat session with Antigravity.
3. The tutor will automatically detect your workspace rules (`AGENTS.md`) and greet you with:
   > *"어느 문서/섹션부터 시작할까요? 본문을 붙여 넣으셔도 좋고, 이전 기록에 따른 다음 추천 섹션([Next Recommended Section])으로 바로 진행할 수도 있습니다."*
4. Respond with the section name from the curriculum (e.g. `A Tour of Go: Packages, variables, and functions`) or paste your own excerpt from `go.dev`.

### 2. The 5-Step Session Cycle (5단계 수업 흐름)
Each session covers one section and takes about 15–20 minutes:

| Step | Name | What Happens |
| :--- | :--- | :--- |
| **Step 1** | **Pre-reading (사전 어휘)** | 5–8 key technical terms with English definitions and short Korean meanings. *(Omitted in Advanced tier)* |
| **Step 2** | **Skimming (통독 및 영문 요약)** | Read English excerpt without a dictionary; write a 1–2 sentence summary in English. |
| **Step 3** | **Close Reading (정밀 독해)** | Dissect misunderstood sentence syntax in Korean; learn 1–3 technical idioms & prose patterns. |
| **Step 4** | **Production (산출 연습)** | Rotate between: (1) Peer explanation, (2) Technical Q&A, or (3) Git commit / docstring drafting in English. |
| **Step 5** | **Wrap-up & Save (마무리 및 저장)** | Compact Before → After feedback; flashcards; auto-save session log and vocabulary; prompt to start fresh chat. |

### 3. Fresh Conversation Protocol (대화 새로 시작 원칙)
- **Why?** Running each session in a fresh conversation prevents context bloat, guarantees fast response times, and keeps every session sharp and focused.
- **Continuity:** You don't lose anything! At the end of Step 5, the tutor automatically records your progress in `sessions/` and updates your flashcard deck in `vocabulary/flashcards.md`.
- When you start your next chat, Antigravity reads the latest session log and immediately picks up where you left off.

---

## 📂 Repository Structure (저장소 구조)

```
.
├── AGENTS.md                  # Primary system prompt & rules for Antigravity (English)
├── GEMINI.md                  # Compatibility mirror of AGENTS.md
├── README.md                  # Workspace instructions and usage guide
├── curriculum/
│   └── roadmap.md             # Modern go.dev reading syllabus (5 Stages)
├── templates/
│   └── session_template.md    # Standard format for session logs & difficulty tracking
├── vocabulary/
│   └── flashcards.md          # Cumulative flashcards (5 words + 2 idioms per session)
└── sessions/                  # Daily session logs (YYYY-MM-DD_session_NN.md)
```

---

## 📈 Difficulty Scaling (난이도 조절)

- **Normal Tier:** Standard 150–250 word excerpts, all 5 steps active.
- **Advanced Tier:** Triggered after 3 consecutive accurate summaries (`streak_accurate >= 3`). Excerpt length increases by 50% (250–350 words) and Step 1 vocabulary preview is skipped.
- **Assisted Tier:** Triggered after 2 consecutive miscomprehensions (`miss_counter >= 2`). Excerpt length is halved (80–120 words) with sentence-by-sentence guidance.

---

## 💡 Key Tips for the Learner (학습 팁)
- **Direct English Understanding:** Resist the urge to translate word-by-word into Korean in your head. Try to understand the logical clauses directly in English.
- **Contextual Deduction:** In Step 2, don't look up unknown words in a dictionary. Try guessing their meaning from how they function in the sentence.
- **Focus on Meaning:** The tutor focuses on whether your English expresses the correct technical meaning, rather than nitpicking minor grammatical slips.
