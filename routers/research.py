from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

# Request/Response models
class ResearchRequest(BaseModel):
    topic: str

class ResearchResponse(BaseModel):
    success: bool
    topic: str
    result: str

# Try to import Gemini API
try:
    from google import genai
    api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
    client = genai.Client(api_key=api_key) if api_key else None
except ImportError:
    client = None

@router.post("/research", response_model=ResearchResponse)
async def research(request: ResearchRequest):
    """Research endpoint using Gemini API"""
    
    if not request.topic:
        return {
            "success": False,
            "topic": "",
            "result": "Topic is required"
        }
    
    if not client:
        return {
            "success": False,
            "topic": request.topic,
            "result": "Gemini API not configured. Please set GOOGLE_GEMINI_API_KEY environment variable."
        }
    
    try:
        prompt = f"""
Do deep research on the following topic:

{request.topic}

Return the research in approximately 100 words.
"""
        
        interaction = client.interactions.create(
            model="gemini-3.6-flash", 
            input=prompt
        )
        
        return {
            "success": True,
            "topic": request.topic,
            "result": interaction.output_text
        }
    except Exception as e:
        return {
            "success": False,
            "topic": request.topic,
            "result": f"Error: {str(e)}"
        }
