# mathQuiz.py
# Michael Retalic-Solio
# CIS 115 (I01) Intro to Prog & Logic (2022FA)
# This program will give the user a simple math quiz. The program will first
# give two random numbers to be added. The user will input an answer to the 
# question. If correct, the program will congratulate the user. If not correct
# the program will issue the correct answer.

# imports random integer to generate a random number 
from random import randint 

def generateRandom(): # function to generate random number
    randomNumber = randint(0, 1000) # sets limits of random number
    return randomNumber # returns random number to function

def addNum(numA, numB): # function to add two numbers with parameters
    addedSum = numA + numB # adding those numbers together 
    return addedSum # return to function

def mathQuiz(numA, numB): # formats the question to look like a math problem
    print(" ", numA) # print statements for first number 
    print("+", numB) # second number
    print("_______") # line under addition problem

def answerCheck(correctAnswer, userInput): # checks the user input against 
    # the correct answer
    if correctAnswer == userInput: # if input is equal to correct answer
        return True
    return False

def main(): # main function where 
    numA = generateRandom() # generates a random number for numA
    numB = generateRandom() # generates a random number for numB
    correctAnswer = addNum(numA, numB) # calls function for numbers
    mathQuiz(numA, numB) # calls function for quiz
    userInput = int(input("What is the answer? ")) # takes input for the math problem
    while userInput != -999: # while loop with sentinel of -999
        if answerCheck(correctAnswer, userInput): # checks input answer 
            print("Congratulations, your answer is correct!"), main() # prints congrats
        else:
            print("Sorry, the correct answer was:", + correctAnswer), main() # prints sorry

main() # calls main function

    
    





