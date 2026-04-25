# Ask user values
lives = int(input("Please enter the numbers of lives: "))
energy = int(input("Please enter the energy level: "))
shield = int(input("Please enter the shield level: "))

print("\nHealth has been set.\n")

# Display results using string multiplication
print(f"Lives: {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")