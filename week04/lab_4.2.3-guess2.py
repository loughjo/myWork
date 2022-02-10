# modify the program in 3 (guess2.py) above, so that the
# program tells the user if there guess is too high or too low, each time they
# guess

# Author John Loughnane

numberToGuess = 30

guessTheNumber = int(input("Please guess the number : "))

while guessTheNumber != numberToGuess:
    if(guessTheNumber < numberToGuess):
        print("Too low")
        guessTheNumber = int(input("Please guess again : "))
    elif(guessTheNumber > numberToGuess):
        print("Too high")
        guessTheNumber = int(input("Please guess again : "))
print("Well done! Yes the number was ", guessTheNumber)
    
