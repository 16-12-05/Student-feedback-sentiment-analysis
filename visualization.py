import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sentiment_results.csv")

sentiment_counts = df["sentiment"].value_counts()

print(sentiment_counts)

plt.figure(figsize=(6,6))
plt.pie(sentiment_counts,
        labels=sentiment_counts.index,
        autopct='%1.1f%%')

plt.title("Student Feedback Sentiment Analysis")
plt.show()

