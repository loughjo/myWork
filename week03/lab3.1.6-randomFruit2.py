# Author John Loughnane

# A program that chooses a random fruit
import random

# Create a Tuple with items of fruit. Tuples use round brackets and lists square brackets
fruitList = ("Apple", "Plum", "Grapes", "Oranges", "Pear", "Banana", "Tomato", "Cherries", "Lemon", "Lime")

random_index = random.randint(0,len(fruitList)-1)

print(fruitList[random_index])