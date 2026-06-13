import csv


# Reads the csv file and stores each review row in a list.
def load_reviews_from_csv(file_name):
    reviews = []

    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row:
                reviews.append(row)

    return reviews

# Returns all reviews for the select park.
def get_reviews_by_park(data, park_name):
    matching_reviews = []

    # Format user input to match the CSV naming style.
    user_input = park_name.strip().lower().replace(" ", "_")

    for review in data:
        park_from_csv = review[4].strip().lower()

        if park_from_csv == user_input:
            matching_reviews.append(review)

    return matching_reviews

# Counts reviews for a selected park and reviewer location.
def count_reviews_by_park_and_location(data, park_name, reviewer_location):
    count = 0

    user_park = park_name.strip().lower().replace(" ", "_")
    user_location = reviewer_location.strip().lower()

    for review in data:
        park_from_csv = review[4].strip().lower()
        location_from_csv = review[3].strip().lower()

        if park_from_csv == user_park and location_from_csv == user_location:
            count += 1

    return count

# Calculates average rating for a park in a given year.
def get_average_score_by_park_and_year(data, park_name, year):
    total_score = 0
    review_count = 0

    user_park = park_name.strip().lower().replace(" ", "_")
    user_year = year.strip()

    for review in data:
        park_from_csv = review[4].strip().lower()
        year_month = review[2].strip()

        # Skip rows with missing dates.
        if not year_month or year_month.lower() == "missing":
            continue

        try:
            rating = int(review[1])
        except (ValueError, IndexError):
            continue

        if park_from_csv == user_park and year_month.startswith(user_year):
            total_score += rating
            review_count += 1

    # Return None if no matching reviews were found.
    if review_count == 0:
        return None
    return total_score / review_count

# Counts how many reviews each park has received.
def get_review_counts_by_park(data):
    park_counts = {}

    for review in data:
        park_name = review[4].strip()

        if park_name in park_counts:
            park_counts[park_name] += 1
        else:
            park_counts[park_name] = 1
    return park_counts

# Returns the top 10 reviewer locations by average rating.
def get_top_10_locations_by_average_rating(data, park_name):
    location_ratings = {}

    user_park = park_name.strip().lower().replace(" ", "_")

    for review in data:
        park_from_csv = review[4].strip().lower()
        location = review[3].strip()
        try:
            rating = int(review[1])
        except (ValueError, IndexError):
            continue

        if park_from_csv == user_park:
            if location in location_ratings:
                location_ratings[location].append(rating)
            else:
                location_ratings[location] = [rating]

    average_ratings = []

    # Sort locations by highest average rating.
    for location, ratings in location_ratings.items():
        average_score = sum(ratings) / len(ratings)

        # Count five-star reviews for tie-breaking.
        five_star_count = ratings.count(5)

        average_ratings.append((location, average_score, five_star_count))

    # Sort by average score first,
    # then by number of five-star reviews.
    average_ratings.sort(key=lambda item: (item[1], item[2]),reverse=True)

    return [(location, average_score)
            for location, average_score, five_star_count
            in average_ratings[:10]
            ]

# Calculates average ratings for each month of the year.
def get_monthly_average_ratings_by_park(data, park_name):
    month_ratings = {
        "Jan": [],
        "Feb": [],
        "Mar": [],
        "Apr": [],
        "May": [],
        "Jun": [],
        "Jul": [],
        "Aug": [],
        "Sep": [],
        "Oct": [],
        "Nov": [],
        "Dec": []
    }

    month_map = {
        "01": "Jan",
        "02": "Feb",
        "03": "Mar",
        "04": "Apr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Aug",
        "09": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec"
    }

    user_park = park_name.strip().lower().replace(" ", "_")

    for review in data:
        park_from_csv = review[4].strip().lower()
        year_month = review[2].strip()

        # Skip rows with missing dates.
        if not year_month or year_month.lower() == "missing":
            continue

        try:
            rating = int(review[1])
        except (ValueError, IndexError):
            continue

        # Collect ratings for the selected park by month.
        if park_from_csv == user_park:
            parts = year_month.split("-")

            if len(parts) == 2:
                month_number = parts[1].zfill(2)

                if month_number in month_map:
                    month_name = month_map[month_number]
                    month_ratings[month_name].append(rating)

    monthly_averages = {}

    # Calculate average rating for each month.
    for month, ratings in month_ratings.items():
        if len(ratings) > 0:
            monthly_averages[month] = sum(ratings) / len(ratings)
        else:
            monthly_averages[month] = 0

    return monthly_averages

# Calculates average ratings for each park by reviewer location.
def get_average_score_per_park_by_location(data):
    park_location_ratings = {}

    for review in data:
        park_name = review[4].strip()
        location = review[3].strip()
        try:
            rating = int(review[1])
        except (ValueError, IndexError):
            continue

        # Create a nested dictionary for each park and location.
        if park_name not in park_location_ratings:
            park_location_ratings[park_name] = {}

        if location not in park_location_ratings[park_name]:
            park_location_ratings[park_name][location] = []

        park_location_ratings[park_name][location].append(rating)

    average_scores = {}

    # Calculate the average score for each park and location.
    for park_name, locations in park_location_ratings.items():
        average_scores[park_name] = {}

        for location, ratings in locations.items():
            average_scores[park_name][location] = sum(ratings) / len(ratings)

    return average_scores

# Prepares summary data for each park before exporting.
def get_export_data_by_park(data):
    park_data = {}

    for review in data:
        park_name = review[4].strip()
        try:
            rating = int(review[1])
        except (ValueError, IndexError):
            continue
        country = review[3].strip()

        # Create a summary record for each park.
        if park_name not in park_data:
            park_data[park_name] = {
                "number_of_reviews": 0,
                "number_of_positive_reviews": 0,
                "total_score": 0,
                "countries": set()
            }
        park_data[park_name]["number_of_reviews"] += 1
        park_data[park_name]["total_score"] += rating

        if rating >= 4:
            park_data[park_name]["number_of_positive_reviews"] += 1

        park_data[park_name]["countries"].add(country)

    # Convert summary data into a list for the exporter classes.
    export_data = []

    for park_name, info in park_data.items():
        average_score = info["total_score"] / info ["number_of_reviews"]

        export_data.append({
            "park_name": park_name,
            "number_of_reviews": info["number_of_reviews"],
            "number_of_positive_reviews": info["number_of_positive_reviews"],
            "average_review_score": round(average_score, 2),
            "number_of_countries": len(info["countries"])
        })

    return export_data





