# Program 3: Read a specific line from file

file = open("students.txt", "r")   # Open file in read mode

lines = file.readlines()   # Store all lines in a list

if len(lines) >= 2:
    print("Second line:", lines[1].strip())   # Print second line
else:
    print("Not enough data in file.")

file.close()
