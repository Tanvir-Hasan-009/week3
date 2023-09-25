try:
    score = int(input("Your_Enter_Score: "))
    
    if score < 0 or score > 100:
        print("Please enter a numeric input between 0 and 100.")
    else:
        if score >= 90:
            print("A", end="")
        elif score >= 80:
            print("B", end="")
        elif score >= 70:
            print("C", end="")
        elif score >= 60:
            print("D", end="")
        else:
            print("F", end="")
    
        print(" Grade")  # Moved "Grade" inside the else block to print the grade label
    
except ValueError:
    print("Please enter a numeric input between 0 and 100.")
