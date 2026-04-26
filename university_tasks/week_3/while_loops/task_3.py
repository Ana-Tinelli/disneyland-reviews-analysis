# Ask the user how many bars should be charged
total_bars = int(input("How many bars should be charged? "))

# Variable to track charged bars
bars = 0

# Loop until all bars are charged
while bars < total_bars:
    print("Charging: ", end="") #keep all the same line
    bars += 1 # increment number of charged bars

    # Display bars visually
    print("█" * bars)

print("The battery is fully charged.")