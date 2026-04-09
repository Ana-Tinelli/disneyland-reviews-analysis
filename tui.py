def display_title():
    title = "Disneyland Review Analyser"
    border = "_" * len(title)

    print(border)
    print(title)
    print(border)

def display_dataset_loaded_message(row_count):
    print("\nDataset has been loaded successfully.")
    print(f"Number of rows in the dataset: {row_count}")

def display_main_menu():
    print("\nPlease enter the letter which corresponds with your desired menu choice:")
    print("   [A] View Data")
    print("   [B] Visualise Data")
    print("   [X] Exit")

def get_user_menu_choice():
    choice = input("\nEnter your choice: ")
    return choice.upper()

def confirm_menu_choice(choice):
    if choice == "A":
        print("\nYou have chosen option A - View Data")

    elif choice == "B":
        print("\nYou have chosen option B - Visualise Data")

    elif choice == "X":
        print("\nYou have chosen option X - Exit")

    else:
        print("\nInvalid menu choice. Please try again.")

def display_view_data_menu():
    print("\nPlease enter one of the following options:")
    print("   [A] View Reviews by Park")
    print("   [B] Numbers of Reviews by Park and Reviewer Location")
    print("   [C] Average Score per year by Park")
    print("   [D] Average Score per Park by Reviewer Location")

def display_visualise_data_menu():
    print("\nPlease enter one of the following options:")
    print("   [A] Most reviewed Parks")
    print("   [B] Park Ranking by Nationality")
    print("   [C] Most Popular Month by Park")

def get_submenu_choice():
    choice = input("\nEnter your submenu choice: ")
    return choice.upper()

def confirm_view_data_choice(choice):
    if choice == "A":
        print("\nYou selected submenu option A - View Reviews by Park")
    elif choice == "B":
        print("\nYou selected submenu option B - Number of Reviews by park and Reviewer Location")
    elif choice == "C":
        print("\nYou selected submenu option C - Average Score per year by Park")
    elif choice == "D":
        print("\nYou selected submenu option D - Average Score per Park by Reviewer Location")
    else:
        print("\nInvalid submenu choice. Please try again.")

def confirm_visualise_data_choice(choice):
    if choice == "A":
        print("\nYou selected submenu option A - Most reviewed Parks")
    elif choice == "B":
        print("\nYou selected submenu option B - Park Ranking by Nationality")
    elif choice == "C":
        print("\nYou selected submenu option C - Most Popular Month by Park")
    else:
        print("\nInvalid submenu choice. Please try again.")