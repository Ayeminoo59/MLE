


print("Smart Expense & Bonus Tracker")

employee = []

# Put employee data function 

def put_employee_data():
    
    name = input("Enter your name :").upper()
    salary = float(input("Enter your salary :"))
    # expense more than one
    expense_list =[]
    print("Expense တွေရိုက်ပါ (ပြီးရင် '0' ရိုက်ပြီး ပိတ်ပါ):")
    while True:
        amount = float(input("Enter amount : "))
        if amount == 0:
            break
        expense_list.append(amount)

    employe = {
        "Name":name,
        "Salary":salary,
        "Expense":expense_list
    }
    employee.append(employe)

def calculate_net_pay(salary, *expense):
    
    total_expense = sum(expense)
    
    # အခွန် ၅% ကို အရင်ရှာမယ်
    # တစ်ခုရှိတာ company ရဲ့  logic မူလလစာထဲကအခွန်ဖျက်လို အခွန်ဖျက်တာကြမ်း
    tax = salary * 0.05
    
    # လစာထဲက အခွန်ရော၊ အသုံးစရိတ်ပါ နှုတ်မယ်
    net_pay = salary - tax - total_expense
    
    return round(net_pay, 2)

def get_level(salary):
    if salary >= 4000:
        return "Senior"
    else :
        return "Junior"
   
 
# Show detail employes list
def show_list_employes():
     print(employee)
#net_pay = (salary - expenses )* (1-0.05)

# This is main function program run from this 
def main():
    while True:
        print(
            """\n
              press 1 for put employee data \n 
              press 2 for show list employes data \n
              press 3 for Net pay result and level\n
              press 4 for exit\n
        """)
        
        user_choice = int(input("Please enter number :"))

        if user_choice == 1:
            put_employee_data()
        elif user_choice == 2:
            show_list_employes()
        elif user_choice == 3:
            for emp in employee:
                level = get_level(emp['Salary'])
                # need to unpacking import list to calculate net pay function
                net_result = calculate_net_pay(emp['Salary'],*emp['Expense'])
                name_upper = emp['Name'].upper()
                if net_result <= 0:
                    print ("\nBanance Alert\n")
                else:
                    print(f"\nEmployee: {name_upper} | level : {level} | Netpay :{net_result:,.2f} MMK\n")
                
        elif user_choice == 4:
            print ("Thank! have a nice day")
            break
        else:
            print("You can only choose between 1 to 3")


main()