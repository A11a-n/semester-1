# Worksheet 1.2: Task 2 Solution
from util import read_numbers

numbers = read_numbers()
max_num = max(numbers)
min_num = min(numbers)
average = sum(numbers) / len(numbers)

numbers.sort()
length = len(numbers)

if length % 2 == 1:
    median = numbers[length // 2]
else:
    median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2

print(f"Maximum number is {max_num}")
print(f"Minimum number is {min_num}")
print(f"Mean number is {average}")
print(f"Median number is {median}")
