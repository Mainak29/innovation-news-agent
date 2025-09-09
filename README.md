# Innovation Agent (Groq-powered)

This automation agent researches innovation news daily, summarizes with Groq LLMs, and drafts LinkedIn posts.

## 🚀 Setup

1. Clone repo & install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` → `.env` and add your **Groq API key**.

3. Run once:
   ```bash
   python -m src.run
   ```

4. If you want to save drafts in the projects and uncomment the code in run.py 
   See drafts in `out/` folder.

5. Deploy on GitHub Actions (schedule at 09:00 IST).

## ⚡ Switching LLM Providers
- Default = Groq (`llama-3-8b-instant`)
- You can also set `.env` to `ollama` or `openai`.

