import asyncio

async def fetch_data():
    print("📡 Database ကနေ data စယူပြီ...")
    await asyncio.sleep(2)  # ၂ စက္ကန့်ကြာအောင် စောင့်မယ် (Blocking မဖြစ်စေဘဲ)
    print("✅ Data ရပါပြီ!")
    return {"user": "Mg Mg"}

async def show_animation():
    print("🎬 Animation လေးတွေ ပြနေမယ်...")
    await asyncio.sleep(1)
    print("🎬 Animation ဆက်ပြနေတယ်...")

async def main():
    # အလုပ် ၂ ခုလုံးကို တစ်ပြိုင်နက် (Concurrent) ခိုင်းလိုက်တာ
    await asyncio.gather(fetch_data(), show_animation())

asyncio.run(main()) 