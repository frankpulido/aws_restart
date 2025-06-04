# Mixed data type Lists
print("Creating a mixed data type list with integers, floats, strings, bolleans and a tuple")
mixedList = [1, 2.5, "apple", True, (3, 4)]
print(mixedList)
print("The type of mixedList is: " + str(type(mixedList)))
print("The first element is: " + str(mixedList[0]) + " of type " + str(type(mixedList[0])))
print("The second element is: " + str(mixedList[1]) + " of type " + str(type(mixedList[1])))
print("The third element is: " + str(mixedList[2]) + " of type " + str(type(mixedList[2])))
print("The fourth element is: " + str(mixedList[3]) + " of type " + str(type(mixedList[3])))
print("The fifth element is: " + str(mixedList[4]) + " of type " + str(type(mixedList[4])))
print()

# Let's simplify the code above using for each loop
print("Using a for loop to print each element in the mixed list:")
for element in mixedList:
    print(f"Element: {element}, Type: {type(element)}")
print()
print("Again, using .format() to print each element in the mixed list:")
for element in mixedList:
    print("Element: {}, Type: {}".format(element, type(element)))
print()

# Let's take a step ahead trying random function
import random
print("Random element from the mixed list:")
print(random.choice(mixedList))