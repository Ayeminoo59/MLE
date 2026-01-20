"""
1. Setup & Config (ပထမဆုံးအကြိမ် သတ်မှတ်ခြင်း)
Git ကို စတင်အသုံးပြုခါစမှာ ကိုယ့်ရဲ့ နာမည်နဲ့ Email ကို အရင်သတ်မှတ်ပေးရပါမယ်။

git config --global user.name "Your Name" - အသုံးပြုသူအမည် သတ်မှတ်ရန်။

git config --global user.email "mail@example.com" - အီးမေးလ် သတ်မှတ်ရန်။

git config --list - လက်ရှိ setting တွေကို ပြန်ကြည့်ရန်။

"""

"""
   2. Starting a Project (Project အသစ်စတင်ခြင်း)
Project တစ်ခုကို Git နဲ့ စတင်ချိတ်ဆက်ဖို့ သုံးပါတယ်။

git init - Folder အသစ်တစ်ခုထဲမှာ Git repository တစ်ခု စတင်ပြုလုပ်ရန်။

git clone <url> - Remote (ဥပမာ GitHub) ပေါ်က project ကို ကိုယ့်စက်ထဲ ကူးယူရန်။

# ၁။ Desktop ပေါ်သွားမယ်
cd Desktop

# ၂။ Mac မှာ တင်ထားတဲ့ Project ကို Windows ထဲ ဆွဲယူမယ်
git clone https://github.com/Ayeminoo59/MLE.git
 
"""

"""
 3. Basic Workflow (နေ့စဉ်အသုံးများဆုံး)
File တွေကို ပြင်ဆင်ပြီးတိုင်း အဆင့်ဆင့်လုပ်ဆောင်ရမယ့် command များ ဖြစ်ပါတယ်။

git status - လက်ရှိ ဘယ် file တွေ ပြင်ထားသလဲ၊ ဘယ်အဆင့်ရောက်နေသလဲဆိုတာ စစ်ဆေးရန်။

git add <file> - ပြင်လိုက်တဲ့ file ကို stage လုပ်ရန် (သိမ်းဖို့ အသင့်ပြင်ခြင်း)။

git add . - ပြင်ထားတဲ့ file အားလုံးကို တစ်ခါတည်း stage လုပ်ရန်။

git commit -m "message" - ပြင်ဆင်ချက်တွေကို အတည်ပြုပြီး သိမ်းဆည်းရန်။

"""


"""
4. Branching & Merging (အဖွဲ့လိုက်လုပ်ဆောင်ခြင်း)
Feature အသစ်တွေ ထည့်တဲ့အခါ မူရင်း code တွေကို မထိခိုက်အောင် ခွဲထုတ်လုပ်ဆောင်ခြင်း ဖြစ်ပါတယ်။

git branch - ရှိနေတဲ့ branch စာရင်းကို ကြည့်ရန်။

git branch <branch-name> - Branch အသစ်တစ်ခု တည်ဆောက်ရန်။

git checkout <branch-name> - တခြား branch တစ်ခုသို့ ပြောင်းသွားရန်။

git checkout -b <branch-name> - Branch အသစ်ဆောက်ပြီး တစ်ခါတည်း ပြောင်းရန်။

git merge <branch-name> - Branch တစ်ခုကို လက်ရှိ branch ထဲသို့ ပေါင်းထည့်ရန်။

"""

"""
5. Remote Syncing (GitHub နဲ့ ချိတ်ဆက်ခြင်း)
ကိုယ့်စက်ထဲက code တွေကို Server ပေါ်တင်တာ ဒါမှမဟုတ် တခြားသူတင်ထားတာကို ယူတာတွေ လုပ်ဖို့ သုံးပါတယ်။

git remote add origin <url> - ကိုယ့်စက်က Git ကို GitHub/GitLab repository နဲ့ ချိတ်ဆက်ရန်။

git push -u origin <branch-name> - ကိုယ့်စက်ထဲက code တွေကို server ပေါ်သို့ တင်ပို့ရန်။

git pull - Server ပေါ်က နောက်ဆုံး update တွေကို ကိုယ့်စက်ထဲ ဆွဲယူရန်။

git fetch - Server ပေါ်က ပြောင်းလဲမှုတွေကို ကြည့်ရန် (Merge မလုပ်သေးဘဲ)။

"""

"""
6. Undoing Changes (အမှားပြင်ခြင်း)
မှားသွားတဲ့အခါ နောက်ပြန်ဆုတ်ဖို့ သုံးပါတယ်။

git log - အရင်က လုပ်ခဲ့သမျှ commit ရာဇဝင်တွေကို ကြည့်ရန်။

git checkout -- <file> - File တစ်ခုကို မပြင်ခင် မူလအတိုင်း ပြန်ဖြစ်အောင်လုပ်ရန်။

git reset --hard HEAD - အလုပ်လုပ်နေတဲ့ file တွေအားလုံးကို နောက်ဆုံး commit အတိုင်း ပြန်သွားရန်။
"""


"""
"""