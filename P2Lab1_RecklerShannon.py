#Title: Shannon Reckler
#Date: 10042025
#Assignment Name: P2 Lab 1
#A brief description of the project: Assignment tests student's knowledge of how to write code that performs mathematical calculations and displays information to users.

import math

radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print(f"The diameter of the circle is {diameter:.1f}.")
print(f"The circumference of the circle is {circumference:.2f}.")
print(f"The area of the circle is {area:.3f}.")