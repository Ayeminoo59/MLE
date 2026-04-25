from fastapi import FastAPI

# 1. App Instance ဆောက်တာ (စနစ်ကြီးကို စတင်နှိုးလိုက်တာ)
app = FastAPI()

# 2. Endpoint သတ်မှတ်တာ (User ဘယ်တံခါးပေါက်က လာရမလဲဆိုတာ)
@app.get("/")
def read_root():
    # 3. Python ရဲ့ Logic အပိုင်း (အဖြေပြန်ပေးတာ)
    return {"message": "မင်္ဂလာပါ"}

"""
run
uvicorn Api_test.Fastapi_test:app --reload --port 8001
"""