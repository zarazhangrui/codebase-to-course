# Codebase to Course

A Claude Code skill that turns any codebase into a beautiful, interactive single-page HTML course.

Point it at a repo. Get back a stunning, self-contained course that teaches how the code works - with scroll-based navigation, animated visualizations, embedded quizzes, and code-with-plain-English side-by-side translations.

## Who is this for?

**"Vibe coders"** - people who build software by instructing AI coding tools in natural language, without a traditional CS education.

You've built something (or found something cool on GitHub). It works. But you don't really understand *how* it works under the hood. This skill generates a course that teaches you - not by lecturing, but by tracing what happens when you actually use the app.

**Your goals are practical, not academic:**
- Steer AI coding tools better (make smarter architectural decisions)
- Detect when AI is wrong (spot hallucinations, catch bad patterns)
- Debug when AI gets stuck (break out of bug loops)
- Talk to engineers without feeling lost

You're not trying to become a software engineer. You want coding as a superpower.

## What the course looks like

The output is a **single HTML file** - no dependencies, no setup, works offline. It includes:

- **Scroll-based modules** with progress tracking and keyboard navigation
- **Code <-> Plain English translations** - real code on the left, what it means on the right
<img width="720" alt="Code translation block" src="https://github.com/user-attachments/assets/fb9e7fac-05c1-4f98-b80c-46543ef81afc" />

- **Animated visualizations** - data flow animations, group chat between components, architecture diagrams
<img width="720" alt="Animated data flow" src="https://github.com/user-attachments/assets/20fb403e-7dfd-4a47-989b-bbae86ca8041" />

- **Interactive quizzes** that test *application* not memorization ("You want to add favorites - which files change?")
<img width="720" alt="Interactive quiz" src="https://github.com/user-attachments/assets/57706496-9fa8-457a-8450-3da22789951c" />

- **Glossary tooltips** - hover any technical term for a plain-English definition
<img width="720" alt="Glossary tooltip" src="https://github.com/user-attachments/assets/ac2f160a-d73f-4779-97b2-a06fdb5f3227" />

  
- **Warm, distinctive design** - not the typical purple-gradient AI look

## How to use

### As a Claude Code skill

1. Copy the `codebase-to-course` folder into `~/.claude/skills/`
2. Open any project in Claude Code
3. Say: *"Turn this codebase into an interactive course"*

### Trigger phrases

- "Turn this into a course"
- "Explain this codebase interactively"
- "Make a course from this project"
- "Teach me how this code works"
- "Interactive tutorial from this code"

## Design philosophy

### Build first, understand later

This inverts traditional CS education. The old way: memorize concepts for years -> eventually build something -> finally see the point (most people quit before step 3). This way: **build something -> experience it working -> now understand how it works.**

## Security note

This repository contains documentation and skill instructions only. It does not ship executable binaries, install scripts, or runtime dependencies.

Security posture for generated courses:
- Secrets must be redacted from snippets (`[REDACTED]` placeholders)
- `.env`, private keys, tokens, and passwords must never be included in output
- External repositories are treated as untrusted input and should be analyzed from trusted local checkouts

### Show, don't tell

Every screen is at least 50% visual. Max 2-3 sentences per text block. If something can be a diagram, animation, or interactive element — it shouldn't be a paragraph.

### Quizzes test doing, not knowing

No "What does API stand for?" Instead: "A user reports stale data after switching pages. Where would you look first?" Quizzes test whether you can *use* what you learned to solve a new problem.

### No recycled metaphors

Each concept gets a metaphor that fits *that specific idea*. A database is a library with a card catalog. Auth is a bouncer checking IDs. API rate limiting is a nightclub with a capacity limit. Never the same metaphor twice.

### Faithful code, safe output

Snippets should stay faithful to the real implementation, but sensitive values must never be exposed. If source code contains credentials or private values, redact only the secret portion (for example `API_KEY=[REDACTED]`) while preserving surrounding logic.

Never include `.env` files, private keys, tokens, passwords, or other secrets in generated course output.

### Untrusted repositories

External repositories are treated as untrusted input. Prefer analyzing a local checkout the user already trusts. Do not auto-clone and execute arbitrary repo code as part of course generation.

## Skill structure

```
codebase-to-course/
├── SKILL.md                          # Main skill instructions
└── references/
    ├── design-system.md              # CSS tokens, typography, colors, layout
    └── interactive-elements.md       # Quiz, animation, and visualization patterns
```


---

Built by [Zara](https://x.com/zarazhangrui) with Claude Code.
