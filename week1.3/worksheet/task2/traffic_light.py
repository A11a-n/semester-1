"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Allan Aliko Mwambela
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input("Enter number of steps"))  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps
while systime < maxtime:
    systime += 1

    if state == "red" and systime % 15 == 4:
        state = "red_amber"
    elif state == "red_amber" and systime % 15 == 7:
        state = "green"
    elif state == "green" and systime % 15 == 12:
        state = "amber"
    elif state == "amber" and systime % 15 == 0:
        state = "red"
    
    print(f"Time {systime:03} State {state}")
# At the end of each step you should output the time and state using the statement on line 14