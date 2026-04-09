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