import csv
import os

input_file = "students_records_with_scores.csv"
output_file = "students_results.csv"

# Check if file exists
if not os.path.exists(input_file):
    print("Error: Input file not found!")
else:
    with open(input_file, "r", newline="") as file:
        reader = csv.reader(file)

        header = next(reader, None)  # Safe header skip
        print("Header:", header)  # Debug: confirm file is read

        with open(output_file, "w", newline="") as output:
            writer = csv.writer(output)

            writer.writerow(["Category", "Student Name", "Score", "Grade"])

            print("\nSTUDENT RESULTS\n")

            count = 0  # To check if loop runs

            for row in reader:
                if not row:  # Skip empty rows
                    continue

                name = row[0]
                score = int(row[5])
                grade = row[6]

                if score > 70:
                    category = "Above 70"
                elif 60 <= score <= 69:
                    category = "60 - 69"
                else:
                    category = "Below 60"

                # Display on screen
                print(category, "-", name, "| Score:", score, "| Grade:", grade)

                # Write to file
                writer.writerow([category, name, score, grade])

                count += 1

            if count == 0:
                print("No data found in CSV file!")

    print("\nResults have been saved to", output_file)
