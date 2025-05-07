import pandas as pd

def load_amazon_reviews(file_path):
    df = pd.read_csv(file_path)
    df.dropna(subset=['reviewText', 'overall'], inplace=True)
    return df