"""
from pydantic import BaseModel, Field
from typing import Optional

# AI Chatbot အတွက် User ဆီက လာမယ့် Request ပုံစံကို သတ်မှတ်မယ်
class ChatRequest(BaseModel):
    user_id: int
    message: str = Field(min_length=1, max_length=500) # စာသားက ၁ လုံးကနေ ၅၀၀ ကြားပဲ ဖြစ်ရမယ်
    temperature: Optional[float] = 0.7 # ရှိချင်မှရှိမယ်၊ ရှိရင် decimal (float) ဖြစ်ရမယ်

# အသုံးပြုပုံ (Data မှန်တဲ့အခါ)
try:
    data = {
        "user_id": 101,
        "message": "Please explain me about ai",
        "temperature": 0.5
    }
    request = ChatRequest(**data)
    print(f"✅ User {request.user_id}  I have a message: {request.message}")

except Exception as e:
    print(f"❌ Error {e}")
    """
from pydantic import BaseModel, Field
from typing import Optional

class ChatInput(BaseModel):
    prompt: str = Field(min_length=5)

u = ChatInput(prompt = "I")
print(u)