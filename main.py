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

@app.get("/api/health", tags=["Status"])
async def health_check():
    """Health check endpoint confirming FastAPI server status."""
    return {
        "status": "online",
        "app": "Backend Notes API",
        "version": "1.0.0",
        "total_chapters": len(CHAPTERS_DB),
        "playlist": PLAYLIST_INFO.playlist_url
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
