import csv

# File ကို ဖတ်ဖို့ ဖွင့်တယ်
with open('name.csv', 'r') as csv_file:
    # DictReader ကို သုံးလိုက်ရင် row တစ်ခုချင်းစီက dictionary ဖြစ်သွားမယ်
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # column နာမည်နဲ့ တိုက်ရိုက်ခေါ်လို့ရပြီ
        print(line['first_name'], line['email'])