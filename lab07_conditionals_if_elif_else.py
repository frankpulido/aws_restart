# This program demonstrates the use of conditionals in Python.
print()
print("This program demonstrates the use of conditionals in Python.")
# We will use if, elif, and else statements to control the flow of the program based on conditions.
print()

choice = input("Do you want to deliver a packege? (yes/no): ")
if choice.lower() == "yes":
    print("Great! Let's get started with the delivery process.")
    package_weight = float(input("Enter the weight of the package in kg: "))
    
    while package_weight <= 0:
        package_weight = float(input("Invalid weight. Enter the weight of the package in kg: "))

    if package_weight < 5:
        print("This is a light package. Delivery will be quick! (next day)")
    elif package_weight < 20:
        print("This is a medium package. Delivery will take a bit longer (2-3 days)")
    else:
        print("This is a heavy package. Delivery can take upto a week.")
    print("Thank you for using our delivery service!")
else:
    print("No problem! If you change your mind, just let us know.")
print()