# PackageWeight.py
# Michael Retalic-Solio
# CIS 115 (I01) Intro to Prog & Logic (2022FA)
# This program will ask a user to input the weight of a package that they want
# to ship and will give them the appropriate price of that shipment. 

weight = float(input('How much does your package weigh in pounds? ')) #Assigns user input about weight of package to weight variable 
if weight <0:
    print("Sorry your package cannot be a negative weight")
elif weight <= 2: #Starts if statement to find out what category the package falls into
    print('The shipping cost for your package is: $1.50') # prints appropriate price for package
elif weight > 2 and weight <= 6: #If elif and else statements place package into appropriate category
    print('The shipping cost for your package is: $3.00')
elif weight > 6 and weight <= 10: #6-10
    print('The shipping cost for your package is: $4.00')
else: # above 10 
    print('The shipping cost for your package is: $4.75')
