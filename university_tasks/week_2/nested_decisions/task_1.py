book = input("What kind of cover has the book (Soft/Hard)? ")

if book == "Soft":
    situation = input("Is the book perfect bound (Yes/No?) ")
    if situation == "Yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books.")

if book == "Hard":
    print("Books with hard covers can be more expensive!")
