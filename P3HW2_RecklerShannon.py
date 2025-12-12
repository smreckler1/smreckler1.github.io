#Title: Shannon Reckler
#Date: 10/26/25
#Assignment Name: P3HW2
#A brief description of the project: Assignment assess student understanding of decision structures

"""
Pseudocode

START program
DISPLAY message asking for employee's name
INPUT employee_name
DISPLAY message asking for number of hours worked
INPUT hours_worked
DISPLAY message asking for employee's pay rate
INPUT pay_rate
IF hours_worked > 40 THEN
    SET overtime_hours = hours_worked - 40
    SET regular_hours = 40
ELSE
    SET overtime_hours = 0
    SET regular_hours = hours_worked
CALCULATE regular_pay = regular_hours * pay_rate
CALCULATE overtime_pay = overtime_hours * (pay_rate * 1.5)
CALCULATE gross_pay = regular_pay + overtime_pay
DISPLAY line separator
DISPLAY employee_name
DISPLAY headers: Hours Worked, Pay Rate, Overtime, Overtime Pay, Regular Pay, Gross Pay
DISPLAY line separator
DISPLAY corresponding calculated values 
END program

"""

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

overtime_hours = 0
overtime_pay = 0
regular_hours = hours_worked
regular_pay = 0

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

regular_pay = regular_hours * pay_rate

gross_pay = regular_pay + overtime_pay

print("----------------------------------------")
print(f"Employee name: {employee_name}")
print(f"\n{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("--------------------------------------------------------------------------------------------")
print(f"{hours_worked:<15.1f}{pay_rate:<15.1f}{overtime_hours:<15.1f}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<15.2f}")
