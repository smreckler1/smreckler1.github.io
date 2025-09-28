#Title: Shannon Reckler
#Date: 09282025
#Assignment Name: P1 HW 1
#A brief description of the project: Assignment tests student's knowledge of how to write code that collects information from user, processes information collected and display results to user.

print ("-----Calculating Exponents-----")

base_value = int(input('Enter an integer as the base value: '))
exponent = int(input('Enter an integer as the exponent: '))

exp_result = base_value ** exponent

print (f"{base_value} raised to the power of {exponent} is {exp_result} !!\n")

print ("-----Addition and Subtraction----")

starting_integer = int(input('Enter a starting integer: '))
add = int(input('Enter an integer to add: '))
subtract = int(input('Enter an integer to subtract: '))

sum_result = starting_integer + add - subtract

print(f"{starting_integer} + {add} - {subtract} is equal to {sum_result}")