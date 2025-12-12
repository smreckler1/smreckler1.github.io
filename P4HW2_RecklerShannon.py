#Title: Shannon Reckler
#Date: 10/26/25
#Assignment Name: P3HW2
#A brief description of the project: Assignment assess student understanding of decision structures

"""
Pseudocode

Initialize total_overtime_pay to 0
Initialize total_regular_pay to 0
Initialize total_gross_pay to 0
Initialize employee_count to 0

Prompt user: "Enter employee's name or 'Done' to terminate"
Read employee_name

WHILE employee_name is not "Done" DO:

    Prompt user: "How many hours did [employee_name] work?"
    Read hours_worked

    Prompt user: "What is [employee_name]'s pay rate?"
    Read pay_rate

    IF hours_worked > 40 THEN
        overtime_hours = hours_worked - 40
        regular_hours = 40
    ELSE
        overtime_hours = 0
        regular_hours = hours_worked
    ENDIF

    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    Add overtime_pay to total_overtime_pay
    Add regular_pay to total_regular_pay
    Add gross_pay to total_gross_pay
    Increment employee_count by 1

    Display employee payroll information:
        - Employee Name
        - Hours Worked
        - Pay Rate
        - Overtime Hours
        - Overtime Pay
        - Regular Pay
        - Gross Pay

    Prompt user: "Enter employee's name or 'Done' to terminate"
    Read employee_name

ENDWHILE

Display total number of employees: employee_count
Display total overtime paid: total_overtime_pay
Display total regular pay: total_regular_pay
Display total gross pay: total_gross_pay

"""
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

employee_name = input("Enter employee's name or 'Done' to terminate: ")

while employee_name != "Done":

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = overtime_pay + regular_pay

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    print(f"\nEmployee name:\t {employee_name}\n")
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
    print("--------------------------------------------------------------------------")
    print(
        f"{hours_worked:<15.1f}"
        f"{pay_rate:<15.2f}"
        f"{overtime_hours:<15.1f}"
        f"{overtime_pay:<15.2f}"
        f"${regular_pay:<14.2f}"
        f"${gross_pay:<10.2f}"
    )

    print()
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")    