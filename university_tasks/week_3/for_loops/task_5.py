# Ask the user for a word
print("What word do you see?")
word = input()

# Display heading
print("\nDisplaying index positions...\n")

# Loop through each index position
for index in range(len(word)):

    # Display the index and character
    print(f"index {index}: {word[index]}")

# Final message
print("\nDone!")