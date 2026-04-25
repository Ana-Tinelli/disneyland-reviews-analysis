# Program 2: Take user input and save to file

file = open("students.txt", "a")   # Open file in append mode

name = input("Enter student name: ")

file.write(name + "\n")   # Save input to file

file.close()

print("Student saved successfully.")

