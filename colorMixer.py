# colorMixer.py
# Michael Retalic-Solio
# CIS 115 (I01) Intro to Prog & Logic (2022FA)
# This program asks for the user to pick two colors from magenta, yellow, or cyan and the program will give the appropriate mixed color. The program will then change the background of Turtle to the correct color picked. 

import turtle

#Assigning colors needed for input to variables
m = "magenta"
y = "yellow"
c = "cyan"
g = "green"
b = "blue"
r = "red"

#This portion introduces what the program will do and takes the users input for the colors. 
firstColor = input("You will choose two colors and the program will blend them together. You may choose from magenta, yellow, or cyan. What is your first color? \n").lower()
secondColor = input("What is your second color? \n").lower()

#This portion takes the user input and tests what the outcome will be and displays it in Turtle
if firstColor == secondColor:
    turtle.bgcolor(firstColor)
else:
    if firstColor == y or firstColor == c:
        if secondColor == c or secondColor == y:
            turtle.bgcolor(g)
        else:
            if firstColor == y:
                turtle.bgcolor(r)
            else:
                turtle.bgcolor(b)
    else:
        if secondColor == c:
            turtle.bgcolor(b)
        else:
            turtle.bgcolor(r)

turtle.done()


