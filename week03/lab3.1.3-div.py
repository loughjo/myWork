# Author John Loughnane

firstNumber = int(input('Enter the first number please : '))
secondNumber = int(input('Enter the second number please : '))

answer = firstNumber // secondNumber
remainder = firstNumber % secondNumber
print("{} divided by {} is {} with remainder {}".format(firstNumber, secondNumber, answer, remainder))