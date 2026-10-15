# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
username = input("Enter your name: ")
age = (input("Enter your age: "))
fav_colour = input("Enter your favorite colour: ")
# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.
with open("user_info.txt", "w") as file:
    file.write("Name: " + username + "\n")
    file.write("Age: " + age + "\n")
    file.write("Favorite colour: " + fav_colour + "\n")

print("Your details have been saved successfully!")

with open("user_info.txt", "r") as file:
    content = file.read()
print(content)
# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
