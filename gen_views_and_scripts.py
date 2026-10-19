# gen_views_and_scripts.py - Reader, Revision, Flashcards, Quiz, Drawers, Modals, and Client-Side JS

def get_reader_view():
    return """
    <!-- =========================================================================
         VIEW 2: READER (DIGITAL TEXTBOOK MODE)
         ========================================================================= -->
    <section id="readerView" class="reader-mode" style="display:none;">
      <article class="reader-chapter">
        <header class="reader-header">
          <span class="tag tag-blue">SYSTEM DESIGN COMPREHENSIVE TEXTBOOK</span>
          <h1 class="sketch-heading" style="font-size:2.4rem; color:var(--ink-blue); margin:0.75rem 0 0.5rem 0;">
            Designing a Web-Scale URL Shortener (TinyURL / Bitly)
          </h1>
          <p style="font-size:1.1rem; color:var(--pencil-grey); max-width:850px; line-height:1.6;">
            A complete first-principles engineering breakdown covering functional specs, non-functional capacity math, core entities, REST contracts, the 3 ID generation architectures (SHA-1, Redis/ZooKeeper Counter, 64-bit Twitter Snowflake), wire protocol tradeoffs (301 vs 302), and multi-layer caching with Bloom filters.
          </p>
        </header>

        <!-- Chapter 1 -->
        <section class="reader-section">
          <h2 class="sketch-heading" style="color:var(--ink-blue); border-bottom:2px solid var(--border-dark); padding-bottom:0.4rem;">
            1. What is a URL Shortener &amp; The 5-Step Interview Framework
          </h2>
          <p>
            A URL shortener converts long, unwieldy destination URLs (often 100+ characters loaded with UTM tracking tokens and search queries) into concise, 6-7 character alphanumeric slugs. For instance:
          </p>
          <div class="card card-yellow" style="font-family:JetBrains Mono, monospace; font-size:0.95rem; margin:1rem 0;">
            Input:  https://www.facebook.com/anindya.s.dasgupta/ (42 chars)<br>
            Output: https://bit.ly/4kycpo (6-char slug: '4kycpo' &bull; 90% reduction)
          </div>
          <p>
            To successfully execute this problem in a high-stakes engineering interview, you must follow the battle-tested <strong>5-Step System Design Interview Framework</strong>:
          </p>
          <ol style="padding-left:1.5rem; line-height:1.8;">
            <li><strong>Functional &amp; Non-Functional Requirements:</strong> Clarify core features, read-to-write ratios, SLAs, and capacity boundaries.</li>
            <li><strong>Core Entity Identification:</strong> Define domain models (User, URL) and relationship cardinality.</li>
            <li><strong>REST API Design:</strong> Establish clean HTTP endpoints with idempotency, payloads, and response status codes.</li>
            <li><strong>High-Level Architecture (HLD):</strong> Lay out the basic 4-box architecture (Client, Load Balancer, Application Servers, Database).</li>
            <li><strong>Deep Dive &amp; Bottlenecks:</strong> Analyze unique ID generation algorithms, distributed caching, database indexing, edge cases, and high-concurrency scaling.</li>
          </ol>
        </section>

        <!-- Chapter 2 -->
        <section class="reader-section">
          <h2 class="sketch-heading" style="color:var(--ink-blue); border-bottom:2px solid var(--border-dark); padding-bottom:0.4rem;">
            2. Requirements &amp; Rigorous Capacity Estimations
          </h2>
          <p>
            URL shorteners are notoriously <strong>read-heavy</strong> workloads. When a promotional tweet or marketing campaign goes live, millions of people click the link, while only a small handful of marketers generate new short URLs.
          </p>
          <div class="grid grid-2" style="margin:1rem 0;">
            <div class="card card-blue">
              <h3 class="sketch-heading" style="font-size:1.1rem; color:var(--ink-blue);">Functional Scope</h3>
              <ul class="checklist" style="font-size:0.9rem;">
                <li><span class="check-icon">&#10003;</span> Generate clean 6-7 character short URLs from valid long URLs.</li>
                <li><span class="check-icon">&#10003;</span> HTTP redirect incoming short URLs to destination in &lt; 2ms.</li>
                <li><span class="check-icon">&#10003;</span> Support custom vanity slugs (e.g. <code>bit.ly/summer-sale</code>).</li>
                <li><span class="check-icon">&#10003;</span> Configurable expiration dates with automatic link retirement.</li>
              </ul>
            </div>
            <div class="card card-red">
              <h3 class="sketch-heading" style="font-size:1.1rem; color:var(--alert-red);">Non-Functional SLAs</h3>
              <ul class="checklist" style="font-size:0.9rem;">
                <li><span class="check-icon">&#10003;</span> <strong>Availability:</strong> 99.99% uptime (downtime breaks millions of links).</li>
                <li><span class="check-icon">&#10003;</span> <strong>Latency:</strong> p99 redirect &lt; 10ms, p99 write &lt; 100ms.</li>
                <li><span class="check-icon">&#10003;</span> <strong>Uniqueness:</strong> 100% collision-free guarantee across billions of URLs.</li>
                <li><span class="check-icon">&#10003;</span> <strong>Unpredictability:</strong> Non-guessable IDs to prevent URL enumeration scrapers.</li>
              </ul>
            </div>
          </div>
          <h3 class="sketch-heading" style="font-size:1.1rem; color:var(--ink-blue); margin-top:1.5rem;">System Sizing Math</h3>
          <ul style="padding-left:1.5rem; line-height:1.7;">
            <li><strong>Write Throughput:</strong> 100 Million new URLs created per month &rarr; $100\\text{M} / (30 \\times 86400) \\approx 40\\text{ URLs/sec}$. Peak load (10x) = <strong>400 writes/sec</strong>.</li>
            <li><strong>Read Throughput (100:1 Read-to-Write):</strong> 100 Million $\\times 100$ = 10 Billion redirects/month &rarr; <strong>4,000 read QPS average</strong>, with peak traffic reaching <strong>40,000 to 80,000 QPS</strong>.</li>
            <li><strong>Storage Sizing:</strong> Average URL row = 500 bytes (Short code 10B + Destination 400B + Metadata 90B). Over 5 years: $100\\text{M} \\times 12 \\times 5 = 6\\text{ Billion URLs} \\times 500\\text{ bytes} \\approx \\mathbf{3\\text{ Terabytes}}$. Very manageable for PostgreSQL or MySQL!</li>
            <li><strong>Cache Memory (80-20 Pareto Rule):</strong> 20% of daily URLs generate 80% of redirect clicks. Daily read volume = $10\\text{B} / 30 \\approx 330\\text{M clicks/day}$. Caching 20% of daily URLs requires: $66\\text{M URLs} \\times 500\\text{ bytes} \\approx \\mathbf{33\\text{ GB of RAM}}$ in Redis!</li>
          </ul>
        </section>

        <!-- Chapter 3 -->
        <section class="reader-section">
          <h2 class="sketch-heading" style="color:var(--ink-blue); border-bottom:2px solid var(--border-dark); padding-bottom:0.4rem;">
            3. Core Entities, Relational Schema &amp; REST APIs
          </h2>
          <p>
            The domain requires two core models: <code>User</code> and <code>URL</code>. The relationship is strictly <strong>1-to-Many</strong>: One registered user can create millions of short links, but each short link belongs to exactly one user (or null for anonymous links).
          </p>
          <div class="code-box">
            <div class="code-header">
              <span class="code-lang">sql &bull; schema.sql</span>
              <span class="tag tag-blue">PostgreSQL DDL</span>
            </div>
            <pre><code>CREATE TABLE urls (
    id BIGINT PRIMARY KEY,              -- 64-bit Snowflake ID
    short_url VARCHAR(32) NOT NULL,     -- Base62 slug or custom vanity
    long_url VARCHAR(2048) NOT NULL,    -- Destination URL
    user_id BIGINT REFERENCES users(id),-- Optional user ownership
    is_custom BOOLEAN DEFAULT FALSE,    -- Flag for vanity slugs
    click_count BIGINT DEFAULT 0,       -- Approximate counter
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE -- Nullable expiration timestamp
);

-- Crucial unique B-Tree index for sub-millisecond lookup
CREATE UNIQUE INDEX idx_urls_short_url ON urls (short_url);
CREATE INDEX idx_urls_user_id ON urls (user_id);
CREATE INDEX idx_urls_expires_at ON urls (expires_at) WHERE expires_at IS NOT NULL;</code></pre>
          </div>
        </section>

        <!-- Chapter 4 -->
        <section class="reader-section">
          <h2 class="sketch-heading" style="color:var(--ink-blue); border-bottom:2px solid var(--border-dark); padding-bottom:0.4rem;">
            4. The Three ID Generation Architectures
          </h2>
          <p>
            How do we generate guaranteed unique, short (6-7 char) strings at high scale? The lecture whiteboard breaks this down into three distinct approaches:
          </p>
          <div class="grid grid-3" style="margin:1rem 0;">
            <div class="card card-yellow">
              <h4 class="sketch-heading" style="color:var(--ink-blue);">Approach 1: SHA-1 / MD5</h4>
              <p style="font-size:0.85rem; line-height:1.5;">
                Hash destination URL with SHA-1, take first 7 chars. <strong>Flaw:</strong> Deterministic hashes produce identical outputs for identical URLs, and hash collisions require expensive DB retry loops (<code>= 16ms + 16ms</code> latency penalty).
              </p>
            </div>
            <div class="card card-red">
              <h4 class="sketch-heading" style="color:var(--alert-red);">Approach 2: Redis Counter</h4>
              <p style="font-size:0.85rem; line-height:1.5;">
                A centralized Redis instance issues atomic incremental integers (<code>INCR</code>). <strong>Flaw:</strong> Single Point of Failure (SPOF) and network bottleneck at &gt; 50,000 writes/sec.
              </p>
            </div>
            <div class="card card-green">
              <h4 class="sketch-heading" style="color:var(--ink-blue);">Approach 3: Snowflake (Winner)</h4>
              <p style="font-size:0.85rem; line-height:1.5;">
                Distributed 64-bit integer generator. Servers use local clocks and pre-assigned ZooKeeper worker IDs. Generates <strong>4,096 IDs per millisecond per node</strong> with zero network RPCs!
              </p>
            </div>
          </div>
        </section>

        <!-- Chapter 5 -->
        <section class="reader-section">
          <h2 class="sketch-heading" style="color:var(--ink-blue); border-bottom:2px solid var(--border-dark); padding-bottom:0.4rem;">
            5. Wire Protocols, Caching, and Abuse Protection
          </h2>
          <p>
            Redirecting traffic involves crucial tradeoffs between HTTP 301 and HTTP 302:
          </p>
          <ul style="padding-left:1.5rem; line-height:1.8;">
            <li><strong>HTTP 301 (Moved Permanently):</strong> The browser caches the redirect mapping permanently. Subsequent clicks bypass your servers entirely, saving bandwidth but <strong>destroying click analytics</strong>.</li>
            <li><strong>HTTP 302 (Found / Temporary):</strong> The browser queries your servers on every click. Enables 100% click telemetry, geolocation tracking, and instant URL revocation.</li>
          </ul>
          <p>
            To protect your database from DDoS attacks requesting random invalid short codes, install a <strong>Redis Bloom Filter</strong> in front of the cache. Consuming only 11MB of memory for 10 million URLs, it rejects non-existent keys in sub-millisecond time with a 0% false negative rate!
          </p>
        </section>
      </article>
    </section>
"""

