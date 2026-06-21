# Interactive Elements Reference

Implementation patterns for every interactive element type used in courses. Pick the elements that best serve each module's teaching goal.

> **Architecture note:** All CSS and JavaScript for these elements live in `references/styles.css` and `references/main.js`, which are copied verbatim into every course directory. When writing module HTML files, use only the HTML patterns below — do **not** inline `<style>` or `<script>` tags for these elements. The engines in `main.js` auto-initialize on page load by scanning for the relevant class names and `data-*` attributes described here.

## Table of Contents
1. [Code ↔ English Translation Blocks](#code--english-translation-blocks)
2. [Multiple-Choice Quizzes](#multiple-choice-quizzes)
3. [Drag-and-Drop Matching](#drag-and-drop-matching)
4. [Group Chat Animation](#group-chat-animation)
5. [Message Flow / Data Flow Animation](#message-flow--data-flow-animation)
6. [Interactive Architecture Diagram](#interactive-architecture-diagram)
7. [Layer Toggle Demo](#layer-toggle-demo)
8. ["Spot the Bug" Challenge](#spot-the-bug-challenge)
9. [Scenario Quiz](#scenario-quiz)
10. [Callout Boxes](#callout-boxes)
11. [Pattern/Feature Cards](#patternfeature-cards)
12. [Flow Diagrams](#flow-diagrams)
13. [Permission/Config Badges](#permissionconfig-badges)
14. [Glossary Tooltips](#glossary-tooltips)
15. [Visual File Tree](#visual-file-tree)
16. [Icon-Label Rows](#icon-label-rows)
17. [Numbered Step Cards](#numbered-step-cards)
18. [ADR Cards (Engineer Mode)](#adr-cards-engineer-mode)
19. [Trade-off Matrix (Engineer Mode)](#trade-off-matrix-engineer-mode)
20. [Scenario Judge (Engineer Mode)](#scenario-judge-engineer-mode)
21. [Integration Blueprint (Engineer Mode)](#integration-blueprint-engineer-mode)
22. [Risk Indicators (Engineer Mode)](#risk-indicators-engineer-mode)
23. [Verdict Callout (Engineer Mode)](#verdict-callout-engineer-mode)
24. [Critical Path Trace (Engineer Mode)](#critical-path-trace-engineer-mode)
25. [Source File Map (Engineer Mode)](#source-file-map-engineer-mode)

---

## Code ↔ English Translation Blocks

The most important teaching element. Shows real code from the project on the left and a plain English translation on the right, line by line.

**HTML:**
```html
<div class="translation-block animate-in">
  <div class="translation-code">
    <span class="translation-label">CODE</span>
    <pre><code>
<span class="code-line"><span class="code-keyword">const</span> response = <span class="code-keyword">await</span> <span class="code-function">fetch</span>(url, {</span>
<span class="code-line">  <span class="code-property">method</span>: <span class="code-string">'POST'</span>,</span>
<span class="code-line">  <span class="code-property">headers</span>: { <span class="code-string">'Authorization'</span>: apiKey }</span>
<span class="code-line">});</span>
    </code></pre>
  </div>
  <div class="translation-english">
    <span class="translation-label">PLAIN ENGLISH</span>
    <div class="translation-lines">
      <p class="tl">Send a request to the URL and wait for a response...</p>
      <p class="tl">We're sending data (POST), not just asking for it (GET)...</p>
      <p class="tl">Include our API key so the server knows who we are...</p>
      <p class="tl">End of the request setup.</p>
    </div>
  </div>
</div>
```

**CSS:**
```css
.translation-block {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-md);
  margin: var(--space-8) 0;
}
.translation-code {
  background: var(--color-bg-code);
  color: #CDD6F4;
  padding: var(--space-6);
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  line-height: 1.7;
  position: relative;
  overflow-x: hidden;  /* NO horizontal scrollbar — ever */
}
.translation-code pre,
.translation-code code {
  white-space: pre-wrap;       /* wrap long lines instead of scrolling */
  word-break: break-word;      /* break mid-word if needed */
  overflow-x: hidden;
}
.translation-english {
  background: var(--color-surface-warm);
  padding: var(--space-6);
  font-size: var(--text-sm);
  line-height: 1.7;
  border-left: 3px solid var(--color-accent);
}
.translation-label {
  position: absolute;
  top: var(--space-2);
  right: var(--space-3);
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  opacity: 0.5;
}
.translation-english .translation-label {
  color: var(--color-text-muted);
}
/* Responsive: stack vertically on mobile */
@media (max-width: 768px) {
  .translation-block { grid-template-columns: 1fr; }
  .translation-english { border-left: none; border-top: 3px solid var(--color-accent); }
}
```

**Rules:**
- Each English line should correspond to 1-2 code lines
- Use conversational language, not technical jargon
- Highlight the "why" not just the "what" — e.g., "Include our API key so the server knows who we are" not "Set the Authorization header"

---

## Multiple-Choice Quizzes

For testing understanding with instant feedback. Each question has options, one correct answer, and per-question explanations.

**Wiring:** `main.js` exposes `window.selectOption(btn)`, `window.checkQuiz(containerId)`, and `window.resetQuiz(containerId)`. Call them via `onclick`. Per-question explanations go in `data-explanation-right` and `data-explanation-wrong` on the `.quiz-question-block`.

**HTML:**
```html
<div class="quiz-container" id="quiz-module3">
  <div class="quiz-question-block"
       data-correct="option-b"
       data-explanation-right="Exactly — because X is responsible for Y in this architecture."
       data-explanation-wrong="Not quite. Think about where Y lives in the codebase...">
    <h3 class="quiz-question">Question text here?</h3>
    <div class="quiz-options">
      <button class="quiz-option" data-value="option-a" onclick="selectOption(this)">
        <div class="quiz-option-radio"></div>
        <span>Answer A</span>
      </button>
      <button class="quiz-option" data-value="option-b" onclick="selectOption(this)">
        <div class="quiz-option-radio"></div>
        <span>Answer B (correct)</span>
      </button>
      <button class="quiz-option" data-value="option-c" onclick="selectOption(this)">
        <div class="quiz-option-radio"></div>
        <span>Answer C</span>
      </button>
    </div>
    <div class="quiz-feedback"></div>
  </div>

  <button class="quiz-check-btn" onclick="checkQuiz('quiz-module3')">Check Answers</button>
  <button class="quiz-reset-btn" onclick="resetQuiz('quiz-module3')">Try Again</button>
</div>
```

**CSS for quiz states:**
```css
.quiz-option {
  display: flex; align-items: center; gap: var(--space-3);
  padding: var(--space-3) var(--space-4);
  border: 2px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: var(--color-surface);
  cursor: pointer; width: 100%;
  transition: border-color var(--duration-fast), background var(--duration-fast);
}
.quiz-option:hover { border-color: var(--color-accent-muted); }
.quiz-option.selected { border-color: var(--color-accent); background: var(--color-accent-light); }
.quiz-option.correct { border-color: var(--color-success); background: var(--color-success-light); }
.quiz-option.incorrect { border-color: var(--color-error); background: var(--color-error-light); }
.quiz-option-radio {
  width: 18px; height: 18px; border-radius: 50%;
  border: 2px solid var(--color-border);
  transition: all var(--duration-fast);
}
.quiz-option.selected .quiz-option-radio {
  border-color: var(--color-accent);
  background: var(--color-accent);
  box-shadow: inset 0 0 0 3px white;
}
.quiz-feedback {
  max-height: 0; overflow: hidden; opacity: 0;
  transition: max-height var(--duration-normal), opacity var(--duration-normal);
}
.quiz-feedback.show { max-height: 200px; opacity: 1; padding: var(--space-3); margin-top: var(--space-2); border-radius: var(--radius-sm); }
.quiz-feedback.success { background: var(--color-success-light); color: var(--color-success); }
.quiz-feedback.error { background: var(--color-error-light); color: var(--color-error); }
```

---

## Drag-and-Drop Matching

For matching concepts to descriptions. Supports both mouse (HTML5 Drag API) and touch.

**HTML:**
```html
<div class="dnd-container">
  <div class="dnd-chips">
    <div class="dnd-chip" draggable="true" data-answer="actor-a">Actor A</div>
    <div class="dnd-chip" draggable="true" data-answer="actor-b">Actor B</div>
    <div class="dnd-chip" draggable="true" data-answer="actor-c">Actor C</div>
  </div>
  <div class="dnd-zones">
    <div class="dnd-zone" data-correct="actor-a">
      <p class="dnd-zone-label">Description for Actor A</p>
      <div class="dnd-zone-target">Drop here</div>
    </div>
    <!-- more zones -->
  </div>
  <button onclick="checkDnD()">Check Matches</button>
  <button onclick="resetDnD()">Reset</button>
</div>
```

**JS (mouse + touch):**
```javascript
// MOUSE: HTML5 Drag API
chips.forEach(chip => {
  chip.addEventListener('dragstart', (e) => {
    e.dataTransfer.setData('text/plain', chip.dataset.answer);
    chip.classList.add('dragging');
  });
  chip.addEventListener('dragend', () => chip.classList.remove('dragging'));
});

zones.forEach(zone => {
  const target = zone.querySelector('.dnd-zone-target');
  target.addEventListener('dragover', (e) => { e.preventDefault(); target.classList.add('drag-over'); });
  target.addEventListener('dragleave', () => target.classList.remove('drag-over'));
  target.addEventListener('drop', (e) => {
    e.preventDefault();
    target.classList.remove('drag-over');
    const answer = e.dataTransfer.getData('text/plain');
    const chip = document.querySelector(`[data-answer="${answer}"]`);
    target.textContent = chip.textContent;
    target.dataset.placed = answer;
    chip.classList.add('placed');
  });
});

// TOUCH: Custom implementation (HTML5 drag doesn't work on mobile)
chips.forEach(chip => {
  chip.addEventListener('touchstart', (e) => {
    e.preventDefault();
    const touch = e.touches[0];
    const clone = chip.cloneNode(true);
    clone.classList.add('touch-ghost');
    clone.style.cssText = `position:fixed; z-index:1000; pointer-events:none;
      left:${touch.clientX - 40}px; top:${touch.clientY - 20}px;`;
    document.body.appendChild(clone);
    chip._ghost = clone;
    chip._answer = chip.dataset.answer;
  }, { passive: false });

  chip.addEventListener('touchmove', (e) => {
    e.preventDefault();
    const touch = e.touches[0];
    if (chip._ghost) {
      chip._ghost.style.left = (touch.clientX - 40) + 'px';
      chip._ghost.style.top = (touch.clientY - 20) + 'px';
    }
    // Highlight zone under finger
    const el = document.elementFromPoint(touch.clientX, touch.clientY);
    zones.forEach(z => z.querySelector('.dnd-zone-target').classList.remove('drag-over'));
    if (el && el.closest('.dnd-zone-target')) {
      el.closest('.dnd-zone-target').classList.add('drag-over');
    }
  }, { passive: false });

  chip.addEventListener('touchend', (e) => {
    if (chip._ghost) { chip._ghost.remove(); chip._ghost = null; }
    const touch = e.changedTouches[0];
    const el = document.elementFromPoint(touch.clientX, touch.clientY);
    if (el && el.closest('.dnd-zone-target')) {
      const target = el.closest('.dnd-zone-target');
      target.textContent = chip.textContent;
      target.dataset.placed = chip._answer;
      chip.classList.add('placed');
    }
  });
});
```

---

## Group Chat Animation

iMessage/WeChat-style chat showing components "talking" to each other. Messages appear one by one with typing indicators.

**Wiring:** `main.js` auto-initializes every `.chat-window` on page load. Give each chat window a unique `id`. Control buttons need these classes: `.chat-next-btn`, `.chat-all-btn`, `.chat-reset-btn`. The typing indicator avatar element should have `id="{chatWindowId}-typing-avatar"` or simply be the first `.chat-avatar` inside `.chat-typing`.

**HTML:**
```html
<div class="chat-window" id="chat-module2">
  <div class="chat-messages">
    <div class="chat-message" data-msg="0" data-sender="actor-a" style="display:none">
      <div class="chat-avatar" style="background: var(--color-actor-1)">A</div>
      <div class="chat-bubble">
        <span class="chat-sender" style="color: var(--color-actor-1)">Actor A</span>
        <p>Hey Background, I need the data for this item.</p>
      </div>
    </div>
    <!-- more messages... -->
  </div>

  <div class="chat-typing" id="chat-typing" style="display:none">
    <div class="chat-avatar" id="typing-avatar">?</div>
    <div class="chat-typing-dots">
      <span class="typing-dot"></span>
      <span class="typing-dot"></span>
      <span class="typing-dot"></span>
    </div>
  </div>

  <div class="chat-controls">
    <button class="btn chat-next-btn">Next Message</button>
    <button class="btn chat-all-btn">Play All</button>
    <button class="btn chat-reset-btn">Replay</button>
    <span class="chat-progress"></span>
  </div>
</div>
```

**CSS for typing dots:**
```css
.typing-dot {
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--color-text-muted);
  animation: typingBounce 1.4s infinite;
}
.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }
@keyframes typingBounce {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-6px); }
}
```

---

## Message Flow / Data Flow Animation

Step-by-step visualization of data moving between components. User clicks "Next Step" to advance.

**Wiring:** `main.js` auto-initializes every `.flow-animation` on page load. Pass steps as JSON in `data-steps`. Each step object: `{ highlight: "flow-actor-id", label: "description", packet: true, from: "actor-id-suffix", to: "actor-id-suffix" }`. Actor element IDs must be `flow-actor-1`, `flow-actor-2`, etc. Control buttons need classes `.flow-next-btn` and `.flow-reset-btn`.

> **⚠️ Single quotes in step labels will break parsing.** The `data-steps` attribute is delimited by single quotes (`data-steps='[...]'`), so any single quote inside a label (e.g. `"the user's request"`) will terminate the attribute early and cause `JSON.parse` to fail silently — the entire animation will stop working. Either avoid apostrophes in labels, replace them with `&apos;`, or rewrite the attribute using double-quote delimiters with escaped inner quotes (`data-steps="[{\"label\":\"...\"}]"`).

**HTML:**
```html
<div class="flow-animation" data-steps='[
  {"highlight":"flow-actor-1","label":"User clicks the button"},
  {"highlight":"flow-actor-1","label":"Frontend sends request","packet":true,"from":"actor-1","to":"actor-2"},
  {"highlight":"flow-actor-2","label":"Backend calls the database","packet":true,"from":"actor-2","to":"actor-3"}
]'>
  <div class="flow-actors">
    <div class="flow-actor" id="flow-actor-1">
      <div class="flow-actor-icon">A</div>
      <span>Actor 1</span>
    </div>
    <div class="flow-actor" id="flow-actor-2">
      <div class="flow-actor-icon">B</div>
      <span>Actor 2</span>
    </div>
    <div class="flow-actor" id="flow-actor-3">
      <div class="flow-actor-icon">C</div>
      <span>Actor 3</span>
    </div>
  </div>

  <div class="flow-packet" id="flow-packet"></div>

  <div class="flow-step-label" id="flow-label">Click "Next Step" to begin</div>

  <div class="flow-controls">
    <button class="btn flow-next-btn">Next Step</button>
    <button class="btn flow-reset-btn">Restart</button>
    <span class="flow-progress"></span>
  </div>
</div>
```

**CSS for active actor glow:**
```css
.flow-actor.active {
  box-shadow: 0 0 0 3px var(--color-accent), 0 0 20px rgba(217, 79, 48, 0.2);
  transform: scale(1.05);
  transition: all var(--duration-normal) var(--ease-out);
}
```

---

## Interactive Architecture Diagram

Full-system diagram where hovering/clicking a component shows a description tooltip.

**HTML:**
```html
<div class="arch-diagram">
  <div class="arch-zone arch-zone-browser">
    <h4 class="arch-zone-label">Browser</h4>
    <div class="arch-component" data-desc="Injects UI into the web page, reads DOM, captures user actions"
         onclick="showArchDesc(this)">
      <div class="arch-icon">📄</div>
      <span>Component A</span>
    </div>
    <!-- more components -->
  </div>
  <div class="arch-zone arch-zone-external">
    <h4 class="arch-zone-label">External Services</h4>
    <!-- API cards -->
  </div>
  <div class="arch-description" id="arch-desc">Click any component to learn what it does</div>
</div>
```

---

## Layer Toggle Demo

Shows how different layers (e.g., HTML/CSS/JS, or data/logic/UI) build on each other. Three tabs switch between views.

**HTML:**
```html
<div class="layer-demo">
  <div class="layer-tabs">
    <button class="layer-tab active" onclick="showLayer('html')">HTML</button>
    <button class="layer-tab" onclick="showLayer('css')">+ CSS</button>
    <button class="layer-tab" onclick="showLayer('js')">+ JS</button>
  </div>
  <div class="layer-viewport">
    <div class="layer" id="layer-html" style="display:block">
      <!-- Raw unstyled version -->
    </div>
    <div class="layer" id="layer-css" style="display:none">
      <!-- Styled version -->
    </div>
    <div class="layer" id="layer-js" style="display:none">
      <!-- Interactive version -->
    </div>
  </div>
  <p class="layer-description" id="layer-desc">This is the raw HTML...</p>
</div>
```

---

## "Spot the Bug" Challenge

Show code with a deliberate bug. User clicks the buggy line. Reveal explains the issue.

**HTML:**
```html
<div class="bug-challenge">
  <h3>Find the bug in this code:</h3>
  <div class="bug-code">
    <div class="bug-line" data-line="1" onclick="checkBugLine(this, false)">
      <span class="line-num">1</span>
      <code>chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {</code>
    </div>
    <div class="bug-line" data-line="2" onclick="checkBugLine(this, false)">
      <span class="line-num">2</span>
      <code>  if (msg.action === 'fetchData') {</code>
    </div>
    <div class="bug-line bug-target" data-line="3" onclick="checkBugLine(this, true)">
      <span class="line-num">3</span>
      <code>    fetch(url).then(r => r.json()).then(data => sendResponse(data));</code>
    </div>
    <div class="bug-line" data-line="4" onclick="checkBugLine(this, false)">
      <span class="line-num">4</span>
      <code>  }</code>
    </div>
    <div class="bug-line" data-line="5" onclick="checkBugLine(this, false)">
      <span class="line-num">5</span>
      <code>});</code>
    </div>
  </div>
  <div class="bug-feedback" id="bug-feedback"></div>
</div>
```

**JS:**
```javascript
window.checkBugLine = function(el, isCorrect) {
  const feedback = el.closest('.bug-challenge').querySelector('.bug-feedback');
  if (isCorrect) {
    el.classList.add('correct');
    feedback.innerHTML = '<strong>Found it!</strong> The listener uses an async operation (fetch) but doesn\'t return true. Chrome closes the message channel before the response can be sent. Fix: add <code>return true;</code> at the end.';
    feedback.className = 'bug-feedback show success';
  } else {
    el.classList.add('incorrect');
    feedback.innerHTML = 'Not this line — look for where the async timing might cause problems...';
    feedback.className = 'bug-feedback show error';
    setTimeout(() => { el.classList.remove('incorrect'); feedback.className = 'bug-feedback'; }, 2000);
  }
};
```

---

## Scenario Quiz

"What would a senior engineer do?" — situational questions with explanations.

Same HTML/CSS/JS pattern as Multiple-Choice Quizzes, but with longer scenario descriptions and more detailed explanations. Wrap each question in a scenario context block:

```html
<div class="scenario-block">
  <div class="scenario-context">
    <span class="scenario-label">Scenario</span>
    <p>Your app processes a 3-hour podcast transcript. The API has a 16,000 token limit. What do you do?</p>
  </div>
  <!-- quiz-options here -->
</div>
```

---

## Callout Boxes

"Aha!" moments — universal CS insights. Max 2 per module.

```html
<div class="callout callout-accent">
  <div class="callout-icon">💡</div>
  <div class="callout-content">
    <strong class="callout-title">Key Insight</strong>
    <p>This pattern — splitting responsibilities into focused roles — is one of the most important ideas in software engineering. Engineers call it "separation of concerns."</p>
  </div>
</div>
```

**Variants:**
- `callout-accent`: vermillion left border, light accent background (for CS insights)
- `callout-info`: teal left border, light info background (for "good to know")
- `callout-warning`: red left border, light error background (for common mistakes)

---

## Pattern/Feature Cards

Grid of cards highlighting engineering patterns, tech stack components, or key concepts.

```html
<div class="pattern-cards">
  <div class="pattern-card" style="border-top: 3px solid var(--color-actor-1)">
    <div class="pattern-icon" style="background: var(--color-actor-1)">🔄</div>
    <h4 class="pattern-title">Caching</h4>
    <p class="pattern-desc">Store results to avoid redundant work — like keeping leftovers instead of cooking a new meal every time.</p>
  </div>
  <!-- more cards -->
</div>
```

```css
.pattern-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: var(--space-4);
}
.pattern-card {
  background: var(--color-surface);
  border-radius: var(--radius-md);
  padding: var(--space-6);
  box-shadow: var(--shadow-sm);
  transition: transform var(--duration-normal) var(--ease-out), box-shadow var(--duration-normal);
}
.pattern-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}
```

---

## Flow Diagrams

**Horizontal flow (desktop):**
```html
<div class="flow-steps">
  <div class="flow-step">
    <div class="flow-step-num">1</div>
    <p>User clicks button</p>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">
    <div class="flow-step-num">2</div>
    <p>Component A detects click</p>
  </div>
  <div class="flow-arrow">→</div>
  <!-- more steps -->
</div>
```

Arrows rotate to `↓` on mobile via CSS transform.

---

## Permission/Config Badges

For annotating config files, permissions, or settings:

```html
<div class="badge-list">
  <div class="badge-item">
    <code class="badge-code">storage</code>
    <span class="badge-desc">Save data between sessions (like browser bookmarks)</span>
  </div>
  <div class="badge-item">
    <code class="badge-code">activeTab</code>
    <span class="badge-desc">Access the currently open tab (only when the user clicks)</span>
  </div>
</div>
```

```css
.badge-item {
  display: flex; align-items: center; gap: var(--space-4);
  padding: var(--space-3) var(--space-4);
  border: 1px solid var(--color-border-light);
  border-radius: var(--radius-sm);
  transition: border-color var(--duration-fast);
}
.badge-item:hover { border-color: var(--color-accent-muted); }
.badge-code {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  background: var(--color-bg-code);
  color: #CBA6F7;
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-sm);
  white-space: nowrap;
}
```

---

## Glossary Tooltips

The most important accessibility feature for non-technical learners. Any technical term in the course text should be wrapped in a tooltip that shows a plain-English definition on hover (desktop) or tap (mobile). The learner never has to leave the page or Google anything.

**HTML — mark up terms inline:**
```html
<p>The extension uses a
  <span class="term" data-definition="A service worker is a background script that runs independently of the web page — like a behind-the-scenes assistant that's always on, even when you're not looking at the page.">service worker</span>
  to handle API calls.
</p>
```

**CSS:**
```css
.term {
  border-bottom: 1.5px dashed var(--color-accent-muted);
  cursor: pointer;    /* NOT cursor: help — pointer feels clickable and inviting */
  position: relative;
}
.term:hover, .term.active {
  border-bottom-color: var(--color-accent);
  color: var(--color-accent);
}

/* The tooltip bubble — uses position: fixed and is appended to document.body
   via JS so it is NEVER clipped by ancestor overflow: hidden containers
   (like translation blocks). See JS section below for positioning logic. */
.term-tooltip {
  position: fixed;        /* CRITICAL: fixed, not absolute — prevents clipping */
  background: var(--color-bg-code);
  color: #CDD6F4;
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-sm);
  font-size: var(--text-sm);
  font-family: var(--font-body);
  line-height: var(--leading-normal);
  width: max(200px, min(320px, 80vw));
  box-shadow: var(--shadow-lg);
  pointer-events: none;
  opacity: 0;
  transition: opacity var(--duration-fast);
  z-index: 10000;        /* Above everything, including nav */
}
/* Arrow pointing down */
.term-tooltip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 6px solid transparent;
  border-top-color: var(--color-bg-code);
}
.term-tooltip.visible {
  opacity: 1;
}

/* If tooltip goes off-screen top, flip to below */
.term-tooltip.flip {
  bottom: auto;
  top: calc(100% + 8px);
}
.term-tooltip.flip::after {
  top: auto;
  bottom: 100%;
  border-top-color: transparent;
  border-bottom-color: var(--color-bg-code);
}
```

**JS — position: fixed tooltips appended to body (never clipped by overflow):**
```javascript
// Tooltip container — appended to body so it's never clipped
let activeTooltip = null;

function positionTooltip(term, tip) {
  const rect = term.getBoundingClientRect();
  const tipWidth = 300; // approximate
  let left = rect.left + rect.width / 2 - tipWidth / 2;
  // Clamp to viewport
  left = Math.max(8, Math.min(left, window.innerWidth - tipWidth - 8));

  // Try above first
  let top = rect.top - 8;
  tip.style.left = left + 'px';

  // Position above by default, flip below if no room
  document.body.appendChild(tip);
  const tipHeight = tip.offsetHeight;
  if (rect.top - tipHeight - 8 < 0) {
    // Flip below
    tip.style.top = (rect.bottom + 8) + 'px';
    tip.classList.add('flip');
  } else {
    tip.style.top = (rect.top - tipHeight - 8) + 'px';
    tip.classList.remove('flip');
  }
}

document.querySelectorAll('.term').forEach(term => {
  const tip = document.createElement('span');
  tip.className = 'term-tooltip';
  tip.textContent = term.dataset.definition;

  // Hover for desktop
  term.addEventListener('mouseenter', () => {
    if (activeTooltip && activeTooltip !== tip) {
      activeTooltip.classList.remove('visible');
      activeTooltip.remove();
    }
    positionTooltip(term, tip);
    requestAnimationFrame(() => tip.classList.add('visible'));
    activeTooltip = tip;
  });

  term.addEventListener('mouseleave', () => {
    tip.classList.remove('visible');
    setTimeout(() => { if (!tip.classList.contains('visible')) tip.remove(); }, 150);
    activeTooltip = null;
  });

  // Tap for mobile
  term.addEventListener('click', (e) => {
    e.stopPropagation();
    if (activeTooltip && activeTooltip !== tip) {
      activeTooltip.classList.remove('visible');
      activeTooltip.remove();
    }
    if (tip.classList.contains('visible')) {
      tip.classList.remove('visible');
      tip.remove();
      activeTooltip = null;
    } else {
      positionTooltip(term, tip);
      requestAnimationFrame(() => tip.classList.add('visible'));
      activeTooltip = tip;
    }
  });
});

// Close tooltips when clicking elsewhere
document.addEventListener('click', () => {
  if (activeTooltip) {
    activeTooltip.classList.remove('visible');
    activeTooltip.remove();
    activeTooltip = null;
  }
});
```

**Rules:**
- Mark up EVERY technical term on first use in each module (API, DOM, callback, async, endpoint, middleware, etc.)
- Keep definitions to 1-2 sentences max, in everyday language
- Use a metaphor in the definition when it helps — e.g., "A **callback** is like leaving your phone number at a restaurant so they can call you when your table is ready"
- Don't mark the same term twice within the same screen — only on first appearance per module
- The dashed underline should be subtle enough not to distract but visible enough that curious learners discover it

---

## Visual File Tree

Use instead of paragraphs listing "this folder does X, that folder does Y." Much easier to scan.

```html
<div class="file-tree">
  <div class="ft-folder open">
    <span class="ft-name">app/</span>
    <span class="ft-desc">Pages and API routes</span>
    <div class="ft-children">
      <div class="ft-folder">
        <span class="ft-name">api/</span>
        <span class="ft-desc">Backend endpoints the frontend calls</span>
      </div>
      <div class="ft-file">
        <span class="ft-name">layout.tsx</span>
        <span class="ft-desc">The shell that wraps every page</span>
      </div>
    </div>
  </div>
  <div class="ft-folder">
    <span class="ft-name">components/</span>
    <span class="ft-desc">Reusable UI building blocks</span>
  </div>
  <div class="ft-folder">
    <span class="ft-name">lib/</span>
    <span class="ft-desc">Shared logic and utilities</span>
  </div>
</div>
```

```css
.file-tree { font-family: var(--font-mono); font-size: var(--text-sm); }
.ft-folder, .ft-file {
  padding: var(--space-2) var(--space-3);
  border-left: 2px solid var(--color-border-light);
  margin-left: var(--space-4);
}
.ft-folder > .ft-name { color: var(--color-accent); font-weight: 600; }
.ft-folder > .ft-name::before { content: '📁 '; }
.ft-file > .ft-name::before { content: '📄 '; }
.ft-desc {
  color: var(--color-text-secondary);
  font-family: var(--font-body);
  margin-left: var(--space-2);
  font-size: var(--text-xs);
}
.ft-children { margin-left: var(--space-4); }
```

---

## Icon-Label Rows

For listing components, features, or concepts visually. Replaces bullet-point paragraphs.

```html
<div class="icon-rows">
  <div class="icon-row">
    <div class="icon-circle" style="background: var(--color-actor-1)">🖥️</div>
    <div>
      <strong>Frontend (Next.js)</strong>
      <p>What the user sees and interacts with</p>
    </div>
  </div>
  <div class="icon-row">
    <div class="icon-circle" style="background: var(--color-actor-2)">⚡</div>
    <div>
      <strong>API Routes</strong>
      <p>Backend logic that runs on the server</p>
    </div>
  </div>
  <div class="icon-row">
    <div class="icon-circle" style="background: var(--color-actor-3)">🗄️</div>
    <div>
      <strong>Database (Supabase)</strong>
      <p>Where all the data is stored permanently</p>
    </div>
  </div>
</div>
```

```css
.icon-rows { display: flex; flex-direction: column; gap: var(--space-4); }
.icon-row {
  display: flex; align-items: center; gap: var(--space-4);
  padding: var(--space-4);
  background: var(--color-surface);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}
.icon-row p { margin: 0; color: var(--color-text-secondary); font-size: var(--text-sm); }
.icon-circle {
  width: 48px; height: 48px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.25rem; flex-shrink: 0;
}
```

---

## Numbered Step Cards

For sequences that would otherwise be a numbered paragraph list. Visual, scannable, and each step stands alone.

```html
<div class="step-cards">
  <div class="step-card">
    <div class="step-num">1</div>
    <div class="step-body">
      <strong>User pastes a YouTube URL</strong>
      <p>The frontend captures the URL and extracts the video ID</p>
    </div>
  </div>
  <div class="step-card">
    <div class="step-num">2</div>
    <div class="step-body">
      <strong>API fetches the transcript</strong>
      <p>A server-side route calls an external service to get the video's text</p>
    </div>
  </div>
  <div class="step-card">
    <div class="step-num">3</div>
    <div class="step-body">
      <strong>AI analyzes the content</strong>
      <p>The transcript is sent to an AI model that extracts key moments</p>
    </div>
  </div>
</div>
```

```css
.step-cards { display: flex; flex-direction: column; gap: var(--space-3); }
.step-card {
  display: flex; align-items: flex-start; gap: var(--space-4);
  padding: var(--space-4) var(--space-5);
  background: var(--color-surface);
  border-radius: var(--radius-md);
  border-left: 3px solid var(--color-accent);
  box-shadow: var(--shadow-sm);
}
.step-num {
  width: 32px; height: 32px; border-radius: 50%;
  background: var(--color-accent);
  color: white; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--font-display);
  flex-shrink: 0;
}
.step-body p { margin: var(--space-1) 0 0; color: var(--color-text-secondary); font-size: var(--text-sm); }
```

---

## Engineer Mode Interactive Elements

The following elements are **exclusive to Engineer Mode** and are required in every Engineer Mode guide. They replace or supplement the Beginner Mode elements to serve the professional engineer audience.

---

## ADR Cards (Engineer Mode)

Architecture Decision Record cards — the most important Engineer Mode element. Each card presents one major design decision: the problem, the chosen solution, alternatives that were NOT chosen, and the trade-off analysis.

**Wiring:** `main.js` auto-initializes every `.adr-card` on page load. Clicking the card toggles the expanded analysis section. Use `data-adr-id` for unique identification.

**HTML:**
```html
<div class="adr-card animate-in" data-adr-id="adr-1">
  <div class="adr-header">
    <span class="adr-badge">ADR #1</span>
    <h3 class="adr-title">使用 Pipeline 模式统一处理多种文档格式</h3>
    <p class="adr-summary">将不同格式的文档解析统一为 pipeline 抽象，而不是为每种格式写独立处理逻辑。</p>
    <button class="adr-toggle" onclick="toggleADR(this)">展开分析 ▾</button>
  </div>
  <div class="adr-body" style="display:none">
    <div class="adr-section">
      <h4 class="adr-section-title">问题背景</h4>
      <p>需要支持 PDF、DOCX、HTML 等 10+ 种格式，每种格式有不同的解析需求和边界情况。如果为每种格式写独立逻辑，代码量指数增长且难以维护。</p>
    </div>
    <div class="adr-section">
      <h4 class="adr-section-title">选定方案</h4>
      <p>抽象出统一的 Pipeline 接口，每个格式实现自己的 Backend，共享 Pipeline 处理阶段（OCR、布局分析、表格识别）。</p>
      <div class="adr-code-ref">
        <code class="adr-file-ref">src/pipeline/base.py:42-58</code>
        <p class="adr-code-note">Pipeline 基类定义了 6 个处理阶段的接口</p>
      </div>
    </div>
    <div class="adr-section">
      <h4 class="adr-section-title">备选方案</h4>
      <div class="adr-alternatives">
        <div class="adr-alt">
          <span class="adr-alt-name">方案 B: 格式专属处理器</span>
          <p class="adr-alt-desc">为每种格式写独立的端到端处理函数。简单直接，但无法共享 OCR 等通用组件。</p>
          <span class="adr-alt-verdict">❌ 弃选：扩展性差，每增加一种格式需要完整重写</span>
        </div>
        <div class="adr-alt">
          <span class="adr-alt-name">方案 C: 插件系统 + 微内核</span>
          <p class="adr-alt-desc">微内核调度，格式解析作为外部插件加载。最大灵活性，但增加了部署复杂度和调试难度。</p>
          <span class="adr-alt-verdict">⚠️ 考虑过但认为过度设计：当前格式数量不需要如此复杂的扩展机制</span>
        </div>
      </div>
    </div>
    <div class="adr-section">
      <h4 class="adr-section-title">权衡分析</h4>
      <table class="adr-tradeoff-table">
        <thead>
          <tr><th>维度</th><th>Pipeline 模式</th><th>格式专属</th><th>微内核</th></tr>
        </thead>
        <tbody>
          <tr><td>代码复用</td><td class="adr-good">★★★</td><td class="adr-bad">★☆☆</td><td class="adr-mid">★★☆</td></tr>
          <tr><td>扩展性</td><td class="adr-mid">★★☆</td><td class="adr-bad">★☆☆</td><td class="adr-good">★★★</td></tr>
          <tr><td>调试难度</td><td class="adr-mid">★★☆</td><td class="adr-good">★★★</td><td class="adr-bad">★☆☆</td></tr>
          <tr><td>部署复杂度</td><td class="adr-good">★★★</td><td class="adr-good">★★★</td><td class="adr-bad">★☆☆</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
```

**Rules:**
- At least 3 ADR cards across the entire guide
- Each card must reference specific code with file path and line numbers
- Alternatives must be genuine — don't create strawman alternatives to make the chosen approach look good
- The trade-off table must be honest — if the chosen approach has weaknesses, show them
- Use Chinese or English depending on the guide's language

---

## Trade-off Matrix (Engineer Mode)

A structured comparison table evaluating different approaches, configurations, or tools across multiple dimensions. Engineers think in trade-offs — this element makes the trade-off space explicit.

**HTML:**
```html
<div class="tradeoff-matrix animate-in">
  <h3 class="tradeoff-title">方案对比：文档解析策略</h3>
  <p class="tradeoff-desc">不同解析策略在准确率、速度、资源消耗上的权衡</p>
  <div class="tradeoff-table-wrap">
    <table class="tradeoff-table">
      <thead>
        <tr>
          <th class="tradeoff-dim">维度</th>
          <th>传统 Pipeline<br><span class="tradeoff-sub">多模型组合</span></th>
          <th>VLM 解析<br><span class="tradeoff-sub">视觉语言模型</span></th>
          <th>混合模式<br><span class="tradeoff-sub">规则 + 模型</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="tradeoff-dim">解析准确率</td>
          <td class="tradeoff-good">高（结构化文档）</td>
          <td class="tradeoff-good">高（复杂排版）</td>
          <td class="tradeoff-mid">中高</td>
        </tr>
        <tr>
          <td class="tradeoff-dim">处理速度</td>
          <td class="tradeoff-good">快（~2s/页）</td>
          <td class="tradeoff-bad">慢（~15s/页）</td>
          <td class="tradeoff-mid">中（~5s/页）</td>
        </tr>
        <tr>
          <td class="tradeoff-dim">GPU 内存</td>
          <td class="tradeoff-good">2-4 GB</td>
          <td class="tradeoff-bad">16-24 GB</td>
          <td class="tradeoff-mid">8-12 GB</td>
        </tr>
        <tr>
          <td class="tradeoff-dim">适用场景</td>
          <td>标准 PDF、扫描件</td>
          <td>复杂排版、多语言混排</td>
          <td>需要精确表格提取</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="tradeoff-verdict">
    <strong>结论：</strong>对于大多数场景，传统 Pipeline 是性价比最高的选择。VLM 适合准确率优先且 GPU 资源充足的场景。混合模式是过渡方案。
  </div>
</div>
```

**Rules:**
- At least 1 per guide
- Always include a "verdict" row or section at the bottom with a clear recommendation
- Use color coding: `tradeoff-good` (green), `tradeoff-mid` (amber), `tradeoff-bad` (red)
- Dimensions should cover: performance, resource usage, complexity, accuracy, maintainability
- Data must come from actual code analysis (batch sizes, config defaults, benchmark results)

---

## Scenario Judge (Engineer Mode)

Present 3-4 real-world scenarios and evaluate the project's suitability for each. This helps engineers quickly determine if the project fits their use case.

**Wiring:** `main.js` auto-initializes. Clicking a scenario card expands the detailed analysis. Use `onclick="toggleScenario(this)"`.

**HTML:**
```html
<div class="scenario-judge animate-in">
  <h3 class="sj-title">场景适配评估</h3>
  <p class="sj-desc">评估此项目在典型使用场景下的适用度</p>

  <div class="sj-card" data-verdict="excellent">
    <div class="sj-card-header" onclick="toggleScenario(this)">
      <span class="sj-verdict sj-excellent">非常适合</span>
      <h4 class="sj-scenario">企业内部知识库：处理 PDF/Word 文档，支持全文检索</h4>
      <span class="sj-toggle">▾</span>
    </div>
    <div class="sj-card-body" style="display:none">
      <div class="sj-pros-cons">
        <div class="sj-pros">
          <h5>优势</h5>
          <ul>
            <li>内置 14 种分块模板，适配不同文档结构</li>
            <li>混合检索（全文 + 向量 + 重排序）开箱即用</li>
            <li>支持增量索引，适合持续增长的知识库</li>
          </ul>
        </div>
        <div class="sj-cons">
          <h5>注意</h5>
          <ul>
            <li>DeepDoc 依赖 ONNX 模型，首次启动需下载 ~500MB</li>
            <li>中文文档表格识别准确率约 85%，复杂表格需人工校验</li>
          </ul>
        </div>
      </div>
      <div class="sj-config-tips">
        <strong>推荐配置：</strong>
        <code>chunk_method=naive, chunk_size=512, similarity_threshold=0.7</code>
      </div>
    </div>
  </div>

  <div class="sj-card" data-verdict="caution">
    <div class="sj-card-header" onclick="toggleScenario(this)">
      <span class="sj-verdict sj-caution">需要评估</span>
      <h4 class="sj-scenario">实时聊天机器人：需要 &lt;500ms 响应的客服场景</h4>
      <span class="sj-toggle">▾</span>
    </div>
    <div class="sj-card-body" style="display:none">
      <div class="sj-pros-cons">
        <div class="sj-pros">
          <h5>优势</h5>
          <ul>
            <li>API 设计支持流式输出</li>
            <li>检索缓存机制减少重复查询</li>
          </ul>
        </div>
        <div class="sj-cons">
          <h5>注意</h5>
          <ul>
            <li>完整检索链路（检索 + 重排序 + LLM）平均 2-4 秒</li>
            <li>Go 服务层增加了部署复杂度</li>
            <li>需要额外的缓存层才能达到 500ms 目标</li>
          </ul>
        </div>
      </div>
      <div class="sj-config-tips">
        <strong>如果要使用：</strong>
        <p>建议仅使用检索部分（跳过 LLM 生成），配合外部低延迟模型。考虑 Redis 缓存热门查询。</p>
      </div>
    </div>
  </div>

  <div class="sj-card" data-verdict="poor">
    <div class="sj-card-header" onclick="toggleScenario(this)">
      <span class="sj-verdict sj-poor">不推荐</span>
      <h4 class="sj-scenario">多模态文档处理：视频/音频转文本并建索引</h4>
      <span class="sj-toggle">▾</span>
    </div>
    <div class="sj-card-body" style="display:none">
      <p class="sj-reason">项目核心能力集中在文本和结构化文档，不支持音视频输入。虽然有 Agent 框架可以扩展，但需要自行开发音视频处理管道，工作量接近重新开发。</p>
      <p class="sj-alternative"><strong>替代方案：</strong>考虑 Whisper + 本项目组合：Whisper 处理音视频转文本，输出接入本项目的索引管道。</p>
    </div>
  </div>
</div>
```

**Rules:**
- At least 1 per guide
- Include a mix: 1-2 "excellent fit", 1 "needs evaluation", 1 "not recommended"
- For "not recommended" scenarios, always suggest an alternative or combination approach
- Be specific about configurations and gotchas — don't just say "it works" or "it doesn't"

---

## Integration Blueprint (Engineer Mode)

Shows how data flows between this project and other systems. Includes concrete code examples for common integration patterns.

**HTML:**
```html
<div class="integration-blueprint animate-in">
  <h3 class="ib-title">集成蓝图：与 LlamaIndex 组合使用</h3>
  <p class="ib-desc">将本项目的文档解析能力与 LlamaIndex 的索引和查询能力结合</p>

  <div class="ib-flow">
    <div class="ib-node ib-node-source">
      <div class="ib-node-icon">📄</div>
      <span class="ib-node-label">原始文档</span>
    </div>
    <div class="ib-arrow">→</div>
    <div class="ib-node ib-node-this">
      <div class="ib-node-icon">⚙️</div>
      <span class="ib-node-label">本项目解析器</span>
      <span class="ib-node-detail">PDF → 结构化 JSON</span>
    </div>
    <div class="ib-arrow">→</div>
    <div class="ib-node ib-node-bridge">
      <div class="ib-node-icon">🔗</div>
      <span class="ib-node-label">格式转换</span>
      <span class="ib-node-detail">JSON → LlamaIndex Document</span>
    </div>
    <div class="ib-arrow">→</div>
    <div class="ib-node ib-node-target">
      <div class="ib-node-icon">🔍</div>
      <span class="ib-node-label">LlamaIndex</span>
      <span class="ib-node-detail">VectorStoreIndex + 查询</span>
    </div>
  </div>

  <div class="ib-code-section">
    <h4 class="ib-code-title">桥接代码示例</h4>
    <div class="translation-block">
      <div class="translation-code">
        <span class="translation-label">INTEGRATION CODE</span>
        <pre><code>
<span class="code-line"><span class="code-keyword">from</span> project <span class="code-keyword">import</span> DocumentParser</span>
<span class="code-line"><span class="code-keyword">from</span> llama_index.core <span class="code-keyword">import</span> Document</span>
<span class="code-line"></span>
<span class="code-line">parser = DocumentParser(backend=<span class="code-string">"pipeline"</span>)</span>
<span class="code-line">result = parser.parse(<span class="code-string">"report.pdf"</span>)</span>
<span class="code-line"></span>
<span class="code-line"><span class="code-comment"># 转换为本项目输出格式 → LlamaIndex Document</span></span>
<span class="code-line">documents = [</span>
<span class="code-line">    Document(</span>
<span class="code-line">        text=block.text,</span>
<span class="code-line">        metadata={<span class="code-string">"source"</span>: block.page_num}</span>
<span class="code-line">    )</span>
<span class="code-line">    <span class="code-keyword">for</span> block <span class="code-keyword">in</span> result.blocks</span>
<span class="code-line">    <span class="code-keyword">if</span> block.type != BlockType.IMAGE</span>
<span class="code-line">]</span>
        </code></pre>
      </div>
      <div class="translation-english">
        <span class="translation-label">工程分析</span>
        <div class="translation-lines">
          <p class="tl">直接使用项目 API 而非 CLI 调用——减少进程间通信开销</p>
          <p class="tl">backend 参数可选 pipeline/vlm/hybrid，根据场景选择</p>
          <p class="tl">解析结果为结构化的 block 列表，每个 block 有类型和位置信息</p>
          <p class="tl">过滤掉 IMAGE 类型——LlamaIndex 的文本索引不处理图片，需要单独处理多模态</p>
          <p class="tl">metadata 保留页码信息，方便后续引用溯源</p>
        </div>
      </div>
    </div>
  </div>

  <div class="ib-compat-notes">
    <h4>兼容性注意事项</h4>
    <div class="ib-note ib-note-warn">
      <span class="ib-note-icon">⚠️</span>
      <p>两个项目的 Python 版本要求可能冲突——本项目要求 3.10+，部分 LlamaIndex 集成包要求 3.9。建议使用 venv 隔离。</p>
    </div>
    <div class="ib-note ib-note-info">
      <span class="ib-note-icon">ℹ️</span>
      <p>本项目输出的中间 JSON 格式可以通过 <code>to_llamaindex()</code> 工具函数直接转换（需安装 <code>project[llamaindex]</code> extra）。</p>
    </div>
  </div>
</div>
```

**Rules:**
- At least 1 per guide (if the project has integration points)
- Show REAL code, not pseudocode — the integration example must be runnable
- Include compatibility notes, version conflicts, and gotchas
- The flow diagram at the top gives the big picture; the code below makes it actionable

---

## Risk Indicators (Engineer Mode)

Colored badges that indicate the severity of identified risks, limitations, or failure modes. Use inline within text or in dedicated risk assessment sections.

**HTML — inline usage:**
```html
<p>单节点部署时最大并发查询数约 50 QPS <span class="risk-badge risk-medium">🟡 中等风险</span>，超过此阈值检索延迟显著上升。</p>
```

**HTML — risk assessment panel:**
```html
<div class="risk-panel animate-in">
  <h3 class="risk-panel-title">风险评估</h3>
  <div class="risk-items">
    <div class="risk-item">
      <span class="risk-badge risk-high">🔴 高风险</span>
      <div class="risk-content">
        <strong>表格识别准确率</strong>
        <p>复杂嵌套表格的识别准确率约 70-80%，在生产环境中可能需要人工后处理。<code>src/deepdoc/table_recognizer.py:156</code> 中的 NMS 阈值硬编码为 0.3，无法通过配置调整。</p>
      </div>
    </div>
    <div class="risk-item">
      <span class="risk-badge risk-medium">🟡 中等风险</span>
      <div class="risk-content">
        <strong>Go 服务依赖</strong>
        <p>API 服务层用 Go 实现，Python 核心通过 gRPC 通信。这意味着调试需要同时理解两种语言的工具链，且 gRPC 序列化增加了约 5ms 的延迟。</p>
      </div>
    </div>
    <div class="risk-item">
      <span class="risk-badge risk-low">🟢 低风险</span>
      <div class="risk-content">
        <strong>模型版本锁定</strong>
        <p>ONNX 模型与特定版本绑定，升级需要重新验证。但有版本管理机制，且模型更新频率低（每季度一次）。</p>
      </div>
    </div>
  </div>
</div>
```

**Rules:**
- Use throughout the guide wherever limitations or risks are mentioned
- 🔴 High Risk: Will cause production issues, requires mitigation strategy
- 🟡 Medium Risk: May cause issues in specific scenarios, has workarounds
- 🟢 Low Risk: Minor inconvenience, unlikely to cause production problems
- Always explain WHY the risk exists with a specific code reference

---

## Verdict Callout (Engineer Mode)

Summary judgment at the end of each module. Concise, opinionated, and actionable.

**HTML:**
```html
<div class="verdict-callout animate-in">
  <div class="verdict-icon">⚖️</div>
  <div class="verdict-content">
    <span class="verdict-label">模块结论</span>
    <p class="verdict-text">Pipeline 架构设计<strong class="verdict-strong">合理且有前瞻性</strong>。统一接口 + 后端可插拔的模式在当前规模下是正确选择。唯一的结构性风险是 Pipeline 阶段之间耦合较紧——中间阶段的数据格式变更会影响所有下游阶段。</p>
    <div class="verdict-action">
      <strong>建议：</strong>如果你需要自定义处理阶段，优先通过配置参数而非修改源码来实现。参考 <code>pipeline_config.yaml</code> 中的 stage_options。
    </div>
  </div>
</div>
```

**Variants:**
- `verdict-positive`: green left border, for strong design decisions
- `verdict-mixed`: amber left border, for adequate but imperfect decisions  
- `verdict-negative`: red left border, for weak or problematic design choices

**Rules:**
- One verdict callout at the end of each module
- Must be opinionated — don't hedge with "it depends"
- Must include a concrete, actionable recommendation
- Reference specific code or configuration

---

## Critical Path Trace (Engineer Mode)

Step-by-step code walkthrough of the most important operations. Unlike Beginner Mode's flow animations, this shows actual code with engineering commentary explaining WHY each step exists.

**HTML:**
```html
<div class="critical-path animate-in">
  <h3 class="cp-title">关键路径：PDF 文档解析全流程</h3>
  <p class="cp-desc">追踪一份 PDF 从上传到生成结构化文档的完整代码路径</p>

  <div class="cp-steps">
    <div class="cp-step">
      <div class="cp-step-marker">
        <span class="cp-step-num">1</span>
        <code class="cp-step-file">api/upload.py:34-42</code>
      </div>
      <div class="cp-step-content">
        <div class="translation-block">
          <div class="translation-code">
            <span class="translation-label">CODE</span>
            <pre><code>
<span class="code-line"><span class="code-keyword">async def</span> <span class="code-function">upload_document</span>(file: UploadFile):</span>
<span class="code-line">    content = <span class="code-keyword">await</span> file.read()</span>
<span class="code-line">    doc_hash = hashlib.md5(content).hexdigest()</span>
<span class="code-line">    <span class="code-keyword">if</span> cache.exists(doc_hash):</span>
<span class="code-line">        <span class="code-keyword">return</span> cache.get(doc_hash)</span>
<span class="code-line">    task = parse_queue.enqueue(content, file.filename)</span>
<span class="code-line">    <span class="code-keyword">return</span> {<span class="code-string">"task_id"</span>: task.id, <span class="code-string">"status"</span>: <span class="code-string">"queued"</span>}</span>
            </code></pre>
          </div>
          <div class="translation-english">
            <span class="translation-label">工程分析</span>
            <div class="translation-lines">
              <p class="tl"><strong>入口即异步</strong>——使用 async 避免阻塞事件循环，这对于同时处理多个上传请求至关重要</p>
              <p class="tl"><strong>MD5 哈希做去重</strong>——相同文件不会重复解析，这对知识库场景是重要的优化。但注意：MD5 不适合安全场景，这里仅用于缓存键</p>
              <p class="tl"><strong>入队而非同步处理</strong>——解析是 CPU/GPU 密集型任务，通过队列异步处理，API 立即返回 task_id。这是正确的设计——解析可能需要数十秒</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="cp-step">
      <div class="cp-step-marker">
        <span class="cp-step-num">2</span>
        <code class="cp-step-file">parser/worker.py:78-95</code>
      </div>
      <div class="cp-step-content">
        <div class="translation-block">
          <div class="translation-code">
            <span class="translation-label">CODE</span>
            <pre><code>
<span class="code-line"><span class="code-keyword">def</span> <span class="code-function">process_task</span>(task: ParseTask):</span>
<span class="code-line">    backend = select_backend(task.filename)</span>
<span class="code-line">    pipeline = PipelineFactory.create(backend)</span>
<span class="code-line">    result = pipeline.execute(task.content)</span>
<span class="code-line">    cache.store(task.doc_hash, result)</span>
<span class="code-line">    <span class="code-keyword">return</span> result</span>
            </code></pre>
          </div>
          <div class="translation-english">
            <span class="translation-label">工程分析</span>
            <div class="translation-lines">
              <p class="tl"><strong>后端自动选择</strong>——根据文件扩展名选择最合适的解析后端。这个决策是隐式的，调用方无需关心</p>
              <p class="tl"><strong>工厂模式创建 Pipeline</strong>——PipelineFactory 封装了复杂的依赖注入逻辑。这增加了代码可读性，但让调试时需要多跳一层</p>
              <p class="tl"><strong>结果缓存到持久化存储</strong>——与入口的 MD5 检查形成闭环</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

**Rules:**
- At least 2 critical path traces per guide
- Each step must include real code from the codebase with exact file path and line numbers
- Engineering commentary explains WHY, not WHAT — assume the reader can read code
- Focus on the 3-5 most important code paths in the entire project
- Highlight design patterns, potential issues, and non-obvious decisions

---

## Source File Map (Engineer Mode)

An annotated directory tree that classifies each key source file/directory as **framework** (骨架/框架性) or **functional** (功能/功能性). This is the most important orienting element for developers — it answers "which files should I read first to understand how this project works?"

**Wiring:** `main.js` auto-initializes every `.source-file-map` on page load. Directory nodes are expandable/collapsible via `onclick="toggleSfmDir(this)"`. Role filter buttons toggle visibility.

**HTML:**
```html
<div class="source-file-map animate-in">
  <div class="sfm-header">
    <h3 class="sfm-title">源码文件地图</h3>
    <p class="sfm-desc">项目核心源码分类：<span class="sfm-badge sfm-framework">框架性</span> 文件定义架构骨架，<span class="sfm-badge sfm-functional">功能性</span> 文件实现具体能力</p>
    <div class="sfm-filters">
      <button class="sfm-filter active" onclick="filterSfm(this, 'all')">全部</button>
      <button class="sfm-filter" onclick="filterSfm(this, 'framework')">仅框架</button>
      <button class="sfm-filter" onclick="filterSfm(this, 'functional')">仅功能</button>
      <button class="sfm-filter" onclick="filterSfm(this, 'entry')">入口文件</button>
    </div>
  </div>

  <div class="sfm-stats">
    <div class="sfm-stat">
      <span class="sfm-stat-num">47</span>
      <span class="sfm-stat-label">核心文件</span>
    </div>
    <div class="sfm-stat">
      <span class="sfm-stat-num">12</span>
      <span class="sfm-stat-label">框架文件</span>
    </div>
    <div class="sfm-stat">
      <span class="sfm-stat-num">35</span>
      <span class="sfm-stat-label">功能文件</span>
    </div>
    <div class="sfm-stat">
      <span class="sfm-stat-num">~18K</span>
      <span class="sfm-stat-label">核心代码行</span>
    </div>
  </div>

  <div class="sfm-tree">
    <!-- Directory (expandable) -->
    <div class="sfm-dir open" data-role="framework">
      <div class="sfm-dir-header" onclick="toggleSfmDir(this)">
        <span class="sfm-arrow">▾</span>
        <span class="sfm-dir-name">rag/</span>
        <span class="sfm-role sfm-framework">框架</span>
        <span class="sfm-dir-desc">RAG 核心框架层——定义检索增强的骨架</span>
      </div>
      <div class="sfm-dir-children">
        <!-- Framework file -->
        <div class="sfm-file" data-role="framework">
          <span class="sfm-file-icon">📄</span>
          <span class="sfm-file-name">settings.py</span>
          <span class="sfm-role sfm-framework">框架</span>
          <span class="sfm-file-loc">~280 LOC</span>
          <span class="sfm-file-desc">全局配置单例，定义所有可调参数</span>
        </div>

        <!-- Functional file -->
        <div class="sfm-file" data-role="functional">
          <span class="sfm-file-icon">📄</span>
          <span class="sfm-file-name">naive.py</span>
          <span class="sfm-role sfm-functional">功能</span>
          <span class="sfm-file-loc">~420 LOC</span>
          <span class="sfm-file-desc">通用文档分块实现，14 种模板策略</span>
        </div>

        <!-- Entry point file -->
        <div class="sfm-file sfm-entry" data-role="entry">
          <span class="sfm-file-icon">🚀</span>
          <span class="sfm-file-name">__init__.py</span>
          <span class="sfm-role sfm-framework">框架</span>
          <span class="sfm-file-loc">~45 LOC</span>
          <span class="sfm-file-desc">模块入口，定义公开 API 和导入链</span>
        </div>

        <!-- Nested directory -->
        <div class="sfm-dir" data-role="functional">
          <div class="sfm-dir-header" onclick="toggleSfmDir(this)">
            <span class="sfm-arrow">▸</span>
            <span class="sfm-dir-name">app/</span>
            <span class="sfm-role sfm-functional">功能</span>
            <span class="sfm-dir-desc">各文档类型的具体解析器实现</span>
          </div>
          <div class="sfm-dir-children" style="display:none">
            <div class="sfm-file" data-role="functional">
              <span class="sfm-file-icon">📄</span>
              <span class="sfm-file-name">naive.py</span>
              <span class="sfm-role sfm-functional">功能</span>
              <span class="sfm-file-loc">~340 LOC</span>
              <span class="sfm-file-desc">通用/naive 分块策略</span>
            </div>
            <div class="sfm-file" data-role="functional">
              <span class="sfm-file-icon">📄</span>
              <span class="sfm-file-name">paper.py</span>
              <span class="sfm-role sfm-functional">功能</span>
              <span class="sfm-file-loc">~180 LOC</span>
              <span class="sfm-file-desc">学术论文专用分块（识别 section/abstract）</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Another top-level directory -->
    <div class="sfm-dir" data-role="framework">
      <div class="sfm-dir-header" onclick="toggleSfmDir(this)">
        <span class="sfm-arrow">▸</span>
        <span class="sfm-dir-name">deepdoc/</span>
        <span class="sfm-role sfm-framework">框架</span>
        <span class="sfm-dir-desc">文档理解引擎——OCR、布局分析、表格识别的统一接口</span>
      </div>
      <div class="sfm-dir-children" style="display:none">
        <!-- files here -->
      </div>
    </div>
  </div>

  <div class="sfm-legend">
    <div class="sfm-legend-item">
      <span class="sfm-role sfm-framework">框架</span>
      <span>定义项目骨架——抽象接口、配置系统、插件加载、生命周期管理。读这些文件理解架构。</span>
    </div>
    <div class="sfm-legend-item">
      <span class="sfm-role sfm-functional">功能</span>
      <span>实现具体能力——特定解析器、特定模型、特定 API。读这些文件理解功能边界。</span>
    </div>
    <div class="sfm-legend-item">
      <span class="sfm-role sfm-framework">🚀 入口</span>
      <span>程序启动点——main.py、cli.py、app.py。从这里开始追踪代码执行路径。</span>
    </div>
  </div>

  <div class="sfm-reading-order">
    <h4 class="sfm-reading-title">推荐阅读顺序</h4>
    <div class="sfm-reading-steps">
      <div class="sfm-reading-step">
        <span class="sfm-reading-num">1</span>
        <code>rag/settings.py</code>
        <span class="sfm-reading-reason">先看全局配置，理解所有可调参数的默认值</span>
      </div>
      <div class="sfm-reading-step">
        <span class="sfm-reading-num">2</span>
        <code>deepdoc/vision/__init__.py</code>
        <span class="sfm-reading-reason">理解模型层的抽象接口设计</span>
      </div>
      <div class="sfm-reading-step">
        <span class="sfm-reading-num">3</span>
        <code>rag/svr/task_executor.py</code>
        <span class="sfm-reading-reason">核心执行引擎——文档解析的主循环在这里</span>
      </div>
    </div>
  </div>
</div>
```

**Rules:**
- Exactly 1 Source File Map per guide, placed in Module 1 (架构全景)
- List the top 30-50 most important files/directories — not every file
- Every file/directory must be classified as framework or functional
- Include a "reading order" section: the 3-5 files a developer should read first to understand the architecture
- Use real file paths from the codebase (verify they exist)
- Approximate LOC counts are fine (don't need exact counts)
- Group files by their parent directory, with directory-level summaries
- The filter buttons (全部/仅框架/仅功能/入口文件) must work — this helps engineers focus on what they care about
