move = input("Enter the direction which the robot should move\n(up, down, left or right) ")

if move == "up":
    print("I am moving in an upward direction!")
elif move == "down":
    print("I am move in a downward direction!")
elif move == "left":
    print("I am move in a leftward direction!")
elif move == "right":
    print("I am move in a rightward direction!")
else:
    print("The position should be: up, down, right or left!")