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
#code goes here
name = input("What is your name? ")
age = input("What is your age? ")
year = input("What is the current year? ")
years_until_100 = 100 - int(age)
year_turn_100 = int(year) + years_until_100
when_turn_100 = (f"You will turn 100 in {year_turn_100}.\n")
print(when_turn_100)
copies = input("Give me a number. ")
print(when_turn_100 * int(copies))