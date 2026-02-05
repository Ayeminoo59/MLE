# this is 1 style of import method
"""
import Day3 
name_list = ["ayeminoo", "minmin", "pmk"]
result = Day3.find_index(name_list,"pmk")
print(result)

# this is second style of import method
import Day3 as D
name_list = ["ayeminoo", "minmin", "pmk"]
result = D.find_index(name_list,"pmk")
print(result)

/Users/ayeminoo/Desktop

# thi last style of import method
from Day3 import find_index
import sys

name_list = ["ayeminoo", "minmin", "pmk"]
result = find_index(name_list,"pmk")
print(result)
print(sys.path)


import os

# ၁။ အရင်ရှိနေတဲ့ နေရာကို ကြည့်မယ်
print("အရင်နေရာ:", os.getcwd())

# ၂။ Folder ပြောင်းမယ် (ဒါကို print ထုတ်စရာမလိုဘူး၊ သူက အလုပ်လုပ်ရုံပဲ)
os.chdir("/Users/ayeminoo/Desktop/ml")

# ၃။ ပြောင်းသွားတဲ့ နေရာသစ်ကို ပြန်စစ်မယ်
print("နေရာသစ်:", os.getcwd())
print()
print()
print(os.listdir())



# exist_ok=True ထည့်ရေးခြင်းဖြင့် Folder ရှိပြီးသားဖြစ်နေရင် Error မတက်အောင် ကာကွယ်ပေးတယ်
#os.makedirs("Class/Lesson1/Homework", exist_ok=True)
#os.makedirs("/Users/ayeminoo/Desktop/LUMITE/MINMIN")
#os.mkdir("/Users/ayeminoo/Desktop/panpan")
#os.rmdir("/Users/ayeminoo/Desktop/LUMITE/MINMIN")
#os.removedirs("/Users/ayeminoo/Desktop/LUMITE/MINMIN")
import os

# လက်ရှိ folder ထဲမှာ ရှိသမျှ အကုန်လုံးကို ပတ်ကြည့်မယ်
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('လက်ရှိလမ်းကြောင်း:', dirpath)
    print('Folder များ:', dirnames)
    print('File များ:', filenames)
    print('---')
    print("ြမန်မာမလေးပါရှင်")
    
    # အထူးတလည် import လုပ်စရာမလိုပါ
print("မင်္ဂလာပါ မြန်မာပြည်")

name = input("နာမည်လေး ပြောပါဦး: ")
print(f"နေကောင်းလား {name}")
# အရင်ဆုံး font ပြင်ပြီးမှ ဒါကို run ကြည့်ပါ
print("မင်္ဂလာပါ Cursor AI")
print("မြန်မာစာ output မှန်ကန်စွာ ပေါ်နေပြီလားခင်ဗျာ?")ပ

# standard font test

with open ("text2.txt","w")as f:
    f.write("HEllo ayeminoo")
    f.write("hello minmin\n")
    f.write("hello minmin\n")
    f.write("hello minmin\n")
    f.write("hello minmin\n")
    f.write("hello minmin\n")
    f.write("hello minmin\n")
    f.write("hello minmin\n")
    f.write("hello minmin\n")
    f.write("hello minmin\n")



with open("text2.txt","r")as f:
    for line in f:
        print(line)

"""