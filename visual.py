import matplotlib.pyplot as plt

def plot_review_counts_by_park(park_counts):
    park_names = list(park_counts.keys())
    review_totals = list(park_counts.values())

    plt.figure(figsize=(8, 8))
    plt.pie(review_totals, labels=park_names, autopct="%1.1f%%", startangle=90)
    plt.title("Number of Reviews by Park")
    plt.show()

def plot_top_10_locations(top_locations, park_name):
    if len(top_locations) == 0:
        print(f"No review data found for {park_name}.")
        return

    locations = []
    average_scores = []

    for location, score in top_locations:
        locations.append(location)
        average_scores.append(score)

    plt.figure(figsize=(10,6))
    plt.bar(locations, average_scores)
    plt.title(f"top 10 Locations by average Rating for {park_name}")
    plt.xlabel("Reviewer Location")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def plot_monthly_average_ratings(monthly_averages, park_name):
    months_in_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    average_scores = []

    for month in months_in_order:
        average_scores.append(monthly_averages[month])

    plt.figure(figsize=(10, 6))
    plt.bar(months_in_order, average_scores)
    plt.title(f"Average Rating by Month for {park_name}")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.show()



