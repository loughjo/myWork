#
# Author John Loughnane

grade = int(input("Enter a percentage : "))

if grade < 40:
    print("Fail")
elif grade < 50:
    print("Pass")
elif grade < 60:
    print("Merit2")
elif grade < 70:
    print("Merit1")
else:
    print("Distinction")