#Title: Shannon Reckler
#Date: 09282025
#Assignment Name: P1 HW 1
#A brief description of the project: For this assignment students will create a program that does some basic math on numbers that are entered.

print ("This program calculates and displays travel expenses\n")

budget = int(input('Enter Budget: '))
travel_destination = input('\nEnter your travel destination: ')
gas = int(input('\nHow much do you think you will spend on gas: '))
accommodations = int(input('\nApproximately, how much will you need for accomodation/hotel?: '))
food = int(input('\nLast, how much do you need for food?: '))

print ("\n---------Travel Expenses---------")

print(f'Location: {travel_destination}')
print(f'Initial Budget: {budget}\n')
print(f'Fuel: {gas}')
print(f'Accommodation: {accommodations}')
print(f'Food: {food}\n')

sum_result = budget - gas - accommodations - food

print(f'Remaining Balance: {sum_result}')