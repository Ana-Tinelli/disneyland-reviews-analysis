# displays the application title with border
def display_title():
    title = "Disneyland Review Analyser"
    border = "_" * len(title)

    print(border)
    print(title)
    print(border)

# shows confirmation of CSV dataset loading
def display_dataset_loaded_message(row_count):
    print("\nDataset has been loaded successfully.")
    print(f"Number of rows in the dataset: {row_count}")

# displays the main menu options to the user
def display_main_menu():
    print("\nPlease enter the letter which corresponds with your desired menu choice:")
    print("   [A] View Data")
    print("   [B] Visualise Data")
    print("   [C] Export Data")
    print("   [X] Exit")

# confirms the user main menu choice or displays invalid choice
def get_user_menu_choice():
    choice = input("\nEnter your choice: ")
    return choice.upper()

def confirm_menu_choice(choice):
    if choice == "A":
        print("\nYou have chosen option A - View Data")

    elif choice == "B":
        print("\nYou have chosen option B - Visualise Data")

    elif choice == "C":
        print("\nYou have chosen option C - Export Data")

    elif choice == "X":
        print("\nYou have chosen option X - Exit")

    else:
        print("\nInvalid menu choice. Please try again.")

# displays the view data submenu options
def display_view_data_menu():
    print("\nPlease enter one of the following options:")
    print("   [A] View Reviews by Park")
    print("   [B] Numbers of Reviews by Park and Reviewer Location")
    print("   [C] Average Score per year by Park")
    print("   [D] Average Score per Park by Reviewer Location")


# displays the visualisation submenu options
def display_visualise_data_menu():
    print("\nPlease enter one of the following options:")
    print("   [A] Most reviewed Parks")
    print("   [B] Park Ranking by Nationality")
    print("   [C] Most Popular Month by Park")

# gets the user submenu choice
def get_submenu_choice():
    choice = input("\nEnter your submenu choice: ")
    return choice.upper()

# confirm the selected view data option
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

# gets the park name from the user
def get_park_name():
    park_name = input("\nEnter the park name: ")
    return park_name

# displays all reviews for the selected park
def display_reviews_by_park(park_name, reviews):
    if len(reviews) == 0:
        print(f"\nNo reviews found for {park_name}.")
    else:
        print(f"\nReviews for {park_name}: ")

        for review in reviews:
            print(review)

# gets the reviewer's location from the user
def get_reviewer_location():
    location = input("\nEnter the reviewer location: ")
    return location

# displays the review count for a park and location
def display_review_count_result(park_name, reviewer_location, review_count):
    print(f"\n{park_name} has {review_count} reviews from {reviewer_location}.")

# gets the year from the user
def get_year():
    year = input("\nEnter the year: ")
    return year

# displays the average park rating for a selected year
def display_average_score_result(park_name, year, average_score):
    if average_score is None:
        print(f"\nNo reviews found for {park_name} in {year}.")
    else:
        print(f"\nThe average rating for {park_name} in {year} is {average_score:.2f}.")

def display_average_score_per_park_by_location(average_scores):
    print("\nAverage score per park by reviewer location:\n")

    for park_name, locations in average_scores.items():
        print(park_name)

        for location, average_score in locations. items():
            print(f"  {location}: {average_score:.2f}")

        print()

def display_export_menu():
    print("\nPlease select an export format:")
    print("   [A] TXT")
    print("   [B] CSV")
    print("   [C] JSON")

def confirm_export_choice(choice):
    if choice == "A":
        print("\nYou selected TXT export.")
    elif choice == "B":
        print("\nYou selected CSV export.")
    elif choice == "C":
        print("\nYou selected JSON export.")
    else:
        print("\nInvalid export choice. Please try again.")

def display_export_success_message(file_name):
    print(f"\nData Exported successfully to {file_name}.")



