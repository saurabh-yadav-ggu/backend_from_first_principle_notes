# gen_slides_17_24.py - Slides 17 through 24
def get_slides_17_24():
    return """
        <!-- SLIDE 17: Base62 Encoding & Radix Arithmetic -->
        <article class="slide-wrapper" data-slide-index="16" data-category="Encoding">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 17 of 24</span>
              <span class="slide-topic-tag">Encoding Pipeline</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Base62 Encoding: Converting 64-bit Integers to Clean Web Slugs</h2>
            <p class="slide-intro">
              Why Base62 dominates URL shortening over Hex and Base64, and the exact radix-conversion algorithm.
            </p>

            <div class="grid grid-2" style="margin-bottom:1.5rem;">
              <div class="card card-blue">
                <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:0.75rem;">Why Base62? Character Space Comparison</h3>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:1rem;">
                  Computers store Snowflake IDs as 64-bit binary integers (e.g., <code>1537228672093888512</code>). Displaying a 19-digit number in an SMS or tweet wastes space. We encode it into an alphanumeric representation:
                </p>
                <div class="table-responsive">
                  <table class="sketch-table" style="font-size:0.85rem;">
                    <thead>
                      <tr>
                        <th>Encoding</th>
                        <th>Base</th>
                        <th>Alphabet Character Set</th>
                        <th>URL Safe?</th>
                        <th>Capacity at 7 chars</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>Hexadecimal</strong></td>
                        <td>16</td>
                        <td><code>0-9, a-f</code></td>
                        <td><span class="tag tag-green">Yes</span></td>
                        <td>$16^7 = 268.4\\text{ Million}$ (Too small!)</td>
                      </tr>
                      <tr>
                        <td><strong>Base64</strong></td>
                        <td>64</td>
                        <td><code>0-9, a-z, A-Z, +, /</code></td>
                        <td><span class="tag tag-red">No (+ and / need %-escaping)</span></td>
                        <td>$64^7 = 4.39\\text{ Trillion}$</td>
                      </tr>
                      <tr style="background:var(--highlighter-yellow);">
                        <td><strong>Base62 (Winner)</strong></td>
                        <td>62</td>
                        <td><code>0-9 (10) + a-z (26) + A-Z (26)</code></td>
                        <td><span class="tag tag-green">100% URL-Safe (No escaping)</span></td>
                        <td><strong>$62^7 = 3.52\\text{ Trillion}$ (Huge headroom!)</strong></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>

              <div class="card card-yellow">
                <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:0.75rem;">Radix-62 Conversion Arithmetic</h3>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:0.75rem;">
                  Base62 conversion is identical to converting base-10 decimal to binary, but using <strong>modulo 62</strong> division repeatedly:
                </p>
                <div class="code-box">
                  <div class="code-header">
                    <span class="code-lang">python &bull; base62_encoder.py</span>
                    <span class="tag tag-blue">O(log62 N)</span>
                  </div>
                  <pre><code>ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode_base62(num: int) -> str:
    if num == 0:
        return ALPHABET[0]
    chars = []
    while num > 0:
        num, rem = divmod(num, 62)
        chars.append(ALPHABET[rem])
    return "".join(reversed(chars))

def decode_base62(short_str: str) -> int:
    num = 0
    for char in short_str:
        num = num * 62 + ALPHABET.index(char)
    return num

# Example:
# Snowflake ID: 1537228672093888512 => '4kycpo' (from whiteboard!)</code></pre>
                </div>
              </div>
            </div>

            <!-- SVG Flow of Base62 Division -->
            <div class="sketch-diagram-box" style="margin-bottom:1.5rem;">
              <h4 class="sketch-heading" style="font-size:1rem; color:var(--ink-blue); margin-bottom:0.5rem;">Step-by-Step Remainder Mapping Flow</h4>
              <svg viewBox="0 0 850 140" width="100%" height="140" fill="none">
                <rect x="15" y="10" width="820" height="120" rx="8" fill="#FFFDF8" stroke="#0E2A5C" stroke-width="2" stroke-dasharray="6 3"/>
                
                <!-- Step 1 -->
                <rect x="35" y="30" width="150" height="75" rx="6" fill="#F4F1EA" stroke="#0E2A5C" stroke-width="2"/>
                <text x="110" y="55" text-anchor="middle" font-family="Lexend, sans-serif" font-size="12" font-weight="700" fill="#0E2A5C">Snowflake ID</text>
                <text x="110" y="75" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11" fill="#D12828">11,157</text>
                <text x="110" y="92" text-anchor="middle" font-family="Lexend, sans-serif" font-size="10" fill="#666">Input integer</text>

                <!-- Arrow 1 -->
                <path d="M 185 67 L 225 67" stroke="#0E2A5C" stroke-width="2" marker-end="url(#arrowhead)"/>
                <text x="205" y="60" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#0E2A5C">% 62</text>

                <!-- Step 2 -->
                <rect x="235" y="25" width="170" height="85" rx="6" fill="#FFFFA5" stroke="#0E2A5C" stroke-width="2"/>
                <text x="320" y="45" text-anchor="middle" font-family="Lexend, sans-serif" font-size="11" font-weight="700" fill="#0E2A5C">Divisions &amp; Remainders</text>
                <text x="320" y="63" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#0E2A5C">11157 % 62 = 59 ('x')</text>
                <text x="320" y="80" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#0E2A5C">179 % 62 = 55 ('t')</text>
                <text x="320" y="97" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#0E2A5C">2 % 62 = 2 ('2')</text>

                <!-- Arrow 2 -->
                <path d="M 405 67 L 445 67" stroke="#0E2A5C" stroke-width="2" marker-end="url(#arrowhead)"/>
                <text x="425" y="60" text-anchor="middle" font-family="Lexend, sans-serif" font-size="10" fill="#0E2A5C">Reverse</text>

                <!-- Step 3 -->
                <rect x="455" y="30" width="160" height="75" rx="6" fill="#F4F1EA" stroke="#0E2A5C" stroke-width="2"/>
                <text x="535" y="55" text-anchor="middle" font-family="Lexend, sans-serif" font-size="12" font-weight="700" fill="#0E2A5C">Reverse Order</text>
                <text x="535" y="75" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="13" font-weight="700" fill="#0E2A5C">['x', 't', '2']</text>
                <text x="535" y="92" text-anchor="middle" font-family="Lexend, sans-serif" font-size="10" fill="#D12828">&rarr; '2tx'</text>

                <!-- Arrow 3 -->
                <path d="M 615 67 L 655 67" stroke="#0E2A5C" stroke-width="2" marker-end="url(#arrowhead)"/>

                <!-- Step 4 Result -->
                <rect x="665" y="25" width="150" height="85" rx="6" fill="#d4f8d4" stroke="#0E2A5C" stroke-width="2"/>
                <text x="740" y="50" text-anchor="middle" font-family="Lexend, sans-serif" font-size="12" font-weight="700" fill="#0E2A5C">Clean Short URL</text>
                <text x="740" y="72" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="14" font-weight="700" fill="#0E2A5C">bit.ly/2tx</text>
                <text x="740" y="92" text-anchor="middle" font-family="Lexend, sans-serif" font-size="10" fill="#0E2A5C">&bull; 0 Ambiguity &bull;</text>
              </svg>
            </div>

            <div class="callout callout-tip">
              <div class="callout-title">💡 INTERVIEW MASTER TIP: Padding &amp; Shuffling for Obfuscation</div>
              <div class="callout-body">
                Sequential Snowflake IDs produce incremental short URLs. Competitors can scrape this to deduce your daily URL volume! In production, shorteners either <strong>pad with pseudo-random salt bits</strong> or use a <strong>shuffled Base62 alphabet permutation</strong> known only to the backend server to make consecutive IDs completely unpredictable.
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 18: Wire Redirects HTTP 301 vs 302 -->
        <article class="slide-wrapper" data-slide-index="17" data-category="Redirects">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 18 of 24</span>
              <span class="slide-topic-tag">Wire Protocol</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">HTTP 301 vs HTTP 302: The Critical Architecture Tradeoff</h2>
            <p class="slide-intro">
              Understanding client-side caching, server load reduction, and the sacrifice of analytics tracking.
            </p>

            <div class="grid grid-2" style="margin-bottom:1.5rem;">
              <!-- 301 MOVED PERMANENTLY -->
              <div class="card card-red">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                  <h3 class="sketch-heading" style="color:var(--alert-red); margin:0;">HTTP 301: Moved Permanently</h3>
                  <span class="tag tag-red">Browser Caches Indefinitely</span>
                </div>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:0.75rem;">
                  The browser caches the redirect mapping permanently in its local disk/memory cache.
                </p>
                <ul class="checklist" style="font-size:0.9rem; margin-bottom:1rem;">
                  <li><span class="check-icon">&#10003;</span> <strong>Server Load Reduced:</strong> Subsequent clicks never touch our servers or load balancers.</li>
                  <li><span class="check-icon">&#10003;</span> <strong>Fastest User Experience:</strong> Zero network round-trip latency to shortener on repeat visits.</li>
                  <li><span class="check-icon" style="color:var(--alert-red);">&#10007;</span> <strong>Zero Analytics:</strong> We CANNOT track click counts, user geolocation, or referrer after the first visit!</li>
                  <li><span class="check-icon" style="color:var(--alert-red);">&#10007;</span> <strong>Cannot Revoke or Expire:</strong> If the destination changes or URL expires, cached browsers keep redirecting to old URL.</li>
                </ul>
                <div class="code-box">
                  <div class="code-header">
                    <span class="code-lang">HTTP/1.1 301 Response Wire Trace</span>
                  </div>
                  <pre><code>HTTP/1.1 301 Moved Permanently
Location: https://www.facebook.com/anindya.s.dasgupta/
Cache-Control: public, max-age=31536000
Date: Mon, 19 Oct 2026 10:00:00 GMT</code></pre>
                </div>
              </div>

              <!-- 302 FOUND / 307 TEMPORARY -->
              <div class="card card-green">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                  <h3 class="sketch-heading" style="color:var(--ink-blue); margin:0;">HTTP 302 / 307: Found (Temporary)</h3>
                  <span class="tag tag-green">Industry Standard for Analytics</span>
                </div>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:0.75rem;">
                  The browser redirects immediately but does <em>not</em> cache the mapping permanently.
                </p>
                <ul class="checklist" style="font-size:0.9rem; margin-bottom:1rem;">
                  <li><span class="check-icon">&#10003;</span> <strong>100% Click Tracking:</strong> Every single click hits our decryption server, allowing precise analytics.</li>
                  <li><span class="check-icon">&#10003;</span> <strong>Full Expiration Control:</strong> When URL expires, we immediately return <code>410 Gone</code> without stale client caches.</li>
                  <li><span class="check-icon">&#10003;</span> <strong>Malware Revocation:</strong> We can instantly block malicious URLs reported by Safe Browsing.</li>
                  <li><span class="check-icon" style="color:var(--pencil-grey);">&#9888;</span> <strong>Higher Infrastructure Cost:</strong> All 80,000 read QPS must hit our edge load balancer and Redis cache.</li>
                </ul>
                <div class="code-box">
                  <div class="code-header">
                    <span class="code-lang">HTTP/1.1 302 Response Wire Trace</span>
                  </div>
                  <pre><code>HTTP/1.1 302 Found
Location: https://www.facebook.com/anindya.s.dasgupta/
Cache-Control: no-cache, no-store, must-revalidate
Date: Mon, 19 Oct 2026 10:00:00 GMT</code></pre>
                </div>
              </div>
            </div>

            <div class="callout callout-warning">
              <div class="callout-title">⚠️ WHITEBOARD VERBATIM VERDICT: Which one does Bitly use?</div>
              <div class="callout-body">
                <strong>Bitly uses HTTP 301 for pure URL redirection performance, but appends tracking cookies or query parameters on first visit!</strong> However, modern marketing URL shorteners (like Dub.co or TinyURL analytics tier) utilize <strong>HTTP 302 or 307</strong> because click analytics, geolocation telemetry, and real-time link editing are the core monetization features of paid shortener tiers.
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 19: Custom Vanity URLs -->
        <article class="slide-wrapper" data-slide-index="18" data-category="Edge Cases">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 19 of 24</span>
              <span class="slide-topic-tag">Custom Slugs</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Handling Custom Vanity URLs Without Race Conditions</h2>
            <p class="slide-intro">
              Supporting user-chosen slugs (e.g. <code>bit.ly/summer-sale</code>) while avoiding collisions and security loopholes.
            </p>

            <div class="grid grid-2" style="margin-bottom:1.5rem;">
              <div class="card card-blue">
                <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:0.75rem;">Vanity URL Business Logic &amp; Constraints</h3>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:1rem;">
                  A user may supply an optional <code>custom_alias</code> parameter in the <code>POST /api/v1/shorten</code> payload:
                </p>
                <ul class="checklist" style="font-size:0.9rem;">
                  <li><span class="check-icon">&#10003;</span> <strong>Length Constraints:</strong> Minimum 3 chars, maximum 30 characters (alphanumeric, dashes, underscores).</li>
                  <li><span class="check-icon">&#10003;</span> <strong>Reserved Word Blocklist:</strong> Never allow slugs matching routing paths: <code>api</code>, <code>admin</code>, <code>login</code>, <code>signup</code>, <code>healthz</code>, <code>docs</code>, <code>robots.txt</code>.</li>
                  <li><span class="check-icon">&#10003;</span> <strong>Namespace Isolation:</strong> Check global DB uniqueness index before insertion.</li>
                </ul>
              </div>

              <div class="card card-yellow">
                <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:0.75rem;">Atomic Database Reservation (Zero Race Condition)</h3>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:0.75rem;">
                  If two users concurrently request <code>bit.ly/black-friday</code> at the exact same millisecond:
                </p>
                <div class="code-box">
                  <div class="code-header">
                    <span class="code-lang">sql &bull; atomic_insert.sql</span>
                    <span class="tag tag-green">ACID Safe</span>
                  </div>
                  <pre><code>-- short_url has a UNIQUE B-Tree constraint!
INSERT INTO urls (
    id, short_url, long_url, user_id, is_custom, created_at, expires_at
) VALUES (
    1537228672093888512, 'black-friday', 'https://mystore.com/bf', 42, TRUE, NOW(), NOW() + INTERVAL '30 days'
)
ON CONFLICT (short_url) DO NOTHING;

-- If rows_affected == 0:
-- The server immediately aborts and returns:
-- HTTP 409 Conflict: {"error": "Alias 'black-friday' is already taken."}</code></pre>
                </div>
              </div>
            </div>

            <div class="callout callout-note">
              <div class="callout-title">📌 Whiteboard Note: URL Entity Table Mapping</div>
              <div class="callout-body">
                Notice how our Section 2 Entity Model in <code>image.png</code> specifically separated <code>shortURL</code> and <code>customURL</code> into the database schema! When <code>customURL</code> is populated, the encryption server skips Snowflake ID encoding entirely and directly registers the custom string into the B-Tree index.
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 20: Dual-Layer Expiration -->
        <article class="slide-wrapper" data-slide-index="19" data-category="Data Lifecycle">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 20 of 24</span>
              <span class="slide-topic-tag">Expiration</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Dual-Layer Expiration: Eliminating Zombie Records</h2>
            <p class="slide-intro">
              Why relying solely on Redis TTL or active scans will crash your database or leak expired links.
            </p>

            <div class="grid grid-2" style="margin-bottom:1.5rem;">
              <div class="card card-red">
                <h3 class="sketch-heading" style="color:var(--alert-red); margin-bottom:0.75rem;">The Flaw of Single-Layer Expiration</h3>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:1rem;">
                  Checking <code>expires_at &lt; NOW()</code> on every read or running massive DELETE queries causes fatal system failures:
                </p>
                <ul class="checklist" style="font-size:0.9rem;">
                  <li><span class="check-icon" style="color:var(--alert-red);">&#10007;</span> <strong>Redis Eviction Failure:</strong> Redis is only a cache. If an expired link isn't in Redis, a query falls back to Postgres. Expired links stay live forever!</li>
                  <li><span class="check-icon" style="color:var(--alert-red);">&#10007;</span> <strong>Massive DELETE Locks:</strong> Running <code>DELETE FROM urls WHERE expires_at &lt; NOW()</code> locks the B-Tree table, halting reads and writes for minutes!</li>
                </ul>
              </div>

              <div class="card card-green">
                <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:0.75rem;">The Production Dual-Layer Architecture</h3>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:0.75rem;">
                  We combine <strong>Lazy Passive Expiration</strong> with <strong>Asynchronous Chunked Batch Cleanup</strong>:
                </p>
                <div class="table-responsive">
                  <table class="sketch-table" style="font-size:0.85rem;">
                    <thead>
                      <tr>
                        <th>Layer</th>
                        <th>Mechanism</th>
                        <th>Latency / Load</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>Layer 1: Lazy (Inline)</strong></td>
                        <td>On cache/DB hit, check <code>expires_at &lt; now()</code>. If expired, return <code>410 Gone</code> and trigger async delete.</td>
                        <td>0 ms extra latency. Zero dead links served.</td>
                      </tr>
                      <tr>
                        <td><strong>Layer 2: Daily Cron (Batch)</strong></td>
                        <td>Off-peak scheduled job (2:00 AM) deletes expired rows in chunked limits of 5,000 using keyset pagination.</td>
                        <td>Prevents table lock. Reclaims disk space and shrinks B-Tree indices.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

            <div class="card" style="margin-bottom:1.5rem;">
              <h4 class="sketch-heading" style="font-size:1.05rem; color:var(--ink-blue); margin-bottom:0.75rem;">Production Nightly Cron Job (Chunked Keyset Deletion)</h4>
              <div class="code-box">
                <div class="code-header">
                  <span class="code-lang">python &bull; cron_expire_cleaner.py (Runs daily at 02:00 UTC)</span>
                  <span class="tag tag-yellow">Non-blocking Batch Loop</span>
                </div>
                <pre><code>import time
from sqlalchemy import text

BATCH_SIZE = 5000

def purge_expired_urls(db_engine):
    total_purged = 0
    while True:
        query = text('''
            DELETE FROM urls 
            WHERE id IN (
                SELECT id FROM urls 
                WHERE expires_at IS NOT NULL AND expires_at < NOW() 
                LIMIT :batch_size
            )
        ''')
        with db_engine.begin() as conn:
            result = conn.execute(query, {"batch_size": BATCH_SIZE})
            rows_deleted = result.rowcount
            total_purged += rows_deleted
            if rows_deleted < BATCH_SIZE:
                break
        time.sleep(0.1) # Sleep 100ms between batches to unblock user queries!
    print(f"Purged {total_purged} expired URLs.")</code></pre>
              </div>
            </div>

            <div class="callout callout-tip">
              <div class="callout-title">💡 HTTP 410 GONE VS HTTP 404 NOT FOUND</div>
              <div class="callout-body">
                When a user clicks an expired link, return <strong>HTTP 410 Gone</strong> instead of <strong>HTTP 404 Not Found</strong>. 410 explicitly tells search engine crawlers and browsers that the link intentionally expired and will never return, prompting immediate de-indexing from search engines.
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 21: Bloom Filters & Cache Penetration -->
        <article class="slide-wrapper" data-slide-index="20" data-category="Caching">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 21 of 24</span>
              <span class="slide-topic-tag">High-Perf Caching</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Bloom Filters: Shielding DB from Malicious Cache Penetration</h2>
            <p class="slide-intro">
              How a tiny 11.4MB probabilistic bit array stops 99% of invalid redirect requests from crashing PostgreSQL.
            </p>

            <div class="grid grid-2" style="margin-bottom:1.5rem;">
              <div class="card card-red">
                <h3 class="sketch-heading" style="color:var(--alert-red); margin-bottom:0.75rem;">The Cache Penetration Vulnerability (DDoS Attack)</h3>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:0.75rem;">
                  Suppose an attacker hammers our service with 100,000 QPS of random, non-existent short URLs (e.g. <code>bit.ly/xxxx999</code>):
                </p>
                <ol style="font-size:0.9rem; padding-left:1.25rem; line-height:1.6; color:var(--pencil-grey); margin-bottom:1rem;">
                  <li><strong>Redis Cache MISS:</strong> The random slug does not exist in Redis (2ms).</li>
                  <li><strong>PostgreSQL DB PENETRATION:</strong> The request bypasses cache and queries the DB disk B-Tree index (10ms).</li>
                  <li><strong>Database Overload:</strong> 80,000 queries/sec saturate DB connection pools and disk I/O, crashing the primary cluster!</li>
                </ol>
              </div>

              <div class="card card-blue">
                <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:0.75rem;">The Bloom Filter Solution: Probabilistic Gatekeeper</h3>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:0.75rem;">
                  A Bloom Filter is a space-efficient bit array that can definitively state:
                </p>
                <div style="background:#FFF; padding:0.75rem; border:1.5px solid var(--ink-blue); border-radius:6px; margin-bottom:0.75rem;">
                  <div style="color:var(--alert-red); font-weight:700; font-size:0.9rem;">&bull; "Item is definitely NOT in DB" &rarr; 100% Guaranteed!</div>
                  <div style="color:var(--ink-blue); font-weight:700; font-size:0.9rem; margin-top:0.25rem;">&bull; "Item MIGHT be in DB" &rarr; &le; 1% False Positive Rate.</div>
                </div>
                <ul class="checklist" style="font-size:0.85rem;">
                  <li><span class="check-icon">&#10003;</span> For 10,000,000 URLs with 1% false-positive probability ($p=0.01$):</li>
                  <li><span class="check-icon">&#10003;</span> Bits required: $m = -\\frac{n \\ln p}{(\\ln 2)^2} \\approx \\mathbf{11.4\\text{ MB}}$.</li>
                  <li><span class="check-icon">&#10003;</span> Entire bit array lives in <strong>L3 CPU cache</strong> or Redis cluster via <code>BF.EXISTS</code>!</li>
                </ul>
              </div>
            </div>

            <div class="callout callout-tip">
              <div class="callout-title">💡 REDIS MODULE INTEGRATION: RedisBloom</div>
              <div class="callout-body">
                In modern infrastructure, Redis provides native C-speed Bloom Filters via the <code>RedisBloom</code> extension. Commands: <code>BF.RESERVE urls_bf 0.01 10000000</code>, <code>BF.ADD urls_bf "4kycpo"</code>, and <code>BF.EXISTS urls_bf "fake_slug"</code> execute in sub-millisecond time.
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 22: Async Analytics & Kafka -->
        <article class="slide-wrapper" data-slide-index="21" data-category="Analytics">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 22 of 24</span>
              <span class="slide-topic-tag">Analytics Decoupling</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Asynchronous Click Analytics: Decoupling via Apache Kafka</h2>
            <p class="slide-intro">
              Recording millions of click events, user-agents, and geolocations with zero redirect latency impact.
            </p>

            <div class="grid grid-2" style="margin-bottom:1.5rem;">
              <div class="card card-red">
                <h3 class="sketch-heading" style="color:var(--alert-red); margin-bottom:0.75rem;">Why Synchronous DB Logging Fails</h3>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:1rem;">
                  If the Decryption Server writes a click row into PostgreSQL before returning the <code>302 Redirect</code> response:
                </p>
                <ul class="checklist" style="font-size:0.9rem;">
                  <li><span class="check-icon" style="color:var(--alert-red);">&#10007;</span> <strong>Redirect Latency Doubles:</strong> Redirect time spikes from 2ms to 20ms+, directly degrading user experience.</li>
                  <li><span class="check-icon" style="color:var(--alert-red);">&#10007;</span> <strong>Database Write Bottleneck:</strong> 80,000 read QPS turns into <strong>80,000 DB INSERT/s</strong>. PostgreSQL disk IOPS instantly collapses.</li>
                </ul>
              </div>

              <div class="card card-green">
                <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:0.75rem;">The Asynchronous Event Streaming Architecture</h3>
                <p style="font-size:0.95rem; line-height:1.6; margin-bottom:0.75rem;">
                  The Decryption Server emits a lightweight JSON message to an <strong>Apache Kafka</strong> topic in memory via non-blocking I/O (fire-and-forget, &lt; 0.5ms) and immediately returns the <code>302 Location</code> header to the browser!
                </p>
                <div class="code-box">
                  <div class="code-header">
                    <span class="code-lang">json &bull; Kafka ClickEvent Payload</span>
                  </div>
                  <pre><code>{
  "short_url": "4kycpo",
  "timestamp": 1792410800123,
  "ip_address": "203.0.113.195",
  "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4)",
  "country": "US",
  "referrer": "https://t.co/"
}</code></pre>
                </div>
              </div>
            </div>

            <div class="callout callout-tip">
              <div class="callout-title">💡 ALGORITHMIC GEM: HyperLogLog for Unique Visitors</div>
              <div class="callout-body">
                How do you count 100 million unique visitors on a short link without storing 100M IP addresses? Use <strong>Redis HyperLogLog (HLL)</strong> via <code>PFADD url:4kycpo:uniques &lt;IP&gt;</code>! It estimates unique visitor counts with a standard error of <strong>0.81%</strong> while consuming only <strong>12 KB of fixed memory per URL</strong>!
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 23: Security & Abuse Prevention -->
        <article class="slide-wrapper" data-slide-index="22" data-category="Security">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 23 of 24</span>
              <span class="slide-topic-tag">Security &amp; Abuse</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Security &amp; Abuse Prevention: Stopping Malware &amp; Spammers</h2>
            <p class="slide-intro">
              Multi-tier defense: Token bucket rate limiting, Google Safe Browsing, and Levenshtein phishing heuristics.
            </p>

            <div class="grid grid-3" style="margin-bottom:1.5rem;">
              <div class="card card-yellow">
                <span class="tag tag-blue" style="margin-bottom:0.5rem;">LAYER 1</span>
                <h3 class="sketch-heading" style="color:var(--ink-blue); font-size:1rem; margin-bottom:0.5rem;">IP Rate Limiting</h3>
                <ul class="checklist" style="font-size:0.8rem; line-height:1.4;">
                  <li><span class="check-icon">&#10003;</span> <strong>100 requests/hour</strong> per client IP address.</li>
                  <li><span class="check-icon">&#10003;</span> Redis Sliding Window Counter at Load Balancer.</li>
                  <li><span class="check-icon">&#10003;</span> Returns <code>HTTP 429 Too Many Requests</code>.</li>
                </ul>
              </div>

              <div class="card card-red">
                <span class="tag tag-red" style="margin-bottom:0.5rem;">LAYER 2</span>
                <h3 class="sketch-heading" style="color:var(--alert-red); font-size:1rem; margin-bottom:0.5rem;">Malware &amp; Phishing</h3>
                <ul class="checklist" style="font-size:0.8rem; line-height:1.4;">
                  <li><span class="check-icon">&#10003;</span> Async lookup against <strong>Google Safe Browsing API</strong>.</li>
                  <li><span class="check-icon">&#10003;</span> Check against URLhaus &amp; PhishTank bloom filters.</li>
                  <li><span class="check-icon">&#10003;</span> If flagged, immediately disable redirect.</li>
                </ul>
              </div>

              <div class="card card-blue">
                <span class="tag tag-green" style="margin-bottom:0.5rem;">LAYER 3</span>
                <h3 class="sketch-heading" style="color:var(--ink-blue); font-size:1rem; margin-bottom:0.5rem;">Homograph Defense</h3>
                <ul class="checklist" style="font-size:0.8rem; line-height:1.4;">
                  <li><span class="check-icon">&#10003;</span> Calculate <strong>Levenshtein Edit Distance &le; 2</strong> against top domains.</li>
                  <li><span class="check-icon">&#10003;</span> Detects: <code>paypa1.com</code> vs <code>paypal.com</code>.</li>
                  <li><span class="check-icon">&#10003;</span> Interstitial warning page before redirect!</li>
                </ul>
              </div>
            </div>

            <div class="callout callout-warning">
              <div class="callout-title">⚠️ THE "INTERSTITIAL WARNING" PATTERN</div>
              <div class="callout-body">
                If a destination URL was flagged by machine-learning heuristics with moderate suspicion, our Decryption Server does not return a direct <code>302 Redirect</code>. Instead, it renders an <strong>Interstitial Warning Screen</strong>: <em>"You are leaving Bitly to visit an unverified website: paypa1.com. Are you sure you want to proceed?"</em> with an explicit click-through requirement.
              </div>
            </div>
          </div>
        </article>

        <!-- SLIDE 24: Live Simulator & Wire Inspector -->
        <article class="slide-wrapper" data-slide-index="23" data-category="Lab">
          <div class="slide-card tape-top">
            <div class="slide-meta-row">
              <span class="slide-step-badge">Slide 24 of 24</span>
              <span class="slide-topic-tag">Interactive Lab</span>
              <button class="slide-bookmark-btn" onclick="toggleBookmarkCurrentSlide()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                <span class="bm-text">Bookmark</span>
              </button>
            </div>

            <h2 class="slide-title">Interactive System Simulator: Wire Inspector &amp; Hash Engine</h2>
            <p class="slide-intro">
              Generate real Snowflake IDs, convert to Base62, inspect HTTP wire packets, and simulate redirect latencies.
            </p>

            <div class="grid grid-2" style="margin-bottom:1.5rem;">
              <!-- SIMULATOR CONTROLS -->
              <div class="card card-yellow">
                <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:0.75rem;">1. URL Generation &amp; Encoding Lab</h3>
                <div style="margin-bottom:1rem;">
                  <label style="display:block; font-family:Lexend, sans-serif; font-weight:700; font-size:0.85rem; color:var(--ink-blue); margin-bottom:0.25rem;">
                    Long Destination URL:
                  </label>
                  <input type="text" id="simLongUrl" value="https://www.facebook.com/anindya.s.dasgupta/" class="sketch-input" style="width:100%; font-family:JetBrains Mono, monospace; font-size:0.85rem; padding:0.5rem; border:2px solid var(--ink-blue); border-radius:6px; background:#FFF;">
                </div>

                <div class="grid grid-2" style="gap:0.75rem; margin-bottom:1rem;">
                  <div>
                    <label style="display:block; font-family:Lexend, sans-serif; font-weight:700; font-size:0.85rem; color:var(--ink-blue); margin-bottom:0.25rem;">
                      Generator Mode:
                    </label>
                    <select id="simAlgorithm" class="sketch-input" style="width:100%; font-family:Lexend, sans-serif; font-size:0.85rem; padding:0.45rem; border:2px solid var(--ink-blue); border-radius:6px; background:#FFF;">
                      <option value="snowflake">Approach 3: Snowflake ID (Production)</option>
                      <option value="sha1">Approach 1: SHA-1 Hash (Legacy)</option>
                      <option value="redis">Approach 2: Redis Counter (Atomic)</option>
                    </select>
                  </div>
                  <div>
                    <label style="display:block; font-family:Lexend, sans-serif; font-weight:700; font-size:0.85rem; color:var(--ink-blue); margin-bottom:0.25rem;">
                      Redirect Wire Protocol:
                    </label>
                    <select id="simRedirectType" class="sketch-input" style="width:100%; font-family:Lexend, sans-serif; font-size:0.85rem; padding:0.45rem; border:2px solid var(--ink-blue); border-radius:6px; background:#FFF;">
                      <option value="302">HTTP 302 Found (Analytics Tracked)</option>
                      <option value="301">HTTP 301 Moved (Browser Cached)</option>
                    </select>
                  </div>
                </div>

                <div style="display:flex; gap:0.5rem;">
                  <button class="deck-nav-btn primary" onclick="runShortenerSimulation()" style="flex:1;">
                    <span>&uarr; Run Pipeline Simulation</span>
                  </button>
                  <button class="deck-nav-btn" onclick="resetSimulator()">
                    <span>Reset</span>
                  </button>
                </div>

                <div id="simErrorBox" style="display:none; margin-top:0.75rem; padding:0.5rem; background:#fee2e2; border:1px solid #ef4444; border-radius:4px; color:#b91c1c; font-size:0.85rem;"></div>
              </div>

              <!-- GENERATED OUTPUT INSPECTOR -->
              <div class="card card-blue">
                <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:0.75rem;">2. Live Pipeline Artifacts</h3>
                <div style="display:flex; flex-direction:column; gap:0.75rem;">
                  <div style="background:#FFF; padding:0.65rem; border:1.5px solid var(--ink-blue); border-radius:6px;">
                    <div style="font-size:0.75rem; font-weight:700; color:var(--pencil-light); text-transform:uppercase;">Resulting Short URL</div>
                    <div id="simShortUrlResult" style="font-family:JetBrains Mono, monospace; font-size:1.15rem; font-weight:700; color:var(--alert-red); margin-top:0.25rem;">
                      https://bit.ly/4kycpo
                    </div>
                  </div>

                  <div style="background:#FFF; padding:0.65rem; border:1.5px solid var(--ink-blue); border-radius:6px;">
                    <div style="font-size:0.75rem; font-weight:700; color:var(--pencil-light); text-transform:uppercase;">64-bit Snowflake Bit Layout Breakdown</div>
                    <div id="simBitBreakdown" style="font-family:JetBrains Mono, monospace; font-size:0.8rem; color:var(--ink-blue); margin-top:0.25rem; word-break:break-all;">
                      [0] (Sign) | [41-bit Ts: 1792410800000] | [10-bit Worker: 123] | [12-bit Seq: 001]
                    </div>
                  </div>

                  <div style="background:#FFF; padding:0.65rem; border:1.5px solid var(--ink-blue); border-radius:6px;">
                    <div style="font-size:0.75rem; font-weight:700; color:var(--pencil-light); text-transform:uppercase;">Latency Simulation</div>
                    <div id="simLatencyResult" style="font-family:JetBrains Mono, monospace; font-size:0.85rem; color:var(--ink-blue); margin-top:0.25rem;">
                      Write Latency: <strong>3.2 ms</strong> &bull; Read Latency: <strong>1.8 ms</strong> (Redis Hit)
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- HTTP WIRE PACKET INSPECTOR -->
            <div class="card card-yellow" style="margin-bottom:1.5rem;">
              <h3 class="sketch-heading" style="color:var(--ink-blue); margin-bottom:0.75rem;">3. HTTP Protocol Wire Inspector</h3>
              <div class="grid grid-2" style="gap:1rem;">
                <div>
                  <div style="font-size:0.8rem; font-weight:700; color:var(--ink-blue); margin-bottom:0.25rem;">Request Wire Packet (Client &rarr; Server)</div>
                  <div class="code-box" style="margin-bottom:0;">
                    <pre id="simWireRequest"><code>GET /4kycpo HTTP/1.1
Host: bit.ly
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml
Referer: https://twitter.com/</code></pre>
                  </div>
                </div>

                <div>
                  <div style="font-size:0.8rem; font-weight:700; color:var(--ink-blue); margin-bottom:0.25rem;">Response Wire Packet (Server &rarr; Client)</div>
                  <div class="code-box" style="margin-bottom:0;">
                    <pre id="simWireResponse"><code>HTTP/1.1 302 Found
Location: https://www.facebook.com/anindya.s.dasgupta/
Cache-Control: no-cache, no-store, must-revalidate
Date: Mon, 19 Oct 2026 10:00:00 GMT
X-Served-By: decrypt-worker-03</code></pre>
                  </div>
                </div>
              </div>
            </div>

            <div class="callout callout-note">
              <div class="callout-title">🎉 CONGRATULATIONS! You have mastered the URL Shortener System Design</div>
              <div class="callout-body">
                You have now covered every theoretical, mathematical, architectural, and edge-case aspect of designing a web-scale URL shortener. Switch to <strong>Reader View</strong> for continuous textbook reading, <strong>Revision View</strong> for interview cheat sheets, <strong>Flashcards</strong> for spaced repetition recall, or test your mastery with the <strong>10-Question Certification Quiz</strong>!
              </div>
            </div>
          </div>
        </article>
    """
