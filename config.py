import os

class Config:    
    # API Keys
    OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
    # Server
    API_HOST = os.getenv("API_HOST", "https://ollama.com/v1/chat/completions")
    API_PORT = int(os.getenv("PORT", os.getenv("API_PORT", 8000)))
    API_BASE_URL = f"http://{API_HOST}:{API_PORT}"

config = Config()