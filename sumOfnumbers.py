# sumOfnumbers.py
# Michael Retalic-Solio
# CIS 115 (I01) Intro to Prog & Logic (2022FA)
# This program will ask the user to enter a series of positive numbers and will 
# display their sum. When the user enters a negative number the program will
# stop and display the sum

sumOf = 0 #creates variable
while True: #starts while loop to continue to evaluate program until a negative is entered
    x = int(input("Enter a number, to add, enter a negative number: ")) #takes user number input
    if x < 0: #breaks program when a negative number is entered
        break
    sumOf += x # adds numbers
print(sumOf) # prints sum