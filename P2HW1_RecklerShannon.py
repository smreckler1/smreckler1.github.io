#Title: Shannon Reckler
#Date: 10122025
#Assignment Name: P2 HW 1
#A brief description of the project: Assignment assess student ability to edit and enhance exiting programs

print ("This program calculates and displays travel expenses\n")

budget = float(input('Enter Budget: '))
travel_destination = input('\nEnter your travel destination: ')
gas = float(input('\nHow much do you think you will spend on gas: '))
accommodations = float(input('\nApproximately, how much will you need for accomodation/hotel?: '))
food = float(input('\nLast, how much do you need for food?: '))

print ("\n------------Travel Expenses-----------")

print(f"{'Location: ':15}{travel_destination:>15}")
print(f"{'Initial Budget: ':15}{f'${budget:,.2f}':>15}")
print(f"{'Fuel: ':15}{f'${gas:,.2f}':>15}")
print(f"{'Accommodation: ':15}{f'${accommodations:,.2f}':>15}")
print(f"{'Food: ':15}{f'${food:,.2f}':>15}")
print ("----------------------------------------")

sum_result = budget - gas - accommodations - food

print(f"{'\nRemaining Balance: ':15}{f'${sum_result:,.2f}':>12}")