def get_revision_view():
    return """
    <!-- =========================================================================
         VIEW 3: REVISION (SUMMARY CHEAT-SHEET & INTERVIEW MASTER QUESTIONS)
         ========================================================================= -->
    <section id="revisionView" class="revision-mode" style="display:none;">
      <div class="container" style="max-width:1100px;">
        <header style="margin-bottom:2rem; text-align:center;">
          <span class="tag tag-red">INTERVIEW REVISION CHEAT-SHEET</span>
          <h2 class="sketch-heading" style="font-size:2.2rem; color:var(--ink-blue); margin-top:0.5rem;">
            URL Shortener Architecture at a Glance
          </h2>
          <p style="color:var(--pencil-grey); font-size:1rem;">
            High-density reference cards, critical capacity numbers, and verbatim answers to the 4 toughest interview questions.
          </p>
        </header>

        <!-- High Density Numbers Table -->
        <div class="card card-yellow" style="margin-bottom:2rem;">
          <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:1rem;">
            📊 Key Numbers &amp; Formulas to Memorize for Interviews
          </h3>
          <div class="table-responsive">
            <table class="sketch-table" style="font-size:0.88rem;">
              <thead>
                <tr>
                  <th>Metric / Component</th>
                  <th>Formula / Exact Math</th>
                  <th>Production Value</th>
                  <th>Architectural Significance</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Read-to-Write Ratio</strong></td>
                  <td>Whiteboard annotation: 20% write vs 80% read</td>
                  <td><strong>100 : 1</strong></td>
                  <td>Separates Encryption servers from Decryption servers.</td>
                </tr>
                <tr>
                  <td><strong>Base62 Capacity (7 chars)</strong></td>
                  <td>$62^7 = 3,521,614,606,208$</td>
                  <td><strong>3.52 Trillion URLs</strong></td>
                  <td>Enough namespace to run for 2,900 years at 100M URLs/mo.</td>
                </tr>
                <tr>
                  <td><strong>Snowflake Timestamp Lifespan</strong></td>
                  <td>$2^{41} / (1000 \\times 3600 \\times 24 \\times 365)$</td>
                  <td><strong>69.73 Years</strong></td>
                  <td>Zero clock overflow risk within application lifespan.</td>
                </tr>
                <tr>
                  <td><strong>Snowflake Worker Capacity</strong></td>
                  <td>$2^{10}$ distinct worker nodes</td>
                  <td><strong>1,024 Workers</strong></td>
                  <td>Allocated via ZooKeeper ephemeral sequential nodes.</td>
                </tr>
                <tr>
                  <td><strong>Snowflake Sequence Generation</strong></td>
                  <td>$2^{12} \\times 1000\\text{ ms}$</td>
                  <td><strong>4,096,000 IDs/sec</strong></td>
                  <td>4,096 IDs per millisecond per individual worker node!</td>
                </tr>
                <tr>
                  <td><strong>Redis Cache Hit Latency</strong></td>
                  <td>Direct in-memory RAM lookup</td>
                  <td><strong>2 ms</strong> (Whiteboard annotation)</td>
                  <td>Handles 80% to 90% of all read redirects.</td>
                </tr>
                <tr>
                  <td><strong>PostgreSQL B-Tree Miss Latency</strong></td>
                  <td>Disk seek + network round-trip</td>
                  <td><strong>10 ms</strong> (Whiteboard annotation)</td>
                  <td>Falls back only on cold/unpopular URLs.</td>
                </tr>
                <tr>
                  <td><strong>SHA-1 Retry Collision Penalty</strong></td>
                  <td>$1\\text{ms hash} + 5\\text{ms DB} + 10\\text{ms retry}$</td>
                  <td><strong>= 16 ms + 16 ms</strong></td>
                  <td>Why Approach 1 was abandoned in high-concurrency systems.</td>
                </tr>
                <tr>
                  <td><strong>Bloom Filter Memory Efficiency</strong></td>
                  <td>$m = -\\frac{n \\ln p}{(\\ln 2)^2}$ for 10M keys, $p=1\\%$</td>
                  <td><strong>11.4 MB of RAM</strong></td>
                  <td>Stops 99% of invalid cache-penetration requests.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- 4 MASTER INTERVIEW QUESTIONS & ANSWERS (VERBATIM FROM TRANSCRIPT) -->
        <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:1.25rem;">
          🎯 The 4 Master Interview Questions &amp; Battle-Tested Answers
        </h3>

        <!-- Question 1 -->
        <div class="card card-blue" style="margin-bottom:1.5rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span class="tag tag-red">MASTER QUESTION 1</span>
            <span style="font-size:0.8rem; font-weight:700; color:var(--ink-blue);">Topic: ID Generation &amp; Uniqueness</span>
          </div>
          <h4 class="sketch-heading" style="color:var(--ink-blue); font-size:1.15rem; margin-bottom:0.75rem;">
            "How do you generate guaranteed unique short URLs at scale without collisions?"
          </h4>
          <div style="font-size:0.95rem; line-height:1.7; color:var(--pencil-grey);">
            <p><strong>The Senior Engineer Answer:</strong></p>
            <p>
              "We have three architectural options:
            </p>
            <ol style="padding-left:1.25rem; margin-bottom:0.75rem;">
              <li><strong>Hash-Based (SHA-1/MD5):</strong> Deterministic and deduplicating, but truncation to 7 chars incurs a 0.2% collision rate at 10M URLs, causing expensive DB retry cascades (<code>= 16ms + 16ms</code>).</li>
              <li><strong>Centralized Counter (Redis/ZooKeeper):</strong> Produces short, clean IDs, but centralized counters create a network bottleneck and Single Point of Failure (SPOF) beyond 50K writes/sec.</li>
              <li><strong>Twitter Snowflake (Recommended):</strong> A distributed 64-bit ID generator combining a 41-bit timestamp, 10-bit worker ID, and 12-bit local sequence. When boot-strapped with Apache ZooKeeper ephemeral znodes, worker nodes generate <strong>4,096 IDs per millisecond locally</strong> with zero network coordination. We then Base62 encode this 64-bit integer into a 7-character URL-safe string ($62^7 = 3.52\\text{ Trillion}$ capacity)."</li>
            </ol>
            <p>
              <em>Crucial Interview Edge:</em> Mention that an atomic <code>UNIQUE</code> constraint on <code>urls.short_url</code> in PostgreSQL acts as our final ACID safety net.
            </p>
          </div>
        </div>

        <!-- Question 2 -->
        <div class="card card-green" style="margin-bottom:1.5rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span class="tag tag-green">MASTER QUESTION 2</span>
            <span style="font-size:0.8rem; font-weight:700; color:var(--ink-blue);">Topic: Scalability &amp; Latency SLAs</span>
          </div>
          <h4 class="sketch-heading" style="color:var(--ink-blue); font-size:1.15rem; margin-bottom:0.75rem;">
            "How do you handle 1 Billion redirects per day with sub-5ms p99 latency?"
          </h4>
          <div style="font-size:0.95rem; line-height:1.7; color:var(--pencil-grey);">
            <p><strong>The Senior Engineer Answer:</strong></p>
            <p>
              "1 Billion redirects/day translates to ~11,500 read QPS average and ~80,000 peak QPS. We conquer this using a 4-tier caching and read-scaling topology:
            </p>
            <ol style="padding-left:1.25rem; margin-bottom:0.75rem;">
              <li><strong>Edge Anycast DNS &amp; CDN Caching:</strong> For viral URLs (top 0.1% that generate 50% of traffic), Cloudflare/CloudFront edge nodes terminate connections within 50ms globally.</li>
              <li><strong>Dedicated Decryption Tier:</strong> 80% of our servers handle reads, entirely isolated from the 20% write encryption tier.</li>
              <li><strong>Distributed Redis Cluster (LRU):</strong> Following the 80-20 Pareto principle, caching the top 20% of daily URLs requires only <strong>33 GB of RAM</strong>. Redis achieves &gt; 90% cache hit rate with <strong>sub-2ms response times</strong>.</li>
              <li><strong>PostgreSQL Read Replicas:</strong> The remaining 10% cache misses (~8,000 QPS) are distributed across 5 read-only DB replicas (each handling ~1,600 QPS on an indexed B-Tree seek)."</li>
            </ol>
          </div>
        </div>

        <!-- Question 3 -->
        <div class="card card-red" style="margin-bottom:1.5rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span class="tag tag-red">MASTER QUESTION 3</span>
            <span style="font-size:0.8rem; font-weight:700; color:var(--alert-red);">Topic: Protocols &amp; Analytics Tradeoff</span>
          </div>
          <h4 class="sketch-heading" style="color:var(--alert-red); font-size:1.15rem; margin-bottom:0.75rem;">
            "Should you return HTTP 301 or HTTP 302 for redirects? What is the business impact?"
          </h4>
          <div style="font-size:0.95rem; line-height:1.7; color:var(--pencil-grey);">
            <p><strong>The Senior Engineer Answer:</strong></p>
            <p>
              "This is a fundamental tradeoff between <strong>infrastructure cost</strong> and <strong>analytics capability</strong>:
            </p>
            <ul style="padding-left:1.25rem; margin-bottom:0.75rem;">
              <li><strong>HTTP 301 (Moved Permanently):</strong> The browser caches the redirect mapping permanently. Subsequent clicks never touch our servers. While this minimizes server load and yields the fastest end-user redirect, <strong>we lose 100% of repeat click analytics, user-agent data, and geolocation tracking</strong>! Furthermore, we cannot instantly revoke malicious links or expire dead promotions.</li>
              <li><strong>HTTP 302 (Found) / 307 (Temporary Redirect):</strong> The browser must query our servers on every single click. Although this increases read traffic to 80,000 QPS, it allows us to emit click events to <strong>Apache Kafka</strong> asynchronously, collect granular telemetry, and immediately enforce link expiration (<code>410 Gone</code>).</li>
            </ul>
            <p>
              <em>Verdict:</em> Pure redirection platforms use 301, but modern marketing shorteners (Bitly, Dub.co) use <strong>302 or 307</strong> because click analytics are the primary monetization driver."
            </p>
          </div>
        </div>

        <!-- Question 4 -->
        <div class="card card-yellow" style="margin-bottom:1.5rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span class="tag tag-yellow">MASTER QUESTION 4</span>
            <span style="font-size:0.8rem; font-weight:700; color:var(--ink-blue);">Topic: Security &amp; Abuse Prevention</span>
          </div>
          <h4 class="sketch-heading" style="color:var(--ink-blue); font-size:1.15rem; margin-bottom:0.75rem;">
            "How do you stop spammers from weaponizing the URL shortener for phishing and malware?"
          </h4>
          <div style="font-size:0.95rem; line-height:1.7; color:var(--pencil-grey);">
            <p><strong>The Senior Engineer Answer:</strong></p>
            <p>
              "We implement a defense-in-depth security model across 4 tiers:
            </p>
            <ol style="padding-left:1.25rem; margin-bottom:0.75rem;">
              <li><strong>Rate Limiting:</strong> Redis token-bucket rate limiter restricts anonymous users to 100 URL creations per hour per IP. Authenticated API keys receive 10,000/day.</li>
              <li><strong>Async Malware Scanning:</strong> On link creation, the destination URL is asynchronously dispatched to <strong>Google Safe Browsing API</strong> and cross-referenced with PhishTank/URLhaus bloom filters. Flagged URLs are instantly deactivated.</li>
              <li><strong>Homograph &amp; Typosquatting Detection:</strong> We compute the <strong>Levenshtein Edit Distance</strong> between the destination domain and top 1,000 high-risk domains (e.g., <code>paypa1.com</code> vs <code>paypal.com</code>). If distance is 1 or 2, we force an <strong>Interstitial Warning Screen</strong>.</li>
              <li><strong>Cache Penetration Shield:</strong> A Redis Bloom Filter blocks arbitrary brute-force 404 URL scans from reaching PostgreSQL, protecting disk I/O from exhaustion."</li>
            </ol>
          </div>
        </div>
      </div>
    </section>
"""

