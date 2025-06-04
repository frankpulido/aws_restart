print("Python has a string data type")
# String data type in Python

myString = "A text like this"
print(myString + " is of data type " + str(type(myString)))

# String concatenation in Python
mySecondString = "has no typos"
print(myString + " " + mySecondString)
print(myString, mySecondString)

myThirdString = "Water"
MyFourthString = "fall"
print(myThirdString + MyFourthString)

# Variable CLI input in Python (input function) and formatting with f-strings
# Curly braces are used to format strings in Python, pasing variables inside them
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("you are " + first_name + " " + last_name)
print("you are", first_name, last_name)
print("you are {} {}".format(first_name, last_name))