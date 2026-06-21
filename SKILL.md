---
name: codebase-to-course
version: 2.0.0
description: "Turn any codebase into a beautiful, interactive HTML guide. Two modes: 'beginner mode' for non-technical people, 'engineer mode' for developers doing technical due diligence — architecture decisions, critical paths, limitations, and integration analysis."
description_zh: "将任意代码库转化为精美的交互式 HTML 指南。两种模式：'入门模式'面向非技术人员，'工程师模式'面向开发者做技术选型——架构决策、关键路径、局限分析、集成评估。"
category: education
---

# Codebase-to-Course

Transform any codebase into a stunning, interactive guide. Supports **two modes** that produce fundamentally different outputs:

- **Beginner Mode** (default) — Teaches non-technical people how the code works, using metaphors, plain-language explanations, and interactive visualizations.
- **Engineer Mode** — Deep technical analysis for developers doing due diligence on an open-source project. Focuses on architecture decisions, critical code paths, limitations, performance characteristics, and integration patterns.

The output is a **directory** containing a pre-built `styles.css`, `main.js`, per-module HTML files, and an assembled `index.html` — open it directly in the browser with no setup required (only external dependency: Google Fonts CDN).

## Mode Detection

When the skill is triggered, determine which mode to use:

- **Engineer Mode triggers:** User mentions "engineer mode", "工程师模式", "technical analysis", "技术分析", "deep dive", "深度分析", "code review", "for developers", "面向开发者", "技术选型", "evaluation", "评估", "架构分析", "architecture analysis", or explicitly says they are a developer/engineer evaluating the project.
- **Beginner Mode triggers:** User mentions "course", "课程", "tutorial", "教程", "explain simply", "简单解释", "for beginners", "入门", or does NOT specify a mode (default).

If ambiguous, ask the user: "这个分析是面向工程师做技术选型（工程师模式），还是面向非技术人员理解代码（入门模式）？"

## First-Run Welcome

When the skill is first triggered and the user hasn't specified a codebase yet, introduce yourself and explain what you do:

> **I can turn any codebase into an interactive course that teaches how it works — no coding knowledge required.**
>
> Just point me at a project:
> - **A local folder** — e.g., "turn ./my-project into a course"
> - **A GitHub link** — e.g., "make a course from https://github.com/user/repo"
> - **The current project** — if you're already in a codebase, just say "turn this into a course"
>
> I'll read through the code, figure out how everything fits together, and generate a beautiful single-page HTML course with animated diagrams, plain-English code explanations, and interactive quizzes. The whole thing runs in your browser — no setup needed.

If the user provides a GitHub link, clone the repo first (`git clone <url> /tmp/<repo-name>`) before starting the analysis. If they say "this codebase" or similar, use the current working directory.

**For Engineer Mode**, adjust the welcome message:

> **我可以对任意开源项目做深度技术分析——帮你在引入项目之前看清它的架构、能力边界和集成可能性。**
>
> 给我一个项目：
> - **本地路径** — 如 "分析 ./my-project"
> - **GitHub 链接** — 如 "深度分析 https://github.com/user/repo"
>
> 我会逐行阅读核心代码，生成一份交互式技术分析报告，包含架构决策分析、关键代码路径追踪、性能与局限性评估、以及与其他项目的集成方案。

## Who This Is For (Beginner Mode)

The target learner is a **"vibe coder"** — someone who builds software by instructing AI coding tools in natural language, without a traditional CS education. They may have built this project themselves (without looking at the code), or they may have found an interesting open-source project on GitHub and want to understand how it's built. Either way, they don't yet understand what's happening under the hood.

**Assume zero technical background.** Every CS concept — from variables to APIs to databases — needs to be explained in plain language as if the learner has never encountered it. No jargon without definition. No "as you probably know." The tone should be like a smart friend explaining things, not a professor lecturing.

