# Worksheet 1.2: Task 2 Solution
from util import read_numbers

numbers = read_numbers()
if numbers.isdigit():
    numbers = float(numbers)
    print("Digits read")
else:
    print("Error: no numbers provided")
