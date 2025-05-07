import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder

def clean_text(text):
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.lower()

def preprocess_data(df):
    df['cleanText'] = df['reviewText'].apply(clean_text)
    le = LabelEncoder()
    df['category_encoded'] = le.fit_transform(df['category'])
    return df