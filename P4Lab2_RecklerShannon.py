#Title: Shannon Reckler
#Date: 11/2/25
#Assignment Name: P4 Lab 2
#A brief description of the project: Assignment assess student understanding of decision structures

integer_lab = "yes"

while integer_lab.lower() == "yes":
    number = int(input("Enter an integer: "))

    print()

    if number >= 0:
        for i in range(1, 13):  
            print(f"{number} x {i} = {number * i}")
    else:
        print("This program does not handle negative numbers.")

    print()  
    integer_lab = input("Would you like to run the program again? ")

print("\nExiting program. . .")