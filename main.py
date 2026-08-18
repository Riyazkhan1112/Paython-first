from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routers import health, research, pages
import os

# Initialize FastAPI app
app = FastAPI(
    title="Python Research API",
    description="FastAPI application with research capabilities",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(research.router, prefix="/api", tags=["research"])
app.include_router(pages.router, tags=["pages"])

# Mount static files
if os.path.exists("templates"):
    app.mount("/static", StaticFiles(directory="templates"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