def get_flashcards_view():
    return """
    <!-- =========================================================================
         VIEW 4: FLASHCARDS (3D FLIP-CARDS ACTIVE RECALL MODE)
         ========================================================================= -->
    <section id="flashcardsView" class="flashcards-mode" style="display:none;">
      <div class="container" style="max-width:900px;">
        <header style="margin-bottom:1.5rem; text-align:center;">
          <span class="tag tag-yellow">SPACED REPETITION ACTIVE RECALL</span>
          <h2 class="sketch-heading" style="font-size:2rem; color:var(--ink-blue); margin-top:0.5rem;">
            System Design Flashcards (8 Core Concepts)
          </h2>
          <p style="color:var(--pencil-grey); font-size:0.95rem;">
            Click any card to flip between Question and Production Architectural Answer.
          </p>
        </header>

        <div class="flashcards-grid">
          <!-- CARD 1 -->
          <div class="flashcard" onclick="flipFlashcard(this)">
            <div class="flashcard-inner">
              <div class="flashcard-face flashcard-front">
                <span class="card-num">CARD 01 / 08</span>
                <h3 class="sketch-heading" style="font-size:1.15rem; color:var(--ink-blue);">
                  Why do we use Base62 encoding instead of Base64 or Hexadecimal?
                </h3>
                <span class="flip-hint">&cularr; Click to reveal answer</span>
              </div>
              <div class="flashcard-face flashcard-back">
                <span class="card-num">ANSWER 01</span>
                <p style="font-size:0.9rem; line-height:1.6;">
                  <strong>Hex (Base16)</strong> yields only $16^7 \\approx 268\\text{M}$ URLs (too small). <strong>Base64</strong> includes <code>+</code> and <code>/</code>, which require URL %-encoding. <strong>Base62 (0-9, a-z, A-Z)</strong> is 100% URL-safe without escaping and yields <strong>3.52 Trillion URLs</strong> at 7 characters!
                </p>
              </div>
            </div>
          </div>

          <!-- CARD 2 -->
          <div class="flashcard" onclick="flipFlashcard(this)">
            <div class="flashcard-inner">
              <div class="flashcard-face flashcard-front">
                <span class="card-num">CARD 02 / 08</span>
                <h3 class="sketch-heading" style="font-size:1.15rem; color:var(--ink-blue);">
                  What is the capacity formula for a 7-character Base62 string?
                </h3>
                <span class="flip-hint">&cularr; Click to reveal answer</span>
              </div>
              <div class="flashcard-face flashcard-back">
                <span class="card-num">ANSWER 02</span>
                <p style="font-size:0.9rem; line-height:1.6;">
                  $62^7 = \\mathbf{3,521,614,606,208}$ (over <strong>3.52 Trillion URLs</strong>). At a generation rate of 100 Million new URLs every month, this single 7-character namespace will last for over <strong>2,900 years</strong> without exhausting!
                </p>
              </div>
            </div>
          </div>

          <!-- CARD 3 -->
          <div class="flashcard" onclick="flipFlashcard(this)">
            <div class="flashcard-inner">
              <div class="flashcard-face flashcard-front">
                <span class="card-num">CARD 03 / 08</span>
                <h3 class="sketch-heading" style="font-size:1.15rem; color:var(--ink-blue);">
                  What is the "= 16ms + 16ms" penalty in Approach 1 (SHA-1 hashing)?
                </h3>
                <span class="flip-hint">&cularr; Click to reveal answer</span>
              </div>
              <div class="flashcard-face flashcard-back">
                <span class="card-num">ANSWER 03</span>
                <p style="font-size:0.9rem; line-height:1.6;">
                  When truncating a 160-bit SHA-1 hash to 7 chars, hash collisions occur. The server takes 1ms to hash, 5ms to query DB, detects collision, re-hashes with salt, and queries DB again &rarr; <strong>16ms + 16ms cascade</strong> that collapses write throughput under high concurrency!
                </p>
              </div>
            </div>
          </div>

          <!-- CARD 4 -->
          <div class="flashcard" onclick="flipFlashcard(this)">
            <div class="flashcard-inner">
              <div class="flashcard-face flashcard-front">
                <span class="card-num">CARD 04 / 08</span>
                <h3 class="sketch-heading" style="font-size:1.15rem; color:var(--ink-blue);">
                  Why is a single Redis counter a dangerous bottleneck in Approach 2?
                </h3>
                <span class="flip-hint">&cularr; Click to reveal answer</span>
              </div>
              <div class="flashcard-face flashcard-back">
                <span class="card-num">ANSWER 04</span>
                <p style="font-size:0.9rem; line-height:1.6;">
                  A single Redis node executing <code>INCR</code> is a <strong>Single Point of Failure (SPOF)</strong>. If it crashes, all URL generation stops. Furthermore, network round-trips (2-3ms) saturate the single thread, capping global write throughput at ~50K QPS.
                </p>
              </div>
            </div>
          </div>

          <!-- CARD 5 -->
          <div class="flashcard" onclick="flipFlashcard(this)">
            <div class="flashcard-inner">
              <div class="flashcard-face flashcard-front">
                <span class="card-num">CARD 05 / 08</span>
                <h3 class="sketch-heading" style="font-size:1.15rem; color:var(--ink-blue);">
                  How does Apache ZooKeeper coordinate Snowflake worker nodes?
                </h3>
                <span class="flip-hint">&cularr; Click to reveal answer</span>
              </div>
              <div class="flashcard-face flashcard-back">
                <span class="card-num">ANSWER 05</span>
                <p style="font-size:0.9rem; line-height:1.6;">
                  Encryption servers register an <strong>ephemeral sequential znode</strong> (e.g. <code>/app1/p_1 &rarr; workerID: 123</code>) at boot time. ZooKeeper guarantees unique worker IDs (0 to 1023). When a server dies, its session expires and frees the ID. <strong>Zero runtime RPCs!</strong>
                </p>
              </div>
            </div>
          </div>

          <!-- CARD 6 -->
          <div class="flashcard" onclick="flipFlashcard(this)">
            <div class="flashcard-inner">
              <div class="flashcard-face flashcard-front">
                <span class="card-num">CARD 06 / 08</span>
                <h3 class="sketch-heading" style="font-size:1.15rem; color:var(--ink-blue);">
                  What is the critical business drawback of returning HTTP 301 redirects?
                </h3>
                <span class="flip-hint">&cularr; Click to reveal answer</span>
              </div>
              <div class="flashcard-face flashcard-back">
                <span class="card-num">ANSWER 06</span>
                <p style="font-size:0.9rem; line-height:1.6;">
                  Browsers cache <strong>HTTP 301</strong> responses indefinitely on disk. Subsequent user clicks bypass the backend shortener entirely. <strong>Result: Zero click telemetry, zero user-agent/geo tracking, and no ability to expire or revoke links!</strong>
                </p>
              </div>
            </div>
          </div>

          <!-- CARD 7 -->
          <div class="flashcard" onclick="flipFlashcard(this)">
            <div class="flashcard-inner">
              <div class="flashcard-face flashcard-front">
                <span class="card-num">CARD 07 / 08</span>
                <h3 class="sketch-heading" style="font-size:1.15rem; color:var(--ink-blue);">
                  How does a Bloom filter stop Cache Penetration DDoS attacks?
                </h3>
                <span class="flip-hint">&cularr; Click to reveal answer</span>
              </div>
              <div class="flashcard-face flashcard-back">
                <span class="card-num">ANSWER 07</span>
                <p style="font-size:0.9rem; line-height:1.6;">
                  When an attacker queries random non-existent short URLs, they miss Redis. A <strong>Bloom filter (11MB for 10M keys)</strong> checks the key: if bits are 0, it <strong>guarantees 100%</strong> the key does not exist and returns HTTP 404 instantly without querying PostgreSQL disk!
                </p>
              </div>
            </div>
          </div>

          <!-- CARD 8 -->
          <div class="flashcard" onclick="flipFlashcard(this)">
            <div class="flashcard-inner">
              <div class="flashcard-face flashcard-front">
                <span class="card-num">CARD 08 / 08</span>
                <h3 class="sketch-heading" style="font-size:1.15rem; color:var(--ink-blue);">
                  How does Dual-Layer expiration eliminate "Zombie Links"?
                </h3>
                <span class="flip-hint">&cularr; Click to reveal answer</span>
              </div>
              <div class="flashcard-face flashcard-back">
                <span class="card-num">ANSWER 08</span>
                <p style="font-size:0.9rem; line-height:1.6;">
                  <strong>Layer 1 (Passive):</strong> On read access, check <code>expires_at &lt; now()</code> and return <code>410 Gone</code>. <strong>Layer 2 (Batch Cron):</strong> A nightly 2:00 AM batch job deletes expired rows in chunks of 5,000 to reclaim disk and B-Tree space without locking the database table.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

def get_quiz_view():
    return """
    <!-- =========================================================================
         VIEW 5: QUIZ (10-QUESTION CERTIFICATION ASSESSMENT)
         ========================================================================= -->
    <section id="quizView" class="quiz-mode" style="display:none;">
      <div class="container" style="max-width:900px;">
        <header style="margin-bottom:2rem; text-align:center;">
          <span class="tag tag-green">SENIOR SYSTEM DESIGN CERTIFICATION</span>
          <h2 class="sketch-heading" style="font-size:2.2rem; color:var(--ink-blue); margin-top:0.5rem;">
            URL Shortener Mastery Quiz (10 Questions)
          </h2>
          <p style="color:var(--pencil-grey); font-size:1rem;">
            Test your first-principles knowledge on capacity math, snowflake bit allocations, wire redirects, and caching.
          </p>
          <div id="quizScoreBanner" style="display:none; margin-top:1rem; padding:1rem; border:2px solid var(--ink-blue); border-radius:8px; background:var(--highlighter-yellow); font-family:Lexend, sans-serif; font-size:1.1rem; font-weight:700;"></div>
        </header>

        <form id="quizForm" onsubmit="event.preventDefault(); evaluateQuiz();">
          <!-- QUESTION 1 -->
          <div class="quiz-question-card" id="qCard_1">
            <div class="q-header">
              <span class="q-badge">QUESTION 1 / 10</span>
              <span class="q-topic">Base62 Math</span>
            </div>
            <p class="q-text">How many unique URL slugs can be generated using a 7-character Base62 string?</p>
            <div class="quiz-options">
              <label class="quiz-option"><input type="radio" name="q1" value="A"> A) 56.8 Billion ($62^6$)</label>
              <label class="quiz-option"><input type="radio" name="q1" value="B"> B) 3.52 Trillion ($62^7$)</label>
              <label class="quiz-option"><input type="radio" name="q1" value="C"> C) 268.4 Million ($16^7$)</label>
              <label class="quiz-option"><input type="radio" name="q1" value="D"> D) 4.39 Trillion ($64^7$)</label>
            </div>
            <div class="q-feedback" id="feedback_1"></div>
          </div>

          <!-- QUESTION 2 -->
          <div class="quiz-question-card" id="qCard_2">
            <div class="q-header">
              <span class="q-badge">QUESTION 2 / 10</span>
              <span class="q-topic">Whiteboard Latency Annotation</span>
            </div>
            <p class="q-text">In the lecture whiteboard, what is the exact round-trip latency penalty annotated for an SHA-1 hash collision retry cascade?</p>
            <div class="quiz-options">
              <label class="quiz-option"><input type="radio" name="q2" value="A"> A) = 5ms + 5ms</label>
              <label class="quiz-option"><input type="radio" name="q2" value="B"> B) = 16ms + 16ms</label>
              <label class="quiz-option"><input type="radio" name="q2" value="C"> C) = 2ms + 3ms</label>
              <label class="quiz-option"><input type="radio" name="q2" value="D"> D) = 50ms + 50ms</label>
            </div>
            <div class="q-feedback" id="feedback_2"></div>
          </div>

          <!-- QUESTION 3 -->
          <div class="quiz-question-card" id="qCard_3">
            <div class="q-header">
              <span class="q-badge">QUESTION 3 / 10</span>
              <span class="q-topic">Server Architecture Split</span>
            </div>
            <p class="q-text">What is the workload split annotated on the whiteboard between Encryption (Write) servers and Decryption (Read) servers?</p>
            <div class="quiz-options">
              <label class="quiz-option"><input type="radio" name="q3" value="A"> A) 50% Encryption vs 50% Decryption</label>
              <label class="quiz-option"><input type="radio" name="q3" value="B"> B) 20% Encryption vs 80% Decryption</label>
              <label class="quiz-option"><input type="radio" name="q3" value="C"> C) 1% Encryption vs 99% Decryption</label>
              <label class="quiz-option"><input type="radio" name="q3" value="D"> D) 10% Encryption vs 90% Decryption</label>
            </div>
            <div class="q-feedback" id="feedback_3"></div>
          </div>

          <!-- QUESTION 4 -->
          <div class="quiz-question-card" id="qCard_4">
            <div class="q-header">
              <span class="q-badge">QUESTION 4 / 10</span>
              <span class="q-topic">Snowflake Bit Allocation</span>
            </div>
            <p class="q-text">How long can a 41-bit timestamp run in Twitter Snowflake before epoch exhaustion occurs?</p>
            <div class="quiz-options">
              <label class="quiz-option"><input type="radio" name="q4" value="A"> A) 34.8 Years</label>
              <label class="quiz-option"><input type="radio" name="q4" value="B"> B) 69.73 Years</label>
              <label class="quiz-option"><input type="radio" name="q4" value="C"> C) 136.4 Years</label>
              <label class="quiz-option"><input type="radio" name="q4" value="D"> D) 1024 Years</label>
            </div>
            <div class="q-feedback" id="feedback_4"></div>
          </div>

          <!-- QUESTION 5 -->
          <div class="quiz-question-card" id="qCard_5">
            <div class="q-header">
              <span class="q-badge">QUESTION 5 / 10</span>
              <span class="q-topic">ZooKeeper Ephemeral Znodes</span>
            </div>
            <p class="q-text">Why does Approach 3 register worker IDs in ZooKeeper only during server boot rather than on every URL creation?</p>
            <div class="quiz-options">
              <label class="quiz-option"><input type="radio" name="q5" value="A"> A) ZooKeeper cannot handle more than 10 requests per second.</label>
              <label class="quiz-option"><input type="radio" name="q5" value="B"> B) Boot-time allocation eliminates all network coordination latency during runtime ID generation.</label>
              <label class="quiz-option"><input type="radio" name="q5" value="C"> C) Ephemeral znodes are deleted every 10 milliseconds automatically.</label>
              <label class="quiz-option"><input type="radio" name="q5" value="D"> D) Snowflake requires persistent SQL storage to work.</label>
            </div>
            <div class="q-feedback" id="feedback_5"></div>
          </div>

          <!-- QUESTION 6 -->
          <div class="quiz-question-card" id="qCard_6">
            <div class="q-header">
              <span class="q-badge">QUESTION 6 / 10</span>
              <span class="q-topic">Wire Redirect Protocols</span>
            </div>
            <p class="q-text">If real-time click tracking, geolocation analytics, and link expiration are business requirements, which HTTP redirect code MUST you use?</p>
            <div class="quiz-options">
              <label class="quiz-option"><input type="radio" name="q6" value="A"> A) HTTP 301 (Moved Permanently)</label>
              <label class="quiz-option"><input type="radio" name="q6" value="B"> B) HTTP 302 (Found) or HTTP 307 (Temporary Redirect)</label>
              <label class="quiz-option"><input type="radio" name="q6" value="C"> C) HTTP 200 (OK)</label>
              <label class="quiz-option"><input type="radio" name="q6" value="D"> D) HTTP 304 (Not Modified)</label>
            </div>
            <div class="q-feedback" id="feedback_6"></div>
          </div>

          <!-- QUESTION 7 -->
          <div class="quiz-question-card" id="qCard_7">
            <div class="q-header">
              <span class="q-badge">QUESTION 7 / 10</span>
              <span class="q-topic">Bloom Filter Mechanics</span>
            </div>
            <p class="q-text">What is the space requirement for a Bloom filter protecting 10,000,000 URLs with a 1% false positive rate?</p>
            <div class="quiz-options">
              <label class="quiz-option"><input type="radio" name="q7" value="A"> A) ~500 MB</label>
              <label class="quiz-option"><input type="radio" name="q7" value="B"> B) ~5 MB to 11.4 MB</label>
              <label class="quiz-option"><input type="radio" name="q7" value="C"> C) ~2 GB</label>
              <label class="quiz-option"><input type="radio" name="q7" value="D"> D) Exactly 100 KB</label>
            </div>
            <div class="q-feedback" id="feedback_7"></div>
          </div>

          <!-- QUESTION 8 -->
          <div class="quiz-question-card" id="qCard_8">
            <div class="q-header">
              <span class="q-badge">QUESTION 8 / 10</span>
              <span class="q-topic">Database Lifecycle Management</span>
            </div>
            <p class="q-text">Why is executing 'DELETE FROM urls WHERE expires_at &lt; NOW()' on the entire database during peak hours considered a fatal mistake?</p>
            <div class="quiz-options">
              <label class="quiz-option"><input type="radio" name="q8" value="A"> A) PostgreSQL does not support timestamps.</label>
              <label class="quiz-option"><input type="radio" name="q8" value="B"> B) It acquires an exclusive table/page lock on the B-Tree, stalling all incoming read and write queries.</label>
              <label class="quiz-option"><input type="radio" name="q8" value="C"> C) Expired URLs cannot be deleted once inserted.</label>
              <label class="quiz-option"><input type="radio" name="q8" value="D"> D) It deletes user accounts accidentally.</label>
            </div>
            <div class="q-feedback" id="feedback_8"></div>
          </div>

          <!-- QUESTION 9 -->
          <div class="quiz-question-card" id="qCard_9">
            <div class="q-header">
              <span class="q-badge">QUESTION 9 / 10</span>
              <span class="q-topic">Distributed Analytics</span>
            </div>
            <p class="q-text">Which probabilistic data structure allows estimating 100M unique visitors per short link using only ~12 KB of fixed memory in Redis?</p>
            <div class="quiz-options">
              <label class="quiz-option"><input type="radio" name="q9" value="A"> A) B-Tree Index</label>
              <label class="quiz-option"><input type="radio" name="q9" value="B"> B) HyperLogLog (HLL)</label>
              <label class="quiz-option"><input type="radio" name="q9" value="C"> C) Count-Min Sketch</label>
              <label class="quiz-option"><input type="radio" name="q9" value="D"> D) Hash Ring</label>
            </div>
            <div class="q-feedback" id="feedback_9"></div>
          </div>

          <!-- QUESTION 10 -->
          <div class="quiz-question-card" id="qCard_10">
            <div class="q-header">
              <span class="q-badge">QUESTION 10 / 10</span>
              <span class="q-topic">Phishing &amp; Security</span>
            </div>
            <p class="q-text">Which metric is used to detect homograph phishing spoofing attacks (e.g. 'paypa1.com' targeting 'paypal.com')?</p>
            <div class="quiz-options">
              <label class="quiz-option"><input type="radio" name="q10" value="A"> A) SHA-256 Hamming Distance</label>
              <label class="quiz-option"><input type="radio" name="q10" value="B"> B) Levenshtein Edit Distance &le; 2</label>
              <label class="quiz-option"><input type="radio" name="q10" value="C"> C) Euclidean Vector Distance</label>
              <label class="quiz-option"><input type="radio" name="q10" value="D"> D) Cosine Similarity &gt; 0.99</label>
            </div>
            <div class="q-feedback" id="feedback_10"></div>
          </div>

          <div style="text-align:center; margin-top:2rem;">
            <button type="submit" class="sketch-btn primary" style="font-size:1.1rem; padding:0.85rem 2.5rem;">
              Submit Quiz &amp; Calculate Mastery Score
            </button>
          </div>
        </form>
      </div>
    </section>
