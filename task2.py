#!python3

# Reciprocal
# have the program iterate through the list and determine the
# reciprocal of each number as a decimal and print it.
# use the try/except to find any invalid values and display
# the error message

#sample output:
"""
The reciprocal of 0 does not exist
The reciprocal of 1 is 1.0
The reciprocal of 2 is 0.5
The reciprocal of 3 is 0.3333333333333333
The reciprocal of 4 is 0.25
"""


numbers = [0,1,2,3,4]

try:
    x = int(input("enter a number from : "))
    y = 1/x
    print(f"the reciprocal of {x} is " + str(y))
except:
    print(f"the reciprocal of {x} does not exist")