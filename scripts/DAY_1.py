# Day  1:  String  
# print message using print function
"""
my_message = "Hello,world!"
print(my_message)

# length of the string use len function
Length_my_message = len(my_message)
print(Length_my_message)

# lower case and upper case string use lower() and upper() function
print(my_message.lower())
print(my_message.upper())

# Use count of string use count() function 
print(my_message.count("H"))

# access character in the string use [] operator
print(my_message[4])
print(my_message[-1])

# slice string use [start:end] operator
print(my_message[0:5])

# find string use find() function
print(my_message.find("world"))

# replace string use replace() function
print(my_message.replace("world", "Yangon"))

new_message = my_message.replace("Yangon","Myanmar")

#combine string use + operator
greeting ='Hello'
name ="Ayeminoo"
message = greeting + ", " + name + "!"
print(message)

#f string use f-string function
greeting = "Hello"
name ="Ayeminoo"
message = f"{greeting}, {name} . welcome "


# dir function
print(dir(my_message))

# help function
print(help(str))


# Day 1: String Basics
# Senior တွေက code ကို logic အလိုက် စုစည်းတတ်ကြတယ်

message = "Hello, world!"

# Formatting strings (f-string က အကောင်းဆုံးပဲ)
greeting = "Hello"
name = "Ayeminoo"
full_message = f"{greeting}, {name}. Welcome!"
print(full_message)

# String manipulation
# Variable နာမည်တွေကို snake_case သုံးမယ်
message_length = len(message)
print(f"Length: {message_length}")

# Transformations (Method chaining ကိုလည်း သုံးတတ်ရမယ်)
print(message.lower())
print(message.upper())

# Search and Replace
# find() ထက် အခြေအနေပေါ်မူတည်ပြီး 'in' operator ကိုလည်း သုံးတတ်ရမယ်
if "world" in message:
    new_message = message.replace("world", "Yangon")
    print(new_message)

# Slicing
print(message[:5])   # 0 ကနေစရင် 0 ကို ထည့်ရေးစရာမလိုဘူး
print(message[-1:])  # နောက်ဆုံးစာလုံး


ml_model = {
    'algorithm': 'Random Forest',
    'accuracy': 0.95,
    'parameters': {'n_estimators': 100, 'max_depth': 10}
}
ml_model.update({'accuracy':0.98})
print(ml_model['parameters'].get("max_depth"))

ml_model = {
    'algorithm': 'Random Forest',
    'accuracy': 0.95
}
if ml_model['accuracy'] > 0.90 and ml_model['algorithm'] == 'Random Forest':
    print("Excellent Model")
elif ml_model['accuracy'] <  0.90 and ml_model['accuracy'] > 0.50:
    print("Average Model")


even_number = []

for i in range(1,101):
    if i == 50:
        break
    elif (i % 2) == 0:
        even_number.append(i)
    

print(even_number)

Task: ၁။ calculate_bonus ဆိုတဲ့ function တစ်ခုဆောက်ပါ။ 
သူက *args (လစာများ - salaries) နဲ့ **kwargs (အချက်အလက်များ - employee_info) ကို လက်ခံရမယ်။
 ၂။ အဲ့ဒီ function ထဲမှာ args ထဲက လစာတွေကို အကုန်ပေါင်းပါ။
  ၃။ ပြီးရင် kwargs ထဲက name ကို ယူပြီး "Employee [Name] has total salary of [Total]" 
  လို့ return ပြန်ပေးပါ။


  def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

# အထုပ်မဖြည်ဘဲ ထည့်ရင် - (မင်း ဒါကို အရင်ကြည့်ပါ)
student_info(courses, info)
# Result: 
# args   -> (['Math', 'Art'], {'name': 'John', 'age': 22})  <-- အထုပ်ကြီးအတိုင်း ရောက်သွားတယ်
# kwargs -> {}

# အထုပ်ဖြည် (Unpacking) ပြီး ထည့်ရင် -
student_info(*courses, **info)
# Result:
# args   -> ('Math', 'Art')  <-- တစ်ခုချင်းစီ ဖြစ်သွားပြီ
# kwargs -> {'name': 'John', 'age': 22} <-- Dictionary logic ဖြစ်သွားပြီ
"""

