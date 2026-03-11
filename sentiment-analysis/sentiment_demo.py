import csv

sentences = [
    "I love this product",
    "The service was terrible",
    "Delivery was on time",
    "This app is amazing",
    "I am disappointed with the quality"
]

labels = ["Positive", "Negative", "Neutral", "Positive", "Negative"]

with open('sentiment_demo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["sentence", "label"])
    for s, l in zip(sentences, labels):
        writer.writerow([s, l])

print("CSV dataset created successfully!")