# Gotchas — Common Failure Points

> **When to read this:** During Phase 3 (writing module HTML) and Phase 4 (review). Check every one of these before considering a course complete.

These are real problems encountered when building courses. Check every one before considering a course complete.

### Tooltip Clipping
Translation blocks use `overflow: hidden` for code wrapping. If tooltips use `position: absolute` inside the term element, they get clipped by the container. **Fix:** Tooltips must use `position: fixed` and be appended to `document.body`. Calculate position from `getBoundingClientRect()`. This is already handled by `main.js` but is the #1 bug that appears in every build.

### Not Enough Tooltips
The most common failure is under-tooltipping. Non-technical learners don't know terms like REPL, JSON, flag, entry point, PATH, pip, namespace, function, class, module, PR, E2E, or even software names like Blender/GIMP. **Rule of thumb:** if a term wouldn't appear in everyday conversation with a non-technical friend, tooltip it. Err heavily on the side of too many. BUT: don't tooltip terms the user already knows well from their domain (e.g., AI/ML concepts for someone in AI).

### Walls of Text
The course looks like a textbook instead of an infographic. This happens when you write more than 2-3 sentences in a row without a visual break. Every screen must be at least 50% visual. Convert any list of 3+ items into cards, any sequence into step cards or flow diagrams, any code explanation into a code↔English translation block.

### Recycled Metaphors
Using "restaurant" or "kitchen" for everything. Every module needs its own metaphor that feels inevitable for that specific concept. If you catch yourself reaching for the same metaphor twice, stop and find one that fits the concept organically.

### Code Modifications
Trimming, simplifying, or "cleaning up" code snippets from the codebase. The learner should be able to open the real file and see the exact same code. Instead of editing code to be shorter, *choose* naturally short snippets (5-10 lines) from the codebase that illustrate the point.

### Quiz Questions That Test Memory
Asking "What does API stand for?" or "Which file handles X?" — those test recall, not understanding. Every quiz question should present a new scenario the learner hasn't seen and ask them to *apply* what they learned.

### Scroll-Snap Mandatory
Using `scroll-snap-type: y mandatory` traps users inside long modules. Always use `proximity`.

### Module Quality Degradation
Trying to write all modules in one pass causes later modules to be thin and rushed. Build one module at a time and verify each before moving on. For complex codebases, use the parallel path with module briefs.

### Missing Interactive Elements
A module with only text and code blocks, no interactivity. Every module needs at least one of: quiz, data flow animation, group chat, architecture diagram, drag-and-drop. These aren't decorations — they're how non-technical learners actually process information.

### Malformed Quiz Blocks (the stray `>`)
The single most common authoring bug. A `.quiz-question-block` carries three attributes — `data-correct`, `data-explanation-right`, `data-explanation-wrong` — across multiple lines. It is dangerously easy to drop a `>` after the *first* explanation, which closes the opening tag early and pushes `data-explanation-wrong` out as page text, silently breaking the wrong-answer feedback. **Fix:** put each attribute on its own line and the closing `>` alone on the final line, and run the verifier (see below), which parses every quiz block and confirms all three attributes are real attributes. Also note: the engine auto-prepends **"Exactly!"** / **"Not quite."** to your explanations, so do *not* begin them with those words.

### Apostrophes in Flow `data-steps`
The `.flow-animation` `data-steps` attribute is JSON inside *single quotes* (`data-steps='[...]'`). A single apostrophe in any label (`"the user's request"`) terminates the attribute early, `JSON.parse` fails, and the **entire animation silently dies**. **Fix:** keep labels apostrophe-free, use `&apos;`, or switch to double-quote-delimited `data-steps="[{\"label\":\"...\"}]"`. The verifier flags raw apostrophes inside `data-steps`.

### Fonts Require a Network
The course is *not* fully offline: `_base.html` pulls Bricolage Grotesque / DM Sans / JetBrains Mono from the Google Fonts CDN. With no network the page still works but falls back to serif/sans, and — importantly — headless screenshot tools often hang waiting on the blocked font request's `load` event. **When verifying in a headless browser, use DOM/`eval` checks rather than screenshots**, or self-host the fonts if true offline use is required.

### Shipping Without Verifying
"It looked fine when I skimmed it" is how the bugs above ship. After `build.sh`, run `scripts/verify_courses.py` (bundled) — it HTML-parses every `index.html` and checks: one `<!DOCTYPE>`/`</html>`, modules == nav-dots, ≥1 chat + ≥1 flow, ≥1 translation per module, one quiz per module, every quiz block's three data-attributes present as real attributes, every flow `data-steps` parses as JSON, and no leftover placeholders. Structural correctness is cheap to verify and expensive to eyeball.
