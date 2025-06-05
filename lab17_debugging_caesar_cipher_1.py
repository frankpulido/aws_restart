# Python 3.9.6
# Author: Frank Pulido
# Date: June 05, 2025
# Purpose: Using the debugger in AWS Cloud9 to debug Caesar Cipher Program
# File: lab11_analyze_insulin.py
# Encoding: ASCII (a subset of UTF-8)

# In a previous lab [LAB 13] I created a Caesar cipher program.
# This version of the program is buggy. We have to use a debugger to find the bug and fix it.

from datetime import datetime
updated = datetime(2025, 6, 5)

# Double the given alphabet
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Get a message to encrypt
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Get a cipher key
def getCipherKey():
    #shiftAmount = input("Please enter a key (whole number from 1-25): ")
    shiftAmount = int(input("Please enter a key (whole number from 1-25): ")) # Fixed casting to integer
    return shiftAmount

# Encrypt message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + cipherKey
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Decrypt message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Main program logic
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

# Main logic
runCaesarCipherProgram()

print()
print("The error occured after entering cipherKey. 'newPosition = position + cipherKey'. TypeError: unsupported operand type(s) for +: 'int' and 'str'")
print("The error was in Line 26, where the variable needed to be casted to INTEGER")
print()

days = datetime.now() - updated
print("Days since last update: {} days".format(days.days))
#print("Days since last update: {:.0f} days".format(days))
print()