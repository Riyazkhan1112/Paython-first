import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings"""
    APP_NAME = "Python Research API"
    APP_VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "False") == "True"
    
    # API Settings
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    
    # Gemini API
    GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY", "")
    
    # Database (if needed in future)
    DATABASE_URL = os.getenv("DATABASE_URL", "")

settings = Settings()
