import os
from dotenv import load_dotenv

load_dotenv()

# === General Settings ===
print("printing from config.py FEEDS :", os.getenv("FEEDS", ""))
FEEDS = [f.strip() for f in os.getenv("FEEDS", "").split(",") if f.strip()]
KEYWORDS = [k.strip().lower() for k in os.getenv("KEYWORDS", "").split(",") if k.strip()]
DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"

# === LLM Settings ===
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq").lower()
LLM_MODEL = os.getenv("LLM_MODEL", "llama-3-8b-instant")

# === Provider-specific keys ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
