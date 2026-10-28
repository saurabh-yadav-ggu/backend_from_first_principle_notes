@echo off
echo ========================================================
echo  Backend Notes - FastAPI Server
echo ========================================================
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Starting Uvicorn server on http://127.0.0.1:8000
echo - Landing Page: http://127.0.0.1:8000
echo - Chapter 01 (What is Backend): http://127.0.0.1:8000/what_is_backend
echo - Chapter 11 (REST API Masterclass): http://127.0.0.1:8000/rest_api
echo - System Design (URL Shortener): http://127.0.0.1:8000/system_design
echo - Java Notes: http://127.0.0.1:8000/java_notes
echo - Interactive Swagger Docs: http://127.0.0.1:8000/docs
echo ========================================================
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
pause
