'''
##################################
Lab 2.02 Booleans & Expressions
##################################
In your Notebook
Predict if each of the following examples will produce a True or False output. Check your answers in interactive mode.
                 
Example 1
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b == "science"       Prediction:                     Actual:
Example 2
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b != "science"       Prediction:                     Actual:
Example 3
    >>> a = 100
    >>> b = "science"
    >>> a > 75 or b != "science"        Prediction:                     Actual:
Example 4
    >>> a = 100
    >>> b = "science"
    >>> c = True
    >>> not c and a > 75 and b == "science"     Prediction:                     Actual:

In your Console

Complete the following coding challenge
Create a "Can I be President?" program, which determines if the user meets the minimum requirements for becoming the President of the United States. 
Have the user input the information needed.

The minimum requirements to be president of the United States are:

1. Older than 35

2. Resident of US for 14 Years

3. Natural born citizen

Print True if the person could be president and False if they can't be president.

Create a "I can't be President?" program. Print True if the user cannot be President and False if they can be President.

Create a "Can I ride the roller coaster?" program. A roller coaster has the rule that a rider has to be over the height of 50 inches. Because of a legal loophole, if you are over the age of 18 you can ride regardless of your height. If you are allowed to ride, the coaster costs 4 quarters (although the operator accepts tips so more money is appreciated).

Also, the theme park sells frequent rider passes: with a frequent rider pass the roller coaster costs only 2 quarters. Ask the user how tall they are in inches, their age, how many quarters they have, and if they have a frequent rider pass. Print True if the person can ride and False if they can't.


Are the following expressions equivalent? Research DeMorgan's Laws and write why you think they are the same or why they are not the same
not(x or y) == not x and not y 
  The following expressions are not equivlent. The or in the first espression indicates that at least one statement is true. The and in the second expression indicates that both statements are true. 
not(x and y) == not x or not y
'''
'''
age = 35
resident_of_US = 14
natural_born_citizen = True
can_become_president = age >= 35 and resident_of_US >=14 and natural_born_citizen
print(can_become_president)
'''
'''
age = 16
resident_of_US = 12
natural_born_citizen = False
cannot_become_president = age < 35 and resident_of_US < 14 and not natural_born_citizen
print(cannot_become_president)
'''
#Can I Ride a Roller Coaster?

height = input("How tall are you in inches? ")
age = input("What is your age? ")
quarters = input("How many quarters do you have? ")
frequent_rider_pass = input("Do you have a frequent rider pass? ")
can_ride_the_roller_coaster = int(height) > 50 or int(age) > 18 and int(quarters) > 4 or frequent_rider_pass
print(can_ride_the_roller_coaster)