"""

def get_drawers_and_modals():
    return """
  <!-- =========================================================================
       DRAWERS & MODALS (rules.md & notestructre.md)
       ========================================================================= -->

  <!-- DRAWER 1: TABLE OF CONTENTS -->
  <div id="tocDrawer" class="drawer">
    <div class="drawer-header">
      <h3 class="sketch-heading" style="color:var(--ink-blue); margin:0;">Lecture Syllabus &amp; Roadmap</h3>
      <button class="drawer-close-btn" onclick="closeDrawer('tocDrawer')">&times;</button>
    </div>
    <div class="drawer-content">
      <ul class="toc-list" id="tocListContainer">
        <li onclick="jumpToSlide(1)" class="toc-item"><span>01. System Roadmap &amp; Overview</span></li>
        <li onclick="jumpToSlide(2)" class="toc-item"><span>02. Functional Scope &amp; Bitly Examples</span></li>
        <li onclick="jumpToSlide(3)" class="toc-item"><span>03. Non-Functional SLAs &amp; Capacity Math</span></li>
        <li onclick="jumpToSlide(4)" class="toc-item"><span>04. Core Entity Models (User &amp; URL)</span></li>
        <li onclick="jumpToSlide(5)" class="toc-item"><span>05. REST API Specifications</span></li>
        <li onclick="jumpToSlide(6)" class="toc-item"><span>06. Section 4: High-Level Architecture (HLD)</span></li>
        <li onclick="jumpToSlide(7)" class="toc-item"><span>07. Relational Schema &amp; B-Tree Indexing</span></li>
        <li onclick="jumpToSlide(8)" class="toc-item"><span>08. The 3 ID Generation Architectures</span></li>
        <li onclick="jumpToSlide(9)" class="toc-item"><span>09. Approach 1: SHA-1 Encryption Deep Dive</span></li>
        <li onclick="jumpToSlide(10)" class="toc-item"><span>10. SHA-1 Collision Cascade (=16ms+16ms)</span></li>
        <li onclick="jumpToSlide(11)" class="toc-item"><span>11. Approach 2: Counter &amp; Monolith Bottleneck</span></li>
        <li onclick="jumpToSlide(12)" class="toc-item"><span>12. Load Balancer Race Condition &amp; Duplicate 0</span></li>
        <li onclick="jumpToSlide(13)" class="toc-item"><span>13. Redis Counter Split: 20% Write vs 80% Read</span></li>
        <li onclick="jumpToSlide(14)" class="toc-item"><span>14. ZooKeeper Distributed Coordination &amp; Tree</span></li>
        <li onclick="jumpToSlide(15)" class="toc-item"><span>15. Approach 3: Snowflake Master Topology</span></li>
        <li onclick="jumpToSlide(16)" class="toc-item"><span>16. Snowflake 64-bit Binary Math (69.73 Yrs)</span></li>
        <li onclick="jumpToSlide(17)" class="toc-item"><span>17. Base62 Conversion Pipeline &amp; Radix Math</span></li>
        <li onclick="jumpToSlide(18)" class="toc-item"><span>18. Wire Redirects: HTTP 301 vs HTTP 302</span></li>
        <li onclick="jumpToSlide(19)" class="toc-item"><span>19. Edge Cases: Custom Vanity URLs</span></li>
        <li onclick="jumpToSlide(20)" class="toc-item"><span>20. Edge Cases: Dual-Layer Expiration (Cron+TTL)</span></li>
        <li onclick="jumpToSlide(21)" class="toc-item"><span>21. Bloom Filters &amp; Cache Penetration Shield</span></li>
        <li onclick="jumpToSlide(22)" class="toc-item"><span>22. Asynchronous Analytics Decoupling (Kafka)</span></li>
        <li onclick="jumpToSlide(23)" class="toc-item"><span>23. Security, Abuse Prevention &amp; Phishing Filter</span></li>
        <li onclick="jumpToSlide(24)" class="toc-item"><span>24. Interactive Simulator &amp; Wire Inspector</span></li>
      </ul>
    </div>
  </div>

  <!-- DRAWER 2: PERSONAL NOTEPAD -->
  <div id="notesDrawer" class="drawer">
    <div class="drawer-header">
      <h3 class="sketch-heading" style="color:var(--ink-blue); margin:0;">Personal Lecture Scratchpad</h3>
      <button class="drawer-close-btn" onclick="closeDrawer('notesDrawer')">&times;</button>
    </div>
    <div class="drawer-content" style="display:flex; flex-direction:column; height:calc(100% - 70px);">
      <p style="font-size:0.85rem; color:var(--pencil-grey); margin-bottom:0.75rem;">
        Your notes are automatically saved to your browser's local storage. Export anytime as a Markdown file!
      </p>
      <textarea id="personalNotepadArea" class="sketch-input" style="flex:1; width:100%; resize:none; font-family:JetBrains Mono, monospace; font-size:0.88rem; padding:0.75rem; border:2px solid var(--ink-blue); border-radius:6px; background:#FFFDF8; line-height:1.5;" placeholder="Write your interview takeaways, formula scratchpad, or questions here..."></textarea>
      <div style="display:flex; gap:0.5rem; margin-top:0.75rem;">
        <button class="sketch-btn primary" onclick="exportNotesMarkdown()" style="flex:1;">
          &darr; Export as Markdown (.md)
        </button>
        <button class="sketch-btn" onclick="clearNotepad()" style="border:2px solid var(--alert-red); color:var(--alert-red);">
          Clear
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL: GLOBAL SEARCH (CTRL+K) -->
  <div id="searchModal" class="modal-backdrop" onclick="if(event.target === this) closeSearchModal()">
    <div class="modal-card" style="max-width:620px;">
      <div class="modal-header">
        <h3 class="sketch-heading" style="color:var(--ink-blue); margin:0;">Search URL Shortener Knowledge Base</h3>
        <button class="drawer-close-btn" onclick="closeSearchModal()">&times;</button>
      </div>
      <div class="modal-body">
        <input type="text" id="globalSearchInput" placeholder="Search formulas, 301, Snowflake, ZooKeeper, Base62..." oninput="handleSearchQuery(this.value)" class="sketch-input" style="width:100%; padding:0.75rem; font-size:1rem; border:2px solid var(--ink-blue); border-radius:6px; background:#FFF; margin-bottom:1rem;">
        <div id="searchResultsList" style="max-height:350px; overflow-y:auto; display:flex; flex-direction:column; gap:0.5rem;">
          <div style="font-size:0.85rem; color:var(--pencil-light); text-align:center; padding:1.5rem 0;">
            Type at least 2 characters to search across all 24 slides, formulas, and whiteboard notes...
          </div>
        </div>
      </div>
    </div>
  </div>
