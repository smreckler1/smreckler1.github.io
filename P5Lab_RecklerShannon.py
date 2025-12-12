#Title: Shannon Reckler
#Date: 11302025
#Assignment Name: P5 Lab
#A brief description of the project: Use of loops, functions and module import to complete assignments.
def disperse_change(amount):

    total_cents = int(round(amount * 100))  # convert to cents and round
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

def main():

    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    cash_given = float(input("How much cash will you put in the self-checkout? "))

    change_owed = cash_given - amount_owed

    if change_owed < 0:
        print("Insufficient funds provided.")
    elif change_owed == 0:
        print("Exact payment received. No change needed.")
    else:
        print(f"\nChange is: ${change_owed:.2f}")
        disperse_change(change_owed)


main()