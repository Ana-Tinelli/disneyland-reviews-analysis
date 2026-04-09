def load_reviews_from_csv(file_name):
    reviews = []

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines[1:]:
            line = line.strip()

            if line != "":
                row = line.split(",")
                reviews.append(row)

    return reviews

def get_reviews_by_park(data, park_name):
    matching_reviews = []

    user_input = park_name.strip().lower().replace(" ", "_")

    for review in data:
        park_from_csv = review[4].strip().lower()

        if park_from_csv == user_input:
            matching_reviews.append(review)

    return matching_reviews

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

def get_average_score_by_park_and_year(data, park_name, year):
    total_score = 0
    review_count = 0

    user_park = park_name.strip().lower().replace(" ","_")
    user_year = year.strip()

    for review in data:
        park_from_csv = review[4].strip().lower()
        year_month = review[2].strip()
        rating = int(review[1])

        if park_from_csv == user_park and year_month.startswith(user_year):
            total_score += rating
            review_count += 1

    if review_count == 0:
        return None
    return total_score / review_count

