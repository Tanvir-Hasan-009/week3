count = 0
total = 0

while True:

    user_input = input("Enter a number: ")
    if user_input == 'Done':
        break

    try:
        num = float(user_input) 
        total += num
        count += 1

    except ValueError:
        print("Invalid input, enter a number.")

if count > 0:

    average = total / count
    print("Sum of numbers:", total)
    print("Number of inputs:", count)
    print("Average of the numbers:", average)
    

else:
    print("No valid numbers entered.")
