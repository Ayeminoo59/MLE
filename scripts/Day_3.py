"""
def my_name():
    return 'Hello AyeMinOo'

print("welcome from my company"+ my_name())


def welcome_(name = "MGMG",age = 18):
    return f"{name},{age}"
  

print("hello" + welcome_("ayeminoo",17))



def student(*arg , **keyword):
    print(arg)
    print(keyword)

student('water', "minmin", name = "ayeminoo",   age = 18  )

num = (1,2,3,4)
my_list = [2,2,2,2,12]
def total_num(*arg):
    return sum(arg)

print(total_num(*num))
print(total_num(*my_list))


def info(name, age):
    print(f"Name: {name}, Age: {age}")

# 1. List/Tuple Unpacking (*)
my_data = ["Ayeminoo", 18]
info(*my_data)  # info("Ayeminoo", 18) နဲ့ အတူတူပဲ

# 2. Dictionary Unpacking (**)
my_dict = {"name": "Minmin", "age": 20}
info(**my_dict) # info(name="Minmin", age=20) နဲ့ အတူတူပဲ



my_dic = { "name":"ayeminoo" , "age": 28}


def info (**key_pair):
    for key,value in key_pair.items():
        print(f"{key} : {value}")

info(**my_dic)


my_dic = { "name":"ayeminoo" , "age": 28}
def info (name , age):
    print(name + " ", age)

info(**my_dic)


def master_function(*args,**keygs):
    print("လုပ်ငန်းစတင်နေပြီ")
    sub_function(*args,**keygs)
    

def sub_function(a,b):
    print(f"ရလဒ်မှာ {a+b} ဖြစ်ပါသည်")

my_list = [1,2,3,4,5]


master_function(*my_list,6)


# dictionary
#create dictionary

my_dic ={"name":"ayeminoo","age":28}

# data access လုပ်မယ်
print(my_dic["name"])
# ပိုစိတ်ချရ
print(my_dic.get("age"))
print(my_dic.get("city","Not found"))
print(len(my_dic))
print(my_dic.keys())
print(my_dic.values())
print(my_dic.items())

for key,value in my_dic.items():
    print(f"{key} : {value}")


amount = 5000.399

print (f"{amount:,.2f}MMK")

"""
# ၁။ အချက်အလက်
employees = [
    {'name': 'Thar Gyi', 'salary': 5000, 'expenses': [100, 200, 50]},
 
]

# ၂။ Level ခွဲတဲ့ Function (Salary တစ်ခုပဲ သုံးတယ်)
def get_level(salary):
    if salary >= 4000:
        return "Senior"
    else:
        return "Junior"

# ၃။ Net Pay တွက်တဲ့ Function (Salary နဲ့ Expenses အကုန်သုံးတယ်)
def calculate_net_pay(salary, *expenses):
    total_expense = sum(expenses)
    tax = salary * 0.05
    net_pay = salary - tax - total_expense
    return round(net_pay, 2)

# ၄။ Loop ပတ်ပြီး ရလဒ်ထုတ်ခြင်း
for emp in employees:
    # Function (၁) ကို ခေါ်ပြီး level ယူမယ်
    level = get_level(emp['salary'])
    
    # Function (၂) ကို ခေါ်ပြီး net pay တွက်မယ်
    net_result = calculate_net_pay(emp['salary'], *emp['expenses'])
    
    # f-string နဲ့ အဖြေထုတ်မယ်
    name_upper = emp['name'].upper()
    print(f"Employee: {name_upper} | Level: {level} | Net Pay: {net_result:,.2f} MMK")