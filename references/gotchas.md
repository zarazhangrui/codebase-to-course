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

---

## Engineer Mode — Additional Gotchas

### Strawman Alternatives in ADR Cards
Presenting obviously inferior alternatives to make the chosen approach look brilliant. Engineers will spot this instantly and lose trust in the entire analysis. **Fix:** Every alternative must be a genuine option that a reasonable team might have chosen. Show the real trade-offs — sometimes the alternative is better in specific dimensions.

### Vague Performance Claims
Writing "handles large workloads efficiently" or "good performance" without specifics. Engineers need numbers. **Fix:** Extract actual configuration defaults, benchmark results, batch sizes, and resource requirements from the code. If the codebase has no benchmarks, estimate from algorithm complexity, model sizes, and configuration parameters. Include file paths and line numbers for every performance-relevant setting.

### Cheerleading Without Criticism
Only highlighting strengths while ignoring or downplaying weaknesses. This is the #1 trust-killer for Engineer Mode content. **Fix:** Every module must include at least one `callout-warning` or risk indicator for a genuine limitation. If you can't find any weaknesses, you haven't looked deep enough.

### Missing Code References
Making architectural claims without pointing to the specific code that implements them. **Fix:** Every claim about architecture, performance, or design must be accompanied by at least one code snippet with exact file path and line numbers. No hand-waving.

### Over-Tooltipping Basic Concepts
In Engineer Mode, tooltiping terms like "API", "async", "middleware", or "callback" insults the reader's intelligence and clutters the page. **Fix:** Only tooltip project-specific terms, domain-specific jargon, and configuration parameters. Assume the reader has solid CS fundamentals.

### Non-Actionable Integration Sections
Describing integration points abstractly ("Project A can work with Project B via their REST API") without showing actual code. **Fix:** Every integration description must include a concrete code example showing how to bridge the two systems. Include data format conversions, API calls, and error handling.

### Missing Verdicts
Ending a module without a clear, opinionated recommendation. Engineers read these analyses to make decisions — if every section ends with "it depends," they learn nothing. **Fix:** Every module must end with a verdict callout that gives a clear recommendation for specific scenarios.

### Scenario Judge Without Honesty
Marking every scenario as "excellent fit" because the analysis is supposed to be positive. **Fix:** Include at least one "not recommended" scenario per guide. Suggest alternative tools or combination approaches. This honesty builds trust and is genuinely useful for the engineer.

### Trade-off Matrix Without Real Trade-offs
Creating comparison tables where one approach wins on every dimension. **Fix:** Every approach in a trade-off matrix should win on at least one dimension. If an approach loses on every dimension, it shouldn't be in the comparison — or you haven't analyzed it fairly.
