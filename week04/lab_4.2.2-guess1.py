# a program (guess1.py) that prompts the user to guess a number, the
# program should keep prompting the user to guess the number until the user
# gets the right on
# Author John Loughnane

guessThisNumber = 42

numberGuessed = int(input("Please guess the number : " ))

while numberGuessed != guessThisNumber:
    print("wrong")
    numberGuessed = int(input("Please guess again : " ))

print("Well done. Yes the number was {}".format(numberGuessed))
