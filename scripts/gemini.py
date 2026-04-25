import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel

# ၁။ Gemini Configuration
# မင်းရလာတဲ့ Key ကို ဒီအောက်က မျက်တောင်ဖွင့်ပိတ်ထဲမှာ ထည့်ပါ
GEMINI_API_KEY = "AIzaSyBtQ-7oa-rwZcep7iyWy4cs42M4hqOL5qc" 
genai.configure(api_key=GEMINI_API_KEY)

# Gemini Model ကို သတ်မှတ်ခြင်း (flash က အမြန်ဆုံးမို့လို့ သူ့ကို သုံးမယ်)
model = genai.GenerativeModel('gemini-pro')

app = FastAPI(title="Gemini Real-World AI API")

# ၂။ Request Body သတ်မှတ်ခြင်း
class AIInput(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Gemini AI API is now LIVE!"}

# ၃။ Gemini ဆီက အဖြေတောင်းတဲ့ Endpoint
@app.post("/ask-ai")
async def ask_gemini(data: AIInput):
    try:
        # User ပို့လိုက်တဲ့ prompt ကို Gemini ဆီ ပို့လိုက်တယ်
        response = model.generate_content(data.prompt)
        
        return {
            "status": "success",
            "input_received": data.prompt,
            "ai_answer": response.text  # ဒါက Gemini ပြန်ဖြေတဲ့ စာသား
        }
    except Exception as e:
        # တစ်ခုခု မှားသွားရင် (ဥပမာ Key မှားတာမျိုး) error ပြခိုင်းတာ
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
