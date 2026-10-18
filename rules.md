# Development & Design Rules for Backend Notes 📜

This document defines the **binding engineering, design, typography, and architectural rules** for all contributors and agents working on the *Backend from First Principles* repository.

---

## 1. 🔤 Typography & Font Style Rules

### Primary Font: **Lexend**
The Google Font **Lexend** is the **exclusive, mandatory primary font** across the entire project. It must be applied to the Landing Page, all Chapter Notes, modals, buttons, forms, and flashcards.

* **Google Fonts Import:**
  ```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Lexend:wght@100..900&display=swap" rel="stylesheet">
  ```
* **CSS Font Declaration:**
  ```css
  :root {
    --font-hand: 'Lexend', sans-serif;
    --font-sans: 'Lexend', sans-serif;
    --font-caveat: 'Lexend', sans-serif;
    --font-architect: 'Lexend', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
  }

  body, input, textarea, button, select {
    font-family: 'Lexend', sans-serif;
    font-optical-sizing: auto;
    font-style: normal;
  }
  ```

### Code & Wire Protocol Font: **JetBrains Mono**
* **Font Family:** `'JetBrains Mono', monospace`
* **Mandatory Usage:** All code blocks, cURL commands, HTTP request/response headers, JSON wire payloads, status code badges, and URL paths must strictly use `JetBrains Mono`.

### Font Hierarchy & Sizing
* **Page / Slide Titles (`h1`):** `font-weight: 800` (Extrabold), size `2.25rem` to `3rem`, line-height `1.2`.
* **Section Headings (`h2`):** `font-weight: 700` (Bold), size `1.5rem` to `2rem`.
* **Card & Sub-headings (`h3`):** `font-weight: 600` (Semi-bold), size `1.15rem` to `1.35rem`.
* **Body Text (`p`, `li`):** `font-weight: 400` or `300`, size `1rem` to `1.15rem`, line-height `1.6` to `1.7`.
* **Metadata & Badges:** `font-weight: 700`, uppercase, size `0.75rem` to `0.85rem`.

---

## 2. 🎨 Sketch-Note Visual Identity & Styling Rules

All pages must preserve the custom **hand-drawn engineering sketch-note** look and feel:

1. **Notebook Background:**
   * Warm off-white paper: `#F4F1EA`
   * Subtle horizontal ruling lines: `linear-gradient(rgba(180, 195, 220, 0.25) 1px, transparent 1px)` with `background-size: 100% 1.6em`.
2. **Ink Color Palette:**
   * Primary Pen Ink: `#0E2A5C` (Navy Ink Blue)
   * Red Correction Ink: `#D12828` (Alerts, naive patterns, critical warnings)
   * Electric Ballpoint: `#0000FF` (Interactive hyperlinks, secondary badges)
   * Highlighter Yellow: `#FFFFA5` (Accent markers, key takeaway badges)
   * Highlighter Green: `#D4F8D4` (Success states, correct answers, production patterns)
   * Pencil Grey: `#333333` (Main body copy)
3. **Sketch Borders & Hard Shadows:**
   * Never use sterile flat borders (`border: 1px solid #ccc`).
   * Use wobbly hand-drawn border radiuses:
     ```css
     .sketch-border {
       border: 2px solid var(--ink-blue);
       border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
     }
     ```
   * Use solid offset drop shadows without blur: `box-shadow: 4px 5px 0px 0px var(--ink-blue);`.
4. **Paper Stationery Elements:**
   * Use semi-transparent washi tape (`.tape-top`) on top of cards and sticky notes.
   * Use folded dog-ear corners (`.paper-fold`) on revision sticky notes.

---

## 3. ✅ WHAT YOU MUST DO (Mandatory Best Practices)

1. **Derive Content From Source Transcripts:**
   * Always ground every chapter note in the exact transcript located in `transcript/` or the chapter folder.
   * Explain the first principles: kernel sockets, network routing, RFC standards, idempotency proofs, caching headers, connection pooling.
2. **Build Interactive Widgets in Every Note:**
   * Every chapter note MUST have at least 1–2 real-time interactive widgets (e.g., Idempotency Simulator, URL Builder, Packet Flow Tracer, Status Code Wheel).
3. **Follow the 5-View Learning Architecture:**
   * Ensure every chapter note implements the multi-view system: `presentation` (slides), `reader` (digital textbook), `revision` (summary cards), `flashcards` (flip deck), and `quiz` (interactive test).
4. **Keep Interactivity Self-Contained & Resilient:**
   * All simulators, quizzes, and search features must run client-side in pure vanilla JavaScript without requiring external API servers for basic rendering.
5. **Persist User State to `localStorage`:**
   * Personal notes written in the Notepad drawer must auto-save to `localStorage`.
   * Bookmarked slides, quiz completion, and visited slides must persist across browser reloads.
6. **Support Full Keyboard & Accessibility Navigation:**
   * Support `ArrowLeft` and `ArrowRight` for slide navigation.
   * Support `Escape` to close drawers and modals.
   * Support `/` to focus the search drawer.
   * Support `f` or `F` for fullscreen toggle.
7. **Organize All Web Pages in `templates/`:**
   * All HTML files served by FastAPI MUST live in `d:\Learning\Backend_Notes\templates/`.
   * Register routes cleanly in `main.py` using Jinja2 `TemplateResponse`.
   * Keep shared styles in `static/css/sketch-theme.css`.
8. **Provide Markdown Export for Notes:**
   * The Personal Notepad drawer must feature a 1-click **Export (.md)** button so users can download their notes locally.
