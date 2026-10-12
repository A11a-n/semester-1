# Worksheet 1.2: Task 1 Solution
import sys
grade = input("Enter an integer between 0 and 100: ")

if grade.isdigit():
    grade = int(grade)
    if grade >= 0 and grade <= 100:
        if grade > 69:
            print(f"{grade} is a Distinction")
        elif grade < 40:
            print(f"{grade} is a Fail")
        else:
            print(f"{grade} is a Pass")
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100.")
else:
    sys.exit("Error: Grade must be an integer between 0 and 100.")