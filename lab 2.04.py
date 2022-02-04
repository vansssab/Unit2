'''
###########################
Lab 2.04
###########################
1. In your notebook
For each example below, predict what will be printed. Run the program and write down the output in your notebook.

Example 1
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[3])

    prediction: a , d                                           
    actual: a ,  d

Example 2
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 3])

    prediction: c
    actual: c

Example 3
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 6])

    prediction: a
    actual: e

Example 4
    a = ['a', 'b', 'c', 'd', 'e']
    a[3] = 'haha'
    print(a)

    prediction: ['a', 'b', 'c', 'haha', 'e']
    actual:['a', 'b', 'c', 'haha', 'e']

2. Create this game again using lists and indexes
--------------------------------------------------
Declare 10 prizes (prize0, prize1, prize2 at the top of your file), but store them all in a list.

User picks a number.

Print prize associated with the door user picked.

3. Create a quiz
--------------------------------------------------
Create a food quiz using lists and indexes.

List of 6 different foods.

Ask the user 8 vague questions to find out what their favorite food is using the list.

Update the score and print their top 2 favorite foods.

Hint: Use a search engine to find the largest number in a python list.

----------------------
​Starter code here​:
----------------------
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

##############################
Together in class:
##############################
Research nested lists and work through the following Examples:

Bonus Example 1
a = ['a', 'b', 'c', ['d', 'e']]
print(len(a))
Bonus Example 2
a = ['a', 'b', 'c', ['d', 'e']]
b = a[3]
print(b)
Bonus - In your Notebook
How would you access d from the list a? print(a[3][0])
'''
#game show
'''
prizes = ['1 million dollars', '$500,000', '$250,000', '$100,000', '$75,000', '$50,000', '$25,000', '$10,000', '$5,000', '$1,000']
guess = int(input("Choose a door for it's prize. "))
if guess == 1:
    print(prizes[0])
if guess == 2:
    print(prizes[1])
if guess == 3:
    print(prizes[2])
if guess == 4:
    print(prizes[3])
if guess == 5:
    print(prizes[4])
if guess == 6:
    print(prizes[5])
if guess == 7:
    print(prizes[6])
if guess == 8:
    print(prizes[7])
if guess == 9:
    print(prizes[8])
if guess == 10:
    print(prizes[9])
'''
#food guess
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1
user_input = input('Do you like food made from animals? ')
if user_input == 'y':
    score[2] = score[2] + 1
    score[4] = score[4] + 1
user_input = input('Do you like food are NOT round? ')
if user_input == 'y':
    score[2] = score[2] + 1
user_input = input('Do you like food that are fried? ')
if user_input == 'y':
    score[0] = score[0] + 1
    score[1] = score[1] +  1
    score[2] = score[2] +  1
    score[3] = score[3] +  1
    score[4] = score[4] +  1
user_input = input('Do you like food that are sweet? ')
if user_input == 'y':
    score[0] = score[0] + 1
    score[1] = score[1] + 1
    score[3] = score[3] + 1
user_input = input('Do you like food that are salty? ')
if user_input == 'y':
    score[2] = score[2] + 1
    score[4] = score[4] + 1
user_input = input('Do you like food that are round? ')
if user_input == 'y':
    score[0] = score[0] + 1
    score[1] = score[1] + 1
    score[3] = score[3] + 1
    score[4] = score[4] + 1
    score[5] = score[5] + 1
user_input = input('Do you like food that consists of mainly meat? ')
if user_input == 'y':
    score[2] = score[2] + 1

print(f"donuts score = {score[0]}, \n" 
    f"pancakes score = {score[1]}, \n" 
    f"bacon score = {score[2]}, \n"
    f"waffles score = {score[3]}, \n"
    f"eggs score = {score[4]}, \n"
    f"bagels score = {score[5]}.")


