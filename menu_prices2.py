# menu_prices.py
# Michael Retalic-Solio
# CIS 115 (I01) Intro to Prog & Logic (2022FA)
# Calculate a tip, tax, and total price based on user input and display with all
# items ordered.

#1. Input: asks user to list their items ordered and asks for the total of the bill
print ("What was your lunch item? ")
lunch = input()
print ("what was your sweet? ")
sweet = input()
print ("what was your drink? ")
drink = input()

food_charge = float(input("What was the charge for your food? $"))

#2. process: calculates tip and sales tax and bill total for everything
tip_percentage = .18
sales_tax = .0475

tip = (food_charge * tip_percentage)
sales_tax = (food_charge * sales_tax)
bill_total = (food_charge + tip + sales_tax)

#3. Output: completes calculations and lists items order with grand total
print("Items ordered:", lunch, "with", sweet, "and", drink)
print("Charge for food = $" , format(food_charge, ",.2f"), sep = "")
print("Tip = $" , format(tip, ",.2f"), sep = "")
print("Sales tax = $", format(sales_tax, ",.2f"), sep = "")
print("Bill total = $", format(bill_total, ",.2f"), sep = "")
