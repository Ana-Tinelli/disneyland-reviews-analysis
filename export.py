import csv
import json
from abc import ABC, abstractmethod

# Base for all export formats.
class Exporter(ABC):
    def __init__(self, data):
        self.data = data

    # Each exporter must define its own export method.
    @abstractmethod
    def export(self, file_name):
        pass

# Exports park summary data to a text file.
class TXTExporter(Exporter):
    def export(self, file_name):
        # Write each park summary in a readable text format.
        with open(file_name, "w", encoding="utf-8") as file:
            for park in self.data:
                file.write(f"Park Name: {park['park_name']}\n")
                file.write(f"Number of Reviews: {park['number_of_reviews']}\n")
                file.write(
                    f"Number of Positive Reviews: "
                    f"{park['number_of_positive_reviews']}\n"
                )
                file.write(
                f"Average Review Score: {park['average_review_score']}\n"
                )
                file.write(f"Number of Countries: {park['number_of_countries']}")
                file.write("\n")

# Exports park summary data to a CSV file.
class CSVExporter(Exporter):
    def export(self, file_name):
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write the column headings.
            writer.writerow([
                "Park Name",
                "Number of Reviews",
                "Number of Positive Reviews",
                "Average Review Score",
                "Number of Countries"
            ])

            # Write one row for each park.
            for park in self.data:
                writer.writerow([
                    park["park_name"],
                    park["number_of_reviews"],
                    park["number_of_positive_reviews"],
                    park["average_review_score"],
                    park["number_of_countries"]
                ])

# Exports park summary data to a JSON file.
class JSONExporter(Exporter):
    def export(self, file_name):
        with open(file_name, 'w', encoding="utf-8") as file:
            # save the summary data using an indented JSON format
            json.dump(self.data, file, indent=4)
