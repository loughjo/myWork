# program (average.py) that keeps reading numbers until the user enters a 0. 
# (the program should append each of them into a list)
# The program should then print out each of the numbers entered and the average of them.

# Author John Loughnane

listOfNumbers = []
stop = 0
addNumbers = 0
numberEntered = int(input("Enter number (0 to quit) : "))

while numberEntered != stop: 
    listOfNumbers.append(numberEntered)
    addNumbers = numberEntered + addNumbers
    numberEntered = int(input("Enter number (0 to quit) : "))

averageOfNumbers = addNumbers / len(listOfNumbers)
print("The average is ",averageOfNumbers)



