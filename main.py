import os
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

# Initialize FastAPI app
app = FastAPI(
    title="Backend Notes API",
    description="FastAPI Backend for 'Backend from First Principles' Course Notes, Curriculum, and Chapter Transcripts",
    version="1.0.0"
)

# Enable CORS for local development and frontend clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files directory (CSS, JS, images)
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Initialize Jinja2 templates directory
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Pydantic Models
class Chapter(BaseModel):
    id: int
    title: str
    category: str
    folder: str
    summary: str
    takeaways: List[str]
    has_transcript: bool = False
    has_interactive_notes: bool = False
    status: str = "upcoming"  # 'completed', 'in_progress', 'upcoming'

class PlaylistInfo(BaseModel):
    title: str
    creator: str
    playlist_id: str
    playlist_url: str
    total_chapters: int

# Full 30-Chapter Curriculum from Sriniously's "Backend from First Principles" Playlist
PLAYLIST_INFO = PlaylistInfo(
    title="Backend from First Principles",
    creator="K Srinivas Rao (Sriniously)",
    playlist_id="PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1",
    playlist_url="https://youtube.com/playlist?list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1&si=2rctmwtew8ThcJnU",
    total_chapters=30
)

# System Design Curriculum (High-Scale Case Studies & Distributed Systems)
SYSTEM_DESIGN_INFO = PlaylistInfo(
    title="System Design from First Principles",
    creator="System Architecture First Principles",
    playlist_id="system-design-first-principles",
    playlist_url="https://youtube.com/playlist?list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1",
    total_chapters=12
)

SYSTEM_DESIGN_CHAPTERS_DB: List[Chapter] = [
    Chapter(
        id=1,
        title="Design a URL Shortener (TinyURL / Bitly)",
        category="case_study",
        folder="url_shortener",
        summary="Architecting a high-throughput, read-heavy URL shortener capable of generating compact unique aliases and redirecting millions of daily users. In-depth breakdown of Base62 encoding, Key Generation Service (KGS), 301 vs 302 redirect HTTP semantics, Redis cache-aside caching, database indexing & sharding, and collision mitigation.",
        takeaways=[
            "Base62 encoding (62^7 ≈ 3.52 Trillion URLs) vs MD5/SHA-256 hash truncation",
            "HTTP 301 (Permanent / Browser Cached) vs HTTP 302 (Temporary / Server Tracked Analytics)",
            "100:1 Read-to-Write traffic asymmetry & multi-tier Redis Cache-Aside sizing",
            "Database partitioning by Hash(short_key) % N and KGS pre-allocated key ranges"
        ],
        has_transcript=True,
        has_interactive_notes=True,
        status="completed"
    ),
    Chapter(
        id=2,
        title="Scale from Zero to Millions of Users",
        category="fundamentals",
        folder="scale_zero_to_millions",
        summary="Systematic evolution from a monolithic single server setup to horizontal scaling: DNS Anycast, stateless web tiers, database replication, multi-datacenter failover, and CDN edge caching.",
        takeaways=["Vertical vs Horizontal scaling trade-offs", "Stateless tier decoupling for auto-scaling", "Multi-region active-active deployment"],
        status="upcoming"
    ),
    Chapter(
        id=3,
        title="Consistent Hashing & Distributed Caching",
        category="caching",
        folder="consistent_hashing",
        summary="Resolving the hot-spot hash rehashing problem with consistent hashing rings, virtual nodes, cache-aside vs write-through patterns, and cache stampede mitigation.",
        takeaways=["Virtual nodes for uniform load distribution", "Cache stampede & dog-piling prevention", "LRU/LFU eviction in memory clusters"],
        status="upcoming"
    ),
    Chapter(
        id=4,
        title="Design a Distributed Rate Limiter",
        category="system",
        folder="rate_limiter",
        summary="Throttling abuse at the API gateway layer using Token Bucket, Leaky Bucket, Sliding Window Log, and distributed Redis synchronization via Lua scripts.",
        takeaways=["Token Bucket vs Sliding Window Counter", "Race conditions & atomic Redis Lua execution", "HTTP 429 Too Many Requests response envelope"],
        status="upcoming"
    ),
    Chapter(
        id=5,
        title="Database Sharding & Partitioning Strategies",
        category="data",
        folder="database_sharding",
        summary="Scaling relational storage horizontally: range-based vs hash-based sharding, join bottlenecks, distributed transactions (2PC/Saga), and schema migration at scale.",
        takeaways=["Choosing the optimal shard key", "Resharding & data migration with zero downtime", "Cross-shard joins & scatter-gather queries"],
        status="upcoming"
    ),
    Chapter(
        id=6,
        title="Message Queues & Event-Driven Architecture",
        category="system",
        folder="message_queues",
        summary="Decoupling services with high-throughput distributed commit logs: Kafka partitions, consumer groups, offset commits, at-least-once vs exactly-once semantics.",
        takeaways=["Log partitions and consumer group parallelism", "Idempotent consumer message processing", "Dead-letter queues and poison pill isolation"],
        status="upcoming"
    ),
    Chapter(
        id=7,
        title="Design a Distributed Key-Value Store",
        category="data",
        folder="distributed_kv_store",
        summary="Building Dynamo-style decentralized storage: CAP theorem trade-offs, vector clocks, quorum consensus (N, R, W), and hinted handoff.",
        takeaways=["Sloppy quorum & hinted handoff", "Vector clocks for concurrent conflict resolution", "SSTables & LSM Trees write path"],
        status="upcoming"
    ),
    Chapter(
        id=8,
        title="Design a Distributed Notification Service",
        category="system",
        folder="notification_service",
        summary="Building multi-channel push notification pipelines: mobile APNs/FCM, SMS, email gateways, rate limiting, and prioritized worker queues.",
        takeaways=["De-duplication mechanisms across delivery retries", "Priority queues for transactional vs marketing alerts", "Vendor gateway fallback routing"],
        status="upcoming"
    ),
    Chapter(
        id=9,
        title="Design a News Feed System (Twitter / Facebook)",
        category="case_study",
        folder="news_feed",
        summary="Architecting timeline generation: Fan-out on write (push model) vs Fan-out on read (pull model), hybrid celebrity fan-out, and Redis timeline caching.",
        takeaways=["Push model vs Pull model trade-offs", "Celebrity user fan-out mitigation", "Multi-tiered feed ranking & caching"],
        status="upcoming"
    ),
    Chapter(
        id=10,
        title="Design a Distributed Web Crawler",
        category="case_study",
        folder="web_crawler",
        summary="Scraping billions of web pages: URL frontier, politeness delays, DNS caching, content-seen duplicate detection with Bloom Filters, and distributed workers.",
        takeaways=["Bloom filters for billion-URL set membership", "Politeness & priority queues", "Robust HTML parsing & dead-loop traps"],
        status="upcoming"
    ),
    Chapter(
        id=11,
        title="Design a Real-Time Chat System (WhatsApp / Discord)",
        category="case_study",
        folder="chat_system",
        summary="Bi-directional real-time communication: WebSocket connection managers, presence servers, group message fan-out, and message sequencing with Snowflakes.",
        takeaways=["Maintaining persistent WebSocket connections at scale", "Distributed presence tracking with Redis heartbeats", "Message ordering across partitions"],
        status="upcoming"
    ),
    Chapter(
        id=12,
        title="Design a Video Streaming Platform (YouTube / Netflix)",
        category="case_study",
        folder="video_streaming",
        summary="Massive media delivery: distributed video transcoding DAGs, Adaptive Bitrate Streaming (HLS/DASH), multi-tier CDN edge caching, and DRM encryption.",
        takeaways=["Video chunking & parallel transcoding pipelines", "Adaptive bitrate switching mechanics", "CDN peering & origin shielding"],
        status="upcoming"
    )
]

