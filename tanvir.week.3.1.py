try:
    hours = int(input("Enter hours worked: "))
    rate = float(input("Enter rate of salary: "))

    if hours <= 40:
        salary = hours * rate
        print("Total Salary", end="")
    else:
        regular_hours = 40
        overtime_hours = hours - 40
        overtime_rate = 1.5 * rate
        salary = (regular_hours * rate) + (overtime_hours * overtime_rate)
        print(" Total Salary", end="")

    print(": $", salary)
except ValueError:
    print("Error! Please enter numaric values only.")
