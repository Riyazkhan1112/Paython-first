# FastAPI Research Application

A refactored Python application using **FastAPI** instead of Flask, with organized project structure.

## Project Structure

```
.
├── main.py                    # Main FastAPI application
├── config.py                  # Configuration settings
├── routers/                   # API route handlers
│   ├── __init__.py
│   ├── health.py             # Health check endpoint (Hello World)
│   ├── pages.py              # HTML page endpoints
│   └── research.py           # Research API endpoint
├── templates/                # HTML templates (optional)
├── requirements_fastapi.txt  # Python dependencies
├── .env.example             # Environment variables template
└── README_FASTAPI.md        # This file
```

## Features

✅ **Hello World** - Health check endpoint at `/api/health`
✅ **FastAPI** - Modern, fast web framework with automatic documentation
✅ **Organized Routes** - Separate router files for different features
✅ **CORS Support** - Cross-Origin Resource Sharing enabled
✅ **Pydantic Models** - Type-safe request/response validation
✅ **Configuration** - Centralized settings management
✅ **Gemini AI Integration** - Research capabilities with Google Gemini API

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements_fastapi.txt
```

### 2. Setup Environment Variables

Copy `.env.example` to `.env` and add your API keys:

```bash
GOOGLE_GEMINI_API_KEY=your_api_key_here
DEBUG=False
HOST=0.0.0.0
PORT=8000
```

## Running the Application

### Option 1: Direct Python
```bash
python main.py
```

### Option 2: Uvicorn (Recommended)
```bash
uvicorn main:app --reload
```

The application will start at `http://localhost:8000`

## API Endpoints

### Health Check (Hello World)
- **GET** `/api/health` - Returns: `{"status": "healthy", "message": "Hello World! API is running"}`

### Pages
- **GET** `/` - Main page with navigation
- **GET** `/research` - Research tool page
- **GET** `/chatbot` - Chatbot interface

### Research API
- **POST** `/api/research` - Perform research on a topic
  - Request: `{"topic": "machine learning"}`
  - Response: `{"success": true, "topic": "...", "result": "..."}`

## Interactive API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Migrating from Flask

### Key Changes:
- **Framework**: Flask → FastAPI
- **Server**: Flask dev server → Uvicorn
- **Routing**: `@app.route()` → `APIRouter()` in separate files
- **Request Handling**: Direct → `pydantic` models
- **Response Handling**: `jsonify()` → Automatic JSON serialization
- **Type Safety**: Added type hints throughout

### File Separation:
- `main.py` - Application factory and router setup
- `config.py` - Centralized configuration
- `routers/health.py` - Health check (Hello World)
- `routers/pages.py` - HTML page rendering
- `routers/research.py` - API endpoints

## Development

### Add a New Route

1. Create a new file in `routers/` directory
2. Define your router:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/my-endpoint")
async def my_endpoint():
    return {"message": "Hello"}
```

3. Include it in `main.py`:

```python
from routers import my_router
app.include_router(my_router.router, prefix="/api")
```

## Testing the Hello World Endpoint

```bash
curl http://localhost:8000/api/health
```

Response:
```json
{
  "status": "healthy",
  "message": "Hello World! API is running"
}
```

## Requirements

- Python 3.8+
- FastAPI 0.100+
- Uvicorn 0.23+
- Pydantic 2.0+

## License

MIT
