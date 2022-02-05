# Author John Loughnane
# program that takes in a float amount of dollars, and returns that absolute amount in cent

floatAmount = float(input("Enter an amount : "))

amount = abs(floatAmount)
amount = int(amount * 100)

print('That amount in cent is :{}'.format(amount))
