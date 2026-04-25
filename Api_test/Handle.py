from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_ai(request: ChatRequest):
    user_query = request.question
    response_text = f"မင်းမေးတာက '{user_query}' လား? ခဏစောင့်နော်၊ AI က တွက်နေတယ်..."
    return {"answer": response_text}