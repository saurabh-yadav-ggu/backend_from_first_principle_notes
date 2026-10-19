# gen_head.py - Head, CSS, Header, and Modal
def get_head_css():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Design a URL Shortener (TinyURL / Bitly) — Complete hand-drawn sketch notes masterclass covering 5-step framework, MD5 collisions, distributed counters, Apache ZooKeeper, 64-bit Snowflake IDs, Bloom filters, 301 vs 302 redirects, and dual-layer cache TTL expiry.">
  <title>Design a URL Shortener — System Design Sketch Notes Masterclass</title>

  <!-- Google Fonts: Lexend (rules.md) & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Lexend:wght@100..900&display=swap" rel="stylesheet">

  <!-- Shared Sketch Theme CSS -->
  <link rel="stylesheet" href="{{ url_for('static', path='css/sketch-theme.css') }}">

  <style>
    /* Scoped Chapter Styles & Design System (rules.md & notestructre.md) */
    :root {
      --paper-note: #F4F1EA;
      --paper-card: #FFFFFF;
      --ink-blue: #0E2A5C;
      --ink-subtle: #1e3a6d;
      --pencil-grey: #333333;
      --pencil-light: #555555;
      --alert-red: #D12828;
      --alert-red-subtle: rgba(209, 40, 40, 0.12);
      --highlighter-yellow: #FFFFA5;
      --highlighter-green: #d4f8d4;
      --ballpoint-blue: #0000FF;
      --border-dark: #0E2A5C;
      --border-subtle: #cbd5e1;

      --font-hand: 'Lexend', sans-serif;
      --font-sans: 'Lexend', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;

      --header-height: 68px;
      --footer-height: 64px;
      --container-max: 1180px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html { scroll-behavior: smooth; }

    body {
      background-color: var(--paper-note);
      color: var(--pencil-grey);
      font-family: 'Lexend', sans-serif;
      font-optical-sizing: auto;
      background-image: linear-gradient(rgba(180, 195, 220, 0.25) 1px, transparent 1px);
      background-size: 100% 1.6em;
      line-height: 1.6;
      font-size: 1.05rem;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    a { color: inherit; text-decoration: none; }
    button { font-family: inherit; cursor: pointer; border: none; background: none; }

    .container {
      width: 100%;
      max-width: var(--container-max);
      margin: 0 auto;
      padding: 0 1.25rem;
    }

    /* Global Header */
    .app-header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(244, 241, 234, 0.95);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border-bottom: 2px solid var(--ink-blue);
      box-shadow: 0 2px 6px rgba(14, 42, 92, 0.08);
      height: var(--header-height);
    }

    .header-inner {
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      flex-wrap: wrap;
    }

    .nav-portal-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.3rem 0.65rem;
      background: var(--paper-card);
      border: 2px solid var(--ink-blue);
      border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--ink-blue);
      box-shadow: 2px 2px 0px 0px var(--ink-blue);
      transition: all 0.15s ease;
    }
    .nav-portal-btn:hover {
      transform: translateY(-1px);
      box-shadow: 3px 3px 0px 0px var(--alert-red);
      border-color: var(--alert-red);
      color: var(--alert-red);
    }

    .chapter-badge-title {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.25rem 0.6rem;
      background: var(--highlighter-yellow);
      border: 2px solid var(--ink-blue);
      border-radius: 255px 12px 225px 12px/12px 225px 12px 255px;
      font-size: 0.82rem;
      font-weight: 800;
      color: var(--ink-blue);
    }

    /* View Switcher Tabs */
    .view-tabs {
      display: inline-flex;
      align-items: center;
      background: #EAE6DC;
      border: 2px solid var(--ink-blue);
      border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;
      padding: 0.2rem;
      gap: 0.2rem;
    }

    .view-tab-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.35rem 0.65rem;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--ink-blue);
      transition: all 0.15s ease;
    }
    .view-tab-btn:hover { background: rgba(255, 255, 165, 0.6); }
    .view-tab-btn.active {
      background: var(--ink-blue);
      color: #FFF;
      box-shadow: 1px 2px 0px 0px rgba(0,0,0,0.2);
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .icon-action-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 36px;
      height: 36px;
      background: var(--paper-card);
      border: 2px solid var(--ink-blue);
      border-radius: 255px 10px 225px 10px/10px 225px 10px 255px;
      color: var(--ink-blue);
      box-shadow: 2px 2px 0px 0px var(--ink-blue);
      transition: all 0.15s ease;
    }
    .icon-action-btn:hover {
      transform: translateY(-1px);
      background: var(--highlighter-yellow);
    }
    .icon-action-btn.active {
      background: var(--alert-red);
      color: #FFF;
      border-color: var(--alert-red);
    }

    /* Main Container & Layout */
    main { flex: 1; padding: 2rem 0 4rem; }

    .presentation-deck {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .slide-wrapper {
      display: none;
      animation: fadeIn 0.25s ease-in-out;
    }
    .slide-wrapper.active { display: block; }
    .presentation-deck.scroll-all-mode .slide-wrapper {
      display: block !important;
      margin-bottom: 2.5rem;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Sketch Cards & Borders */
    .slide-card {
      background: var(--paper-card);
      border: 2px solid var(--ink-blue);
      border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;
      box-shadow: 4px 5px 0px 0px var(--ink-blue);
      padding: 2.25rem;
      position: relative;
    }

    .tape-top::before {
      content: "";
      position: absolute;
      top: -12px;
      left: 50%;
      transform: translateX(-50%) rotate(-1deg);
      width: 140px;
      height: 24px;
      background: rgba(255, 255, 255, 0.65);
      border: 1px dashed rgba(14, 42, 92, 0.35);
      backdrop-filter: blur(2px);
      box-shadow: 0 1px 3px rgba(0,0,0,0.08);
      z-index: 10;
    }

    .slide-meta-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2px dashed #e2e8f0;
      padding-bottom: 1rem;
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .slide-step-badge {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.2rem 0.55rem;
      background: var(--ink-blue);
      color: #FFF;
      border-radius: 4px;
      font-family: var(--font-mono);
    }

    .slide-topic-tag {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--alert-red);
      font-family: var(--font-mono);
    }

    .slide-bookmark-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--ink-blue);
      padding: 0.2rem 0.5rem;
      border: 1px dashed var(--ink-blue);
      border-radius: 4px;
      background: #F4F1EA;
      transition: all 0.15s ease;
    }
    .slide-bookmark-btn:hover, .slide-bookmark-btn.active {
      background: var(--highlighter-yellow);
      color: var(--alert-red);
      border-color: var(--alert-red);
    }

    .slide-title {
      font-size: 2.1rem;
      font-weight: 800;
      color: var(--ink-blue);
      line-height: 1.25;
      margin-bottom: 0.85rem;
      letter-spacing: -0.02em;
    }

    .slide-intro {
      font-size: 1.15rem;
      color: #444;
      margin-bottom: 1.75rem;
      font-weight: 400;
      max-width: 950px;
      line-height: 1.6;
    }

    /* Content Layout Grids */
    .content-grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      margin-top: 1.25rem;
    }

    .content-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.25rem;
      margin-top: 1.25rem;
    }

    @media (max-width: 860px) {
      .content-grid-2, .content-grid-3 { grid-template-columns: 1fr; }
      .slide-title { font-size: 1.65rem; }
      .slide-card { padding: 1.5rem; }
    }

    .card {
      padding: 1.25rem;
      border-radius: 8px;
      border: 2px solid var(--ink-blue);
      box-shadow: 2px 2px 0px 0px var(--ink-blue);
      background: #FFF;
      position: relative;
    }

    .card-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--ink-blue);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .card-yellow { background: var(--highlighter-yellow); }
    .card-blue { background: #EBF3FF; }
    .card-red { background: #FFF0F0; border-color: var(--alert-red); }
    .card-green { background: #F0FDF4; border-color: #166534; }
    .card-white { background: #FFFFFF; }

    /* Diagram Canvas Containers */
    .sketch-diagram-box {
      background: #FFFFFF;
      border: 2px solid var(--ink-blue);
      border-radius: 10px;
      padding: 1.5rem;
      margin: 1.5rem 0;
      box-shadow: inset 0 0 10px rgba(0,0,0,0.03);
      position: relative;
    }

    .diagram-caption {
      margin-top: 0.75rem;
      font-size: 0.82rem;
      font-family: var(--font-mono);
      color: #666;
      text-align: center;
      border-top: 1px dashed #cbd5e1;
      padding-top: 0.5rem;
    }

    pre, code { font-family: var(--font-mono); }
    code {
      background: #EAE6DC;
      color: #0E2A5C;
      padding: 0.15rem 0.35rem;
      border-radius: 4px;
      font-size: 0.9em;
      border: 1px solid #d5cebf;
    }
    pre code { background: transparent; padding: 0; border: none; color: inherit; }

    .code-terminal {
      background: #1E293B;
      color: #E2E8F0;
      border-radius: 8px;
      border: 2px solid var(--ink-blue);
      box-shadow: 3px 3px 0px 0px var(--ink-blue);
      padding: 1.25rem;
      overflow-x: auto;
      font-size: 0.88rem;
      margin: 1rem 0;
      position: relative;
    }

    .sticky-note-callout {
      background: var(--highlighter-yellow);
      border: 2px solid var(--ink-blue);
      border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;
      box-shadow: 3px 3px 0px 0px var(--ink-blue);
      padding: 1rem 1.25rem;
      margin: 1.25rem 0;
      transform: rotate(-0.5deg);
    }

    /* Deck Controls Bar */
    .deck-controls-bar {
      position: sticky;
      bottom: 1.25rem;
      z-index: 90;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      border: 2px solid var(--ink-blue);
      border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;
      box-shadow: 0 4px 12px rgba(14, 42, 92, 0.15);
      padding: 0.65rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 1.5rem;
      gap: 1rem;
    }

    .deck-nav-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.45rem 1rem;
      border: 2px solid var(--ink-blue);
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.9rem;
      background: #FFF;
      color: var(--ink-blue);
      box-shadow: 2px 2px 0px 0px var(--ink-blue);
      transition: all 0.15s ease;
    }
    .deck-nav-btn:hover:not(:disabled) {
      transform: translateY(-1px);
      background: var(--highlighter-yellow);
    }
    .deck-nav-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      box-shadow: none;
    }
    .deck-nav-btn.primary {
      background: var(--alert-red);
      color: #FFF;
      border-color: var(--alert-red);
    }
    .deck-nav-btn.primary:hover:not(:disabled) {
      background: #b91c1c;
      color: #FFF;
    }

    .slide-progress-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.25rem;
      flex: 1;
      max-width: 380px;
    }

    .slide-counter-text {
      font-size: 0.82rem;
      font-weight: 800;
      font-family: var(--font-mono);
      color: var(--ink-blue);
    }

    .progress-bar-track {
      width: 100%;
      height: 8px;
      background: #EAE6DC;
      border: 1.5px solid var(--ink-blue);
      border-radius: 10px;
      overflow: hidden;
    }

    .progress-bar-fill {
      height: 100%;
      background: var(--alert-red);
      width: 4%;
      transition: width 0.2s ease;
    }

    .view-content-wrapper { display: none; }
    .view-content-wrapper.active {
      display: block;
      animation: fadeIn 0.25s ease-in-out;
    }

    /* Drawers */
    .slide-drawer {
      position: fixed;
      top: 0;
      right: -420px;
      width: 400px;
      max-width: 90vw;
      height: 100vh;
      background: var(--paper-note);
      border-left: 2px solid var(--ink-blue);
      box-shadow: -4px 0 20px rgba(0,0,0,0.15);
      z-index: 200;
      transition: right 0.25s ease;
      display: flex;
      flex-direction: column;
      padding: 1.5rem;
    }
    .slide-drawer.active { right: 0; }

    .drawer-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 1rem;
      border-bottom: 2px dashed var(--ink-blue);
      margin-bottom: 1.25rem;
    }

    .drawer-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--ink-blue);
    }

    .drawer-close-btn {
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--alert-red);
      padding: 0.25rem 0.5rem;
    }

    .drawer-overlay {
      position: fixed;
      inset: 0;
      background: rgba(14, 42, 92, 0.4);
      backdrop-filter: blur(3px);
      z-index: 150;
      display: none;
    }
    .drawer-overlay.active { display: block; }

    /* Flashcards */
    .flashcard-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 1.5rem;
      margin-top: 1.5rem;
    }

    .flashcard-item {
      perspective: 1000px;
      height: 240px;
      cursor: pointer;
    }

    .flashcard-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.5s;
      transform-style: preserve-3d;
      border: 2px solid var(--ink-blue);
      border-radius: 12px;
      box-shadow: 3px 4px 0px 0px var(--ink-blue);
    }

    .flashcard-item.flipped .flashcard-inner {
      transform: rotateY(180deg);
    }

    .flashcard-front, .flashcard-back {
      position: absolute;
      width: 100%;
      height: 100%;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 1.5rem;
      border-radius: 10px;
    }

    .flashcard-front { background: #FFFFFF; }
    .flashcard-back {
      background: var(--highlighter-yellow);
      transform: rotateY(180deg);
      text-align: left;
    }

    /* Quiz */
    .quiz-card {
      background: #FFF;
      border: 2px solid var(--ink-blue);
      border-radius: 10px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: 3px 3px 0px 0px var(--ink-blue);
    }

    .quiz-option-btn {
      display: block;
      width: 100%;
      text-align: left;
      padding: 0.75rem 1rem;
      margin: 0.5rem 0;
      background: #F4F1EA;
      border: 1.5px solid var(--ink-blue);
      border-radius: 6px;
      font-size: 0.92rem;
      font-weight: 600;
      color: var(--ink-blue);
      transition: all 0.15s ease;
    }
    .quiz-option-btn:hover:not(.locked) {
      background: var(--highlighter-yellow);
      transform: translateX(4px);
    }
    .quiz-option-btn.correct {
      background: var(--highlighter-green);
      border-color: #166534;
      color: #14532d;
    }
    .quiz-option-btn.incorrect {
      background: #FFE4E4;
      border-color: var(--alert-red);
      color: var(--alert-red);
    }
    .quiz-option-btn.locked { cursor: default; }

    .quiz-explanation-box {
      margin-top: 0.85rem;
      padding: 0.75rem 1rem;
      border-radius: 6px;
      font-size: 0.88rem;
      display: none;
    }

    /* Search Modal Box */
    .search-modal-box {
      position: fixed;
      top: 15%;
      left: 50%;
      transform: translateX(-50%);
      width: 600px;
      max-width: 92vw;
      background: #FFF;
      border: 2px solid var(--ink-blue);
      border-radius: 12px;
      box-shadow: 6px 8px 0px 0px var(--ink-blue);
      z-index: 300;
      padding: 1.5rem;
    }

    /* Simulator Styles */
    .simulator-panel {
      background: #FFF;
      border: 2px solid var(--ink-blue);
      border-radius: 10px;
      padding: 1.5rem;
      box-shadow: 3px 3px 0px 0px var(--ink-blue);
    }

    .sim-input {
      width: 100%;
      background: #F4F1EA;
      border: 2px solid var(--ink-blue);
      padding: 0.65rem 0.85rem;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 0.88rem;
      color: var(--ink-blue);
      margin-top: 0.35rem;
    }
    .sim-input:focus {
      background: #FFF;
      outline: none;
      border-color: var(--alert-red);
    }
  </style>
</head>
<body>
"""

def get_header_and_modal():
    return """
  <!-- =========================================================================
       GLOBAL APP HEADER
       ========================================================================= -->
  <header class="app-header">
    <div class="container header-inner">
      <div class="header-left">
        <a href="/system_design" class="nav-portal-btn" title="Back to System Design Portal">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          <span>System Design Hub</span>
        </a>

        <a href="/" class="nav-portal-btn" style="background:#FFFFA5; color:#0E2A5C; border-color:#0E2A5C;" title="Go to Backend Curriculum">
          <span>Backend Hub →</span>
        </a>

        <button onclick="openWhiteboardModal()" class="nav-portal-btn" style="background:#FFFFA5; color:#0E2A5C; font-weight:800;" title="View Bunny's Hand-Drawn Whiteboard Architecture">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
          <span>Whiteboard Canvas 🖼️</span>
        </button>

        <div class="chapter-badge-title">
          <span class="chapter-text">CH 01 • Design a URL Shortener (Bitly)</span>
        </div>
      </div>

      <!-- View Switcher -->
      <nav class="view-tabs" aria-label="Learning View Selection">
        <button class="view-tab-btn active" data-view="presentation" onclick="switchView('presentation')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
          <span>Slides</span>
        </button>
        <button class="view-tab-btn" data-view="reader" onclick="switchView('reader')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          <span>Textbook</span>
        </button>
        <button class="view-tab-btn" data-view="revision" onclick="switchView('revision')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          <span>Revision</span>
        </button>
        <button class="view-tab-btn" data-view="flashcards" onclick="switchView('flashcards')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
          <span>Flashcards</span>
        </button>
        <button class="view-tab-btn" data-view="quiz" onclick="switchView('quiz')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
          <span>Quiz</span>
        </button>
      </nav>

      <!-- Productivity Tools (Drawers & Modals) -->
      <div class="header-right">
        <button id="headerBookmarkBtn" class="icon-action-btn" title="Toggle Slide Bookmark" onclick="toggleBookmarkCurrentSlide()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
        </button>
        <button class="icon-action-btn" title="Open Global Search (or press /)" onclick="openSearchModal()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        </button>
        <button class="icon-action-btn" title="Table of Contents" onclick="toggleDrawer('tocDrawer')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
        </button>
        <button class="icon-action-btn" title="Personal Study Notes" onclick="toggleDrawer('notesDrawer')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
        </button>
      </div>
    </div>
  </header>

  <!-- Whiteboard Canvas Modal -->
  <div id="whiteboardModal" style="display:none; position:fixed; inset:0; z-index:9999;">
    <div class="drawer-overlay active" onclick="closeWhiteboardModal()"></div>
    <div class="sketch-border sketch-shadow-lg" style="position:fixed; top:4%; left:4%; right:4%; bottom:4%; background:#F4F1EA; z-index:10000; border-radius:12px; display:flex; flex-direction:column; overflow:hidden;">
      <div style="padding:0.75rem 1.25rem; background:#FFF; border-bottom:2px solid var(--ink-blue); display:flex; justify-content:space-between; align-items:center;">
        <div style="display:flex; align-items:center; gap:0.75rem;">
          <span class="slide-step-badge" style="background:#FFFFA5; color:#0E2A5C;">Lecture Source</span>
          <h3 style="font-size:1.15rem; font-weight:800; color:var(--ink-blue); font-family:'Lexend';">
            Interview with Bunny: Original Hand-Drawn Whiteboard Blueprint
          </h3>
        </div>
        <div style="display:flex; align-items:center; gap:0.5rem;">
          <a href="/static/images/url_shortener_whiteboard.png" target="_blank" class="nav-portal-btn" style="font-size:0.78rem;">Full Res ↗</a>
          <button onclick="closeWhiteboardModal()" style="font-size:1.5rem; font-weight:800; color:var(--alert-red); cursor:pointer;">&times;</button>
        </div>
      </div>
      <div style="flex:1; overflow:auto; padding:1.25rem; display:flex; flex-direction:column; align-items:center; background:#EAE6DC; gap:1rem;">
        <div class="card card-yellow" style="width:100%; max-width:980px; font-size:0.85rem; padding:0.65rem 1rem;">
          💡 <strong>Whiteboard Canvas Index:</strong> Section 1: Functional &amp; Non-Functional • Section 2: Core Entities • Section 3: API Contracts • Section 4: HLD • Section 5.1: SHA-1 Encryption (16ms+16ms) • Section 5.2: Counter + Load Balancer + Redis (20% vs 80%) • Section 5.3: ZooKeeper Ephemeral Tree &amp; Snowflake ID Math (69.73 Yrs).
        </div>
        <img src="/static/images/url_shortener_whiteboard.png" alt="Original URL Shortener Whiteboard Lecture by Bunny" style="max-width:100%; border:2px solid var(--ink-blue); border-radius:8px; box-shadow:4px 4px 0px rgba(14,42,92,0.3); background:#FFF;">
      </div>
    </div>
  </div>
"""

def get_deck_controls():
    return """
      <!-- FLOATING DECK CONTROLS -->
      <div id="deckControlsBar" class="deck-controls-bar">
        <button id="prevSlideBtn" class="deck-nav-btn" onclick="navigateSlide(-1)">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
          <span>Previous</span>
        </button>

        <div class="slide-progress-container">
          <div class="slide-counter-text">
            Slide <span id="currentSlideDisplay">1</span> of <span id="totalSlidesDisplay">24</span>
          </div>
          <div class="progress-bar-track">
            <div id="progressBarFill" class="progress-bar-fill"></div>
          </div>
        </div>

        <button id="nextSlideBtn" class="deck-nav-btn primary" onclick="navigateSlide(1)">
          <span>Next</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
        </button>

        <button id="toggleScrollModeBtn" class="deck-nav-btn" onclick="toggleScrollAllMode()" title="Toggle between single slide and viewing all slides stacked" style="margin-left:0.5rem;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
          <span id="scrollModeBtnText">Scroll All Slides</span>
        </button>
      </div>
"""
