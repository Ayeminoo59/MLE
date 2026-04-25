import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

# ဒီနေရာက 'app' ဆိုတဲ့ နာမည်က အရေးကြီးဆုံးပဲ
app = FastAPI()

class AIInput(BaseModel):
    prompt: str
    max_tokens: int = 100

async def fake_ai_engine(user_prompt: str):
    await asyncio.sleep(2) 
    if "hello" in user_prompt.lower():
        return "Mingalarba! I am your AI assistant."
    elif "python" in user_prompt.lower():
        return "Python is the king of AI development!"
    else:
        return f"Response for: {user_prompt}"

@app.get("/")
def home():
    return {"message": "Server is running!"}

@app.post("/ask-ai")
async def ask_ai(data: AIInput):
    result = await fake_ai_engine(data.prompt)
    return {"answer": result}