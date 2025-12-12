#Title: Shannon Reckler
#Date: 10192025
#Assignment Name: P3 Lab
#A brief description of the project: Assignment tests student's knowledge of how to write code that displays information to users.

amount = float(input("Enter the amount of money as a float: $"))

total_cents = int(amount * 100)

change = {}

dollars = total_cents // 100
total_cents -= dollars * 100
if dollars > 0:
    change["Dollar"] = dollars

quarters = total_cents // 25
total_cents -= quarters * 25
if quarters > 0:
    change["Quarter"] = quarters

dimes = total_cents // 10
total_cents -= dimes * 10
if dimes > 0:
    change["Dime"] = dimes

nickels = total_cents // 5
total_cents -= nickels * 5
if nickels > 0:
    change["Nickel"] = nickels

pennies = total_cents
if pennies > 0:
    change["Penny"] = pennies

for coin, count in change.items():
    if count == 1:
        print(f"{count} {coin}")
    else:
        if coin == "Penny":
            print(f"{count} Pennies")
        else:
            print(f"{count} {coin}s")
