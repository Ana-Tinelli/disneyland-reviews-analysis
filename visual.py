import matplotlib.pyplot as plt

# Displays a pie chart of review counts by park.
def plot_review_counts_by_park(park_counts):
    park_names = list(park_counts.keys())
    review_totals = list(park_counts.values())

    plt.figure(figsize=(8, 8))
    plt.pie(review_totals, labels=park_names, autopct="%1.1f%%", startangle=90)
    plt.title("Number of Reviews by Park")
    plt.show()

# Displays a bar chart of the top 10 locations by rating.
def plot_top_10_locations(top_locations, park_name):
    if len(top_locations) == 0:
        print(f"No review data found for {park_name}.")
        return

    locations = []
    average_scores = []

    # Separate locations and scores for plotting.
    for location, score in top_locations:
        locations.append(location)
        average_scores.append(score)

    # Create a bar chart.
    plt.figure(figsize=(10, 6))
    plt.bar(locations, average_scores)
    plt.title(f"Top 10 Locations by average Rating for {park_name}")
    plt.xlabel("Reviewer Location")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

# Displays average monthly ratings for a selected park.
def plot_monthly_average_ratings(monthly_averages, park_name):
    months_in_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    average_scores = []

    # Collect average scores for plotting.
    for month in months_in_order:
        average_scores.append(monthly_averages[month])

    # Create the monthly ratings chart.
    plt.figure(figsize=(10, 6))
    plt.bar(months_in_order, average_scores)
    plt.title(f"Average Rating by Month for {park_name}")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.show()



