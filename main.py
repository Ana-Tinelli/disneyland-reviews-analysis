import tui
import process
import visual
import export

# runs main program from title screen to menu loop
def main():
    tui.display_title()

# load the CSV data once when starts the program
    reviews = process.load_reviews_from_csv("disneyland_reviews.csv")

# confirm dataset loading and shows the row count
    tui.display_dataset_loaded_message(len(reviews))

    while True:
        tui.display_main_menu()
        user_choice = tui.get_user_menu_choice()
        tui.confirm_menu_choice(user_choice)

# open the view data submenu
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

            elif submenu_choice == "D":
                average_scores = process.get_average_score_per_park_by_location(reviews)
                tui.display_average_score_per_park_by_location(average_scores)

# open the visualisation submenu
        elif user_choice == 'B':
            tui.display_visualise_data_menu()
            submenu_choice = tui.get_submenu_choice()
            tui.confirm_visualise_data_choice(submenu_choice)

            if submenu_choice == "A":
                park_counts = process.get_review_counts_by_park(reviews)
                visual.plot_review_counts_by_park(park_counts)

            elif submenu_choice == "B":
                park_name = tui.get_park_name()
                top_locations = process.get_top_10_locations_by_average_rating(reviews, park_name)
                visual.plot_top_10_locations(top_locations, park_name)

            elif submenu_choice == "C":
                park_name = tui.get_park_name()
                monthly_averages = process.get_monthly_average_ratings_by_park(reviews, park_name)
                visual.plot_monthly_average_ratings(monthly_averages, park_name)

# open the export menu
        elif user_choice == "C":
            tui.display_export_menu()
            export_choice = tui.get_submenu_choice()
            tui.confirm_export_choice(export_choice)

            export_data = process.get_export_data_by_park(reviews)

            if export_choice == "A":
                txt_exporter = export.TXTExporter(export_data)
                txt_exporter.export("park_export.txt")
                tui.display_export_success_message("park_export.txt")

            elif export_choice == "B":
                csv_exporter = export.CSVExporter(export_data)
                csv_exporter.export("park_export.csv")
                tui.display_export_success_message("park_export.csv")

            elif export_choice == "C":
                json_exporter = export.JSONExporter(export_data)
                json_exporter.export("park_export.json")
                tui.display_export_success_message("park_export.json")

# exit the menu loop and end the program
        elif user_choice == "X":
            break


if __name__ == "__main__":
    main()

