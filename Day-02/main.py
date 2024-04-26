print("Welcome to tip calculator")
bill = float(input( "what was the total bill\n"))
tip = int(input("how much tip you will like to give 10, 15, 20 \n"))
people = int(input("how many will you like to split with \n"))
tip_as_percent = tip/100
totat_tip_amount = tip_as_percent* bill
total_bill = bill + totat_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
print(f" Each person should pay {final_amount}")