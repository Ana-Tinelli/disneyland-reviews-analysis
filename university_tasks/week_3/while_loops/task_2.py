total = int(input("How many obstacles must I avoid? "))

avoided = 0

while avoided < total:
    print("Avoiding...", end="") #keep all the same line
    avoided += 1
    print(f"Done! {avoided} obstacles avoided.")

print("All obstacles have been avoided.")