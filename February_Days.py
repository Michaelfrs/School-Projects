# February_Days.py
# Michael Retalic-Solio
# CIS 115 (I01) Intro to Prog & Logic (2022FA)
# Ask user to input a year and program will test if that year was a leap year or not. 

year = int(input("Enter a year: "))
message = ""

if year > 0 : 
    message = "In " + format (year) + " February was "
    
    if year % 100 == 0 : 
        if year % 400 == 0 :
            message += "a leap"
        else : 
            message += "not a leap"
    else : 
        if year % 4 == 0 : 
            message += "a leap"
        else : 
            message += "not a leap"
    message += " year."

else:
    message = "Please enter a year greater than 0 and try again"

print(message)