# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
with open("student_data.csv", "r") as file:
    lines = file.readlines()

with open("report.txt", "w") as report:
    report.write("Student Grade Report\n")
    report.write("====================\n")

for line in lines[1:]:
    data = line.strip().split(",")

    student_id = data[0]
    name = data[1]
    maths = float(data[2])
    science = float(data[3])
    history = float(data[4])

    average = (maths + science + history) / 3

    report.write(f"{name}: {average:.2f}\n")

print ("Report created successfully")
# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3

# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
