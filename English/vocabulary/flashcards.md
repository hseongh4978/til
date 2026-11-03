# Cumulative Vocabulary & Technical Idioms Deck

This repository stores all cumulative vocabulary words (5 per session) and idiomatic expressions (2 per session) generated during technical reading sessions.

---

## 1. Technical Terms Bank

| Term | POS | English Definition | Korean Meaning | Session | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *Example: zero value* | noun | The default value assigned to an uninitialized variable in Go | 기본값 | Initial | Mastered |
| `exported name` | noun | An identifier starting with an uppercase letter that is accessible outside its defining package | 패키지 외부 접근 가능한 대문자 식별자 | Session 01 | Learning |
| `naked return` | noun | A return statement without explicit arguments that returns the current values of named return variables | 이름 붙은 반환값의 인수 없는 return문 | Session 01 | Learning |
| `zero value` | noun | The default value automatically assigned to a variable declared without an explicit initial value | 초기화 없는 변수의 기본값 | Session 01 | Learning |
| `short assignment statement` | noun | A syntactic construct (`:=`) used inside functions to declare and initialize variables with inferred types | 함수 내 타입 추론 단축 변수 선언문 | Session 01 | Learning |
| `type inference` | noun | The compiler's automatic deduction of an expression's data type from the assigned value | 대입된 값 기반 타입 자동 추론 | Session 01 | Learning |

---

## 2. Technical Idioms & Phrasal Patterns

| Expression / Idiom | Pragmatic Nuance in Technical Docs | Example Sentence from Go Documentation | Session |
| :--- | :--- | :--- | :--- |
| *Example: is said to* | Used to state a formal specification definition without asserting physical causality | *"A variable is said to be initialized when its storage has been allocated..."* | Initial |
| *Example: must not* | Expresses absolute normative prohibition (RFC 2119 keyword equivalent) | *"Code must not assume any evaluation order of goroutines."* | Initial |
| `in place of` | Used to denote syntactic substitution or a more concise alternative without semantic change | *"Inside a function, the := short assignment statement can be used in place of a var declaration..."* | Session 01 |
| `harm readability` | Used in Go guidelines to strongly discourage patterns that impede code clarity (SHOULD NOT equivalent) | *"Naked return statements should be used only in short functions, as they can harm readability in longer programs."* | Session 01 |

---

## 3. Spaced Repetition Review Queue

Review previous session items every 3–5 sessions.

- [ ] Review Sessions 1–5 Deck
- [ ] Review Sessions 6–10 Deck
- [ ] Review Sessions 11–15 Deck
- [ ] Review Sessions 16–20 Deck
