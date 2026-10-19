# gen_slides_9_16.py - Slides 9 through 16
def get_slides_9_16():
    return """
        <!-- SLIDE 09: Approach 1 - Encryption Logic (SHA-1) Mechanics -->
        <article class="slide-wrapper" data-slide-index="8" data-category="Approach 1">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 09 of 24</span>
              <span class="slide-topic-tag">Approach 1: Hashing</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Approach 1: Encryption Logic (SHA-1 Hashing Mechanics)</h2>
            <p class="slide-intro">
              Directly reflecting Section 5.1 of Bunny's whiteboard: The long URL is passed to a cryptographic hashing algorithm (SHA-1 or MD5), and the first 6 or 7 characters are extracted as the short code.
            </p>

            <!-- SVG Diagram from Section 5.1 of image.png -->
            <div class="sketch-diagram-box">
              <svg width="100%" height="200" viewBox="0 0 780 180" fill="none">
                <!-- Whiteboard Title Note -->
                <rect x="20" y="15" width="460" height="35" rx="6" fill="#FFFFA5" stroke="#0E2A5C" stroke-width="1.5"/>
                <text x="35" y="38" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#0E2A5C">1. Encryption Logic: sha1(longUrl) =&gt; {shortURL: 6,7}-&gt; response</text>

                <!-- Server Box -->
                <rect x="60" y="70" width="160" height="80" rx="8" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFFF"/>
                <text x="140" y="105" text-anchor="middle" font-family="Lexend" font-size="16" font-weight="800" fill="#0E2A5C">server</text>
                <text x="140" y="130" text-anchor="middle" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#D12828">encrypt: 1ms</text>

                <!-- Arrow Server to DB with 5ms latency -->
                <path d="M225 110 L485 110" stroke="#0E2A5C" stroke-width="2.5"/>
                <polygon points="485,110 475,104 475,116" fill="#0E2A5C"/>
                <rect x="315" y="85" width="80" height="26" rx="4" fill="#FFFFA5" stroke="#0E2A5C" stroke-width="1"/>
                <text x="355" y="103" text-anchor="middle" font-family="JetBrains Mono" font-size="12" font-weight="700" fill="#0E2A5C">5ms</text>

                <!-- DB Circle -->
                <circle cx="550" cy="110" r="45" stroke="#0E2A5C" stroke-width="2.5" fill="#F4F1EA"/>
                <text x="550" y="115" text-anchor="middle" font-family="Lexend" font-size="16" font-weight="800" fill="#0E2A5C">DB</text>

                <!-- Calculation Box -->
                <rect x="630" y="85" width="130" height="50" rx="6" fill="#FFE4E4" stroke="#D12828" stroke-width="2"/>
                <text x="695" y="115" text-anchor="middle" font-family="JetBrains Mono" font-size="13" font-weight="800" fill="#D12828">= 16ms</text>
              </svg>
              <div class="diagram-caption">FIGURE 9.1: Encryption logic round-trip calculation from Section 5.1 of Bunny's whiteboard.</div>
            </div>

            <div class="content-grid-2">
              <div class="card card-white">
                <div class="card-title">⚙️ Hash Extraction Flow</div>
                <p style="font-size:0.9rem;">
                  1. Input: <code>https://www.facebook.com/anindya.s.dasgupta/</code><br>
                  2. SHA-1 generates 40 hexadecimal characters (160 bits):<br>
                  <code style="word-break:break-all; display:block; margin:0.35rem 0; font-size:0.8rem;">d3e8f9a2b1c4e5f6a7b8c9d0e1f2a3b4c5d6e7f8</code><br>
                  3. Take first 7 characters: <code>d3e8f9a</code>.<br>
                  4. Latency: SHA-1 computation takes <strong>1ms</strong>; DB round trip takes <strong>5ms-15ms</strong>.
                </p>
              </div>

              <div class="card card-yellow">
                <div class="card-title">💎 The Deduplication Benefit</div>
                <p style="font-size:0.9rem;">
                  Because cryptographic hashing is <strong>deterministic</strong>, hashing the exact same URL twice always yields the exact same hash. If two users attempt to shorten the same long link, the system returns the existing short link, saving storage space.
                </p>
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 10: Approach 1 - The Collision Problem & Latency Cascade -->
        <article class="slide-wrapper" data-slide-index="9" data-category="Approach 1">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 10 of 24</span>
              <span class="slide-topic-tag">Collision Cascade</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Approach 1 Failure: Hash Collision &amp; Latency Cascade</h2>
            <p class="slide-intro">
              Here is the fundamental flaw Bunny explains on the whiteboard: Truncating a 40-character hash down to 6 characters inevitably causes <strong>Birthday Paradox collisions</strong>, triggering an expensive database retry loop.
            </p>

            <!-- Whiteboard Collision Example -->
            <div class="sketch-diagram-box">
              <div style="font-family:'JetBrains Mono'; font-size:0.85rem; display:flex; flex-direction:column; gap:0.6rem;">
                <div style="background:#FFF; padding:0.65rem; border:1.5px solid var(--ink-blue); border-radius:6px;">
                  1. Input: <code>https://www.facebook.com/anindya.s.dasgupta/</code> ──▶ Hash: <span style="color:var(--alert-red); font-weight:800;">9191c0</span>37d0c5f4408f0caf5c3cd39edd...
                </div>
                <div style="background:#FFF; padding:0.65rem; border:1.5px solid var(--ink-blue); border-radius:6px;">
                  2. Input: <code>https://www.amazon.in/</code> ──▶ Hash: <span style="color:var(--alert-red); font-weight:800;">9191c0</span>37d0c5f4408f0caf5c3cd39e3rd...
                </div>
                <div style="background:#FFE4E4; border:2px solid var(--alert-red); padding:0.75rem; border-radius:6px; color:var(--alert-red); font-weight:800; font-size:0.95rem;">
                  💥 BOTH TRUNCATE TO "9191c0" ──▶ DATABASE PRIMARY KEY COLLISION!
                </div>
              </div>
              <div class="diagram-caption">FIGURE 10.1: Verbatim collision example from Bunny's whiteboard. Two completely different websites share the identical 6-character prefix.</div>
            </div>

            <div class="content-grid-2">
              <div class="card card-red">
                <div class="card-title">⏱️ The Compounding Latency Cascade</div>
                <p style="font-size:0.9rem;">
                  When a collision occurs, the database throws a duplicate key error. The server must append a salt or timestamp, re-hash, and re-query the database:<br>
                  • <strong>Attempt 1 (No collision):</strong> 1ms encrypt + 15ms DB = <strong>16ms</strong><br>
                  • <strong>Attempt 2 (1 Collision):</strong> 16ms consumed + 16ms retry = <strong style="color:var(--alert-red);">32ms</strong><br>
                  • <strong>Attempt 3 (2 Collisions):</strong> 32ms + 16ms retry = <strong style="color:var(--alert-red);">48ms</strong><br>
                  As the database reaches hundreds of millions of rows, collision probability explodes, violating our SLA!
                </p>
              </div>

              <div class="card card-white">
                <div class="card-title">📊 Mathematical Probability Formula</div>
                <p style="font-size:0.9rem;">
                  With $k=7$ hexadecimal characters ($16^7 = 268\text{M}$ space), the collision probability formula is:
                  <code style="display:block; margin:0.5rem 0; padding:0.4rem; background:#F4F1EA;">P(collision) ≈ (n²) / (2 × 16^k)</code>
                  At 1 Million URLs, collision probability is ~0.002%. But at 10 Million URLs, it jumps to <strong>0.2%</strong>. At 1 Billion URLs, collisions happen on almost every request!
                </p>
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 11: Approach 2 - Counter-Based Auto-Increment -->
        <article class="slide-wrapper" data-slide-index="10" data-category="Approach 2">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 11 of 24</span>
              <span class="slide-topic-tag">Approach 2: Counters</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Approach 2: Counter-Based Generation &amp; Monolith Wall</h2>
            <p class="slide-intro">
              Instead of hashing unpredictable text strings, what if the server uses an <strong>auto-incrementing counter</strong> (1, 2, 3, 4...)? Each request gets a unique integer, dropping DB collision scans completely!
            </p>

            <div class="content-grid-2">
              <div class="card card-green">
                <div class="card-title">⚡ Why Counters Slash Latency to 6ms</div>
                <p style="font-size:0.92rem;">
                  Request 1 receives ID <code>1</code>. Request 2 receives ID <code>2</code>. Because numbers strictly increment, <strong>duplicates are mathematically impossible</strong>! We no longer need to execute a 10ms database scan. Latency drops from 16ms to just <strong>6ms</strong> (local increment + DB save).
                </p>
              </div>

              <div class="card card-red">
                <div class="card-title">🧱 The Monolith Scaling Wall</div>
                <p style="font-size:0.92rem;">
                  This single counter works flawlessly on a <em>single monolithic server</em>. But our non-functional requirement specifies <strong>100 Million DAU</strong>! A single machine cannot handle this throughput. We must scale horizontally with microservices.
                </p>
              </div>
            </div>

            <div class="sketch-diagram-box">
              <div style="font-family:'JetBrains Mono'; font-size:0.9rem; text-align:center;">
                <span style="background:#FFFFA5; padding:0.4rem 0.8rem; border:2px solid var(--ink-blue); border-radius:4px; font-weight:700;">
                  Vertical Scaling (Bigger RAM/CPU) ❌ DOES NOT SCALE TO 100M USERS
                </span>
                <div style="margin: 0.5rem 0; font-weight:800; color:var(--alert-red);">▼ MUST USE HORIZONTAL MICROSERVICE REPLICATION ▼</div>
                <span style="background:#FFF; padding:0.4rem 0.8rem; border:2px solid var(--ink-blue); border-radius:4px; font-weight:700;">
                  Horizontal Scaling (Multiple App Servers behind Load Balancer)
                </span>
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 12: Approach 2 - Concurrency Failure behind Load Balancer -->
        <article class="slide-wrapper" data-slide-index="11" data-category="Approach 2">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 12 of 24</span>
              <span class="slide-topic-tag">Concurrency Failure</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Approach 2 Flaw: Load Balancer &amp; Local Counter Collisions</h2>
            <p class="slide-intro">
              When we deploy multiple server instances (Server 1, Server 2, Server 3) behind a Round-Robin Load Balancer, a catastrophic concurrency bug appears: <strong>each server maintains its own local counter</strong>.
            </p>

            <!-- Load Balancer Collision Diagram -->
            <div class="sketch-diagram-box">
              <svg width="100%" height="220" viewBox="0 0 760 210" fill="none">
                <!-- LB -->
                <rect x="30" y="60" width="130" height="90" rx="8" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFA5"/>
                <text x="95" y="95" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800" fill="#0E2A5C">LOAD BALANCER</text>
                <text x="95" y="115" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#D12828">-round robin (5ms)</text>

                <!-- Arrows to servers -->
                <path d="M165 75 L285 45" stroke="#0E2A5C" stroke-width="2"/>
                <polygon points="285,45 275,40 277,52" fill="#0E2A5C"/>
                <path d="M165 105 L285 105" stroke="#0E2A5C" stroke-width="2"/>
                <polygon points="285,105 275,99 275,111" fill="#0E2A5C"/>
                <path d="M165 135 L285 165" stroke="#0E2A5C" stroke-width="2"/>
                <polygon points="285,165 277,158 275,170" fill="#0E2A5C"/>

                <!-- Server 1 -->
                <rect x="290" y="20" width="180" height="50" rx="6" stroke="#0E2A5C" stroke-width="2" fill="#FFFFFF"/>
                <text x="380" y="40" text-anchor="middle" font-family="Lexend" font-size="11" font-weight="700">SERVER 1 (counter=0)</text>
                <text x="380" y="58" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#166534">Returns ID = 0</text>

                <!-- Server 2 -->
                <rect x="290" y="80" width="180" height="50" rx="6" stroke="#D12828" stroke-width="2.5" fill="#FFE4E4"/>
                <text x="380" y="100" text-anchor="middle" font-family="Lexend" font-size="11" font-weight="700" fill="#D12828">SERVER 2 (counter=0)</text>
                <text x="380" y="118" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#D12828">Returns ID = 0 (COLLISION!)</text>

                <!-- Server 3 -->
                <rect x="290" y="140" width="180" height="50" rx="6" stroke="#0E2A5C" stroke-width="2" fill="#FFFFFF"/>
                <text x="380" y="160" text-anchor="middle" font-family="Lexend" font-size="11" font-weight="700">SERVER 3 (counter=0)</text>
                <text x="380" y="178" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#444">Returns ID = 0</text>

                <!-- Arrows to DB -->
                <path d="M475 45 L590 85" stroke="#0E2A5C" stroke-width="2"/>
                <path d="M475 105 L590 105" stroke="#D12828" stroke-width="2.5"/>
                <path d="M475 165 L590 125" stroke="#0E2A5C" stroke-width="2"/>

                <!-- DB -->
                <rect x="595" y="65" width="140" height="80" rx="8" stroke="#D12828" stroke-width="2.5" fill="#FFF0F0"/>
                <text x="665" y="100" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800" fill="#D12828">DATABASE</text>
                <text x="665" y="120" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#D12828">💥 Duplicate Key Error</text>
              </svg>
              <div class="diagram-caption">FIGURE 12.1: When servers boot independently, their local counters all start at 0, corrupting database uniqueness.</div>
            </div>

            <div class="sticky-note-callout">
              <p><strong>The Failure:</strong> Server 1 gets request 1 and returns <code>0</code>. Server 2 gets request 2 and also returns <code>0</code>! The database crashes with a duplicate key violation. Local in-memory counters cannot exist in distributed architectures.</p>
            </div>
          </div>
        </article>

        <!-- SLIDE 13: Approach 2.5 - Centralized Redis Counter & Workload Split -->
        <article class="slide-wrapper" data-slide-index="12" data-category="Approach 2">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 13 of 24</span>
              <span class="slide-topic-tag">Centralized Cache &amp; SPOF</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Approach 2.5: Centralized Redis Counter &amp; Workload Split</h2>
            <p class="slide-intro">
              This diagram mirrors Section 5.2 of Bunny's whiteboard: Introducing a central <strong>Redis counter (2ms-3ms)</strong> and separating servers into <strong>Encryption (20% workload)</strong> vs <strong>Decryption (80% workload)</strong>.
            </p>

            <!-- SVG Diagram from Section 5.2 of image.png -->
            <div class="sketch-diagram-box">
              <svg width="100%" height="280" viewBox="0 0 820 260" fill="none">
                <!-- Client -->
                <rect x="20" y="90" width="100" height="70" rx="8" stroke="#0E2A5C" stroke-width="2" fill="#FFFFFF"/>
                <text x="70" y="130" text-anchor="middle" font-family="Lexend" font-size="14" font-weight="800">client</text>

                <!-- Arrow to LB -->
                <path d="M125 125 L165 125" stroke="#0E2A5C" stroke-width="2"/>
                <polygon points="165,125 155,119 155,131" fill="#0E2A5C"/>

                <!-- Load Balancer -->
                <rect x="170" y="65" width="110" height="120" rx="8" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFA5"/>
                <text x="225" y="110" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Load</text>
                <text x="225" y="128" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Balancer</text>
                <text x="225" y="148" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#D12828">-round robin</text>

                <!-- 5ms latency indicator -->
                <rect x="290" y="112" width="45" height="22" rx="4" fill="#FFFFA5" stroke="#0E2A5C" stroke-width="1"/>
                <text x="312" y="127" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700">5ms</text>

                <!-- Arrows from LB to servers -->
                <path d="M280 95 L345 55" stroke="#0E2A5C" stroke-width="2"/>
                <polygon points="345,55 335,52 338,64" fill="#0E2A5C"/>
                <path d="M280 155 L345 195" stroke="#0E2A5C" stroke-width="2"/>
                <polygon points="345,195 338,186 335,198" fill="#0E2A5C"/>

                <!-- Encryption Server (20% workload) -->
                <rect x="350" y="25" width="160" height="65" rx="8" stroke="#0E2A5C" stroke-width="2" fill="#FFFFFF"/>
                <text x="430" y="52" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Encryption Server</text>
                <text x="430" y="72" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#D12828">encryption (20%)</text>

                <!-- Decryption Server (80% workload) -->
                <rect x="350" y="170" width="160" height="65" rx="8" stroke="#0E2A5C" stroke-width="2" fill="#FFFFFF"/>
                <text x="430" y="197" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Decryption Server</text>
                <text x="430" y="217" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#15803d">decryption (80%)</text>

                <!-- Redis Counter at Top -->
                <circle cx="430" cy="10" r="8" fill="#D12828"/>
                <rect x="580" y="15" width="130" height="50" rx="8" stroke="#D12828" stroke-width="2.5" fill="#FFE4E4"/>
                <text x="645" y="37" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800" fill="#D12828">Redis</text>
                <text x="645" y="54" text-anchor="middle" font-family="JetBrains Mono" font-size="11" font-weight="700" fill="#D12828">counter</text>
                <text x="545" y="32" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#D12828">2ms-3ms</text>

                <!-- Line from Encryption Server to Redis counter -->
                <path d="M515 50 L575 40" stroke="#D12828" stroke-width="2" stroke-dasharray="2 2"/>
                <polygon points="575,40 565,37 567,49" fill="#D12828"/>

                <!-- Database (10ms) -->
                <circle cx="645" cy="130" r="35" stroke="#0E2A5C" stroke-width="2.5" fill="#F4F1EA"/>
                <text x="645" y="135" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Database</text>
                <text x="590" y="150" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#0E2A5C">10ms</text>

                <!-- Redis Cache (2ms) at bottom -->
                <rect x="580" y="195" width="130" height="45" rx="8" stroke="#0E2A5C" stroke-width="2" fill="#FFFFA5"/>
                <text x="645" y="222" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Redis</text>
                <text x="545" y="222" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#15803d">2ms</text>

                <!-- Lines from Decryption server to DB and Redis -->
                <path d="M515 190 L595 145" stroke="#0E2A5C" stroke-width="2"/>
                <path d="M515 210 L575 215" stroke="#0E2A5C" stroke-width="2"/>
              </svg>
              <div class="diagram-caption">FIGURE 13.1: Section 5.2 from Bunny's whiteboard. 20% write workload hits Redis counter; 80% read workload hits Redis cache (2ms) &amp; DB (10ms).</div>
            </div>

            <div class="content-grid-2">
              <div class="card card-white">
                <div class="card-title">⚖️ 20% Write vs 80% Read Workload</div>
                <p style="font-size:0.9rem;">
                  On the whiteboard, Bunny notes: <strong>Encryption = 20%</strong> (URL creation writes) and <strong>Decryption = 80%</strong> (URL redirection reads). By separating the pools into Encryption Servers and Decryption Servers, we isolate heavy CPU encryption from I/O-bound read redirection.
                </p>
              </div>

              <div class="card card-red">
                <div class="card-title">💣 Single Point of Failure (SPOF)</div>
                <p style="font-size:0.9rem;">
                  If the Redis counter node goes down or network partitions, <strong>all URL creation stops</strong>! If you deploy multi-node Redis clusters, synchronizing distributed counters across nodes recreates the exact split-brain duplicate problem we tried to avoid.
                </p>
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 14: Apache ZooKeeper - The Distributed Coordinator -->
        <article class="slide-wrapper" data-slide-index="13" data-category="ZooKeeper">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 14 of 24</span>
              <span class="slide-topic-tag">Distributed Coordination</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Apache ZooKeeper: The Distributed Coordinator</h2>
            <p class="slide-intro">
              Before presenting the final hybrid solution, Bunny explains what <strong>Apache ZooKeeper</strong> actually is: a centralized, highly reliable coordination service that manages distributed clusters.
            </p>

            <!-- Verbatim Definition Card from image.png -->
            <div class="card card-yellow" style="margin-bottom:1.25rem;">
              <div class="card-title">📜 ZooKeeper Verbatim Whiteboard Definition:</div>
              <p style="font-size:0.95rem; line-height:1.6; color:#222;">
                <em>"ZooKeeper is a distributed, open-source coordination service for distributed applications, providing centralized services for configuration management, naming, synchronization, and group services, making it easy to build large clusters.<br><br>
                <strong>Used for:</strong> maintaining configuration information, naming, providing distributed synchronization, distributed locking, group service etc."</em>
              </p>
            </div>

            <!-- Znode Tree SVG from Section 5.3 of image.png -->
            <div class="sketch-diagram-box">
              <svg width="100%" height="220" viewBox="0 0 760 200" fill="none">
                <!-- Root Node -->
                <circle cx="380" cy="30" r="20" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFA5"/>
                <text x="380" y="35" text-anchor="middle" font-family="JetBrains Mono" font-size="14" font-weight="800">/</text>

                <!-- Lines to app1 and app2 -->
                <path d="M365 45 L240 85" stroke="#0E2A5C" stroke-width="2"/>
                <path d="M395 45 L520 85" stroke="#0E2A5C" stroke-width="2"/>

                <!-- /app1 Node -->
                <circle cx="240" cy="95" r="22" stroke="#0E2A5C" stroke-width="2" fill="#FFFFFF"/>
                <text x="240" y="100" text-anchor="middle" font-family="JetBrains Mono" font-size="11" font-weight="700">/app1</text>

                <!-- /app2 Node -->
                <circle cx="520" cy="95" r="22" stroke="#0E2A5C" stroke-width="2" fill="#FFFFFF"/>
                <text x="520" y="100" text-anchor="middle" font-family="JetBrains Mono" font-size="11" font-weight="700">/app2</text>

                <!-- Lines from app1 to leaves p_1, p_2, p_3 -->
                <path d="M225 110 L150 155" stroke="#0E2A5C" stroke-width="1.5"/>
                <path d="M240 117 L240 155" stroke="#0E2A5C" stroke-width="1.5"/>
                <path d="M255 110 L330 155" stroke="#0E2A5C" stroke-width="1.5"/>

                <!-- Leaves -->
                <circle cx="150" cy="165" r="16" stroke="#166534" stroke-width="2" fill="#D4F8D4"/>
                <text x="150" y="195" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700">/app1/p_1</text>

                <circle cx="240" cy="165" r="16" stroke="#166534" stroke-width="2" fill="#D4F8D4"/>
                <text x="240" y="195" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700">/app1/p_2</text>

                <circle cx="330" cy="165" r="16" stroke="#166534" stroke-width="2" fill="#D4F8D4"/>
                <text x="330" y="195" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700">/app1/p_3</text>

                <!-- Dotted line from app2 -->
                <path d="M520 117 L520 160" stroke="#0E2A5C" stroke-width="1.5" stroke-dasharray="3 3"/>
              </svg>
              <div class="diagram-caption">FIGURE 14.1: ZooKeeper hierarchical ZNode tree directly reflecting Section 5.3 of Bunny's whiteboard.</div>
            </div>

            <div class="content-grid-2">
              <div class="card card-white">
                <div class="card-title">🌲 Persistent Nodes</div>
                <p style="font-size:0.9rem;">
                  Permanent storage nodes that survive server reboots. Ideal for configuration data, static schema definitions, and persistent cluster metadata.
                </p>
              </div>

              <div class="card card-green">
                <div class="card-title">💓 Ephemeral Nodes &amp; Heartbeats</div>
                <p style="font-size:0.9rem;">
                  Tied directly to the client session. When an app server connects, ZooKeeper assigns an ephemeral znode (e.g. <code>/workers/worker-123</code>). If the server crashes or drops heartbeat, ZooKeeper automatically cleans up the node!
                </p>
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 15: Approach 3 - The Bunny Hybrid Architecture -->
        <article class="slide-wrapper" data-slide-index="14" data-category="Approach 3">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 15 of 24</span>
              <span class="slide-topic-tag">The Optimal Architecture</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Approach 3: The Bunny Hybrid Architecture</h2>
            <p class="slide-intro">
              This master diagram reflects Section 5.3 of Bunny's whiteboard: <strong>ZooKeeper assigns unique Worker IDs strictly at boot time</strong>, allowing each Encryption Server to generate IDs locally via Twitter Snowflake with <strong>ZERO runtime network calls</strong>!
            </p>

            <!-- Complete Master Architecture SVG from Section 5.3 of image.png -->
            <div class="sketch-diagram-box">
              <svg width="100%" height="340" viewBox="0 0 840 320" fill="none">
                <!-- Client -->
                <rect x="15" y="115" width="90" height="60" rx="8" stroke="#0E2A5C" stroke-width="2" fill="#FFFFFF"/>
                <text x="60" y="150" text-anchor="middle" font-family="Lexend" font-size="14" font-weight="800">client</text>

                <!-- Arrow to LB -->
                <path d="M110 145 L145 145" stroke="#0E2A5C" stroke-width="2"/>
                <polygon points="145,145 135,139 135,151" fill="#0E2A5C"/>

                <!-- Load Balancer -->
                <rect x="150" y="85" width="105" height="130" rx="8" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFA5"/>
                <text x="202" y="125" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Load</text>
                <text x="202" y="145" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Balancer</text>
                <text x="202" y="168" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#D12828">-round robin</text>
                <text x="260" y="135" font-family="JetBrains Mono" font-size="10" font-weight="700">5ms</text>

                <!-- Top Tier: Encryption Server with counter -->
                <rect x="300" y="50" width="160" height="70" rx="8" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFFF"/>
                <text x="380" y="75" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Encryption Server</text>
                <rect x="330" y="85" width="100" height="25" rx="4" fill="#EAE6DC" stroke="#0E2A5C" stroke-width="1"/>
                <text x="380" y="102" text-anchor="middle" font-family="JetBrains Mono" font-size="11" font-weight="700">counter</text>

                <!-- Arrow LB to Encryption Server -->
                <path d="M255 125 L295 90" stroke="#0E2A5C" stroke-width="2"/>
                <polygon points="295,90 285,88 289,100" fill="#0E2A5C"/>

                <!-- ZooKeeper Block -->
                <rect x="520" y="20" width="160" height="90" rx="8" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFA5"/>
                <text x="600" y="45" text-anchor="middle" font-family="Lexend" font-size="13" font-weight="800" fill="#0E2A5C">zookeeper</text>
                <line x1="535" y1="55" x2="665" y2="55" stroke="#0E2A5C" stroke-dasharray="2 2"/>
                <text x="600" y="72" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700">workerID: 123</text>
                <text x="600" y="87" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700">workerID: 234</text>
                <text x="600" y="102" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700">workerID: 345</text>

                <!-- Line from Encryption Server to ZooKeeper -->
                <path d="M465 75 L515 55" stroke="#0E2A5C" stroke-width="2" stroke-dasharray="3 2"/>
                <polygon points="515,55 505,53 508,65" fill="#0E2A5C"/>

                <!-- Snowflake Box -->
                <rect x="695" y="30" width="130" height="70" rx="8" stroke="#166534" stroke-width="2" fill="#D4F8D4"/>
                <text x="760" y="55" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800" fill="#166534">Snowflake</text>
                <text x="760" y="75" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700">timestamp</text>
                <text x="760" y="90" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700">+ workerID</text>

                <!-- Bottom Tier: Decryption Server -->
                <rect x="300" y="180" width="160" height="70" rx="8" stroke="#0E2A5C" stroke-width="2.5" fill="#FFFFFF"/>
                <text x="380" y="205" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Decryption Server</text>
                <rect x="320" y="215" width="120" height="25" rx="4" fill="#FFE4E4" stroke="#D12828" stroke-width="1"/>
                <text x="380" y="232" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="700" fill="#D12828">301, 302-redirect</text>

                <!-- Arrow LB to Decryption Server -->
                <path d="M255 165 L295 200" stroke="#0E2A5C" stroke-width="2"/>
                <polygon points="295,200 289,190 285,202" fill="#0E2A5C"/>

                <!-- Database -->
                <circle cx="560" cy="215" r="40" stroke="#0E2A5C" stroke-width="2.5" fill="#F4F1EA"/>
                <text x="560" y="220" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Database</text>

                <!-- Cron Job connected to Database -->
                <rect x="650" y="235" width="70" height="35" rx="6" stroke="#0E2A5C" stroke-width="2" fill="#FFFFA5"/>
                <text x="685" y="257" text-anchor="middle" font-family="JetBrains Mono" font-size="12" font-weight="800">cron</text>
                <path d="M645 245 L605 230" stroke="#0E2A5C" stroke-width="2"/>
                <polygon points="605,230 613,238 616,226" fill="#0E2A5C"/>

                <!-- Redis (2ms) at bottom -->
                <rect x="500" y="275" width="120" height="38" rx="8" stroke="#0E2A5C" stroke-width="2" fill="#FFFFA5"/>
                <text x="560" y="295" text-anchor="middle" font-family="Lexend" font-size="12" font-weight="800">Redis</text>
                <text x="560" y="308" text-anchor="middle" font-family="JetBrains Mono" font-size="9" font-weight="700">2ms</text>

                <!-- Lines Decryption to DB and Redis -->
                <path d="M465 215 L515 215" stroke="#0E2A5C" stroke-width="2"/>
                <polygon points="515,215 505,209 505,221" fill="#0E2A5C"/>
                <path d="M440 250 L500 280" stroke="#0E2A5C" stroke-width="2"/>
              </svg>
              <div class="diagram-caption">FIGURE 15.1: Complete System Architecture from Section 5.3 of Bunny's whiteboard. Boot-time ZooKeeper worker allocation + local Snowflake generation + Decryption redirect + daily Cron expiration cleanup.</div>
            </div>

            <div class="content-grid-2">
              <div class="card card-green">
                <div class="card-title">🚀 Boot-Time Coordination Only</div>
                <p style="font-size:0.9rem;">
                  When Server 1 boots, it registers with ZooKeeper to get <code>workerID = 123</code>. Server 2 gets <code>workerID = 234</code>. Server 3 gets <code>workerID = 345</code>. During live URL shortening, <strong>zero network calls are made to ZooKeeper</strong>!
                </p>
              </div>

              <div class="card card-white">
                <div class="card-title">🛡️ Resilient to ZooKeeper Outages</div>
                <p style="font-size:0.9rem;">
                  Even if ZooKeeper crashes completely, all running application servers continue generating unique URLs with zero downtime! ZooKeeper is only required when new server instances boot or scale up.
                </p>
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 16: Snowflake 64-Bit Binary Layout & Exact Math -->
        <article class="slide-wrapper" data-slide-index="15" data-category="Snowflake">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 16 of 24</span>
              <span class="slide-topic-tag">Snowflake ID Math</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">The 64-Bit Snowflake ID: Exact Binary Math</h2>
            <p class="slide-intro">
              This slide breaks down the exact mathematical formulas written at the bottom of Bunny's whiteboard. With time, worker ID, and a local sequence combined, 100% collision-free uniqueness is achieved in CPU registers.
            </p>

            <!-- 64-Bit Layout SVG -->
            <div class="sketch-diagram-box">
              <div style="width: 100%; overflow-x: auto;">
                <svg width="780" height="120" viewBox="0 0 780 120" fill="none">
                  <!-- Sign bit -->
                  <rect x="10" y="30" width="45" height="60" fill="#EAE6DC" stroke="#0E2A5C" stroke-width="2"/>
                  <text x="32" y="55" text-anchor="middle" font-family="JetBrains Mono" font-size="11" font-weight="700">1 bit</text>
                  <text x="32" y="75" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#666">Sign</text>

                  <!-- Timestamp -->
                  <rect x="60" y="30" width="370" height="60" fill="#FFFFA5" stroke="#0E2A5C" stroke-width="2"/>
                  <text x="245" y="55" text-anchor="middle" font-family="JetBrains Mono" font-size="12" font-weight="800" fill="#0E2A5C">41 BITS: TIMESTAMP</text>
                  <text x="245" y="75" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#444">Milliseconds since custom epoch (~69.73 years)</text>

                  <!-- Worker ID -->
                  <rect x="435" y="30" width="165" height="60" fill="#D4F8D4" stroke="#0E2A5C" stroke-width="2"/>
                  <text x="517" y="55" text-anchor="middle" font-family="JetBrains Mono" font-size="12" font-weight="800" fill="#15803d">10 BITS: WORKER ID</text>
                  <text x="517" y="75" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#15803d">From ZooKeeper (1024 workers)</text>

                  <!-- Sequence Counter -->
                  <rect x="605" y="30" width="165" height="60" fill="#FFE4E4" stroke="#0E2A5C" stroke-width="2"/>
                  <text x="687" y="55" text-anchor="middle" font-family="JetBrains Mono" font-size="12" font-weight="800" fill="#D12828">12 BITS: SEQUENCE</text>
                  <text x="687" y="75" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#D12828">4096 IDs / millisecond</text>
                </svg>
              </div>
              <div class="diagram-caption">FIGURE 16.1: Complete 64-bit binary layout of the Twitter Snowflake ID format.</div>
            </div>

            <!-- Exact Mathematical Formulas from bottom of image.png -->
            <div class="content-grid-3">
              <div class="card card-yellow">
                <div class="card-title">41-Bit Timestamp Math</div>
                <div style="font-family:'JetBrains Mono'; font-size:0.85rem; background:#FFF; padding:0.5rem; border:1px solid #ccc; border-radius:4px; margin-bottom:0.5rem;">
                  2^41 / (365 * 24 * 60 * 60 * 1000L) = <strong>69.73 Years</strong>
                </div>
                <p style="font-size:0.82rem; color:#444;">
                  Provides nearly 70 years of unique, monotonically increasing IDs before timestamp rollover.
                </p>
              </div>

              <div class="card card-green">
                <div class="card-title">10-Bit Worker ID Math</div>
                <div style="font-family:'JetBrains Mono'; font-size:0.85rem; background:#FFF; padding:0.5rem; border:1px solid #ccc; border-radius:4px; margin-bottom:0.5rem;">
                  2^10 = <strong>1,024 Workers</strong>
                </div>
                <p style="font-size:0.82rem; color:#444;">
                  ZooKeeper can coordinate up to 1,024 concurrent app server instances running in parallel without conflict.
                </p>
              </div>

              <div class="card card-red">
                <div class="card-title">12-Bit Sequence Math</div>
                <div style="font-family:'JetBrains Mono'; font-size:0.85rem; background:#FFF; padding:0.5rem; border:1px solid #ccc; border-radius:4px; margin-bottom:0.5rem;">
                  2^12 * 1000 = <strong>4,096,000 IDs/sec</strong>
                </div>
                <p style="font-size:0.82rem; color:#444;">
                  Each single server can emit 4,096 IDs per millisecond (over 4 Million IDs per second per node!).
                </p>
              </div>
            </div>

            <div class="sticky-note-callout">
              <p><strong>The Latency Breakthrough:</strong> Generating a Snowflake ID requires <strong>0ms network round-trip time</strong>. It is computed in CPU registers in less than 1 microsecond!</p>
            </div>
          </div>
        </article>
"""

print("gen_slides_9_16 ready.")
