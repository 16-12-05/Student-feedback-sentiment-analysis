import os

print("Current Folder:", os.getcwd())
print("CSV Exists:", os.path.exists("cleaned_student_feedback.csv"))


import pandas as pd
from textblob import TextBlob

print("Loading cleaned data...")

df = pd.read_csv("cleaned_student_feedback.csv")

def get_sentiment(text):
    if pd.isna(text):
        return "Neutral"

    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["sentiment"] = df["cleaned_teaching"].apply(get_sentiment)

df.to_csv("sentiment_results.csv", index=False)
import os

print("File Saved At:")
print(os.path.abspath("sentiment_results.csv"))


print("\nSentiment Analysis Completed!")

print(df[["cleaned_teaching", "sentiment"]].head(10))