9. **Maintain Clean Git Hygiene:**
   * Always respect `.gitignore`.
   * Never commit virtual environments (`venv/`), Python cache (`__pycache__/`), or scratch logs.
10. **Implement Mobile Touch Gestures & Responsive Layouts:**
   * Every presentation slide deck must support horizontal touch swipe gestures (`touchstart`, `touchend`) for navigation on mobile devices.
   * All multi-column grids must gracefully stack to a single column on screens `<= 768px`.
   * Card padding, box shadows, and heading font sizes must scale down on mobile screens to prevent cramped or broken layouts.

---

## 4. 📱 Mobile Device Optimization Rules

Every template in this repository must provide a **first-class smartphone & tablet experience** across all device viewports (from 320px compact phones to 820px tablets):

### Mobile Layout & Typography
* **Viewport Meta Tag:** Always specify `<meta name="viewport" content="width=device-width, initial-scale=1.0">`. Never set `user-scalable=no` (maintain accessibility zoom).
* **Responsive Title Scaling:**
  * Desktop `h1`: `2.5rem` to `3rem`.
  * Mobile (`<= 768px`) `h1`: Scale down to `1.65rem` – `1.85rem` with `line-height: 1.2` so titles never wrap into 5 lines.
  * Mobile (`<= 480px`) `h1`: Scale to `1.45rem` – `1.6rem`.
* **Adaptive Card Padding & Shadows:**
  * Desktop slide cards: `padding: 2.25rem; box-shadow: 8px 10px 0px 0px var(--ink-blue);`.
  * Mobile slide cards: `padding: 1.25rem 0.85rem; box-shadow: 4px 6px 0px 0px var(--ink-blue); border-radius: 16px;`.
* **Stacking Multi-Column Grids:**
  * All `.content-grid-2`, `.content-grid-3`, `.content-grid-4`, and comparison panels MUST collapse to `grid-template-columns: 1fr` on screens `<= 768px`.
* **Touch Targets:**
  * Every button, tab, and interactive selector must have a minimum tap area of `44px × 44px` (or `min-height: 38px` with at least `8px` spacing between tap targets).
* **Code & Table Scrolling:**
  * All `<pre>`, `<code>`, `.sketch-code`, and `<table>` blocks must have `max-width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch;`.
* **Floating Arrow Controls:**
  * Hide fixed side navigation buttons (`.floating-slide-nav`) on screens `<= 900px` so they never overlap slide text or interactive widgets. Rely on touch swipe gestures and bottom controls.
* **Touch Swipe Navigation:**
  * Support intuitive left/right swipe gestures on touchscreens:
    - **Swipe Left:** Navigate to the next slide (`navigateSlideStep(1)`).
    - **Swipe Right:** Navigate to the previous slide (`navigateSlideStep(-1)`).
* **Mobile Drawers & Sheets:**
  * On mobile (`<= 768px`), slide drawers (`tocDrawer`, `notesDrawer`) must expand to `width: 100vw; max-width: 100vw;` with full overlay backdrop.

---

## 5. ❌ WHAT YOU MUST NOT DO (Strict Prohibitions)

1. **DO NOT Use Any Font Other Than Lexend & JetBrains Mono:**
   * Never let headings or body copy revert to browser default fonts (`Arial`, `Times New Roman`, system serif/sans).
   * Never use illegible cursive handwriting fonts for paragraph reading.
2. **DO NOT Create Static, Passive Markdown Dumps:**
   * Never generate notes as flat walls of text without diagrams, interactive elements, or structured slide cards.
3. **DO NOT Cause Horizontal Page Wobble / Overflow on Mobile:**
   * Never allow `overflow-x` on `body` or container elements. The page must stay firmly locked at `100vw` without horizontal shifting while scrolling.
4. **DO NOT Use Fixed Pixel Widths on Layout Containers:**
   * Never use fixed widths like `width: 900px` or `width: 650px`. Always use `width: 100%; max-width: ...; min-width: 0;`.
5. **DO NOT Cover Text With Floating Elements on Mobile:**
   * Never leave desktop floating arrows or sticky overlays pinned over readable content on narrow screens.
6. **DO NOT Create Orphaned HTML Files in Root or Subdirectories:**
   * Do NOT save `.html` files in the root folder (`d:\Learning\Backend_Notes\`) or inside `rest_api/` or `what_is backend_and_its_working/`.
   * Only `templates/` holds active HTML files.
7. **DO NOT Leave Dead Links or Dummy Placeholders:**
   * Never create buttons that do nothing or links pointing to `href="#"`.
   * All navigation must link cleanly to `/`, `/what_is_backend`, `/rest_api`, or open active modals/drawers.
8. **DO NOT Hardcode Hostnames or Absolute Machine Paths in Links:**
   * Never hardcode `http://localhost:8000` or `http://127.0.0.1:8000` inside template links.
   * Use clean relative paths (e.g. `href="/"`, `href="/rest_api"`).
9. **DO NOT Break the Sketch-Note Identity:**
   * Do NOT use generic, corporate Bootstrap or Tailwind default themes (e.g. plain rounded gray cards).
   * The washi tape, sketch borders, notebook lines, and ink colors are mandatory.
10. **DO NOT Rely on Heavy External Front-End Frameworks for Notes:**
   * Do not introduce React, Vue, or Angular builds into the templates unless explicitly requested. Vanilla JS and CSS guarantee instant page loads, zero build steps, and lifetime maintainability.
11. **DO NOT Delete Source Markdown Transcripts:**
   * The `.md` transcript files in `transcript/` and chapter directories are the source of truth for the curriculum and must always be preserved.