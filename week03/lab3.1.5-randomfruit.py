# Author John Loughnane

# A program that chooses a random fruit
import random

fruitList = ["Apple", "Plum", "Grapes", "Oranges", "Pear", "Banana", "Tomato", "Cherries", "Lemon", "Lime"]

random_index = random.randint(0,len(fruitList)-1)

print(fruitList[random_index])