"""
LISTS
"""
# We start by creating a list. We use square brackets
print("Creating a list of fruits")
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print("The type of myFruitList is: " + str(type(myFruitList)))
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
print()

# Let's take a step ahead trying random function
import random
print("Random fruit from the list:")
print(random.choice(myFruitList))
print()

# Change an element, lists are variables
print("Changing the third element of the list from 'cherry' to 'orange'... Lists are mutable")
myFruitList[2] = "orange"
print(myFruitList)
print()
print()

"""
TUPLES
"""
#We start by creating a tuple, we use parentheses
print("Creating a tuple of fruits. We use parentheses. Tuples are immutable")
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print("The type of myFinalAnswerTuple is: " + str(type(myFinalAnswerTuple)))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
print()

# Let's take a step ahead trying random function
# import random # Already imported in Line 14. Note: random.choice works with both lists and tuples
print("Random fruit from the tuple:")
print(random.choice(myFinalAnswerTuple))
print()

#We cannot change tupple elements, the tupple is a constant
print("Lists elements can be modiifed, tupple elements cannot, the tupple is a constant")
print("Trying to change the third element of the tuple from 'pineapple' to 'orange' will cause an error")
print()
print()

"""
DICTIONARIES
"""
# A dictionary is an associative list keys=>values
print("Creating a dictionary of fruits. We use curly braces. Dictionaries are mutable associative lists. Keys are unique")
myFavoriteFruitDictionary = {
  "Laura" : "apple",
  "Frank" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print()

# We can access elements using the keys
print("We can access the elements using the keys. Frank's favorite fruit is " + myFavoriteFruitDictionary["Frank"])
print()

# We can also change the value associated to any key
print("Changing Frank's favorite fruit from 'banana' to 'kiwi'...")
myFavoriteFruitDictionary["Frank"] = "kiwi"
print("Frank's favorite fruit is now " + myFavoriteFruitDictionary["Frank"])
print()

# We can add new key-value pairs
print("Adding a new key-value pair to the dictionary...")
myFavoriteFruitDictionary["Alice"] = "orange"
print(myFavoriteFruitDictionary)
print()

# We can remove key-value pairs
print("Removing Alice's favorite fruit from the dictionary...")
del myFavoriteFruitDictionary["Alice"]
print(myFavoriteFruitDictionary)
print()

# We can check if a key exists in the dictionary
print("Checking if 'Laura' is in the dictionary...")
if "Laura" in myFavoriteFruitDictionary:
    print("Yes, Laura is in the dictionary")
else:
    print("No, Laura is not in the dictionary")
print()

# We can iterate over the dictionary
print("Iterating over the dictionary...")
for key, value in myFavoriteFruitDictionary.items():
    print(f"{key}'s favorite fruit is {value}")
print()

# We can get all keys and values
print("Getting all keys and values from the dictionary...")
print("Keys:", myFavoriteFruitDictionary.keys())
print("Values:", myFavoriteFruitDictionary.values())
print()

# We can get the length of the dictionary
print("Getting the length of the dictionary...")
print("The dictionary has " + str(len(myFavoriteFruitDictionary)) + " key-value pairs")
print()