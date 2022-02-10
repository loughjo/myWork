#
# Author John Loughnane

import random

tenRandomNumbers = 0
randomList = []

while tenRandomNumbers < 10:
    randomNumber = random.randint(1,100)
    randomList.append(randomNumber)
    tenRandomNumbers = tenRandomNumbers + 1

randomList.sort()
print(*randomList[7:10])