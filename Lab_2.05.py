'''
############################
Lab 2.05 - Tic-Tac-Toe
############################
In your Notebook
1. Predict what will be printed. Then run the program and confirm
Example 1
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[0:3])
print(a[1:4])

Prediction: a:c , b:e
Actual: ['a', 'b', 'c'] , ['b', 'c', 'd']

Example 2
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:len(a) - 3])

Prediction: ['b']
Actual:['b']

Example 3
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.remove('b')
print(a) 
print(b)

Prediction: ['a', 'b', 'c', 'd', 'e'] , ['a', 'c', 'd', 'e']
Actual: ['a', 'c', 'd', 'e'] , None

Example 4
---------
a = ['a', 'b', 'c', 'd', 'e']
a[0] = 'haha'
b = a.pop()
print(a)
print(b)

Prediction: ['haha', 'b', 'c', 'd', 'e'] , None
Actual: ['haha', 'b', 'c', 'd'] , e

Example 5
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a + ['abc']
print(a)
print(b)

Prediction: ['a', 'b', 'c', 'd', 'e'] , ['a', 'b', 'c', 'd', 'e']['abc']
Actual: ['a', 'b', 'c', 'd', 'e'] , ['a', 'b', 'c', 'd', 'e', 'abc']
Example 6
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.append('f')
print(a) 
print(b)

Prediction: ['a', 'b', 'c', 'd', 'e'] , ['a', 'b', 'c', 'd', 'e', 'f']
Actual: ['a', 'b', 'c', 'd', 'e', 'f'] , None
2. In script mode (Type your program below the multi-line comment)
We are going to start implementing Tic-Tac-Toe using a single list.
1. The user picks a location on the board according to the number:
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
2. Depending on the position that the user inputs, update the position of the board to an "X" to reflect
that.
    Example:
        1 | 2 | 3
        ---------
        4 | 5 | X
        ---------
        7 | 8 | 9
3. Print the updated board out, but don't worry about making it look pretty.
4. Only need to implement one turn of the game
'''
# tic tac toe
spots = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
    "--------- \n"
    f"{spots[3]} | {spots[4]} | {spots[5]} \n"
    "--------- \n"
    f"{spots[6]} | {spots[7]} | {spots[8]}")
print("Let's play Tic-Tac-Toe!")
mark = input("Where would you like to mark or put an x on? ")
if mark == '1':
    spots[0] = 'X'
elif mark == '2':
    spots[1] = 'X'
elif mark == '3':
    spots[2] = 'X'
elif mark == '4':
    spots[3] = 'X'
elif mark == '5':
    spots[4] = 'X'
elif mark == '6':
    spots[5] = 'X'
elif mark == '7':
    spots[6] = 'X'
elif mark == '8':
    spots[7] = 'X'
elif mark == '9':
    spots[8] = 'X'
else:
    print('Sorry, that is not a spot on the board.')

print(f"{spots[0]} | {spots[1]} | {spots[2]} \n"
    "--------- \n"
    f"{spots[3]} | {spots[4]} | {spots[5]} \n"
    "--------- \n"
    f"{spots[6]} | {spots[7]} | {spots[8]}")