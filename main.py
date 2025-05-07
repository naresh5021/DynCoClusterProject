from data.load_data import load_amazon_reviews
from preprocessing.preprocess import preprocess_data
from feature_engineering.feature_extract import extract_features
from co_clustering.dyn_co_cluster import parallel_co_clustering
from evaluation.metrics import compute_metrics

def main():
    df = load_amazon_reviews("data/amazon_reviews_sample.csv")
    df = preprocess_data(df)
    features, _ = extract_features(df['cleanText'])
    clusters = parallel_co_clustering(features)
    # Assume some ground-truth labels exist for evaluation
    precision, recall, f1 = compute_metrics(df['category_encoded'], clusters)
    print(f"Precision: {precision:.2f}, Recall: {recall:.2f}, F1: {f1:.2f}")

if __name__ == "__main__":
    main()