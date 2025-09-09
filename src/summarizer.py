import requests
from config import LLM_PROVIDER, LLM_MODEL, GROQ_API_KEY, OLLAMA_BASE_URL, OPENAI_API_KEY

def summarize(prompt: str) -> str:
    if LLM_PROVIDER == "groq":
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
        data = {
            "model": LLM_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500,
            "temperature": 0.7,
        }
        print(f'Sending data from summarizer: {data}')
        resp = requests.post(url, headers=headers, json=data)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    elif LLM_PROVIDER == "ollama":
        resp = requests.post(f"{OLLAMA_BASE_URL}/api/generate",
                             json={"model": LLM_MODEL, "prompt": prompt})
        return resp.json().get("response", "")
    elif LLM_PROVIDER == "openai":
        raise NotImplementedError("OpenAI support not wired here.")
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: {LLM_PROVIDER}")
