print("This is my second file")
import sys
print(sys.version)
number1 = 5
number2 = 10
print("$number1 + $number2 = " + str(number1 + number2))
print("$number1 - $number2 = " + str(number1 - number2))
print("$number1 * $number2 = " + str(number1 * number2))
print("$number1 / $number2 = " + str(number1 / number2))
print("$number1 % $number2 = " + str(number1 % number2))

# The IF statement
if number1 > number2:
    print("$number1 is greater than $number2")
elif number1 < number2:
    print("$number1 is less than $number2")
else:
    print("$number1 is equal to $number2")

# Casting
x = str(3.55)
print(x)
print(type(x)) # <class 'str'> (x)
x = int(3.55)
print(x)
print(type(x)) # <class 'int'> (x)
x = float(3.55)
print(x)
print(type(x)) # <class 'float'> (x)

# WRONG : The input function + casting
number1 = int(input("Enter a number: ")) # This will cast the input to an integer, breaks if the input is not an integer
print(number1)

# RIGHT : The input function + casting
number1 = int(float(input("Enter a number: ")))
# This will cast the input to an integer, but to avoid breaking the program, we first cast it to a float
print(number1)
# Output : The input function + casting