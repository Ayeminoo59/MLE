from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AIInput(BaseModel):
    prompt: str
    max_tokens: int = 100

# --- ဒီအပိုင်းကို အသစ်ထည့်လိုက်ပါ ---
@app.get("/")
async def home():
    return {"message": "API is running! Go to /docs to test the AI."}
# -----------------------------

@app.post("/ask-ai")
async def ask_ai(data: AIInput):
    ai_response = f"Your prompt was: {data.prompt}. AI is thinking..."
    return {
        "status": "success",
        "answer": ai_response,
        "tokens_used": data.max_tokens
    }