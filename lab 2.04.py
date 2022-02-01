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

    prediction: (blank)
                 a, b, c                                           
    actual: a
            d

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

    prediction: a b c haha e
    actual: ['a', 'b', 'c', 'haha', 'e']

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
How would you access d from the list a?  
'''
#game_show
a = ['1 milllion dollars', '$500,000', '$250,000', '$100,000', '$75,000', '$50,000', '$25,000', '$10,000', '$5,000', '$1,000']
number = input("Choose a door with the numbers between 1 and 10. ")
'''
if int(number) == 1:
    print(a[1])
elif int(number) == 2:
    print(a[2])
elif int(number) == 3:
    print(a[3])
elif int(number) == 4:
    print(a[4])
elif int(number) == 5:
    print(a[5])
elif int(number) == 6:
    print(a[6])
elif int(number) == 7:
    print(a[7])
elif int(number) == 8:
    print(a[8])
elif int(number) == 9: 
    print(a[9])
else:
    print(a[10])
'''
#favorite_food
ood = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','bagles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[6] = score[6] + 1
user_input = input('Do you like food made from animals? ')
if user_input == 'y':
    score[3] = score[3] + 1
    score[5] = score[5] + 1
user_input = input('Do you like food that are sweet? ')
if user_input == 'y':
    score[1] = score[1] + 1
user_input 