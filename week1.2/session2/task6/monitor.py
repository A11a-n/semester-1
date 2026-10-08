# Week 1.2, Session 2: Task 6
print("Monitor the status of your machine")



status = int(input("Enter machine's status (1 for operating, 0 for stopped): "))

if status == 1:
    print("Machine is currently operating")
    temperature = int(input("Enter machine's temperature: "))
    pressure = int(input("Enter machine's pressure: "))

    if temperature > 80:
        print("Temperature is too high, shut down the machine.")
    elif temperature < 50:
        print("Temperature is too low, no action needed.")
    else:
        print("Temperature is within safe limits.")

    if pressure > 100:
        print("Pressure is high, please conduct maintenance.")
    elif pressure < 70:
        print("Pressure is low, the system is operating normally.")
    else:
        print("Pressure is stable")
else:
    print("Machine is stopped. No immediate action is required.")
