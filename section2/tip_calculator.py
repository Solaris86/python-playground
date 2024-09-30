print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people_count = int(input("How many people to split the bill? "))

bill_amount_per_person = (total_bill + total_bill * tip / 100) / people_count
bill_amount_per_person_rounded = round(bill_amount_per_person, 2)
print(f"Each person should pay: ${bill_amount_per_person_rounded}")