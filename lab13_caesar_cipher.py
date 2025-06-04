# Python 3.9.6
# Author: Frank Pulido
# Date: June 04, 2025
# Purpose: Analyze the insulin sequence
# File: lab13_caesar_cipher.py
# Encoding: ASCII (a subset of UTF-8)

import math

def caesar_cipher(text, shift):
    """Encrypts the text using Caesar cipher with the given shift."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

print("Caesar Cipher Encryption Program")
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value (1-25): "))

while not (1 <= shift <= 25):
    shift = int(input("Invalid input. Please enter a number between 1 and 25: "))

encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)

# This program demonstrates the use of a Caesar cipher for text encryption.
# It is one of the simplest and most widely known encryption techniques.
# It takes a string input and a shift value, then encrypts the string by shifting each letter by the specified value.
# The program handles both uppercase and lowercase letters, leaving non-alphabetic characters unchanged.
# The Caesar cipher is a simple substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down or up the alphabet.
# The program includes input validation for the shift value to ensure it is within the range of 1 to 25.
# The main function orchestrates the input and output, calling the caesar_cipher function to perform the encryption.
# The encrypted text is printed to the console.
# The Caesar cipher is named after Julius Caesar, who reportedly used it to communicate with his generals.
# The program is a simple demonstration of encryption techniques in Python, showcasing basic string manipulation and control flow.