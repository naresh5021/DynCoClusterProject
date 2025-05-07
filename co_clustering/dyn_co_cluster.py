import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD

def parallel_co_clustering(features, n_clusters=10):
    svd = TruncatedSVD(n_components=50)
    reduced = svd.fit_transform(features)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(reduced)
    return clusters