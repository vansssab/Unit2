'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''
name = input("What is you name? ")
age = int(input("How old are you? "))
current_year = int(input("What is the current year? "))
birth_year = current_year - age
year_turn_100 = birth_year + 100
print(f"You will turn 100 in {year_turn_100}.")
repeat = int(input("Give me a random number. "))
print(f"You will turn 100 in {year_turn_100}. \n" * repeat) 


