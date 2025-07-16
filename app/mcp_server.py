from fastapi import FastAPI, Request
import httpx
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for your frontend (on port 5173 or file://)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FAQS = {
    "what are your working hours?": "We’re open 9am–5pm, Mon–Fri.",
    "where are you located?": "We're based out of Zendar",
    "how can I contact support?": "You can email support@example.com."
}

def is_faq(query: str) -> bool:
    return query.lower().strip() in FAQS

async def query_ollama(prompt: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://localhost:11434/api/generate",
                json={"model": "llama3", "prompt": prompt},
                timeout=None
            )
            full_response = ""
            async for line in response.aiter_lines():
                if line:
                    try:
                        json_data = json.loads(line)
                        full_response += json_data.get("response", "")
                    except json.JSONDecodeError:
                        continue
            return full_response.strip()
        except Exception as e:
            return f"Error from Ollama: {e}" 

@app.post("/query")
async def route_query(request: Request):
    data = await request.json()
    user_input = data.get("prompt", "")

    if is_faq(user_input):
        answer = FAQS[user_input.lower().strip()]
        route = "faq"
    else:
        answer = await query_ollama(user_input)
        route = "llm"

    return {"route": route, "response": answer}