# gen_slides_1_8.py - Slides 1 through 8
def get_slides_1_8():
    return """
        <!-- SLIDE 01: Executive Overview & The 5-Step Roadmap -->
        <article class="slide-wrapper active" data-slide-index="0" data-category="Framework">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 01 of 24</span>
              <span class="slide-topic-tag">Masterclass Overview</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h1 class="slide-title">Design a URL Shortener (Bitly) from First Principles</h1>
            <p class="slide-intro">
              Based on the lecture from <strong>Interview with Bunny</strong>: How to architect a global, bulletproof URL shortening service capable of handling <strong>100 Million Daily Active Users</strong>, <strong>1 Billion stored links</strong>, and sub-100ms redirect latency without hash collisions.
            </p>

            <div class="card card-yellow" style="margin-bottom:1.25rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem;">
              <div>
                <strong style="color:var(--ink-blue);">Source Whiteboard Definition:</strong>
                <div style="font-size:0.92rem; color:#333; margin-top:0.25rem;">
                  <em>"Bit.ly is a URL shortener service that lets you shorten and customize links.<br>
                  eg: <code>https://www.facebook.com/anindya.s.dasgupta/</code> ──▶ <code>http://bit.ly/4kycpo</code>"</em>
                </div>
              </div>
              <button onclick="openWhiteboardModal()" class="deck-nav-btn primary" style="font-size:0.82rem; padding:0.4rem 0.8rem;">
                <span>View Whiteboard Canvas 🖼️</span>
              </button>
            </div>

            <!-- 5-Step Strategy Roadmap SVG -->
            <div class="sketch-diagram-box">
              <svg width="100%" height="160" viewBox="0 0 850 150" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Step 1 -->
                <rect x="10" y="30" width="150" height="90" rx="8" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFA5" stroke-dasharray="2 1"/>
                <text x="85" y="60" text-anchor="middle" font-family="Lexend" font-size="13" font-weight="700" fill="#0E2A5C">STEP 1 (10-15m)</text>
                <text x="85" y="82" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="600" fill="#333">Gather Requirements</text>
                <text x="85" y="100" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#D12828">Functional + Non-Func</text>

                <!-- Arrow 1 -->
                <path d="M165 75 L185 75" stroke="#0E2A5C" stroke-width="2.5"/>
                
                <!-- Step 2 -->
                <rect x="190" y="30" width="130" height="90" rx="8" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFFF"/>
                <text x="255" y="60" text-anchor="middle" font-family="Lexend" font-size="13" font-weight="700" fill="#0E2A5C">STEP 2</text>
                <text x="255" y="82" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="600" fill="#333">Core Entities</text>
                <text x="255" y="100" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#0000FF">Short, Long, User</text>

                <!-- Arrow 2 -->
                <path d="M325 75 L345 75" stroke="#0E2A5C" stroke-width="2.5"/>

                <!-- Step 3 -->
                <rect x="350" y="30" width="130" height="90" rx="8" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFFF"/>
                <text x="415" y="60" text-anchor="middle" font-family="Lexend" font-size="13" font-weight="700" fill="#0E2A5C">STEP 3</text>
                <text x="415" y="82" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="600" fill="#333">API Creation</text>
                <text x="415" y="100" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#D12828">POST &amp; GET Contracts</text>

                <!-- Arrow 3 -->
                <path d="M485 75 L505 75" stroke="#0E2A5C" stroke-width="2.5"/>

                <!-- Step 4 -->
                <rect x="510" y="30" width="140" height="90" rx="8" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFFF"/>
                <text x="580" y="60" text-anchor="middle" font-family="Lexend" font-size="13" font-weight="700" fill="#0E2A5C">STEP 4</text>
                <text x="580" y="82" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="600" fill="#333">High-Level Design</text>
                <text x="580" y="100" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#15803d">Client • App • DB</text>

                <!-- Arrow 4 -->
                <path d="M655 75 L675 75" stroke="#0E2A5C" stroke-width="2.5"/>

                <!-- Step 5 -->
                <rect x="680" y="30" width="160" height="90" rx="8" stroke="#D12828" stroke-width="3" fill="#FFFFA5"/>
                <text x="760" y="60" text-anchor="middle" font-family="Lexend" font-size="13" font-weight="800" fill="#D12828">STEP 5 (CORE MEAT)</text>
                <text x="760" y="82" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="600" fill="#333">Low-Level Design</text>
                <text x="760" y="100" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#0E2A5C">ZK + Snowflake + TTL</text>
              </svg>
              <div class="diagram-caption">FIGURE 1.1: Chronological 5-step roadmap followed throughout this masterclass.</div>
            </div>

            <div class="content-grid-2">
              <div class="card card-blue">
                <div class="card-title">⏱️ The 45-Minute Interview Strategy</div>
                <p style="font-size:0.92rem;">
                  Never jump immediately into drawing databases or caches! Spend the first <strong>10 to 15 minutes</strong> clarifying requirements, calculating scale, choosing CAP theorem priorities, and defining REST contracts. If you skip Step 1, you will design the wrong architecture.
                </p>
              </div>

              <div class="card card-yellow">
                <div class="card-title">🏆 What Sets Apart Senior Engineers</div>
                <p style="font-size:0.92rem;">
                  Most candidates recite naive algorithms (random numbers or MD5 truncation). In this masterclass, we explore <strong>3 progressive approaches</strong>, exposing why each fails, leading to Bunny's robust <strong>Hybrid Architecture</strong>: Apache ZooKeeper + 64-bit Snowflake IDs.
                </p>
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 02: Step 1 - Functional Requirements -->
        <article class="slide-wrapper" data-slide-index="1" data-category="Requirements">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 02 of 24</span>
              <span class="slide-topic-tag">Step 1: Functional Scope</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Step 1: Functional Requirements (Scope Definition)</h2>
            <p class="slide-intro">
              Functional requirements define the exact features the system MUST support. From the lecture whiteboard, here are the core functional requirements agreed upon with the interviewer:
            </p>

            <div class="sketch-diagram-box">
              <div style="font-family:'JetBrains Mono'; font-size:0.88rem; display:flex; flex-direction:column; gap:0.6rem;">
                <div style="background:#F4F1EA; border:1.5px solid var(--ink-blue); padding:0.6rem 0.85rem; border-radius:6px;">
                  <strong style="color:var(--ink-blue);">Original Long URL:</strong> <code>https://www.facebook.com/anindya.s.dasgupta/</code>
                </div>
                <div style="text-align:center; font-weight:800; color:var(--alert-red); font-size:1rem;">
                  ▼ URL Shortening Transformation ▼
                </div>
                <div style="background:var(--highlighter-yellow); border:1.5px solid var(--ink-blue); padding:0.6rem 0.85rem; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
                  <div>
                    <strong style="color:var(--ink-blue);">Shortened Link:</strong> <span style="font-weight:800; color:var(--alert-red);">http://bit.ly/4kycpo</span>
                  </div>
                  <span style="font-size:0.8rem; background:#FFF; padding:0.2rem 0.5rem; border:1px solid #ccc; border-radius:4px;">Domain (bit.ly/) + 6-char token (4kycpo)</span>
                </div>
              </div>
              <div class="diagram-caption">FIGURE 2.1: Transformation of long URL into compact 6-character alias.</div>
            </div>

            <div class="content-grid-2">
              <div class="card card-white">
                <div class="card-title">✅ Core Must-Have Features</div>
                <ul style="font-size:0.9rem; padding-left:1.25rem; line-height:1.6; list-style:disc;">
                  <li><strong>Feature 1 (URL Shortening):</strong> Generate a unique compact URL from an arbitrary long URL string.</li>
                  <li><strong>Feature 4 (Redirection):</strong> When a user accesses the short URL, redirect them immediately to the original destination (HTTP 301/302).</li>
                </ul>
              </div>

              <div class="card card-green">
                <div class="card-title">🌟 Optional / Value-Add Features</div>
                <ul style="font-size:0.9rem; padding-left:1.25rem; line-height:1.6; list-style:disc;">
                  <li><strong>Feature 2 (Custom Vanity URL):</strong> Allow users to specify custom aliases (e.g. <code>bit.ly/mywork</code> or <code>bit.ly/bunny</code>).</li>
                  <li><strong>Feature 3 (Expiration Date):</strong> Short links can have an optional TTL (e.g., expires in 30 days, 1 year, or never).</li>
                  <li><strong>Feature 5 (Analytics Tracking):</strong> Track click count, user agent, referrer, and timestamps for telemetry dashboards.</li>
                </ul>
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 03: Step 1 - Non-Functional Requirements & Capacity Numbers -->
        <article class="slide-wrapper" data-slide-index="2" data-category="Requirements">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 03 of 24</span>
              <span class="slide-topic-tag">Scale &amp; Capacity</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Step 1: Non-Functional Requirements &amp; Math</h2>
            <p class="slide-intro">
              Non-functional requirements dictate the engineering constraints: throughput, latency SLA, consistency guarantees, and storage envelope.
            </p>

            <div class="content-grid-3">
              <div class="card card-white">
                <div class="card-title">🌐 Scale Envelope</div>
                <ul style="font-size:0.88rem; padding-left:1.25rem; line-height:1.6; list-style:disc;">
                  <li><strong>100M DAU</strong> (Daily Active Users)</li>
                  <li><strong>1 Billion URLs</strong> stored in DB</li>
                  <li><strong>1 Billion Redirects/Day</strong></li>
                  <li>Average QPS: ~11,500 req/sec</li>
                  <li>Peak QPS (10x): <strong>115,000 req/sec</strong></li>
                </ul>
              </div>

              <div class="card card-yellow">
                <div class="card-title">⚡ Latency SLA</div>
                <ul style="font-size:0.88rem; padding-left:1.25rem; line-height:1.6; list-style:disc;">
                  <li><strong>Redirect Latency:</strong> &lt; 100ms (Redis cache hit &lt; 2ms)</li>
                  <li><strong>URL Creation:</strong> ~200ms acceptable</li>
                  <li><strong>Read:Write Ratio:</strong> 100:1 (read-heavy asymmetric workload)</li>
                </ul>
              </div>

              <div class="card card-red">
                <div class="card-title">🔒 Uniqueness Guarantee</div>
                <ul style="font-size:0.88rem; padding-left:1.25rem; line-height:1.6; list-style:disc;">
                  <li><strong>100% Collision-Free:</strong> No two users can EVER receive the same short code for different URLs.</li>
                  <li><strong>CAP Theorem:</strong> Availability &gt;&gt; Consistency (AP over CP).</li>
                </ul>
              </div>
            </div>

            <div class="sticky-note-callout">
              <p><strong>CAP Theorem First Principle:</strong> Why Availability over Consistency? If Bitly is temporarily inconsistent for 200ms (replica sync delay), nobody notices because a human takes seconds to copy and paste a link. But if Bitly goes down (503 Service Unavailable), the entire business collapses. Hence, <strong>AP (Availability + Partition Tolerance)</strong> is chosen!</p>
            </div>
          </div>
        </article>

        <!-- SLIDE 04: Step 2 - Identifying Core Entities -->
        <article class="slide-wrapper" data-slide-index="3" data-category="Entities">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 04 of 24</span>
              <span class="slide-topic-tag">Step 2: Core Entities</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Step 2: Identifying the Core System Entities</h2>
            <p class="slide-intro">
              From Section 2 of Bunny's whiteboard, there are only <strong>three core entities</strong> involved in the entire lifecycle. Identifying them upfront makes high-level design and schema definition straightforward.
            </p>

            <div class="content-grid-3">
              <div class="card card-white" style="border-top: 4px solid var(--alert-red);">
                <div class="card-title">1. Short URL Entity</div>
                <ul style="font-size: 0.88rem; list-style: disc; padding-left: 1.25rem; line-height: 1.6;">
                  <li><code>short_code</code> (Unique 6-7 char token)</li>
                  <li><code>created_at</code> timestamp</li>
                  <li><code>expires_at</code> timestamp</li>
                  <li><code>is_custom</code> boolean</li>
                </ul>
              </div>

              <div class="card card-white" style="border-top: 4px solid var(--ink-blue);">
                <div class="card-title">2. Long URL Entity</div>
                <ul style="font-size: 0.88rem; list-style: disc; padding-left: 1.25rem; line-height: 1.6;">
                  <li><code>original_url</code> (Full destination string)</li>
                  <li>Protocol (<code>http://</code> or <code>https://</code>)</li>
                  <li>Sanitized target format</li>
                  <li>Payload size up to 2,048 bytes</li>
                </ul>
              </div>

              <div class="card card-white" style="border-top: 4px solid #166534;">
                <div class="card-title">3. User Metadata Entity</div>
                <ul style="font-size: 0.88rem; list-style: disc; padding-left: 1.25rem; line-height: 1.6;">
                  <li><code>user_id</code> (Unique ID)</li>
                  <li><code>account_tier</code> (Free vs Premium)</li>
                  <li>Created links list</li>
                  <li>Rate limit quota usage</li>
                </ul>
              </div>
            </div>

            <div class="card card-yellow" style="margin-top: 1rem;">
              <div class="card-title">💡 Whiteboard Annotation: Combined URL Representation</div>
              <p style="font-size:0.92rem;">
                On the whiteboard, Bunny groups these directly: <strong>URL = (shortURL, longURL, expirationDate, customURL)</strong> and <strong>User = (metadata, auth)</strong>. This clean decoupling prevents bloat in high-throughput query paths.
              </p>
            </div>
          </div>
        </article>

        <!-- SLIDE 05: Step 3 - REST API Designing -->
        <article class="slide-wrapper" data-slide-index="4" data-category="APIs">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 05 of 24</span>
              <span class="slide-topic-tag">Step 3: API Contracts</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Step 3: REST API Designing</h2>
            <p class="slide-intro">
              From Section 3 of Bunny's whiteboard, we define explicit HTTP contracts for URL creation and redirection. Clean API contracts clarify expectations before drawing architecture blocks.
            </p>

            <div class="content-grid-2">
              <!-- POST API -->
              <div class="card card-white">
                <div class="card-title" style="color:var(--alert-red);">1. Create Short URL</div>
                <div class="code-terminal">
                  <div class="code-terminal-header">
                    <span>POST /v1/url (or /s/url)</span>
                    <span>Content-Type: application/json</span>
                  </div>
                  <pre><code>// Request Body
{
  "longURL": "https://www.facebook.com/anindya.s.dasgupta/",
  "customURL": "mywork",         // Optional custom alias
  "expirationDate": "2026-12-31" // Optional TTL
}

// Response (HTTP 201 Created)
{
  "shortURL": "http://bit.ly/4kycpo",
  "longURL": "https://www.facebook.com/anindya.s.dasgupta/",
  "createdAt": "2026-01-26T10:30:00Z",
  "expiresAt": "2026-12-31T23:59:59Z"
}</code></pre>
                </div>
              </div>

              <!-- GET API -->
              <div class="card card-white">
                <div class="card-title" style="color:var(--ink-blue);">2. Redirect to Original URL</div>
                <div class="code-terminal">
                  <div class="code-terminal-header">
                    <span>GET /v1/url/{shortURL}</span>
                    <span>HTTP Wire Headers</span>
                  </div>
                  <pre><code>// Browser Request
GET /4kycpo HTTP/1.1
Host: bit.ly

// Server Redirect Response
HTTP/1.1 302 Found
Location: https://www.facebook.com/anindya.s.dasgupta/
Cache-Control: no-cache, no-store
Date: Mon, 26 Jan 2026 10:30:45 GMT</code></pre>
                </div>
              </div>
            </div>

            <div class="sticky-note-callout">
              <p><strong>REST Design Rule:</strong> The redirect endpoint does not return a JSON body to browser clients; it returns an HTTP status code <code>301 Moved Permanently</code> or <code>302 Found</code> with the <code>Location</code> header set to the destination URL.</p>
            </div>
          </div>
        </article>

        <!-- SLIDE 06: Step 4 - High-Level Design (HLD) -->
        <article class="slide-wrapper" data-slide-index="5" data-category="HLD">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 06 of 24</span>
              <span class="slide-topic-tag">Step 4: Architecture Blocks</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Step 4: High-Level Design (HLD) Architecture</h2>
            <p class="slide-intro">
              This diagram mirrors Section 4 of Bunny's whiteboard: mapping the abstract 30,000-foot component flow between Client, Backend Server, and Database.
            </p>

            <!-- HLD Diagram from Section 4 of image.png -->
            <div class="sketch-diagram-box">
              <svg width="100%" height="240" viewBox="0 0 820 220" fill="none">
                <!-- Client Box -->
                <rect x="20" y="45" width="160" height="130" rx="12" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFA5"/>
                <text x="100" y="85" text-anchor="middle" font-family="Lexend" font-size="16" font-weight="800" fill="#0E2A5C">Client</text>
                <text x="100" y="110" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#333">Browser / App / API</text>
                <text x="100" y="135" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#666">100M DAU Scale</text>

                <!-- Top Arrow: redirect(short) / longerURL -->
                <path d="M185 80 L355 80" stroke="#0E2A5C" stroke-width="2.5"/>
                <polygon points="355,80 345,74 345,86" fill="#0E2A5C"/>
                <text x="270" y="70" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#D12828">redirect(short) / longerURL</text>

                <!-- Bottom Arrow: generateUrl(longURL) / shorter URL -->
                <path d="M355 125 L185 125" stroke="#166534" stroke-width="2.5" stroke-dasharray="3 3"/>
                <polygon points="185,125 195,119 195,131" fill="#166534"/>
                <text x="270" y="145" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#166534">generateUrl(longURL) / shorter URL</text>

                <!-- Server Box -->
                <rect x="360" y="35" width="200" height="150" rx="12" stroke="#0E2A5C" stroke-width="3" fill="#FFFFFF"/>
                <text x="460" y="75" text-anchor="middle" font-family="Lexend" font-size="16" font-weight="800" fill="#0E2A5C">Server</text>
                <rect x="380" y="90" width="160" height="40" rx="6" fill="#F4F1EA" stroke="#0E2A5C" stroke-width="1.5"/>
                <text x="460" y="115" text-anchor="middle" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#0E2A5C">generate the short url</text>
                <text x="460" y="155" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#555">• Handles 301/302 Redirect</text>
                <text x="460" y="170" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#555">• Encryption / Decryption</text>

                <!-- Arrow to DB -->
                <path d="M565 105 L635 105" stroke="#0E2A5C" stroke-width="2.5"/>
                <polygon points="635,105 625,99 625,111" fill="#0E2A5C"/>

                <!-- Database Circle / Cylinder from image -->
                <circle cx="720" cy="110" r="65" stroke="#0E2A5C" stroke-width="2.5" fill="#F4F1EA"/>
                <text x="720" y="75" text-anchor="middle" font-family="Lexend" font-size="14" font-weight="800" fill="#0E2A5C">Database</text>
                <line x1="670" y1="88" x2="770" y2="88" stroke="#0E2A5C" stroke-dasharray="2 2"/>
                <text x="720" y="105" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#0E2A5C">User: metadata</text>
                <text x="720" y="125" text-anchor="middle" font-family="JetBrains Mono" font-size="9" fill="#333">URL: shortURL, longURL</text>
                <text x="720" y="140" text-anchor="middle" font-family="JetBrains Mono" font-size="9" fill="#333">expirationDate, customURL</text>
              </svg>
              <div class="diagram-caption">FIGURE 6.1: High-Level Design directly reflecting Section 4 of Bunny's handwritten whiteboard drawing.</div>
            </div>

            <div class="content-grid-2">
              <div class="card card-white">
                <div class="card-title">📝 Write Cycle (URL Shortening)</div>
                <p style="font-size:0.9rem;">
                  1. Client submits <code>longerURL</code>.<br>
                  2. Server executes shortening algorithm.<br>
                  3. Server persists <code>(shortURL, longURL, expirationDate)</code> in Database.<br>
                  4. Returns compact <code>shorter URL</code> to client.
                </p>
              </div>

              <div class="card card-white">
                <div class="card-title">⚡ Read Cycle (URL Redirection)</div>
                <p style="font-size:0.9rem;">
                  1. Client enters <code>bit.ly/4kycpo</code>.<br>
                  2. Server looks up <code>4kycpo</code> in Database/Cache.<br>
                  3. If active, returns HTTP 301/302 with <code>Location: longURL</code>.<br>
                  4. Client browser navigates seamlessly to original destination.
                </p>
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 07: Database Schema Design & Indexing -->
        <article class="slide-wrapper" data-slide-index="6" data-category="Database">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 07 of 24</span>
              <span class="slide-topic-tag">Database Schema</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Database Schema Design &amp; Indexing Strategy</h2>
            <p class="slide-intro">
              With 1 Billion stored records and 115,000 peak read QPS, the database schema must be compact and heavily indexed on the short code lookup key.
            </p>

            <div class="code-terminal">
              <div class="code-terminal-header">
                <span>SQL Schema • urls &amp; analytics tables</span>
                <span>PostgreSQL / MySQL DDL</span>
              </div>
              <pre><code>-- Primary URL Mapping Table (1 Billion Records ~600 GB)
CREATE TABLE urls (
    short_url     VARCHAR(10) PRIMARY KEY,      -- Unique short token (e.g. '4kycpo', 'mywork')
    long_url      TEXT NOT NULL,                 -- Original destination (up to 2048 chars)
    user_id       UUID NULL,                     -- Optional foreign key for authenticated accounts
    created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    expires_at    TIMESTAMPTZ NULL,              -- Optional expiration date (NULL = never expires)
    is_custom     BOOLEAN DEFAULT FALSE,         -- True if user specified custom vanity alias
    click_count   BIGINT DEFAULT 0               -- Real-time / hourly aggregated clicks
);

-- Crucial Production Indexes
CREATE UNIQUE INDEX idx_urls_short_code ON urls (short_url);           -- O(log N) B-Tree lookup for redirects
CREATE INDEX idx_urls_user_created ON urls (user_id, created_at);       -- Fetch user's link history
CREATE INDEX idx_urls_expires_at ON urls (expires_at) WHERE expires_at IS NOT NULL; -- Daily cleanup cron</code></pre>
            </div>

            <div class="content-grid-3">
              <div class="card card-white">
                <div class="card-title">🌲 B-Tree Index Depth</div>
                <p style="font-size:0.85rem;">
                  At 1B records, a B-Tree index on <code>short_url</code> is only 4 to 5 levels deep. Point lookups complete in <strong>under 5ms</strong>!
                </p>
              </div>

              <div class="card card-yellow">
                <div class="card-title">💾 Storage Sizing (~780 GB)</div>
                <p style="font-size:0.85rem;">
                  610 bytes per URL × 1 Billion = 610 GB. Adding 30% overhead for indexes yields <strong>~780 GB</strong> total storage.
                </p>
              </div>

              <div class="card card-green">
                <div class="card-title">🔀 Horizontal Sharding</div>
                <p style="font-size:0.85rem;">
                  Partition across 10 database shards using <code>Hash(short_url) % 10</code>. Each shard handles an easy 100M rows.
                </p>
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 08: Step 5 (LLD) - The 3 Progressive Approaches Overview -->
        <article class="slide-wrapper" data-slide-index="7" data-category="LLD">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 08 of 24</span>
              <span class="slide-topic-tag">Step 5: Low-Level Design</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Step 5: Low-Level Design (The 3 Approaches)</h2>
            <p class="slide-intro">
              This is the heart of the system design interview. In Section 5 of the lecture, Bunny structures the URL shortener evolution into <strong>three progressive technical approaches</strong>:
            </p>

            <div class="content-grid-3">
              <!-- Approach 1 -->
              <div class="card card-red">
                <div class="card-title">❌ Approach 1</div>
                <h4 style="font-weight: 700; color: #111; margin-bottom: 0.5rem;">Encryption Logic (SHA-1 / MD5)</h4>
                <p style="font-size: 0.85rem; color: #444;">
                  Hash <code>long_url</code> with SHA-1, crop the first 6-7 characters, and loop query the DB to resolve collisions.
                </p>
                <div style="margin-top: 0.75rem; font-weight: 800; font-size: 0.75rem; color: var(--alert-red);">FAILS: Collision Latency Cascade (16ms+16ms)</div>
              </div>

              <!-- Approach 2 -->
              <div class="card card-yellow">
                <div class="card-title">⚠️ Approach 2</div>
                <h4 style="font-weight: 700; color: #111; margin-bottom: 0.5rem;">Counter (Distributed Redis)</h4>
                <p style="font-size: 0.85rem; color: #444;">
                  Auto-increment an integer counter. In microservices, local counters collide; a single Redis counter becomes a SPOF.
                </p>
                <div style="margin-top: 0.75rem; font-weight: 800; font-size: 0.75rem; color: #b45309;">FAILS: Single Point of Failure (SPOF)</div>
              </div>

              <!-- Approach 3 -->
              <div class="card card-green">
                <div class="card-title">✅ Approach 3 (Hybrid)</div>
                <h4 style="font-weight: 700; color: #111; margin-bottom: 0.5rem;">ZooKeeper + Snowflake</h4>
                <p style="font-size: 0.85rem; color: #444;">
                  ZooKeeper registers workers on boot only. Each server creates 64-bit Snowflake IDs in-memory with zero network calls!
                </p>
                <div style="margin-top: 0.75rem; font-weight: 800; font-size: 0.75rem; color: #166534;">OPTIMAL: 100% Unique &amp; 0ms Latency</div>
              </div>
            </div>

            <div class="sticky-note-callout">
              <p><strong>Bunny's Pedagogical Strategy:</strong> "Start with Approach 1, explain its exact millisecond latency numbers and failure points. Transition to Approach 2 to show distributed scaling awareness. Then deliver the Hybrid ZooKeeper + Snowflake solution to secure the offer."</p>
            </div>
          </div>
        </article>
"""

print("gen_slides_1_8 ready.")
