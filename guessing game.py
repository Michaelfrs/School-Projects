import random 

true_number = random.randint(1, 100)

guess_number = int(input("Please guess a number between 1 and 100 "))

while True:
    if guess_number == true_number:
        print("You are right!")
        break
        
    elif guess_number < true_number:
        print("Try again your guess is low!")
        guess_number = int(input("Please enter another guess between 1 and 100 "))
        
    elif guess_number > true_number:
        print("Your guess is too high try again")
        guess_number = int(input("Please enter another number"))
