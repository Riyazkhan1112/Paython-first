from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    message: str

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint - Hello World"""
    return {
        "status": "healthy",
        "message": "Hello World! API is running"
    }



@router.get("/hello", response_model=HealthResponse)
async def hello_world():
    """Hello World endpoint"""
    return {
        "status": "healthy",
        "message": "Hello World! This is a FastAPI application."
    }