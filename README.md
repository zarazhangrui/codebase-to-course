# Codebase to Course

**[中文文档](README.zh-CN.md)**

A Claude Code skill that turns any codebase into a beautiful, interactive single-page HTML course. Two modes for two very different audiences.

Point it at a repo. Get back a stunning, self-contained course — with scroll-based navigation, animated visualizations, embedded quizzes, and code-with-plain-English side-by-side translations. Or, if you're a professional engineer evaluating a project for adoption, get a technical due diligence report with architecture decision analysis, critical path traces, risk assessments, and competitive comparisons.

## Two modes

### Beginner Mode — for vibe coders

**Audience:** People who build software by instructing AI coding tools in natural language, without a traditional CS education.

You've built something (or found something cool on GitHub). It works. But you don't really understand *how* it works under the hood. This mode generates a course that teaches you — not by lecturing, but by tracing what happens when you actually use the app.

**Your goals are practical, not academic:**
- Steer AI coding tools better (make smarter architectural decisions)
- Detect when AI is wrong (spot hallucinations, catch bad patterns)
- Debug when AI gets stuck (break out of bug loops)
- Talk to engineers without feeling lost

You're not trying to become a software engineer. You want coding as a superpower.

### Engineer Mode — for technical due diligence

**Audience:** Professional software engineers evaluating whether to adopt an open-source project into their production stack.

You don't need metaphors. You need to know: *Are the design decisions sound? What are the critical paths? Will it work in my scenario? Can it integrate with my stack? How does it compare to alternatives?*

Engineer Mode produces a fundamentally different output — a technical due diligence report with:

- **ADR Cards** — Architecture Decision Records analyzing each key design choice (problem, selected approach, rejected alternatives, trade-off table)
- **Critical Path Traces** — Step-by-step walkthroughs of the most important code execution paths, with engineering commentary referencing exact file names and line numbers
- **Trade-off Matrices** — Color-coded comparison tables evaluating different approaches across multiple dimensions
- **Scenario Judge** — Interactive cards that assess whether the project is a good fit for specific use cases
- **Integration Blueprint** — Complete, copy-pasteable bridge code showing how to integrate with real-world tech stacks
- **Source File Map** — Annotated directory tree classifying each key file as "framework" (skeleton/architectural) or "functional" (concrete implementation), with a recommended 3-5 file reading order
- **Risk Indicators** — Categorized risk items with severity levels (high/medium/low)
- **Verdict Callout** — Each module ends with a clear engineering verdict

## What the course looks like

The output is a **single HTML file** — no dependencies, no setup, works offline. It includes:

- **Scroll-based modules** with progress tracking and keyboard navigation
- **Code ↔ Plain English translations** (Beginner) or **Code ↔ Engineering Commentary** (Engineer) — real code on one side, what it means or why it matters on the other

<img width="720" alt="Code translation block" src="https://github.com/user-attachments/assets/fb9e7fac-05c1-4f98-b80c-46543ef81afc" />

- **Animated visualizations** — data flow animations, group chat between components, architecture diagrams (Beginner Mode)
<img width="720" alt="Animated data flow" src="https://github.com/user-attachments/assets/20fb403e-7dfd-4a47-989b-bbae86ca8041" />

- **Interactive quizzes** that test *application* not memorization ("You want to add favorites — which files change?")
<img width="720" alt="Interactive quiz" src="https://github.com/user-attachments/assets/57706496-9fa8-457a-8450-3da22789951c" />

- **Glossary tooltips** — hover any technical term for a plain-English definition (Beginner Mode)
<img width="720" alt="Glossary tooltip" src="https://github.com/user-attachments/assets/ac2f160a-d73f-4779-97b2-a06fdb5f3227" />

- **Warm, distinctive design** — not the typical purple-gradient AI look. Five accent palettes available (vermillion, coral, teal, amber, forest).

## How to use

### As a Claude Code skill

1. Copy the `codebase-to-course` folder into `~/.claude/skills/`
2. Open any project in Claude Code
3. Say one of:

**For Beginner Mode:**
- *"Turn this codebase into an interactive course"*
- *"Explain this codebase interactively"*
- *"Make a course from this project"*
- *"Teach me how this code works"*

**For Engineer Mode:**
- *"Turn this codebase into an engineer mode report"*
- *"Analyze this codebase for technical due diligence"*
- *"I need an engineering assessment of this project"*
- *"Should we adopt this library? Generate a report"*

The mode is auto-detected from your prompt, or you can specify explicitly.

## Design philosophy

### Build first, understand later

This inverts traditional CS education. The old way: memorize concepts for years → eventually build something → finally see the point (most people quit before step 3). This way: **build something → experience it working → now understand how it works.**

### Show, don't tell

Every screen is at least 50% visual. Max 2-3 sentences per text block. If something can be a diagram, animation, or interactive element — it shouldn't be a paragraph.

### Quizzes test doing, not knowing

No "What does API stand for?" Instead: "A user reports stale data after switching pages. Where would you look first?" Quizzes test whether you can *use* what you learned to solve a new problem.

### No recycled metaphors

Each concept gets a metaphor that fits *that specific idea*. A database is a library with a card catalog. Auth is a bouncer checking IDs. API rate limiting is a nightclub with a capacity limit. Never the same metaphor twice.

### Original code only

Code snippets are exact copies from the real codebase — never modified or simplified. The learner should be able to open the actual file and see the same code they learned from.

## Skill structure

```
codebase-to-course/
├── SKILL.md                          # Main skill instructions (both modes)
└── references/
    ├── _base.html                    # HTML template shell
    ├── _footer.html                  # Shared footer with navigation logic
    ├── styles.css                    # All styles (both modes + engineer elements)
    ├── main.js                       # Interactive logic (quizzes, file map, etc.)
    ├── build.sh                      # Shell script to assemble single HTML file
    ├── design-system.md              # CSS tokens, typography, colors, layout
    ├── interactive-elements.md       # All 25 interactive element patterns
    ├── content-philosophy.md         # Content writing philosophy per mode
    ├── gotchas.md                    # Common mistakes and how to avoid them
    └── module-brief-template.md      # Template for Phase 2.5 planning checkpoint
```

## Changelog

### v2.0.0 — Engineer Mode (2025)

- Added **Engineer Mode**: a completely separate product targeting professional engineers doing technical due diligence
- 8 new interactive element types: ADR Cards, Critical Path Traces, Trade-off Matrix, Scenario Judge, Integration Blueprint, Source File Map, Risk Indicators, Verdict Callout
- **Source File Map**: annotated directory tree classifying 30-50 key files as "framework" (骨架/框架性) vs "functional" (功能/功能性), with recommended reading order
- Code block style shifted from "Code ↔ Plain English" to "Code ↔ Engineering Commentary" for engineer mode
- Added `content-philosophy.md` and `gotchas.md` as separate reference files
- Added Phase 2.5 planning checkpoint for complex codebases
- Forked Phase 3 into sequential (simple) and parallel (complex) build paths
- Updated skill structure to include HTML template, CSS, JS, and build script

### v1.0.0 — Initial release

- Beginner Mode with scroll-based navigation, animated visualizations, interactive quizzes, and glossary tooltips
- Single-file HTML output with no dependencies

---

Built by [Zara](https://x.com/zarazhangrui) with Claude Code. Engineer Mode and Chinese documentation added by [fogdragon](https://github.com/fogdragon) by Qwen3.7-Max.
