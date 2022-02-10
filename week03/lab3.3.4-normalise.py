# 
# Author John Loughnane

aString = input("Enter a string : ")
lengthOfString = len(aString)
lowerCase = aString.lower()
removeTrailingSpaces = lowerCase.strip()
newStringLength = len(removeTrailingSpaces)

print('The string normalised is : {}\nwe reduced the input string from {} to {}'.format(removeTrailingSpaces,lengthOfString,newStringLength))