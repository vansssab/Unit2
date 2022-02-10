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
turns = 0
print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
    "--------- \n"
    f"{spots[3]} | {spots[4]} | {spots[5]} \n"
    "--------- \n"
    f"{spots[6]} | {spots[7]} | {spots[8]}")
print("Let's play Tic-Tac-Toe!")
print("The first player will be X and the second player will be O.")
while turns < 9:
    print("Player 1")  
    mark = input("Which square would you like to mark? ")
    if mark == '1':
        spots[0] = 'X'
        turns = turns + 1
    elif mark == '2':
        spots[1] = 'X'
        turns = turns + 1
    elif mark == '3':
        spots[2] = 'X'
        turns = turns + 1
    elif mark == '4':
        spots[3] = 'X'
        turns = turns + 1
    elif mark == '5':
        spots[4] = 'X'
        turns = turns + 1
    elif mark == '6':
        spots[5] = 'X'
        turns = turns + 1
    elif mark == '7':
        spots[6] = 'X'
        turns = turns + 1
    elif mark == '8':
        spots[7] = 'X'
        turns = turns + 1
    elif mark == '9':
        spots[8] = 'X'
        turns = turns + 1
    else:
        print('Sorry, that is not a spot on the board.')
        turns = turns + 1
    print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
    "--------- \n"
    f"{spots[3]} | {spots[4]} | {spots[5]} \n"
    "--------- \n"
    f"{spots[6]} | {spots[7]} | {spots[8]}")
    print("Player 2")
    mark = input("Which square would you like to mark? ")
    if mark == '1':
        spots[0] = 'O'
        turns = turns + 1
    elif mark == '2':
        spots[1] = 'O'
        turns = turns + 1
    elif mark == '3':
        spots[2] = 'O'
        turns = turns + 1
    elif mark == '4':
        spots[3] = 'O'
        turns = turns + 1
    elif mark == '5':
        spots[4] = 'O'
        turns = turns + 1
    elif mark == '6':
        spots[5] = 'O'
        turns = turns + 1
    elif mark == '7':
        spots[6] = 'O'
        turns = turns + 1
    elif mark == '8':
        spots[7] = 'O'
        turns = turns + 1
    elif mark == '9':
        spots[8] = 'O'
        turns = turns + 1
    else:
        print('Sorry, that is not a spot on the board.')
        turns = turns + 1
    print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
    "--------- \n"
    f"{spots[3]} | {spots[4]} | {spots[5]} \n"
    "--------- \n"
    f"{spots[6]} | {spots[7]} | {spots[8]}")
    