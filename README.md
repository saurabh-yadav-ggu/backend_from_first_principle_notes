# Backend From First Principles 🚀
### Interactive Sketch-Note Masterclass & FastAPI Learning Portal

A visual, sketch-note educational portal and FastAPI backend exploring production-grade backend engineering concepts from first principles — inspired by Sriniously's *"Backend from First Principles"* curriculum.

---

## ✨ Features

- **🎨 Hand-Drawn Sketch Aesthetics:** Custom notebook ruling background, ink-blue typography, washi tape pins, sketchy borders, and highlighters.
- **🔤 Clean Typography:** Powered by Google's **Lexend** font across all landing pages and chapter notes for readability.
- **📚 30-Chapter Curriculum:** Comprehensive syllabus spanning Networking, Core Logic, Databases & Storage, and System Operations with live search and category filtering.
- **💡 Chapter 01 Notes:** *How Backend Systems Work Behind the Scenes* (network hops, DNS, ISP routing, reverse proxies, PM2, DB connection pooling).
- **🛠️ Chapter 11 REST API Masterclass:** Complete interactive slide deck with:
  - 25 hand-crafted lecture slides
  - Interactive Idempotency Simulator
  - Real-time API Endpoint Validator
  - Live HTTP Status Code Wheel & RFC 7231 Matrix
  - Roy Fielding 6 Architectural Constraints deep dive
  - In-browser Personal Notepad with local storage persistence and markdown export
- **⚡ FastAPI Backend:** High-performance REST endpoints for curriculum metadata, playlist information, transcripts, and OpenAPI documentation (`/docs`).

---

## 🚀 Quickstart

### Prerequisites
- Python 3.10+
- `pip` or virtual environment

### 1. Clone & Setup
```bash
git clone https://github.com/saurabh-yadav-ggu/backend_from_first_principle_notes.git
cd backend_from_first_principle_notes
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the Server
On Windows, you can simply run:
```cmd
run_server.bat
```
Or manually with uvicorn:
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

---

## 🌐 Routes & Endpoints

| URL Path | Type | Description |
|---|---|---|
| `http://127.0.0.1:8000/` | Web Page | 30-Chapter Curriculum Landing Page |
| `http://127.0.0.1:8000/what_is_backend` | Web Page | Chapter 01 Notes & Visual Diagrams |
| `http://127.0.0.1:8000/rest_api` | Web Page | Chapter 11 REST API Masterclass (25 Slides & Widgets) |
| `http://127.0.0.1:8000/docs` | Swagger UI | Interactive OpenAPI Documentation |
| `http://127.0.0.1:8000/api/chapters` | JSON API | All 30 curriculum chapters (with filtering) |
| `http://127.0.0.1:8000/api/playlist` | JSON API | YouTube playlist information |
| `http://127.0.0.1:8000/api/health` | JSON API | Server health status |

---

## 📁 Repository Structure

```
├── main.py                     # FastAPI server, route handlers, and API endpoints
├── requirements.txt            # Python dependencies
├── run_server.bat              # One-click Windows startup script
├── rules.md                    # Design & typography guidelines (Lexend font)
├── templates/                  # Jinja2 HTML templates
│   ├── index.html              # Landing page template
│   ├── what_is_backend.html    # Chapter 01 notes template
│   ├── rest_api.html           # Chapter 11 masterclass template
│   └── 404.html                # Custom 404 error template
├── static/                     # Static assets (CSS, JS, images)
│   ├── css/sketch-theme.css    # Shared sketch-note design system
│   └── js/api.js               # Client-side API integration
├── http/                       # Chapter 02: HTTP protocol notes & transcripts
├── rest_api/                   # Chapter 11: REST API transcripts
└── what_is backend_and_its_working/  # Chapter 01: Transcripts
```

---

## 📜 License
MIT License. Hand-drawn sketch notes inspired by Sriniously's "Backend from First Principles" series.