# Java & JVM Curriculum (First Principles, Low-Level Runtime, Memory & Concurrency)
JAVA_NOTES_INFO = PlaylistInfo(
    title="Java & JVM from First Principles",
    creator="JVM Architecture & Systems Engineering",
    playlist_id="java-notes-first-principles",
    playlist_url="https://youtube.com/playlist?list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1",
    total_chapters=15
)

JAVA_NOTES_CHAPTERS_DB: List[Chapter] = [
    Chapter(
        id=1,
        title="JVM Architecture & Runtime Memory Model",
        category="jvm",
        folder="jvm_architecture",
        summary="Deconstructing the Java Virtual Machine: ClassLoader subsystem (Load, Link, Initialize), Execution Engine (Interpreter, Tiered JIT C1/C2, Garbage Collector), and Runtime Data Areas (Heap, Metaspace, Stack Frames, PC Registers, Native Stacks).",
        takeaways=[
            "Heap (Young Eden/Survivor vs Old Tenured) vs Non-Heap Metaspace (Native OS memory)",
            "Stack Frame anatomy: Local Variable Array, Operand Stack, and Frame Data",
            "Interpreter vs JIT Tiered Compilation (C1 Client with OSR vs C2 Server optimizing compiler)",
            "Compressed OOPs (Ordinary Object Pointers) and 32GB heap threshold"
        ],
        has_transcript=True,
        has_interactive_notes=True,
        status="completed"
    ),
    Chapter(
        id=2,
        title="ClassLoader Subsystem & Bytecode Verification",
        category="jvm",
        folder="classloader_subsystem",
        summary="How Java loads `.class` files into runtime memory: Delegation hierarchy (Bootstrap, Platform, Application), Custom ClassLoaders, bytecode verification security passes, and ClassNotFoundException vs NoClassDefFoundError.",
        takeaways=[
            "Parent delegation principle and classpath shadowing",
            "Bytecode 4-pass verification (Type safety, stack boundary proofs)",
            "Dynamic class unloading when ClassLoader instance becomes unreachable"
        ],
        status="upcoming"
    ),
    Chapter(
        id=3,
        title="Java Memory Model (JMM) & volatile Internals",
        category="concurrency",
        folder="java_memory_model",
        summary="Understanding hardware cache lines, CPU store buffers, and JMM Happens-Before ordering. Hardware memory barriers (LoadLoad, LoadStore, StoreStore, StoreLoad) and why volatile prevents instruction reordering and forces cache coherence (MESI).",
        takeaways=[
            "CPU cache coherence (MESI protocol) & store buffer latency",
            "Happens-Before formal guarantees and memory fences (MFENCE)",
            "Volatile write: StoreStore + StoreLoad fence emission in assembly"
        ],
        status="upcoming"
    ),
    Chapter(
        id=4,
        title="Concurrency: Locks, Synchronized & AQS",
        category="concurrency",
        folder="locks_and_aqs",
        summary="Deep dive into Java thread synchronization: Object header Mark Word state, synchronized monitor lock inflation (Biased -> Thin/Spinlock -> Fat/OS Mutex), and AbstractQueuedSynchronizer (AQS) FIFO state queue behind ReentrantLock and CountDownLatch.",
        takeaways=[
            "Mark Word bits: 01 (Unlock/Biased) -> 00 (Lightweight) -> 10 (Heavyweight OS Mutex)",
            "AQS state `volatile int state` and lock-free CAS enqueueing",
            "Fair vs Non-Fair lock acquisition throughput trade-offs"
        ],
        status="upcoming"
    ),
    Chapter(
        id=5,
        title="Virtual Threads & Project Loom (Java 21)",
        category="concurrency",
        folder="virtual_threads",
        summary="Next-generation high-throughput concurrency: 1:1 OS platform threads vs M:N Virtual Threads. Continuation stacks mounted on Carrier Threads (`ForkJoinPool`), unblocking 1,000,000+ concurrent network connections with synchronous blocking syntax.",
        takeaways=[
            "Platform OS thread (~1MB stack) vs Virtual Thread (~few KB continuation chunk)",
            "Yielding & parking continuations on socket read/write non-blocking calls",
            "Thread pinning hazards (synchronized blocks vs ReentrantLock)"
        ],
        status="upcoming"
    ),
    Chapter(
        id=6,
        title="Garbage Collection Deep Dive: G1, ZGC & Shenandoah",
        category="jvm",
        folder="garbage_collection",
        summary="Generational hypothesis, stop-the-world (STW) pauses, card tables & remember sets, and low-latency collectors. G1 region mixed collections vs ZGC colored pointers and load barriers enabling sub-millisecond pauses on terabyte heaps.",
        takeaways=[
            "Weak Generational Hypothesis: 95%+ objects die young in Eden",
            "G1 Regional heap, humongous objects, and target pause time prediction",
            "ZGC colored pointer reference bits & concurrent load barrier self-healing"
        ],
        status="upcoming"
    ),
    Chapter(
        id=7,
        title="Java Database Connectivity (JDBC) from Scratch",
        category="frameworks",
        folder="java_jdbc",
        summary="Connecting raw Java to relational databases: Type 4 Drivers, DriverManager, Connection, Statement vs PreparedStatement, SQL Injection mechanics, ResultSet cursor navigation, try-with-resources, Transactions (commit/rollback), and HikariCP connection pooling.",
        takeaways=[
            "Type 4 pure Java network socket driver & java.sql.* interface polymorphism",
            "PreparedStatement precompilation & parameter isolation eliminating SQL Injection",
            "ResultSet 1-based indexing & cursor traversal lifecycle (beforeFirst to afterLast)",
            "Manual ACID transactions: setAutoCommit(false), commit(), and rollback()"
        ],
        has_transcript=True,
        has_interactive_notes=True,
        status="completed"
    ),
    Chapter(
        id=8,
        title="Collections Internals: HashMap & ConcurrentHashMap",
        category="collections",
        folder="collections_internals",
        summary="Under the hood of `java.util`: HashMap array of bins, bitwise hash spreading `(h ^ (h >>> 16)) & (n - 1)`, collision resolution, treeification to Red-Black Tree at 8 entries, and ConcurrentHashMap striped bin lock-free CAS updates.",
        takeaways=[
            "Power-of-two table sizing and bitwise modulo index calculation",
            "Treeify threshold = 8, untreeify = 6, and Poisson distribution proof",
            "ConcurrentHashMap: `Node` volatile value, CAS head initialization, and `synchronized(head)`"
        ],
        status="upcoming"
    ),
    Chapter(
        id=9,
        title="Generics Internals, Type Erasure & Wildcards",
        category="collections",
        folder="generics_type_erasure",
        summary="Why Java generics exist only at compile-time: Type erasure to `Object` or bounds, synthetic bridge methods, heap pollution warnings, reifiable vs non-reifiable types, and the PECS rule (Producer Extends, Consumer Super).",
        takeaways=[
            "Type erasure replacing type parameters with leftmost bound",
            "Bridge methods generated by compiler to maintain polymorphic overrides",
            "PECS principle: `List<? extends T>` for read, `List<? super T>` for write"
        ],
        status="upcoming"
    ),
    Chapter(
        id=10,
        title="Java NIO, Netty & Non-Blocking Sockets",
        category="frameworks",
        folder="java_nio_netty",
        summary="Transition from blocking BIO `InputStream` per thread to Non-blocking NIO: `Channel`, `ByteBuffer` (Direct off-heap vs Heap), OS multiplexing (`epoll` / `kqueue` Selectors), and Netty Reactor pattern event loops.",
        takeaways=[
            "DirectByteBuffer off-heap memory and zero-copy OS kernel writes",
            "Selector multiplexer monitoring multiple SocketChannel file descriptors",
            "Netty ByteBuf reference counting and pooling to prevent GC churn"
        ],
        status="upcoming"
    ),
    Chapter(
        id=11,
        title="Reflection, Dynamic Proxies & Bytecode Manipulation",
        category="frameworks",
        folder="reflection_proxies",
        summary="Examining runtime metaprogramming: `java.lang.reflect`, Reflection method accessor inflation to bytecode, JDK Dynamic Proxies (`InvocationHandler`) vs CGLIB/ByteBuddy ASM subclassing.",
        takeaways=[
            "JDK Dynamic Proxy requiring interfaces vs CGLIB subclassing",
            "JVM reflection inflation: JNI native call switches to generated bytecode after 15 invocations",
            "SecurityManager deprecation and JVM module boundaries (`--add-opens`)"
        ],
        status="upcoming"
    ),
    Chapter(
        id=12,
        title="Spring Framework Internals: IoC & Bean Lifecycle",
        category="frameworks",
        folder="spring_internals",
        summary="Deconstructing the enterprise standard: `BeanFactory` and `ApplicationContext`, Bean definition parsing, circular dependency resolution using Spring 3-level singleton cache, and BeanPostProcessor proxy wrapping for `@Transactional`.",
        takeaways=[
            "3-Level Singleton Cache: `singletonObjects`, `earlySingletonObjects`, `singletonFactories`",
            "Bean lifecycle: Instantiate -> Populate -> BeanPostProcessor -> Initialize",
            "Dynamic proxy self-invocation bug: why calling `@Transactional` internally fails"
        ],
        status="upcoming"
    ),
    Chapter(
        id=13,
        title="High-Performance Java: JIT Inlining & JMH",
        category="jvm",
        folder="jit_jmh_performance",
        summary="How HotSpot turns bytecode into blazing machine code: Inlining thresholds (`-XX:MaxInlineLevel`), escape analysis and scalar replacement, loop unrolling, and writing proper microbenchmarks with JMH to avoid Dead Code Elimination.",
        takeaways=[
            "Method inlining: eliminates call stack overhead and enables dead-code pruning",
            "Escape analysis: stack allocating objects that don't escape method scope",
            "JMH Blackhole and compiler warmup loops to prevent false optimizations"
        ],
        status="upcoming"
    ),
    Chapter(
        id=14,
        title="Streams API Internals & Lambda Desugaring",
        category="collections",
        folder="streams_lambdas",
        summary="How functional idioms work on the JVM: `invokedynamic` opcode, bootstrap methods (`LambdaMetafactory`), avoiding anonymous inner class overhead, and `Spliterator` pipeline chaining with lazy evaluation.",
        takeaways=[
            "`invokedynamic` generates private static method and call site linkage",
            "Stream operations are lazy: intermediate ops return StatelessOp/StatefulOp pipelines",
            "Parallel streams use common `ForkJoinPool.commonPool()` work-stealing"
        ],
        status="upcoming"
    ),
    Chapter(
        id=15,
        title="GraalVM Native Image & Ahead-of-Time (AOT)",
        category="frameworks",
        folder="graalvm_native_image",
        summary="AOT compilation for instant startup and low memory: Closed-world analysis, reachability metadata for reflection/resources, SubstrateVM runtime, and comparing JIT peak throughput vs Native Image instant warm-up.",
        takeaways=[
            "Closed-world assumption: all reachable classes compiled at build time",
            "Cold start drop from 2-3 seconds to sub-20ms for serverless/microservices",
            "Trade-off: No runtime JIT speculative profiling optimizations"
        ],
        status="upcoming"
    )
]

