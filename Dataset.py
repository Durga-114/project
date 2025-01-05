import pandas as pd
import random
from faker import Faker

fake = Faker()
num_samples = 100
ratings = [1, 2, 3, 4, 5]
feedback_samples = [
    "Excellent service, would definitely stay again!",
    "The room was clean but the staff was rude.",
    "Good location, but the amenities were average.",
    "The experience was awful, won't return.",
    "Amazing stay, everything exceeded expectations.",
    "Decent, could use some improvements in the food quality."
]

names = []
emails = []
ages = []
feedbacks = []
ratings_given = []
dates = []

for _ in range(num_samples):
    names.append(fake.name())
    emails.append(fake.email())
    ages.append(random.randint(18, 70))  # Random age between 18 and 70
    feedbacks.append(random.choice(feedback_samples))
    ratings_given.append(random.choice(ratings))
    dates.append(fake.date_this_decade())

data = {
    "Customer Name": names,
    "Email": emails,
    "Age": ages,
    "Feedback": feedbacks,
    "Rating": ratings_given,
    "Feedback Date": dates
}

df = pd.DataFrame(data)

print(df.head())

df.to_csv("hotel_feedbacks.csv", index=False)
