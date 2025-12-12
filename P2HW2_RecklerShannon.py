#Title: Shannon Reckler
#Date: 10/12/2025
#Assignment Name: P2 HW 2
#A brief description of the project: Assignment assess student understanding of Lists

module_one = float(input('Enter grade for Module 1: '))
module_two = float(input('Enter grade for Module 2: '))
module_three = float(input('Enter grade for Module 3: '))
module_four = float(input('Enter grade for Module 4: '))
module_five = float(input('Enter grade for Module 5: '))
module_six = float(input('Enter grade for Module 6: '))

grades = [
    module_one,
    module_two,
    module_three,
    module_four,
    module_five,
    module_six
    ]

lowest= min(grades)
highest= max(grades)
sum= sum(grades)
average= sum / len(grades)

print ("\n------------Results-----------")

print(f"{'Lowest Grade: ':15}{lowest:>15,.1f}")
print(f"{'Highest Grade: ':15}{highest:>15,.1f}")
print(f"{'Sum of Grades: ':15}{sum:>15,.1f}")
print(f"{'Average: ':15}{average:>15,.2f}")

print ("-------------------------------")