CHAPTERS_DB: List[Chapter] = [
    Chapter(
        id=1,
        title="How Backend Systems Work Behind the Scenes",
        category="network",
        folder="what_is backend_and_its_working",
        summary="Request routing from browser network hops, firewalls, and ISP routing over the Internet to an AWS-hosted backend server.",
        takeaways=["Request packet flow across sockets", "Network firewalls and entry proxies", "Client-server raw message cycle"],
        has_transcript=True,
        has_interactive_notes=True,
        status="completed"
    ),
    Chapter(
        id=2,
        title="The HTTP Protocol",
        category="network",
        folder="http",
        summary="HTTP semantics, request/response headers, pre-flight CORS flows, caching headers, SSL/TLS, and HTTP/1.1 vs HTTP/2 vs HTTP/3.",
        takeaways=["CORS Simple vs Pre-flight requests", "HTTP/2 multiplexing vs HTTP/3 QUIC", "ETags and cache validation rules"],
        has_transcript=True,
        has_interactive_notes=False,
        status="completed"
    ),
    Chapter(
        id=3,
        title="Routing Mechanics",
        category="core",
        folder="routing_mechanics",
        summary="Mapping incoming URLs and methods to application logic, path/query parameters, wildcard/regex routing, versioning, and deprecation.",
        takeaways=["Dynamic path params vs Query params", "API versioning (URI, Header, Media)", "Route grouping for middlewares"],
        status="upcoming"
    ),
    Chapter(
        id=4,
        title="Serialization & Deserialization",
        category="core",
        folder="serialization_and_deserialization",
        summary="Translating native data structures into transmittable wire formats (JSON, XML vs Protocol Buffers) and examining performance trade-offs.",
        takeaways=["JSON text vs Protobuf binary", "Schema validation & injection risks", "Custom serialization handlers"],
        status="upcoming"
    ),
    Chapter(
        id=5,
        title="Authentication & Authorization",
        category="core",
        folder="authentication_and_authorization",
        summary="Sessions, JWTs, OAuth2/OIDC, RBAC/ABAC/ReBAC, password salting/hashing, and timing attack mitigation.",
        takeaways=["Stateful sessions vs Stateless JWTs", "OAuth2 flows and refresh tokens", "Preventing timing attack side-channels"],
        status="upcoming"
    ),
    Chapter(
        id=6,
        title="Input Validation & Transformation",
        category="core",
        folder="input_validation_and_transformation",
        summary="Sanitizing user input via syntactic, semantic, and type validations alongside data casting and normalization rules.",
        takeaways=["Syntactic vs Semantic checks", "Fail-fast server gateway validation", "Sanitizing input to prevent SQLi/XSS"],
        status="upcoming"
    ),
    Chapter(
        id=7,
        title="Middleware Architecture",
        category="core",
        folder="middleware_architecture",
        summary="Designing pre-request and post-response interceptor pipelines for logging, auth checks, rate limiting, and compression.",
        takeaways=["Middleware execution ordering", "Short-circuiting request chains", "Global error interceptor hooks"],
        status="upcoming"
    ),
    Chapter(
        id=8,
        title="Request Context",
        category="core",
        folder="request_context",
        summary="Managing temporary request-scoped state (auth tokens, correlation IDs, trace IDs, timeouts, and cancellation signals).",
        takeaways=["Correlation IDs for distributed tracing", "Context timeout propagation", "Request-scoped memory cleanup"],
        status="upcoming"
    ),
    Chapter(
        id=9,
        title="Handlers & Controllers",
        category="core",
        folder="handlers_and_controllers",
        summary="Structuring presentation layers with MVC principles, decoupling business logic into services, and standardizing responses.",
        takeaways=["Controller vs Service layer separation", "Centralized response envelope schemas", "Error propagation patterns"],
        status="upcoming"
    ),
    Chapter(
        id=10,
        title="CRUD API Design",
        category="core",
        folder="crud_api_design",
        summary="Implementing clean CRUD operations with proper HTTP verbs, status codes, pagination models, sorting, and filtering.",
        takeaways=["Offset vs Cursor pagination", "HTTP verb semantic mapping", "Handling partial resource updates"],
        status="upcoming"
    ),
    Chapter(
        id=11,
        title="RESTful Architecture & Best Practices",
        category="core",
        folder="rest_api",
        summary="Roy Fielding constraints, HTTP method semantics, idempotency proofs, plural nouns, nested endpoints, and Sane Defaults.",
        takeaways=["Roy Fielding 6 architectural constraints", "State machine & mathematical idempotency proofs", "PUT vs PATCH mutation semantics", "Plural resource URLs & query pagination"],
        has_transcript=True,
        has_interactive_notes=True,
        status="completed"
    ),
    Chapter(
        id=12,
        title="Databases: Relational vs NoSQL",
        category="data",
        folder="databases_relational_vs_nosql",
        summary="Relational vs NoSQL paradigms, ACID guarantees, CAP theorem, indexing, query optimization, connection pooling, and ORMs.",
        takeaways=["ACID vs BASE trade-offs", "B-Tree vs Hash indexing mechanics", "Connection pool sizing rules"],
        status="upcoming"
    ),
    Chapter(
        id=13,
        title="Business Logic Layer (BLL)",
        category="core",
        folder="business_logic_layer",
        summary="Encapsulating core domain rules away from transport controllers and storage persistence using SOLID principles.",
        takeaways=["Layered architectural boundary setup", "Domain models vs DTOs", "Domain validation rule engines"],
        status="upcoming"
    ),
    Chapter(
        id=14,
        title="Caching Strategies",
        category="data",
        folder="caching_strategies",
        summary="Optimizing throughput with In-Memory (Redis) & Distributed caching, eviction policies (LRU/TTL), and multi-level caching.",
        takeaways=["Cache-aside vs Write-through patterns", "LRU/TTL eviction strategies", "Mitigating cache stampede & avalanche"],
        status="upcoming"
    ),
    Chapter(
        id=15,
        title="Transactional Emails",
        category="core",
        folder="transactional_emails",
        summary="Building reliable notification pipelines: HTML email anatomy, dynamic parameters, template rendering, and delivery queues.",
        takeaways=["Email body CTA formatting", "Asynchronous email queuing", "Delivery status webhooks"],
        status="upcoming"
    ),
    Chapter(
        id=16,
        title="Task Queues & Background Workers",
        category="system",
        folder="task_queues_and_background_workers",
        summary="Offloading heavy computations asynchronously using producer-consumer job queues (BullMQ/Celery), cron jobs, and retries.",
        takeaways=["Producer-Broker-Consumer pipelines", "Dead-letter queues & retries", "Task prioritization rules"],
        status="upcoming"
    ),
    Chapter(
        id=17,
        title="Elasticsearch & Full-Text Search",
        category="data",
        folder="elasticsearch_and_full_text_search",
        summary="Inverted indices, TF-IDF / BM25 algorithms, shards, segments, relevance scoring, and log aggregation with Kibana.",
        takeaways=["Inverted index vs Table scanning", "Shards & segment management", "Fuzzy matching & aggregations"],
        status="upcoming"
    ),
    Chapter(
        id=18,
        title="Global Error Handling",
        category="system",
        folder="global_error_handling",
        summary="Designing predictable global exception handlers, custom error classes, graceful degradation, and user error masking.",
        takeaways=["Fail-fast vs Fail-safe strategies", "Obfuscating sensitive stack traces", "Sentry & alerting triggers"],
        status="upcoming"
    ),
    Chapter(
        id=19,
        title="Configuration & Secret Management",
        category="system",
        folder="configuration_and_secret_management",
        summary="Decoupling runtime code from environment configuration, dynamic feature flags, secret vaults, and EnV isolation.",
        takeaways=["12-Factor config isolation", "Secure secret storage (KMS/Vault)", "Dynamic feature flag toggling"],
        status="upcoming"
    ),
    Chapter(
        id=20,
        title="Logging, Monitoring & Observability",
        category="system",
        folder="logging_monitoring_and_observability",
        summary="Structured JSON logs, metrics (Prometheus/Grafana), APM tools, and distributed tracing across microservices.",
        takeaways=["Structured logging levels", "Three pillars: Logs, Metrics, Traces", "Alerting thresholds & SLA tracking"],
        status="upcoming"
    ),
    Chapter(
        id=21,
        title="Graceful Shutdowns",
        category="system",
        folder="graceful_shutdowns",
        summary="Handling process termination signals (SIGTERM/SIGINT) safely by stopping incoming traffic and draining inflight requests.",
        takeaways=["SIGTERM vs SIGKILL signal handling", "Draining inflight requests cleanly", "Closing DB connections and file handles"],
        status="upcoming"
    ),
    Chapter(
        id=22,
        title="System Security & Hardening",
        category="system",
        folder="system_security_and_hardening",
        summary="Mitigating OWASP Top 10 vulnerabilities: SQLi, XSS, CSRF, broken access control, rate limiting, and CSP policies.",
        takeaways=["Principle of Least Privilege", "Mitigating SQLi & XSS", "Security headers & audit trails"],
        status="upcoming"
    ),
    Chapter(
        id=23,
        title="Scaling & Performance Optimization",
        category="system",
        folder="scaling_and_performance_optimization",
        summary="Optimizing throughput and latency: resolving N+1 query bugs, batch processing, memory leak detection, and payload compression.",
        takeaways=["Eliminating N+1 query bugs", "Horizontal vs Vertical scaling", "Profiling CPU & memory bottlenecks"],
        status="upcoming"
    ),
    Chapter(
        id=24,
        title="Concurrency & Parallelism",
        category="system",
        folder="concurrency_and_parallelism",
        summary="Non-blocking async IO vs multi-threading, CPU-bound vs IO-bound workloads, race conditions, mutexes, and atomicity.",
        takeaways=["IO-bound vs CPU-bound execution", "Event loops vs Thread pools", "Preventing race conditions & deadlocks"],
        status="upcoming"
    ),
    Chapter(
        id=25,
        title="Object Storage & Large Files",
        category="data",
        folder="object_storage_and_large_files",
        summary="Managing unstructured blob storage (AWS S3), presigned URLs, streaming file downloads/uploads, and multipart chunking.",
        takeaways=["Presigned URLs for secure upload", "Streaming chunk buffers", "Multipart parallel uploads"],
        status="upcoming"
    ),
    Chapter(
        id=26,
        title="Real-time Backend Systems",
        category="network",
        folder="real_time_backend_systems",
        summary="Bidirectional real-time communication: WebSockets, Server-Sent Events (SSE), HTTP Long Polling, and Pub/Sub brokers.",
        takeaways=["WebSockets vs SSE vs Long-polling", "Scaling sockets with Redis Pub/Sub", "Heartbeats & reconnection logic"],
        status="upcoming"
    ),
    Chapter(
        id=27,
        title="Testing & Code Quality",
        category="system",
        folder="testing_and_code_quality",
        summary="Constructing robust test suites: Unit, Integration, E2E, TDD workflows, CI/CD pipelines, and cyclomatic complexity metrics.",
        takeaways=["Testing Pyramid ratio strategy", "TDD red-green-refactor loop", "Cyclomatic complexity limits"],
        status="upcoming"
    ),
    Chapter(
        id=28,
        title="The 12-Factor App Methodology",
        category="system",
        folder="the_12_factor_app_methodology",
        summary="Adhering to cloud-native application design rules for portability, explicit dependencies, stateless processes, and dev/prod parity.",
        takeaways=["Stateless processes & disposability", "Dev/prod parity guidelines", "Backing service binding"],
        status="upcoming"
    ),
    Chapter(
        id=29,
        title="OpenAPI & API-First Development",
        category="core",
        folder="openapi_and_api_first_development",
        summary="Defining machine-readable API contracts before coding: Swagger/OpenAPI specs, automated client generation, and mock servers.",
        takeaways=["API-First development workflow", "OpenAPI 3.1 schema definitions", "Client code generation tools"],
        status="upcoming"
    ),
    Chapter(
        id=30,
        title="Webhooks Architecture",
        category="network",
        folder="webhooks_architecture",
        summary="Designing event-driven outbound push notifications: HTTP callback receivers, event signatures, idempotency, and retries.",
        takeaways=["API Polling vs Webhook push models", "HMAC secret signature verification", "Exponential backoff retry queues"],
        status="upcoming"
    )
]

