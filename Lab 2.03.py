'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction: Either you go on, the bridgekeeper gets thrown over the bridge, or you get thrown over the bridge.
Actual: Go on. Off you go.

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction: Something different is said for each color that is inputted in.
Actual: A different thing is said whenever you put in different colors.

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
#triangle_lab_program
'''
x = input("What is x? ")
y = input("What is y? ")
z = input("What is z? ")
if int(x) + int(y) > int(z) and int(x) + int(z) > int(y) and int(y) + int(z) > int(x):
    perimeter = int(x) + int(y) + int(z)
    print(f"The perimeter of the triangle is {perimeter}")
    if int(x) * int(x) + int(y) *int(y) == int(z) * int(z):
        print("This is a right triangle.")
    elif int(x) == int(y) and int(y) == int(z):
        print("This is an equilateral triangle.")
    elif int(z) == int(x) or int(z) == int(y) or int(x) == int(y):
        print("This is an isosceles triangle.")
    else: 
        print("This is a scalene triangle.")
else:
    print("Sorry, those inputs don't make a triangle.")
'''
#game_show_program
prize1 = ("1 million dollars!")
prize2 = ("$500,000!")
prize3 = ("$250,000!")
prize4 = ("$100,000!")
prize5 = ("$75,000!")
prize6 = ("$50,000!")
prize7 = ("$25,000!")
prize8 = ("$10,000!")
prize9 = ("$5,000!")
prize10 = ("$1,000!")
number = input("Choose a door with the numbers between 1 and 10. ")
if int(number) == 1:
    print(f" Your prize is {prize1}")
elif int(number) == 2:
    print(f"Your prize is {prize2}")
elif int(number) == 3:
    print(f"Your prize is {prize3}")
elif int(number) == 4:
    print(f"Your prize is {prize4}")
elif int(number) == 5:
    print(f"Your prize is {prize5}")
elif int(number) == 6:
    print(f"YOur prize is {prize6}")
elif int(number) == 7:
    print(f"Your prize is {prize7}")
elif int(number) == 8:
    print(f"Your prize is {prize8}")
elif int(number) == 9: 
    print(f"YOur prize is {prize9}")
else:
    print(f"Your prize is {prize10}")





