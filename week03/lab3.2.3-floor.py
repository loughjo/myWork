# Author John Loughnane
# A program that takes in a float and outputs an int rounded
# down, you will need the math module math.floor()
import math
number = float(input("Enter a number: "))

roundDownNumber = math.floor(number)

print('{} floored is {}'.format(number, roundDownNumber))


