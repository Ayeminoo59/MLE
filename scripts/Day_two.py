
expenses = [
    {"item":"chickern", "Amount":500, "Category":"FOOD"},
    {"item":"TV", "Amount":1000, "Category":"For home"},
    {"item":"PEN", "Amount":10, "Category":"For school"}
]
total_amount = 0

for cost_goods in expenses:
    print("\n__ EXPENSES INFO __")
    print("   _________________  \n")
    for key, value in cost_goods.items():
        if key == "Amount":
            total_amount += value
      
        print(f"{key} : {value}")
print("TOTAL_AMOUNT :", total_amount)


# Output တစ်ခုချင်းစီကို loop ပတ်ပြီး key-value အကုန်ထုတ်ပေးသွားမှာပါ။
