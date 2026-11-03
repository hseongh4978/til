# Official Go Documentation Reading Roadmap for Technical English Mastery

This syllabus is designed for Korean developers who are learning Go and aiming to achieve rapid, accurate comprehension of English technical documentation directly without line-by-line translation into Korean.

Each module is broken down into bite-sized 15–20 minute reading sections (~150–250 words each).

---

## Pedagogical Objectives
1. **Direct Parsing:** Internalize English syntactic sentence structures (relative clauses, participle phrases, passive constraints) standard in systems documentation.
2. **Technical Idioms:** Master normative language conventions (RFC 2119 keywords like *MUST*, *SHOULD*, *OPTIONAL*; idioms like *zero value*, *idiomatic*, *predicated on*, *in terms of*, *opt-in*).
3. **Go Conceptual Accuracy:** Ensure language mastery reinforces idiomatic Go design, concurrency models, and standard library conventions.

---

## Stage 1: Foundations & Fundamentals

Focuses on foundational syntax, type mechanics, and modern workspace mechanics. Replaces legacy *How to Write Go Code* with modern official module workflows.

### 1.1 A Tour of Go
- **URL:** [https://go.dev/tour/](https://go.dev/tour/)
- **Sections:**
  - `tour-01`: Packages, variables, and functions (`tour/basics/1` – `tour/basics/16`)
    - *Key Terms:* export, package-level, naked return, immutable, type inference
  - `tour-02`: Flow control statements (`tour/flowcontrol/1` – `tour/flowcontrol/14`)
    - *Key Terms:* post statement, short statement, implicit break, deferred call
  - `tour-03`: More types — Structs, slices, and maps (`tour/moretypes/1` – `tour/moretypes/26`)
    - *Key Terms:* struct field, slice literal, slice bounds, capacity vs. length, nil slice, mutating maps
  - `tour-04`: Methods and interfaces (`tour/methods/1` – `tour/methods/26`)
    - *Key Terms:* method receiver, pointer receiver, implicit implementation, interface value, type assertion, type switch, empty interface

### 1.2 Official Module Tutorials
- **URL:** [https://go.dev/doc/tutorial/getting-started](https://go.dev/doc/tutorial/getting-started)
- **Sections:**
  - `tut-01`: Tutorial: Get started with Go (`doc/tutorial/getting-started`)
    - *Key Terms:* module path, dependency management, entry point, build cache
  - `tut-02`: Tutorial: Create a Go module (`doc/tutorial/create-module`)
    - *Key Terms:* exported function, error handling convention, unit testing, test table
  - `tut-03`: Tutorial: Multi-module workspaces (`doc/tutorial/workspaces`)
    - *Key Terms:* workspace directive (`go.work`), replace directive, local override, discrete modules

---

## Stage 2: Modern Language Features & Tooling

Covers modern language extensions introduced in Go 1.18+ and official tooling standards.

### 2.1 Generics & Fuzzing
- **URL:** [https://go.dev/doc/tutorial/generics](https://go.dev/doc/tutorial/generics)
- **Sections:**
  - `gen-01`: Getting started with generics (`doc/tutorial/generics`)
    - *Key Terms:* type parameter, type constraint, `any`, `comparable`, type inference, generic instantiation
  - `fuzz-01`: Getting started with fuzzing (`doc/tutorial/fuzz`)
    - *Key Terms:* fuzz target, seed corpus, randomized testing, mutation, crash repro

### 2.2 Go Modules Reference
- **URL:** [https://go.dev/ref/mod](https://go.dev/ref/mod)
- **Sections:**
  - `mod-01`: The `go.mod` file format (`ref/mod#go-mod-file`)
    - *Key Terms:* module directive, require directive, indirect dependency, retract directive
  - `mod-02`: Minimal Version Selection (MVS) & Replace Directives (`ref/mod#minimal-version-selection`)
    - *Key Terms:* semantic import versioning, pseudo-version, build list, transitive dependency

---

## Stage 3: Idiomatic Go & Style Guidelines

Focuses on authoritative code design and stylistic conventions. 

> **Curriculum Note:** *Effective Go* was written for Go 1.0 (2009). The Go team recommends the *Go Style Decisions* guide and *Code Review Comments* as authoritative modern references. Selected sections of *Effective Go* are included with historical context.

### 3.1 Go Wiki: Code Review Comments
- **URL:** [https://go.dev/wiki/CodeReviewComments](https://go.dev/wiki/CodeReviewComments)
- **Sections:**
  - `crc-01`: Contexts, Declaring Empty Slices, and Indent Error Flow
    - *Key Terms:* pass as first parameter, nil slice vs. empty slice allocation, early return, guard clause
  - `crc-02`: Error Strings, Handle Errors, and In-Band Errors
    - *Key Terms:* lowercase error string, sentinel error, wrapped error, multiple return values
  - `crc-03`: Receiver Names, Variable Names, and Synchronous Functions
    - *Key Terms:* short mnemonic receiver, acronym capitalization, unbuffered channel concurrency

### 3.2 Google Go Style Guide (Style Decisions)
- **URL:** [https://google.github.io/styleguide/go/decisions](https://google.github.io/styleguide/go/decisions)
- **Sections:**
  - `style-01`: Clarity, Simplicity, and Naming conventions
    - *Key Terms:* mental model, stuttering package names, self-documenting code
  - `style-02`: Error handling and Pointer vs. Value Semantics
    - *Key Terms:* opaque error, actionable error, value receiver vs. pointer receiver, copying mutexes

### 3.3 Effective Go (Historical & Selected Modern Topics)
- **URL:** [https://go.dev/doc/effective_go](https://go.dev/doc/effective_go)
- **Sections:**
  - `eff-01`: Formatting, Commentary, and Names (`doc/effective_go#formatting`)
    - *Key Terms:* `gofmt`, package doc comment, docstring conventions, getter names
  - `eff-02`: Control Structures and Redeclaration (`doc/effective_go#control-structures`)
    - *Key Terms:* comma-ok idiom, short variable declaration scope, shadowing

---

## Stage 4: Deep Systems, Concurrency & Standard Library Prose

Develops high-level comprehension of concurrency semantics, synchronization primitives, memory specifications, and diagnostic profiles.

### 4.1 Core Standard Library Package Documentation
- **URL:** [https://pkg.go.dev/std](https://pkg.go.dev/std)
- **Sections:**
  - `std-01`: Package `io` (`pkg.go.dev/io`)
    - *Key Terms:* streaming interface, `Reader` contract, `Writer` contract, `EOF` sentinel, non-blocking I/O
  - `std-02`: Package `errors` (`pkg.go.dev/errors`)
    - *Key Terms:* error wrapping, `errors.Is`, `errors.As`, `errors.Join`, unwrapping tree
  - `std-03`: Package `context` (`pkg.go.dev/context`)
    - *Key Terms:* cancellation propagation, deadline, timeout, request-scoped metadata, goroutine leak
  - `std-04`: Package `sync` & `sync/atomic` (`pkg.go.dev/sync`)
    - *Key Terms:* mutual exclusion (`sync.Mutex`), read-write lock, `sync.Once`, memory barrier

### 4.2 Go Blog Deep Dives
- **URL:** [https://go.dev/blog/](https://go.dev/blog/)
- **Sections:**
  - `blog-01`: "Go Slices: usage and internals"
    - *Key Terms:* backing array, slice header, reallocation, memory aliasing
  - `blog-02`: "Go Concurrency Patterns: Pipelines and cancellation"
    - *Key Terms:* pipeline stage, fan-out, fan-in, bounded concurrency, done channel

### 4.3 The Go Memory Model
- **URL:** [https://go.dev/ref/mem](https://go.dev/ref/mem)
- **Sections:**
  - `mem-01`: Happens-Before Relationships & Core Model
    - *Key Terms:* happens-before, sequential consistency, shared memory, race condition, data race
  - `mem-02`: Synchronization Mechanics (Channels, Locks, Once)
    - *Key Terms:* channel send happens before receive, unlock happens before lock, initialization order

### 4.4 Diagnostics & Profiling
- **URL:** [https://go.dev/doc/diagnostics](https://go.dev/doc/diagnostics)
- **Sections:**
  - `diag-01`: Profiling, Tracing, and Debugging
    - *Key Terms:* CPU profile, heap profile, block profile, execution tracer (`go tool trace`), goroutine dump

### 4.5 The Go Language Specification (Selected Clauses)
- **URL:** [https://go.dev/ref/spec](https://go.dev/ref/spec)
- **Sections:**
  - `spec-01`: Type Identity, Assignability, and Conversions
    - *Key Terms:* defined type, underlying type, assignability rules, explicit conversion
  - `spec-02`: Channel Types, Send/Receive Statements, and Select
    - *Key Terms:* buffered channel, unbuffered channel, blocking send, select pseudorandom choice

---

## Stage 5: Practical Web Services & APIs

Integrates reading comprehension with real-world server architectures.

### 5.1 Developing a RESTful API with Go and Gin
- **URL:** [https://go.dev/doc/tutorial/web-service-gin](https://go.dev/doc/tutorial/web-service-gin)
- **Sections:**
  - `gin-01`: Designing API endpoints & Data modeling
    - *Key Terms:* route handler, HTTP method verbs, JSON struct tags, payload serialization
  - `gin-02`: Request binding, status codes, and query params
    - *Key Terms:* model binding, query string parameter, status code semantics, context write
