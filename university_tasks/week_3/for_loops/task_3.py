# Ask user for brightness level
print("What level of brightness is required?")
brightness_desired = int(input())

# Adjust brightness
print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_desired + 1, 2):
    print(f"Brightness level: {'*' * brightness}")

print("Complete!")