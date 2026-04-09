import tui
import process

def main():
    tui.display_title()

    reviews = process.load_reviews_from_csv("disneyland_reviews.csv")
    tui.display_dataset_loaded_message(len(reviews))

    while True:
        tui.display_main_menu()
        user_choice = tui.get_user_menu_choice()
        tui.confirm_menu_choice(user_choice)

        if user_choice == "A":
            tui.display_view_data_menu()
            submenu_choice = tui.get_submenu_choice()
            tui.confirm_view_data_choice(submenu_choice)

            if submenu_choice == "A":
                park_name = tui.get_park_name()
                park_reviews = process.get_reviews_by_park(reviews, park_name)
                tui.display_reviews_by_park(park_name, park_reviews)

            elif submenu_choice == "B":
                park_name = tui.get_park_name()
                reviewer_location = tui.get_reviewer_location()
                review_count = process.count_reviews_by_park_and_location(reviews, park_name, reviewer_location)
                tui.display_review_count_result(park_name, reviewer_location, review_count)

            elif submenu_choice == "C":
                park_name = tui.get_park_name()
                year = tui.get_year()
                average_score = process.get_average_score_by_park_and_year(reviews, park_name, year)
                tui.display_average_score_result(park_name, year, average_score)


        elif user_choice == 'B':
            tui.display_visualise_data_menu()
            submenu_choice = tui.get_submenu_choice()
            tui.confirm_visualise_data_choice(submenu_choice)

        if user_choice == "X":
            break

if __name__ == "__main__":
    main()

