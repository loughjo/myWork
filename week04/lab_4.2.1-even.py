# A program that uses a while loop to print all the even numbers from 2 to 100.
# Author John Loughnane

endNumber = 100
number = 0
numberList = []

while number < endNumber:
    number += 2
    numberList.append(number)
print(*numberList)
 

