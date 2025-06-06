# Author: Frank Pulido
# Date: June 06, 2025
# Purpose: Convert a decimal number to binary representation
# File: binary_conversion.py
# Encoding: ASCII (a subset of UTF-8)
# Python 3.9.6

# This code provides three methods to convert a decimal number (0-255) to its binary representation.
# The code is structured to ensure that the user inputs a valid number within the specified range.
# The binary representations are padded to 8 bits for consistency.

# The first method uses a custom approach (Maribel's method) for 8-bit (1 byte) only, the second uses an iterative approach that works regardless of the number of bits, and the third uses Python's built-in formatting (also for any number of bits).
# The user can input a number, and the program will display the binary representation using all three methods.
# The program continues to prompt for input until the user decides to exit.


def maribel_method(number: int) -> str:
    binary = ''
    for value in [128, 64, 32, 16, 8, 4, 2, 1]:
        if number >= value:
            binary += '1'
            number -= value
        else:
            binary += '0'
    return binary

def iterative_method(number: int) -> str:
    binary_iterative = ''
    temp = number
    while temp > 0:
        modulus = temp % 2
        temp = temp // 2
        binary_iterative = str(modulus) + binary_iterative
    return binary_iterative.zfill(8)

def builtin_method(number: int) -> str:
    return format(number, '08b')

def main():
    while True:
        while True:
            print()
            user_input = input("Enter a number between 0 and 255: ").strip()
            if user_input.isdigit():
                my_number = int(user_input)
                if 0 <= my_number <= 255:
                    break
        
        binary_maribel = maribel_method(my_number)
        binary_iterative = iterative_method(my_number)
        binary_builtin = builtin_method(my_number)

        print(f"Binary representation using Maribel's method : {binary_maribel}")
        print(f"Binary representation using iterative method: {binary_iterative}")
        print(f"Binary representation using built-in function: {binary_builtin}")
        print()

        exit_input = input("Enter 0 to exit or any other key to continue: ").strip()
        if exit_input == '0':
            break
    print("Exiting the program. Thank you for using the binary conversion tool!")
    print()

if __name__ == "__main__":
    main()