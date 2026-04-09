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

        elif user_choice == 'B':
            tui.display_visualise_data_menu()
            submenu_choice = tui.get_submenu_choice()
            tui.confirm_visualise_data_choice(submenu_choice)

        if user_choice == "X":
            break

if __name__ == "__main__":
    main()