"""

def get_scripts():
    return """
  <!-- =========================================================================
       CLIENT-SIDE JAVASCRIPT LOGIC (SLIDE ENGINE, SIMULATOR, QUIZ, NOTES)
       ========================================================================= -->
  <script>
    // State variables
    let currentSlide = 1;
    const totalSlides = 24;
    let currentView = 'presentation';

    // Search Index
    const searchIndex = [
      { slide: 1, title: "System Roadmap & Overview", text: "5-step framework functional non-functional entities API HLD deep dive" },
      { slide: 2, title: "Functional Scope & Bitly Examples", text: "Bitly facebook longURL 4kycpo short URL custom vanity expiration date" },
      { slide: 3, title: "Non-Functional SLAs & Capacity Math", text: "100M DAU 80:20 read write ratio 80000 QPS 3TB storage 33GB Redis memory" },
      { slide: 4, title: "Core Entity Models", text: "User URL metadata shortURL longURL expirationDate customURL relational schema" },
      { slide: 5, title: "REST API Specifications", text: "POST shorten GET 302 redirect 404 410 gone curl JSON payloads" },
      { slide: 6, title: "Section 4: High-Level Architecture", text: "Client Load Balancer Application Server Database generateUrl redirect whiteboard" },
      { slide: 7, title: "Database Schema & B-Tree Indexing", text: "PostgreSQL B-Tree primary key bigint 64 bit unique constraint" },
      { slide: 8, title: "The 3 ID Generation Architectures", text: "SHA-1 hashing Counter Redis ZooKeeper Snowflake distributed IDs" },
      { slide: 9, title: "Approach 1: SHA-1 Encryption Deep Dive", text: "SHA-1 160 bits 40 hex chars base62 collision deterministic" },
      { slide: 10, title: "SHA-1 Collision Cascade (=16ms+16ms)", text: "Whiteboard annotation =16ms + 16ms retry salt birthday paradox" },
      { slide: 11, title: "Approach 2: Counter & Monolith Wall", text: "Auto increment monolith single database bottleneck failure" },
      { slide: 12, title: "Load Balancer Race Condition", text: "Duplicate 0 collision round robin state desynchronization" },
      { slide: 13, title: "Redis Counter Split (20% vs 80%)", text: "Whiteboard 20% write encryption 80% read decryption 2ms 3ms Redis counter SPOF" },
      { slide: 14, title: "ZooKeeper Distributed Coordination", text: "Verbatim whiteboard definition centralized service consensus znode tree /app1/p_1 ephemeral" },
      { slide: 15, title: "Approach 3: Snowflake Master Topology", text: "Whiteboard bunny hybrid workerID 123 234 345 local counter 10ms DB 2ms cache" },
      { slide: 16, title: "Snowflake 64-bit Binary Math", text: "41-bit timestamp 69.73 years 10-bit workerID 1024 workers 12-bit sequence 4096 IDs per ms" },
      { slide: 17, title: "Base62 Conversion Pipeline", text: "Radix 62 modulo division remainder 62^7 3.52 trillion clean string" },
      { slide: 18, title: "Wire Redirects: HTTP 301 vs 302", text: "HTTP 301 browser cache permanent no analytics HTTP 302 temporary click tracking" },
      { slide: 19, title: "Edge Cases: Custom Vanity URLs", text: "Custom slug reserved words length 3 to 30 atomic insert conflict" },
      { slide: 20, title: "Dual-Layer Expiration (Cron + TTL)", text: "Zombie keys lazy expiration 410 gone nightly cron batch limit 5000" },
      { slide: 21, title: "Bloom Filters & Cache Penetration", text: "DDoS mitigation MurmurHash 11.4MB memory 1% false positive RedisBloom" },
      { slide: 22, title: "Asynchronous Analytics (Kafka)", text: "Decoupled ClickEvent topic HyperLogLog 12KB unique visitors" },
      { slide: 23, title: "Security & Abuse Prevention", text: "Rate limit 100/hr Safe Browsing Levenshtein distance paypa1.com phishing" },
      { slide: 24, title: "Interactive Simulator & Wire Inspector", text: "Hands-on lab snowflake generator base62 encoder wire trace test" }
    ];

    // Initialization on page load
    document.addEventListener("DOMContentLoaded", () => {
      initNavigation();
      initNotepad();
      updateSlideDisplay();

      // Keyboard shortcuts
      document.addEventListener("keydown", (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        if (e.key === 'ArrowRight' || e.key === ' ') {
          if (currentView === 'presentation') navigateSlide(1);
        } else if (e.key === 'ArrowLeft') {
          if (currentView === 'presentation') navigateSlide(-1);
        } else if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
          e.preventDefault();
          openSearchModal();
        }
      });
    });

    // View Switching Logic (rules.md & notestructre.md)
    function switchView(viewName) {
      currentView = viewName;
      const views = ['presentationView', 'readerView', 'revisionView', 'flashcardsView', 'quizView'];
      const controls = document.getElementById('deckControlsBar');

      views.forEach(v => {
        const el = document.getElementById(v);
        if (el) el.style.display = (v === viewName + 'View') ? 'block' : 'none';
      });

      // Update View Buttons in Header
      document.querySelectorAll('.view-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-view') === viewName);
      });

      // Show floating deck controls only in Presentation mode
      if (controls) {
        controls.style.display = (viewName === 'presentation') ? 'flex' : 'none';
      }

      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Presentation Slide Navigation
    function navigateSlide(direction) {
      const nextSlide = currentSlide + direction;
      if (nextSlide >= 1 && nextSlide <= totalSlides) {
        jumpToSlide(nextSlide);
      }
    }

    function jumpToSlide(slideNum) {
      currentSlide = slideNum;
      document.querySelectorAll('.slide-card').forEach(slide => {
        const num = parseInt(slide.getAttribute('data-slide'), 10);
        slide.classList.toggle('active', num === currentSlide);
      });

      updateSlideDisplay();
      closeDrawer('tocDrawer');

      // Scroll smoothly to top of slide
      const activeEl = document.querySelector(`.slide-card[data-slide="${currentSlide}"]`);
      if (activeEl) {
        activeEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    function updateSlideDisplay() {
      const currText = document.getElementById('currentSlideDisplay');
      const totalText = document.getElementById('totalSlidesDisplay');
      const barFill = document.getElementById('progressBarFill');
      const prevBtn = document.getElementById('prevSlideBtn');
      const nextBtn = document.getElementById('nextSlideBtn');

      if (currText) currText.textContent = currentSlide;
      if (totalText) totalText.textContent = totalSlides;
      if (barFill) {
        const pct = (currentSlide / totalSlides) * 100;
        barFill.style.width = pct + '%';
      }

      if (prevBtn) prevBtn.disabled = (currentSlide === 1);
      if (nextBtn) nextBtn.disabled = (currentSlide === totalSlides);
    }

    // Drawers & Modals
    function openDrawer(drawerId) {
      const el = document.getElementById(drawerId);
      if (el) el.classList.add('open');
    }

    function closeDrawer(drawerId) {
      const el = document.getElementById(drawerId);
      if (el) el.classList.remove('open');
    }

    // Whiteboard Modal
    function openWhiteboardModal() {
      const modal = document.getElementById('whiteboardModal');
      if (modal) modal.style.display = 'flex';
    }

    function closeWhiteboardModal() {
      const modal = document.getElementById('whiteboardModal');
      if (modal) modal.style.display = 'none';
    }

    // Search Modal
    function openSearchModal() {
      const modal = document.getElementById('searchModal');
      const input = document.getElementById('globalSearchInput');
      if (modal) {
        modal.style.display = 'flex';
        if (input) {
          input.value = '';
          input.focus();
          handleSearchQuery('');
        }
      }
    }

    function closeSearchModal() {
      const modal = document.getElementById('searchModal');
      if (modal) modal.style.display = 'none';
    }

    function handleSearchQuery(query) {
      const resultsContainer = document.getElementById('searchResultsList');
      if (!resultsContainer) return;
      const q = query.trim().toLowerCase();

      if (q.length < 2) {
        resultsContainer.innerHTML = '<div style="font-size:0.85rem; color:var(--pencil-light); text-align:center; padding:1.5rem 0;">Type at least 2 characters to search across all 24 slides...</div>';
        return;
      }

      const matches = searchIndex.filter(item => 
        item.title.toLowerCase().includes(q) || item.text.toLowerCase().includes(q)
      );

      if (matches.length === 0) {
        resultsContainer.innerHTML = '<div style="font-size:0.85rem; color:var(--alert-red); text-align:center; padding:1.5rem 0;">No matching slides found. Try keywords like "Snowflake", "ZooKeeper", "301", "Bloom".</div>';
        return;
      }

      let html = '';
      matches.forEach(m => {
        html += `
          <div onclick="selectSearchResult(${m.slide})" style="padding:0.75rem; border:1.5px solid var(--ink-blue); border-radius:6px; background:#FFF; cursor:pointer; transition:background 0.15s ease;" onmouseover="this.style.background='var(--highlighter-yellow)'" onmouseout="this.style.background='#FFF'">
            <div style="font-size:0.75rem; font-weight:700; color:var(--alert-red); text-transform:uppercase;">Slide ${m.slide.toString().padStart(2, '0')}</div>
            <div style="font-size:0.95rem; font-weight:700; color:var(--ink-blue);">${m.title}</div>
            <div style="font-size:0.8rem; color:var(--pencil-grey); margin-top:0.25rem;">${m.text.substring(0, 80)}...</div>
          </div>
        `;
      });
      resultsContainer.innerHTML = html;
    }

    function selectSearchResult(slideNum) {
      closeSearchModal();
      switchView('presentation');
      jumpToSlide(slideNum);
    }

    // Flashcard 3D Flip
    function flipFlashcard(cardEl) {
      cardEl.classList.toggle('flipped');
    }

    // Notepad Autosave & Export
    function initNotepad() {
      const textarea = document.getElementById('personalNotepadArea');
      if (!textarea) return;
      const saved = localStorage.getItem('url_shortener_notepad');
      if (saved) textarea.value = saved;

      textarea.addEventListener('input', () => {
        localStorage.setItem('url_shortener_notepad', textarea.value);
      });
    }

    function clearNotepad() {
      if (confirm("Are you sure you want to clear your scratchpad notes?")) {
        const textarea = document.getElementById('personalNotepadArea');
        if (textarea) textarea.value = '';
        localStorage.removeItem('url_shortener_notepad');
      }
    }

    function exportNotesMarkdown() {
      const textarea = document.getElementById('personalNotepadArea');
      const content = textarea ? textarea.value : '';
      if (!content.trim()) {
        alert("Your notepad is empty! Write some notes before exporting.");
        return;
      }
      const blob = new Blob([
        `# URL Shortener System Design - Personal Study Notes\\n\\n` + content
      ], { type: 'text/markdown;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'url_shortener_study_notes.md');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    // Interactive Simulator Logic (Slide 24)
    const BASE62_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    function encodeBase62(num) {
      if (num === 0) return "0";
      let s = "";
      while (num > 0) {
        s = BASE62_ALPHABET[num % 62] + s;
        num = Math.floor(num / 62);
      }
      return s;
    }

    function runShortenerSimulation() {
      const longUrl = document.getElementById('simLongUrl').value.trim();
      const algo = document.getElementById('simAlgorithm').value;
      const redirectType = document.getElementById('simRedirectType').value;
      const errBox = document.getElementById('simErrorBox');

      if (!longUrl || !longUrl.startsWith('http')) {
        errBox.style.display = 'block';
        errBox.textContent = "Please enter a valid HTTP/HTTPS destination URL.";
        return;
      }
      errBox.style.display = 'none';

      let shortSlug = "";
      let bitBreakdown = "";
      let latencyInfo = "";

      if (algo === 'snowflake') {
        const now = Date.now();
        const workerId = 123;
        const seq = Math.floor(Math.random() * 4000);
        // Snowflake synthetic integer
        const fakeSnowflake = (now % 100000000) * 10000 + (workerId * 10) + (seq % 10);
        shortSlug = encodeBase62(fakeSnowflake).padStart(6, '0').substring(0, 6);
        bitBreakdown = `[0 sign] | [41-bit Ts: ${now}] | [10-bit WorkerID: ${workerId}] | [12-bit Seq: ${seq.toString().padStart(4, '0')}]`;
        latencyInfo = `Generation Latency: 0.05 ms (Local Memory) &bull; DB Write: 2.8 ms &bull; Cache Set: 1.1 ms`;
      } else if (algo === 'sha1') {
        shortSlug = "9191c0";
        bitBreakdown = `SHA1('${longUrl}') &rarr; 40-char Hex &rarr; Substring(0, 6) &rarr; '9191c0' (from whiteboard!)`;
        latencyInfo = `SHA-1 Hash: 1.0 ms &bull; DB Collision Check: 5.2 ms &bull; Retry Cascade Penalty: = 16ms + 16ms`;
      } else { // redis counter
        const counterVal = 3748547;
        shortSlug = encodeBase62(counterVal);
        bitBreakdown = `Redis INCR url_global_counter &rarr; ${counterVal} &rarr; Base62 Division &rarr; '${shortSlug}'`;
        latencyInfo = `Redis INCR RPC: 2.4 ms &bull; Network Hop: 1.2 ms &bull; DB Write: 4.8 ms`;
      }

      // Update UI results
      document.getElementById('simShortUrlResult').textContent = `https://bit.ly/${shortSlug}`;
      document.getElementById('simBitBreakdown').textContent = bitBreakdown;
      document.getElementById('simLatencyResult').innerHTML = latencyInfo;

      // Update Wire Packets
      document.getElementById('simWireRequest').innerHTML = `<code>GET /${shortSlug} HTTP/1.1
Host: bit.ly
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml
Referer: https://twitter.com/</code>`;

      const cacheHeader = (redirectType === '301') ? 'Cache-Control: public, max-age=31536000' : 'Cache-Control: no-cache, no-store, must-revalidate';
      const statusLine = (redirectType === '301') ? 'HTTP/1.1 301 Moved Permanently' : 'HTTP/1.1 302 Found';

      document.getElementById('simWireResponse').innerHTML = `<code>${statusLine}
Location: ${longUrl}
${cacheHeader}
Date: ${new Date().toUTCString()}
X-Served-By: decrypt-worker-03 (Redis Cache Hit 1.8ms)</code>`;
    }

    function resetSimulator() {
      document.getElementById('simLongUrl').value = "https://www.facebook.com/anindya.s.dasgupta/";
      document.getElementById('simAlgorithm').value = "snowflake";
      document.getElementById('simRedirectType').value = "302";
      runShortenerSimulation();
    }

    // Quiz Evaluation Logic
    const QUIZ_ANSWERS = {
      q1: { ans: 'B', expl: "Correct! 62^7 = 3,521,614,606,208 (3.52 Trillion URLs). 62^6 is only 56.8 Billion." },
      q2: { ans: 'B', expl: "Correct! The lecture whiteboard specifically writes '= 16ms + 16ms' for the collision retry round-trip." },
      q3: { ans: 'B', expl: "Correct! The whiteboard designates 20% workload to Encryption servers and 80% to Decryption servers." },
      q4: { ans: 'B', expl: "Correct! 2^41 milliseconds divided by milliseconds in a year equals 69.73 years." },
      q5: { ans: 'B', expl: "Correct! Allocating worker IDs at boot eliminates runtime RPCs, allowing 4,096 IDs/ms locally." },
      q6: { ans: 'B', expl: "Correct! HTTP 302/307 ensures the browser contacts your servers on every click so you can emit Kafka analytics." },
      q7: { ans: 'B', expl: "Correct! A Bloom filter needs only 11.4 MB (often rounded to 5-11 MB) for 10M URLs with 1% false positive." },
      q8: { ans: 'B', expl: "Correct! Deleting millions of rows in a single query locks B-Tree pages, causing write/read starvation." },
      q9: { ans: 'B', expl: "Correct! Redis HyperLogLog (PFADD) counts unique visitors with 0.81% error in 12 KB memory." },
      q10: { ans: 'B', expl: "Correct! Levenshtein distance <= 2 identifies homograph typosquatting such as 'paypa1.com'." }
    };

    function evaluateQuiz() {
      let score = 0;
      const form = document.getElementById('quizForm');

      for (let i = 1; i <= 10; i++) {
        const qKey = 'q' + i;
        const selected = form[qKey] ? form[qKey].value : null;
        const feedbackEl = document.getElementById('feedback_' + i);
        const cardEl = document.getElementById('qCard_' + i);

        if (selected === QUIZ_ANSWERS[qKey].ans) {
          score++;
          feedbackEl.innerHTML = `<span style="color:#15803d; font-weight:700;">&#10003; Correct!</span> ${QUIZ_ANSWERS[qKey].expl}`;
          cardEl.style.borderColor = "#15803d";
        } else {
          feedbackEl.innerHTML = `<span style="color:var(--alert-red); font-weight:700;">&#10007; Incorrect.</span> ${QUIZ_ANSWERS[qKey].expl}`;
          cardEl.style.borderColor = "var(--alert-red)";
        }
        feedbackEl.style.display = 'block';
      }

      const scoreBanner = document.getElementById('quizScoreBanner');
      scoreBanner.style.display = 'block';
      scoreBanner.innerHTML = `🏆 Your Mastery Score: <strong>${score} / 10 (${score * 10}%)</strong> &bull; ${score >= 8 ? '🎉 PASS! Outstanding Senior System Design mastery!' : '⚠️ Review the slides and flashcards, then retry!'}`;
      scoreBanner.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    function initNavigation() {
      // Set initial presentation view
      jumpToSlide(1);
    }
  </script>
"""
