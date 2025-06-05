# Python 3.9.6
# Author: Frank Pulido
# Date: June 05, 2025
# Purpose: Using the debugger in AWS Cloud9
# File: lab11_analyze_insulin.py
# Encoding: ASCII (a subset of UTF-8)

from datetime import datetime
updated = datetime(2025, 6, 5)

name = "John"
print("Hello " + name + ".")
age = 40
print(name + " is " + str(age) + " years old.")


print()
days = datetime.now() - updated
print("Days since last update: {} days".format(days.days))
#print("Days since last update: {:.0f} days".format(days))
print()