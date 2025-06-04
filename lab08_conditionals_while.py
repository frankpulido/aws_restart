import random

print()
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number from 1 to 10, and you will try to guess it.")
print()

number = random.randint(1, 10)  # Random number between 1 and 10
attempts = 0
guessed_correctly = False

while not guessed_correctly: # Works as != (false)
    guess = input("Enter your guess (1-10): ")
    while not guess.isdigit() or not (1 <= int(guess) <= 10):
        guess = input("Invalid input. Please enter a number between 1 and 10: ")
    guess = int(guess)
    attempts += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        guessed_correctly = True
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        print("Congratulations, you have guessed the number {} in {} attempts.".format(number, attempts))
print("Thank you for playing!")
print()

# How to iterate through a list of numbers
print("Iterating through a list of numbers:")
for x in range(1, 11):
    print(f"Number: {x}")
print()