# Step 1: Create and write to a file
file = open("students.txt", "w") # Open file in write mode (creates file if it does not exist)

file.write("John\n") # Write data to the file
file.write("Mary\n")
file.write("David\n")

file.close() # Close the file after writing

print("Data written to file successfully.")

# Step 2: Read from the file
file = open("students.txt", "r") # Open file in read mode

print("\nReading data from file:")

for line in file: # Loop through each line in the file
       print(line.strip()) # strip() removes extra newline spaces

file.close() # Close the file after reading

