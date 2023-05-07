# PackageWeight.py
# Michael Retalic-Solio
# CIS 115 (I01) Intro to Prog & Logic (2022FA)
# This program will ask a user to input a year from 1 to 25 and will output 
# the rise of sea level for that given year. Years should be input from 1 year
# to 25 years from now.

# Assigns the variable year to an input and aks the user for their input
year = float(input('Please select a year from 1 to 25 to see rise of water levels\n '))
# While loop, ensuring that the year entered is between 1 and 25, calculating
# correct level of rise
while year > 0 and year <= 25:
    level = year * 1.6 # Calculation for rise of sea level 
    total = f'{level:.4f}' #formats to the 4th decimal
    print(total, 'millimeters for this year')
    break # breaks loop 
if year <= 0 or year > 25:  # checks that year is within correct standards
        print('Sorry the year must be between 1 and 25 ') # tells user the input is not valid