**Their goals are practical, not academic:**
- Have enough technical knowledge to effectively **steer AI coding tools** — make better architectural and tech stack decisions
- **Detect when AI is wrong** — spot hallucinations, catch bad patterns, know when something smells off
- **Intervene when AI gets stuck** — break out of bug loops, debug issues, unblock themselves
- Build more advanced software with **production-level quality and reliability**
- Be **technically fluent** enough to discuss decisions with engineers confidently
- **Acquire the vocabulary of software** — learn the precise technical terms so they can describe requirements clearly and unambiguously to AI coding agents (e.g., knowing to say "namespace package" instead of "shared folder thing")

**They are NOT trying to become software engineers.** They want coding as a superpower that amplifies what they're already good at. They don't need to write code from scratch — they need to *read* it, *understand* it, and *direct* it.

## Why This Approach Works

This skill inverts traditional CS education. The old model is: memorize concepts for years → eventually build something → finally see the point (most people quit before step 3). This model is: **build something first → experience it working → now understand how it works.**

The learner already has context that traditional students don't — they've *used* the app, they know what it does, they may have even described its features in natural language. The course meets them where they are: "You know that button you click? Here's what happens under the hood when you click it."

Every module answers **"why should I care?"** before "how does it work?" The answer to "why should I care?" is always practical: *because this knowledge helps you steer AI better, debug faster, or make smarter architectural decisions.*

The directory-based output is intentional: separating CSS/JS from content means AI never regenerates boilerplate, each module is written independently (keeping output size small and quality high), and the assembled `index.html` works offline with zero setup.

---

## Engineer Mode — 技术选型深度分析

When the user triggers Engineer Mode, **everything changes** — the audience, the curriculum, the interactive elements, the tone, and the analytical depth. Engineer Mode is NOT a "harder version" of Beginner Mode; it's a completely different product.

### Who This Is For (Engineer Mode)

The target reader is a **professional software engineer** evaluating whether to adopt an open-source project. They have:
- Solid CS fundamentals (data structures, design patterns, distributed systems)
- Experience with similar tools/frameworks in the same category
- The ability to read code — they don't need metaphors for basic concepts

**What they need to answer:**
1. **"这个项目的设计决策合理吗？"** — Are the architectural choices sound? What were the alternatives? What trade-offs were made and why?
2. **"关键路径是怎么实现的？"** — Trace the most important code paths line by line. Which 50 lines of code carry 80% of the complexity?
3. **"它在我的场景下能工作吗？"** — What are the performance characteristics, limitations, and failure modes? What configurations matter?
4. **"它能和我的技术栈集成吗？"** — What are the integration points, extension mechanisms, and API contracts? How does it combine with other projects?
5. **"和竞品比，选它还是选别的？"** — Where does it excel, where does it fall short, and what decision framework should guide the choice?