# --- HTML TEMPLATES & PAGES ---

@app.get("/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/index.html", response_class=HTMLResponse, tags=["Pages"])
async def serve_landing_page(request: Request):
    """Serves the sketch-note styled curriculum landing page via Jinja2 template."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request, "chapters": CHAPTERS_DB, "playlist": PLAYLIST_INFO}
    )

@app.get("/rest_api", response_class=HTMLResponse, tags=["Pages"])
@app.get("/rest_api/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/rest_api/index.html", response_class=HTMLResponse, tags=["Pages"])
async def serve_rest_api_masterclass(request: Request):
    """Serves Chapter 11 / REST API complete interactive masterclass via Jinja2 template."""
    return templates.TemplateResponse(
        request=request,
        name="rest_api.html",
        context={"request": request}
    )

@app.get("/what_is_backend", response_class=HTMLResponse, tags=["Pages"])
@app.get("/what_is_backend/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/what_is backend_and_its_working", response_class=HTMLResponse, tags=["Pages"])
@app.get("/what_is backend_and_its_working/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/what_is backend_and_its_working/index.html", response_class=HTMLResponse, tags=["Pages"])
async def serve_what_is_backend(request: Request):
    """Serves Chapter 01 / What is Backend interactive notes via Jinja2 template."""
    return templates.TemplateResponse(
        request=request,
        name="what_is_backend.html",
        context={"request": request}
    )

@app.get("/system_design", response_class=HTMLResponse, tags=["Pages"])
@app.get("/system_design/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/system-design", response_class=HTMLResponse, tags=["Pages"])
@app.get("/system-design/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/system_design/index.html", response_class=HTMLResponse, tags=["Pages"])
async def serve_system_design_page(request: Request):
    """Serves the sketch-note styled System Design landing page with URL Shortener case study."""
    return templates.TemplateResponse(
        request=request,
        name="system_design.html",
        context={
            "request": request,
            "chapters": SYSTEM_DESIGN_CHAPTERS_DB,
            "playlist": SYSTEM_DESIGN_INFO
        }
    )

@app.get("/url_shortener", response_class=HTMLResponse, tags=["Pages"])
@app.get("/url_shortener/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/url-shortener", response_class=HTMLResponse, tags=["Pages"])
@app.get("/url-shortener/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/url_shortener/index.html", response_class=HTMLResponse, tags=["Pages"])
async def serve_url_shortener_masterclass(request: Request):
    """Serves Chapter 01 / URL Shortener complete interactive masterclass notes (22 slides, 5 views, simulation) via Jinja2 template."""
    return templates.TemplateResponse(
        request=request,
        name="url_shortener.html",
        context={"request": request}
    )

@app.get("/java_notes", response_class=HTMLResponse, tags=["Pages"])
@app.get("/java_notes/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/java-notes", response_class=HTMLResponse, tags=["Pages"])
@app.get("/java-notes/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/java_notes/index.html", response_class=HTMLResponse, tags=["Pages"])
async def serve_java_notes_page(request: Request):
    """Serves the sketch-note styled Java & JVM Notes landing page with interactive simulators."""
    return templates.TemplateResponse(
        request=request,
        name="java_notes.html",
        context={
            "request": request,
            "chapters": JAVA_NOTES_CHAPTERS_DB,
            "playlist": JAVA_NOTES_INFO
        }
    )

@app.get("/java_jdbc", response_class=HTMLResponse, tags=["Pages"])
@app.get("/java_jdbc/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/java-jdbc", response_class=HTMLResponse, tags=["Pages"])
@app.get("/java-jdbc/", response_class=HTMLResponse, tags=["Pages"])
@app.get("/java_jdbc/index.html", response_class=HTMLResponse, tags=["Pages"])
async def serve_java_jdbc_masterclass(request: Request):
    """Serves Chapter 07 / Java Database Connectivity (JDBC) from Scratch complete interactive masterclass."""
    return templates.TemplateResponse(
        request=request,
        name="java_jdbc.html",
        context={"request": request}
    )

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: HTTPException):
    """Handles 404 errors with JSON for API endpoints and custom sketch template for web pages."""
    if request.url.path.startswith("/api/"):
        return JSONResponse(
            status_code=404,
            content={"detail": getattr(exc, "detail", "API endpoint not found")}
        )
    return templates.TemplateResponse(
        request=request,
        name="404.html",
        context={"request": request, "url": str(request.url)},
        status_code=404
    )

# --- REST API ENDPOINTS ---

@app.get("/api/playlist", response_model=PlaylistInfo, tags=["Curriculum"])
async def get_playlist_info():
    """Returns metadata about the YouTube playlist and course author."""
    return PLAYLIST_INFO

@app.get("/api/chapters", response_model=List[Chapter], tags=["Curriculum"])
async def get_all_chapters(category: Optional[str] = None):
    """Returns all 30 chapters with optional category filtering."""
    if category and category != "all":
        return [ch for ch in CHAPTERS_DB if ch.category == category.lower()]
    return CHAPTERS_DB

@app.get("/api/chapters/{chapter_id}", response_model=Chapter, tags=["Curriculum"])
async def get_chapter_by_id(chapter_id: int):
    """Returns details for a single chapter by ID."""
    for ch in CHAPTERS_DB:
        if ch.id == chapter_id:
            return ch
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Chapter {chapter_id} not found")

@app.get("/api/transcripts/{chapter_name}", response_class=PlainTextResponse, tags=["Transcripts"])
async def get_transcript_text(chapter_name: str):
    """
    Returns raw transcript text for available chapters:
    - 'rest_api' or 'restapi'
    - 'http' or 'https'
    - 'what_is_backend' or 'backend'
    """
    clean_name = chapter_name.lower().replace("-", "_")
    transcript_file = None

    if clean_name in ["rest_api", "restapi", "11"]:
        candidates = [
            BASE_DIR / "transcript" / "transcript_restapi.md",
            BASE_DIR / "rest_api" / "transcript_restapi.md",
            BASE_DIR / "transcript_restapi.md"
        ]
    elif clean_name in ["http", "https", "2"]:
        candidates = [
            BASE_DIR / "transcript" / "transcript_http.md",
            BASE_DIR / "http" / "transcript_http.md",
            BASE_DIR / "transcript_http.md"
        ]
    elif clean_name in ["what_is_backend", "backend", "1"]:
        candidates = [
            BASE_DIR / "what_is backend_and_its_working" / "transcript_backend.md",
            BASE_DIR / "transcript" / "transcript_backend.md",
            BASE_DIR / "transcript_backend.md"
        ]
    elif clean_name in ["url_shortener", "urlshortener", "url_shortner", "urlshortner"]:
        candidates = [
            BASE_DIR / "transcript" / "system_design_transcript" / "url_shortner.md",
            BASE_DIR / "transcript" / "url_shortner.md",
            BASE_DIR / "url_shortner.md"
        ]
    elif clean_name in ["java_jdbc", "javajdbc", "jdbc", "7"]:
        candidates = [
            BASE_DIR / "transcript" / "java" / "java_jdbc.md",
            BASE_DIR / "transcript" / "java_jdbc.md",
            BASE_DIR / "java_jdbc.md"
        ]
    else:
        candidates = []

    for c in candidates:
        if c.exists():
            transcript_file = c
            break

    if transcript_file and transcript_file.exists():
        return PlainTextResponse(transcript_file.read_text(encoding="utf-8"))

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Transcript not found for '{chapter_name}'. Transcripts are available for 'rest_api', 'http', and 'what_is_backend'."
    )

# --- SYSTEM DESIGN ENDPOINTS ---

@app.get("/api/system-design/chapters", response_model=List[Chapter], tags=["System Design"])
async def get_system_design_chapters():
    """Returns all System Design chapters."""
    return SYSTEM_DESIGN_CHAPTERS_DB

@app.get("/api/system-design/chapters/{chapter_id}", response_model=Chapter, tags=["System Design"])
async def get_system_design_chapter_by_id(chapter_id: int):
    """Returns details for a single System Design chapter by ID."""
    for ch in SYSTEM_DESIGN_CHAPTERS_DB:
        if ch.id == chapter_id:
            return ch
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"System Design Chapter {chapter_id} not found")

# --- JAVA NOTES ENDPOINTS ---

@app.get("/api/java-notes/chapters", response_model=List[Chapter], tags=["Java Notes"])
async def get_java_notes_chapters():
    """Returns all Java & JVM chapters."""
    return JAVA_NOTES_CHAPTERS_DB

@app.get("/api/java-notes/chapters/{chapter_id}", response_model=Chapter, tags=["Java Notes"])
async def get_java_notes_chapter_by_id(chapter_id: int):
    """Returns details for a single Java Notes chapter by ID."""
    for ch in JAVA_NOTES_CHAPTERS_DB:
        if ch.id == chapter_id:
            return ch
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Java Notes Chapter {chapter_id} not found")

@app.get("/api/health", tags=["Status"])
async def health_check():
    """Health check endpoint confirming FastAPI server status."""
    return {
        "status": "online",
        "app": "Backend Notes API",
        "version": "1.0.0",
        "total_backend_chapters": len(CHAPTERS_DB),
        "total_system_design_chapters": len(SYSTEM_DESIGN_CHAPTERS_DB),
        "total_java_notes_chapters": len(JAVA_NOTES_CHAPTERS_DB),
        "playlist": PLAYLIST_INFO.playlist_url
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
