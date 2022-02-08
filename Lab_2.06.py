'''
#################
Lab 2.06
#################
1. In your Notebook
-------------------
Predict what will be printed then type the program in your console to confirm
Example 1
    a = 0
    while a < 10:
        print(a)

prediction: 0
actual: repeated 0

Example 2
    a = 0
    while a < 10:
        a = a + 1
        print(a)

prediction: 1
actual: 1 2 3 4 5 6 7 8 9 10

2. In your Notebook
-------------------
Create a set of test cases for the following sample code and predict the behavior
    a = input("Would you like to quit: ")
    while a != "y" and a != "n" :
        a = input("Would you like to quit: ")

test cases: 'y', 'n', 'q', 'cat'
    It will repeat the question unless 'y' or 'n' is an answer.
3. Implement the Tic Tac Toe game using a while loop
----------------------------------------------------
Allow users to keep playing (max 9 times).

Use variables to decide whose turn it is, and greet them as Xs or Os.

User picks a location on the board according to the number:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9


Depending on the position user gave, update the corresponding position of the board to reflect that.

Print the updated board out.

You will not need to determine the winner at this point.
(Copy and paste your previous tic-tac-toe version and modify the code to implement the above)
'''
#test cases
'''
test_cases = ['y', 'n', 'q', 'cat']
a = input("Would you like to quit: ")
while a != "y" and a != "n" :
    a = input("Would you like to quit: ")
'''
#tic tac toe
spots = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
square = ''
turns = 0
print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
    "--------- \n"
    f"{spots[3]} | {spots[4]} | {spots[5]} \n"
    "--------- \n"
    f"{spots[6]} | {spots[7]} | {spots[8]}")
print("Let's play Tic-Tac-Toe!")
while turns < 9:
    print("The first player will be X and the second player will be O.")
    while spots[square - 1] == 'X' or spots[square - 1] == 'O':  
        square = int(input("Which square would you like to mark? "))
    if turns == 1:
        spots[square - 1] = 'X'
    elif turns == 2:
        spots[square - 1] = 'O'
    elif turns == 3:
        spots[square - 1] = 'X'
    elif turns == 4:
        spots[square - 1] = 'O'
    elif turns == 5:
        spots[square - 1] = 'X'
    elif turns == 6:
        spots[square - 1] = 'O'
    elif turns == 7:
        spots[square -1 ] = 'X'
    elif turns == 8:
        spots[square - 1] = 'O'
    elif turns == 9:
        spots[square -1] = 'X'
    else:
        print('Sorry, that is not a spot on the board.')
    turns[0] = turns[0] + 1
    print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
    "--------- \n"
    f"{spots[3]} | {spots[4]} | {spots[5]} \n"
    "--------- \n"
    f"{spots[6]} | {spots[7]} | {spots[8]}")
    