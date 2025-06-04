import csv
import copy
import random
import json

# Composite Data Types in Python
# Composite data types are data structures that can hold multiple values or other data types.
# They include lists, tuples, dictionaries, and sets.
# They can contain mixed data types, including other composite data types.

print()
print("Composite Data Types in Python")
print("We start defining a dictionary with mixed data types to read from a CSV file")

# This code defines a dictionary to hold vehicle information and reads data from a CSV file into it.
# The dictionary contains various fields such as VIN, make, model, year, range, top speed, zero to sixty time, and mileage.
# We can change the value associated to any key

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():
    print(f"{key}: {value} (Type: {type(value)})")
print()

# We need  an empty list to hold the vehicle inventory we will read from the CSV file
myVehicleInventory = []

# We define a function to read data from a CSV file and populate the dictionary
def read_csv_to_dict(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            myVehicle["vin"] = row["vin"]
            myVehicle["make"] = row["make"]
            myVehicle["model"] = row["model"]
            myVehicle["year"] = int(row["year"])
            myVehicle["range"] = int(row["range"])
            myVehicle["topSpeed"] = int(row["topSpeed"])
            myVehicle["zeroSixty"] = float(row["zeroSixty"])
            myVehicle["mileage"] = int(row["mileage"])
            print(f"Read vehicle: {myVehicle}")
            # Append a copy of the vehicle to the inventory
            myVehicleInventory.append(copy.deepcopy(myVehicle))
    # Return the last vehicle read from the CSV file
    #return myVehicle
print()

# We populate the vehicle inventory and print the dictionary
read_csv_to_dict("lab06_car_fleet.csv") # Assuming the CSV file is in the same directory as this script
print()
print("Vehicle data read from CSV file:")
print(myVehicleInventory)
print()
print()
i=1
for element in myVehicleInventory:
    print(f"Vehicle {i}: {element}, Type: {type(element)}")
    i += 1
    print()

print()

# We can print the inventory as a for each loop
print("Vehicle Inventory:")
for vehicle in myVehicleInventory:
    print(vehicle)
print()

# We can also use a random function to select a vehicle from the inventory
random_vehicle = random.choice(myVehicleInventory)
print("Randomly selected vehicle from inventory:")
print(random_vehicle)
print()


quit()





# We can also convert the dictionary to a JSON string
myVehicle_json = json.dumps(myVehicle, indent=4)
print("Vehicle JSON representation:")
print(myVehicle_json)
print()

# We can also convert the dictionary to a JSON string and write it to a file
def write_dict_to_json_file(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
write_dict_to_json_file(myVehicle, "vehicle.json")

# We can also read the JSON string from a file and convert it back to a dictionary
def read_json_to_dict(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Read the JSON file and print the dictionary
myVehicle_from_json = read_json_to_dict("vehicle.json")
print("Vehicle data read from JSON file:")
print(myVehicle_from_json)