**Tone:** Senior engineer writing a technical due diligence report. Precise, honest, occasionally critical. No cheerleading — if something is a weakness, say so clearly. No hand-holding on basic concepts (don't explain what an API is). But DO explain project-specific conventions and domain-specific terms.

### Engineer Mode Curriculum Structure

Structure as **5-7 modules**, following the engineer's decision journey:

| Module Position | Purpose | Key Question It Answers |
|---|---|---|
| 1 | **架构全景与技术栈** | "What is this project, what's the tech stack, and why was it built this way?" High-level architecture with explicit design philosophy. **Must include a Source File Map** — annotated directory tree classifying every key source file as framework or functional. |
| 2 | **关键路径深度追踪** | "When a complex request comes in, what EXACTLY happens?" Trace 1-2 core operations through every layer, with line-level code references. |
| 3 | **核心设计决策** | "What are the 3-5 most important architectural decisions?" For each: the problem, the chosen approach, alternatives considered, and trade-offs. |
| 4 | **性能特征与局限** | "Where does it break? What are the bottlenecks?" Honest assessment of performance, scalability, edge cases, and known limitations. |
| 5 | **扩展与定制** | "How do I extend it?" Plugin systems, hooks, configuration, subclassing patterns. Show the extension API with real examples. |
| 6 | **集成蓝图** | "How does it combine with other projects?" Concrete integration patterns, API contracts, data format compatibility. |
| 7 | **选型决策** | "Should I use this?" Comparison matrix vs alternatives, scenario-based recommendations, final verdict. |

This is a **framework, not a template**. Adapt modules to the project's nature — a CLI tool might skip Module 6, a framework might emphasize Module 5, a library might expand Module 7.

### Engineer Mode — Phase 1: Deep Analysis

Beyond the standard codebase analysis, Engineer Mode requires **deeper extraction:**

**Additional analysis requirements:**
- **Architecture Decision Records**: For each major design choice, extract: the problem it solves, the chosen approach, 2-3 alternatives that were NOT chosen, and why. Look for comments, ADR files, or infer from code structure.
- **Critical Path Code**: Identify and extract the 3-5 most important code paths (the ones that handle the core operations). Include exact file paths and line numbers. These become the "deep trace" screens.
- **Performance-relevant Code**: Find configuration parameters that affect performance (batch sizes, timeouts, concurrency limits, buffer sizes). Extract the code that implements throttling, caching, batching.
- **Extension Points**: Catalog all extension mechanisms — plugin interfaces, abstract base classes meant for subclassing, hook functions, event systems, configuration-driven behavior.
- **Failure Modes**: Search for error handling patterns, retry logic, fallback mechanisms, known issues (from comments, TODOs, issue references).
- **Integration Surface**: Map all external interfaces — REST APIs, SDK methods, data formats, protocol support, webhook systems.
- **Source File Classification**: For every key directory and file in the project, classify it as **framework** (structural/architectural — the skeleton that everything else hangs on) or **functional** (feature-specific — implements a particular capability). Extract file paths, sizes (LOC), and a one-line description of each. This becomes the Source File Map in Module 1.

**Comparative context**: Read the project's README comparison section (if any), check if it mentions competitors, and note its self-positioning.

### Engineer Mode — Module Design Principles

- **Code is the evidence.** Every claim ("this project handles X well") must be backed by a specific code snippet with file path and line numbers. No hand-waving.
- **Show the alternatives.** For every major design decision, mention what could have been done differently and why it wasn't. This is what separates analysis from documentation.
- **Be honest about weaknesses.** Every project has them. Engineers trust analyses that acknowledge limitations. Use `callout-warning` for known issues.
- **Quantify when possible.** "Handles 10K documents/hour on a single GPU" beats "handles documents quickly." Extract benchmarks, performance tests, or compute estimates from the code.
- **Integration is actionable.** Don't just describe APIs — show concrete integration code examples (how to connect Project A's output to Project B's input).

### Engineer Mode — Mandatory Interactive Elements

**These elements are REQUIRED in every Engineer Mode guide (in addition to the standard set):**

- **Architecture Decision Cards (ADR Cards)** — at least 3 across the guide. Each card shows: the problem, the chosen solution, 2-3 alternatives, the trade-off analysis, and the key code that implements it.
- **Critical Path Traces** — at least 2 across the guide. Step-by-step code walkthroughs of the most important operations, with engineering commentary explaining WHY each step exists, not just WHAT it does.
- **Trade-off Matrix** — at least 1 across the guide. A comparison table evaluating different approaches/configurations across multiple dimensions (performance, complexity, memory, accuracy).
- **Scenario Judge** — at least 1 across the guide. Present 3-4 real-world scenarios and evaluate the project's suitability for each, with honest pros/cons.
- **Integration Blueprint** — at least 1 across the guide (if the project has integration points). Show how data flows between this project and other systems, with code examples.
- **Source File Map** — exactly 1, placed in Module 1. An annotated directory tree that classifies every key source file/directory as "framework" (skeleton/architectural) or "functional" (feature implementation). This helps developers quickly orient themselves in the codebase — knowing which files to read first for architecture understanding vs which to read for feature implementation.

**Standard elements still required:** Data Flow Animation, Quizzes (focused on engineering judgment), Code blocks (with engineering commentary, not plain-language translation), Glossary Tooltips (only for project-specific or domain-specific terms, not basic CS).

### Engineer Mode — Code Block Style

Instead of the Beginner Mode "Code ↔ Plain English" translation, Engineer Mode uses **Code ↔ Engineering Commentary:**

- **Left panel**: Real code from the codebase (exact, unmodified)
- **Right panel**: Engineering analysis — WHY this code is written this way, what design pattern it implements, what trade-off it makes, what could go wrong, what alternative approaches exist.

The right panel assumes the reader CAN read code. It adds value by providing context, analysis, and judgment that the code alone doesn't convey.

**HTML pattern:** Use `translation-block` with the label changed from "PLAIN ENGLISH" to "工程分析" / "ENGINEERING ANALYSIS".

### Engineer Mode — Quiz Design

Quizzes test **engineering judgment**, not factual recall:

**Good quiz questions:**
- "Your service needs to process 100K documents/hour. Based on the architecture, which configuration would you choose?"
- "The team wants to add a custom document parser. Based on the extension system, what's the correct approach?"
- "You've noticed search results are missing relevant documents. Based on the retrieval pipeline, where would you look first?"
- "Project A outputs format X, Project B expects format Y. What's the most reliable bridge?"

### Engineer Mode — Design Differences

- **More code per screen** — Allow larger code blocks (15-25 lines) when the analysis requires it.
- **Comparison tables** — Engineers think in trade-offs. Use tables to compare approaches, configurations, and alternatives.
- **"Verdict" callouts** — At the end of each module: "This approach is [strong/adequate/weak] for [scenario] because [reason]."
- **Risk indicators** — Use colored badges: 🟢 Low Risk, 🟡 Medium Risk, 🔴 High Risk for identified limitations and failure modes.

### Engineer Mode — Source File Map

Every Engineer Mode guide **must include a Source File Map** in Module 1 (架构全景). This is an annotated directory tree that classifies each key source file/directory into one of two categories:

- **框架性文件 (Framework)** — The skeleton. Abstract base classes, interfaces, configuration systems, plugin loaders, middleware, routing, dependency injection, lifecycle management. These files define HOW the project is structured. Reading them gives you the architecture. Examples: `base.py`, `registry.py`, `settings.py`, `__init__.py` (with imports), `pipeline.py` (base class), `factory.py`.

- **功能性文件 (Functional)** — The flesh. Concrete implementations of specific features, specific parsers, specific models, specific API endpoints. These files define WHAT the project does. Reading them gives you the capabilities. Examples: `pdf_parser.py`, `ocr_model.py`, `openai_llm.py`, `chunk_app.py`, `table_recognizer.py`.

**Classification rules:**
- A file that defines abstract interfaces → Framework
- A file that implements a specific feature against those interfaces → Functional
- A file that wires things together (factory, registry, config loader) → Framework
- A file that contains business logic for one use case → Functional
- Entry points (`main.py`, `app.py`, `cli.py`) → Framework (they define the startup architecture)
- Test files → Functional (they test specific features), but skip listing individual tests
- Config/Schema files → Framework (they define the configuration contract)

**What to show:**
- Top 30-50 most important files/directories (don't list every file — focus on the ones a developer would actually need to read)
- For each: file path, role tag (框架/功能), one-line description, approximate LOC
- Group by directory, with directory-level summaries
- Highlight the "start here" files — the 3-5 files a developer should read first to understand the architecture
- Use the existing `file-tree` visual element, enhanced with role badges

**Why this matters:** Developers approaching a new codebase don't start from architecture diagrams — they start from the file listing. A Source File Map bridges the gap: "I see 500 files, but which 5 should I read first to understand how this works?" Without it, the analysis feels abstract ("看山不见山" — seeing the mountain but not understanding its composition).

### Engineer Mode — Module 7: Selection Decision Framework

If the guide includes a comparison/selection module (Module 7), it should contain:

1. **Capability Matrix** — Feature-by-feature comparison with 2-3 alternatives in the same category.
2. **Scenario Recommendations** — "If your use case is X, choose this project. If Y, consider alternative Z instead."
3. **Integration Map** — If analyzing multiple related projects, show how they can be combined and which combinations make sense.
4. **Migration Path** — If the engineer is currently using a different tool, what does migration look like?
5. **Final Verdict** — A clear, opinionated recommendation with caveats.

---

## The Process

### Phase 1: Codebase Analysis

Before writing course HTML, deeply understand the codebase. Read all the key files, trace the data flows, identify the "cast of characters" (main components/modules), and map how they communicate. Thoroughness here pays off — the more you understand, the better the course.

**What to extract:**
- The main "actors" (components, services, modules) and their responsibilities
- The primary user journey (what happens when someone uses the app end-to-end)
- Key APIs, data flows, and communication patterns
- Clever engineering patterns (caching, lazy loading, error handling, etc.)
- Real bugs or gotchas (if visible in git history or comments)
- The tech stack and why each piece was chosen

**Figure out what the app does yourself** by reading the README, the main entry points, and the UI code. Don't ask the user to explain the product — they may not be familiar with it either. The course should open by explaining what the app does in plain language (a brief "here's what this thing does and why it's interesting") before diving into how it works. The first module should start with a concrete user action — "imagine you paste a YouTube URL and click Analyze — here's what happens under the hood."

### Phase 2: Curriculum Design

Structure the course as **4-6 modules**. Most courses need 4-6. Only go to 7-8 if the codebase genuinely has that many distinct concepts worth teaching. Fewer, better modules beat more, thinner ones.

The arc always starts from what the learner already knows (the user-facing behavior) and moves toward what they don't (the code underneath). Think of it as zooming in: start wide with the experience, then progressively peel back layers.

| Module Position | Purpose | Why it matters for a vibe coder |
|---|---|---|
| 1 | "Here's what this app does — and what happens when you use it" | Start with the product (what it does, why it's interesting), then trace a core user action into the code. Grounds everything in something concrete. |
| 2 | Meet the actors | Know which components exist so you can tell AI "put this logic in X, not Y" |
| 3 | How the pieces talk | Understand data flow so you can debug "it's not showing up" problems |
| 4 | The outside world (APIs, databases) | Know what's external so you can evaluate costs, rate limits, and failure modes |
| 5 | The clever tricks | Learn patterns (caching, chunking, error handling) so you can request them from AI |
| 6 | When things break | Build debugging intuition so you can escape AI bug loops |
| 7 | The big picture | See the full architecture so you can make better decisions about what to build next |

This is a **menu, not a checklist**. Pick the modules that serve the codebase — a simple CLI tool needs 4, not 7. Adapt the arc to the codebase's complexity.

**The key principle:** Every module should connect back to a practical skill — steering AI, debugging, making decisions. If a module doesn't help the learner DO something better, cut it or reframe it until it does.

**Each module should contain:**
- 3-6 screens (sub-sections that flow within the module)
- At least one code-with-English translation
- At least one interactive element (quiz, visualization, or animation)
- One or two "aha!" callout boxes with universal CS insights
- A metaphor that grounds the technical concept in everyday life — but NEVER reuse the same metaphor across modules, and NEVER default to the "restaurant" metaphor (it's overused). Pick metaphors that organically fit the specific concept. The best metaphors feel *inevitable* for the concept, not forced.

**Mandatory interactive elements (every course must include ALL of these):**
- **Group Chat Animation** — at least one across the course. These are the iMessage/WeChat-style conversations between components. They're one of the most engaging elements and must always appear, even if you have to creatively frame a module's concept as a conversation between actors.
- **Message Flow / Data Flow Animation** — at least one across the course. The step-by-step packet animation between actors. If the codebase has any kind of request/response, data pipeline, or multi-step process, animate it. Every codebase has data flowing somewhere — find it.
- **Code ↔ English Translation Blocks** — at least one per module (already required above, but reiterating: this is non-negotiable).
- **Quizzes** — at least one per module (multiple-choice, scenario, drag-and-drop, or spot-the-bug — any quiz type counts).
- **Glossary Tooltips** — on every technical term, first use per module.

These five element types are the backbone of every course. Other interactive elements (architecture diagrams, layer toggles, pattern cards, etc.) are optional and should be added when they fit. But the five above must ALWAYS be present — no exceptions.

**Do NOT present the curriculum for approval — just build it.** The user wants a course, not a planning document. Design the curriculum internally, then go straight to building. If they want changes, they'll tell you after seeing the result.

**After designing the curriculum, decide which build path to use:**

- **Simple codebase** (single-purpose CLI, small web app, library, one clear entry point, 5 or fewer modules) → go directly to Phase 3 Sequential.
- **Complex codebase** (full-stack app, multiple services, content-heavy site, monorepo, or 6+ modules) → go to Phase 2.5 first, then Phase 3 Parallel.

### Phase 2.5: Module Briefs (complex codebases only)

For complex codebases, write a brief for each module before writing any HTML. This is the critical step that enables parallel writing — each brief gives an agent everything it needs without re-reading the codebase.

Read `references/module-brief-template.md` for the template structure. Read `references/content-philosophy.md` for the content rules that should guide brief writing.

**For each module, write a brief to `course-name/briefs/0N-slug.md` containing:**
- Teaching arc (metaphor, opening hook, key insight)
- Pre-extracted code snippets (copy-pasted from the codebase with file paths and line numbers)
- Interactive elements checklist with enough detail to build them
- Which sections of which reference files the writing agent needs
- What the previous and next modules cover (for transitions)

The code snippets are the critical token-saving step. By pre-extracting them into the brief, writing agents never need to read the codebase at all.

### Phase 3: Build the Course

The course output is a **directory**, not a single file. All CSS and JS are pre-built reference files — never regenerate them. Your job is to write only the HTML content.

**Output structure:**
```
course-name/
  styles.css       ← copied verbatim from references/styles.css
  main.js          ← copied verbatim from references/main.js
  _base.html       ← customized shell (title, accent color, nav dots)
  _footer.html     ← copied verbatim from references/_footer.html
  build.sh         ← copied verbatim from references/build.sh
  briefs/          ← module briefs (complex codebases only, can delete after build)
  modules/
    01-intro.html
    02-actors.html
    ...
  index.html       ← assembled by build.sh (do not write manually)
```

**Step 1 (both paths): Setup** — Create the course directory. Copy these four files verbatim using Read + Write (do not regenerate their contents):
- `references/styles.css` → `course-name/styles.css`
- `references/main.js` → `course-name/main.js`
- `references/_footer.html` → `course-name/_footer.html`
- `references/build.sh` → `course-name/build.sh`

**Step 2 (both paths): Customize `_base.html`** — Read `references/_base.html`, then write it to `course-name/_base.html` with exactly three substitutions:
- Both instances of `COURSE_TITLE` → the actual course title
- The four `ACCENT_*` placeholders → the chosen accent color values (pick one palette from the comments in `_base.html`)
- `NAV_DOTS` → one `<button class="nav-dot" ...>` per module

**Step 3: Write modules** — This is where the paths diverge.

#### Sequential path (simple codebases)

Read `references/content-philosophy.md` and `references/gotchas.md`. Then write modules one at a time. For each module, write `course-name/modules/0N-slug.html` containing only the `<section class="module" id="module-N">` block and its contents. Do not include `<html>`, `<head>`, `<body>`, `<style>`, or `<script>` tags.

Read `references/interactive-elements.md` for HTML patterns for each interactive element type. Read `references/design-system.md` for visual conventions.

#### Parallel path (complex codebases)

Dispatch modules to subagents in batches of up to 3. Each agent receives:
- Its module brief (from `course-name/briefs/`)
- `references/content-philosophy.md` and `references/gotchas.md`
- Only the sections of `references/interactive-elements.md` and `references/design-system.md` listed in the brief

Each agent writes its module file(s) to `course-name/modules/`. Short modules (3 screens, one quiz) can be paired — two briefs given to one agent.

**What agents do NOT receive:** the full codebase (snippets are in the brief), SKILL.md, other modules' briefs, or unneeded reference file sections.

After all agents finish, do a quick consistency check in the main context: nav dots match modules, transitions between modules are coherent, no obvious tone shifts.

**Step 4 (both paths): Assemble** — Run `build.sh` from the course directory:
```bash
cd course-name && bash build.sh
```
This produces `index.html`. Open it in the browser.

**Critical rules:**
- **Never regenerate** `styles.css` or `main.js` — always copy from references
- Module files contain only `<section>` content — no boilerplate
- Use CSS `scroll-snap-type: y proximity` (NOT `mandatory`)
- Use `min-height: 100dvh` with `100vh` fallback on `.module`
- Interactive element JS is in `main.js`; wire up via `data-*` attributes and CSS class names as shown in `references/interactive-elements.md`
- Chat containers need `id` attributes; flow animations need `data-steps='[...]'` JSON on `.flow-animation`

### Phase 4: Review and Open

After running `build.sh`, open `index.html` in the browser. Walk the user through what was built and ask for feedback on content, design, and interactivity.

---

## Design Identity

The visual design should feel like a **beautiful developer notebook** — warm, inviting, and distinctive. Read `references/design-system.md` for the full token system, but here are the non-negotiable principles:

- **Warm palette**: Off-white backgrounds (like aged paper), warm grays, NO cold whites or blues
- **Bold accent**: One confident accent color (vermillion, coral, teal — NOT purple gradients)
- **Distinctive typography**: Display font with personality for headings (Bricolage Grotesque, or similar bold geometric face — NEVER Inter, Roboto, Arial, or Space Grotesk). Clean sans-serif for body (DM Sans or similar). JetBrains Mono for code.
- **Generous whitespace**: Modules breathe. Max 3-4 short paragraphs per screen.
- **Alternating backgrounds**: Even/odd modules alternate between two warm background tones for visual rhythm
- **Dark code blocks**: IDE-style with Catppuccin-inspired syntax highlighting on deep indigo-charcoal (#1E1E2E)
- **Depth without harshness**: Subtle warm shadows, never black drop shadows

---

## Reference Files

The `references/` directory contains detailed specs. **Read them only when you reach the relevant phase** — not upfront. This keeps context lean.

- **`references/content-philosophy.md`** — Visual density rules, metaphor guidelines, quiz design, tooltip rules, code translation guidance. Read during Phase 2.5 (briefs) and Phase 3 (writing modules).
- **`references/gotchas.md`** — Common failure points checklist. Read during Phase 3 and Phase 4 (review).
- **`references/module-brief-template.md`** — Template for Phase 2.5 module briefs. Read only for complex codebases using the parallel path.
- **`references/design-system.md`** — Complete CSS custom properties, color palette, typography scale, spacing system, shadows, animations, scrollbar styling. Read during Phase 3 when writing module HTML.
- **`references/interactive-elements.md`** — Implementation patterns for every interactive element: drag-and-drop quizzes, multiple-choice quizzes, code↔English translations, group chat animations, message flow visualizations, architecture diagrams, pattern cards, callout boxes. Read the relevant sections during Phase 3.
