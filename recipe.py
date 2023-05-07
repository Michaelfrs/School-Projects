# recipe.py
# Michael Retalic-Solio
# CIS 115 (I01) Intro to Prog & Logic (2022FA)
#Using a recipe, ask user how many cookies they woould like to make and calculate appropriate amounts of ingredients. 

#1. Input: asks user how many cookies they want to make
number_of_cookies = float(input("How many cookies are you making? "))

#2. Process: variables are original recipe and totals are calculations for new recipe
cookies = 48 
molasses = 1.5 
butter = 1
flour = 2.75
oats = 2

total_molasses = (molasses * number_of_cookies) / cookies
total_butter = (butter * number_of_cookies) / cookies
total_flour = (flour * number_of_cookies) / cookies
total_oats = (oats * number_of_cookies) / cookies

#3. Output: does calculations and prints new recipe and instructions
print("Number of cookies = " , number_of_cookies)
print("Total cup(s) of molasses = " , format(total_molasses, ".3f"))
print("Total cup(s) of butter = " , format(total_butter, ".3f"))
print("Total cup(s) of flour = " , format(total_flour, ".3f"))
print("Total cup(s) of oats = " , format(total_oats, ".3f"))
print("Directions: Mix all the dry ingredients together, then add the wet ingredients. Roll into 3-in balls onto a baking sheet.")
    