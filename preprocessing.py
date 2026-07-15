
import pandas as pd
import re
import string
import os

print("=== Step 1: Starting Preprocessing ===")

# Simple preprocessing without NLTK
stop_words = {
    'a', 'an', 'the', 'is', 'are', 'was', 'were',
    'in', 'on', 'at', 'to', 'for', 'of', 'and',
    'or', 'but', 'with', 'by', 'from'
}

print("NLTK data ready")

def preprocess_text(text):
    if pd.isna(text):
        return ""

    text = str(text).lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove extra spaces
    text = ' '.join(text.split())

    # Remove stopwords
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]

    return ' '.join(tokens)

print("=== Step 2: Loading Excel File ===")

# Excel file must be in the same folder as preprocessing.py
file_path = "student_feedback.csv.xlsx"

if not os.path.exists(file_path):
    print(f"ERROR: Excel file not found! Check path: {os.path.abspath('C:\\Users\\k.chandra\\OneDrive\\Desktop\\SentimentProject\\student_feedback.csv.xlsx')}")
    exit()

if file_path.endswith(".csv"):
    df = pd.read_csv(file_path, encoding='latin1')
elif file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path)
else:
    print("Unsupported file format")
    exit()

print("\nTeaching Data:")
print(df[['teaching','teaching.1']].head(5))

print("\nCourse Content Data:")
print(df[['coursecontent','coursecontent.1']].head(5))

print("\nLab Work Data:")
print(df[['labwork','labwork.1']].head(5))


print("Columns found:")
print(df.columns.tolist())

print(f"Total rows: {df.shape[0]}")

print("=== Step 3: Cleaning Text ===")

text_columns = [
    'teaching.1',
    'coursecontent.1',
    'Examination',
    'labwork.1',
    ' library_facilities',
    'extracurricular.1'
]


for col in text_columns:
    if col in df.columns:
        print(f"Cleaning column: {col}")
        clean_name = col.replace(".1", "").strip()
        df[f'cleaned_{clean_name}'] = df[col].apply(preprocess_text)
    else:
        print(f"WARNING: Column '{col}' not found in CSV. Skipping.")

output_file = "cleaned_student_feedback.csv"

df.to_csv(output_file, index=False)

print("=== Step 4: Done ===")
print("Cleaning completed successfully!")
print(f"Saved as: {os.path.abspath(output_file)}")

cleaned_cols = [c for c in df.columns if 'cleaned_' in c]

if cleaned_cols:
    print("\nFirst 2 rows of cleaned data:")
    print(df[cleaned_cols].head(2))
    print("\nFirst 5 rows of original data:")
print(df.head())