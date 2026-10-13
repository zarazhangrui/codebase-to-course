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

### Ugly Code Blocks
Source code copied with tabs and newlines between `.code-line` spans renders double-spaced, 8-space indented, and wrapped to column 0. `main.js` tidies code at load (tabs to 2 spaces, shared indent removed, hanging indent on wrapped lines, stray newlines dropped) and `styles.css` turns off font ligatures so `->` and `<=` show as typed. Still write the spans back to back. In Spot-the-Bug lines, also replace tabs and remove the shared indent in the markup, since that pattern has no `.code-line` spans.

### Narrow Split Blocks
Code↔English blocks in a 1fr/1fr grid inside the reading column waste a wide screen and force code to wrap. `styles.css` widens them on screens of 1100px and up. Do not override `.translation-block` width or columns inline.

### Missing Line Links
Every `.tl` row needs `data-lines` so hover highlights its code. Check by script before calling a module done: every `.tl` has the attribute, and every index is within the block's `.code-line` count.
