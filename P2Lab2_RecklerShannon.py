#Title: Shannon Reckler
#Date: 10042025
#Assignment Name: P2 Lab 2
#A brief description of the project: Assignment tests student's knowledge of how to write code that uses a dictionary to store user input and displays output to the user.

my_dict = {
    "Camaro" : 18.21,
    "Prius" : 52.36,
    "Model S" : 110,
    "Silverado" : 26
}

keys = my_dict.keys()

print(keys)

vehicle_choice = input("Enter a vehicle to see it's mpg: ")

mpg = my_dict[vehicle_choice]

print(f"The {vehicle_choice} gets {mpg} mpg.")

miles = float(input(f"How many miles will you drive the {vehicle_choice}? "))

gallons_needed = miles / mpg

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle_choice} {miles} miles.")