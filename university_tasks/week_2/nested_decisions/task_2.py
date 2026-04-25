print("You are looking for your phone... It was literally in your hand a second ago!")
room = (input("Where should I look? "))

if room == "in the bedroom":
    location = input("Where in the bedroom should I look? ")
    if location == "under the bed":
        print("Found some shoes but no phone.")
    else:
        print("Found some mess but no phone.")

elif room == "in the bathroom":
    location = input("Where in the bathroom should I look? ")
    if location == "in the bathtub":
        print("Found a rubber duck but no phone.")
    else:
        print("Found bathroom stuff but no phone.")

elif room == "in the living room":
    location = input("Where in the living room should I look? ")
    if location == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")

