from sklearn.cluster import KMeans, DBSCAN, AffinityPropagation
import matplotlib.pyplot as plt


def clustering_kmeans(array_tsne):
    kmeans = KMeans(n_clusters=2, n_init=10)
    kmeans.fit(array_tsne)
    result = kmeans.predict(array_tsne)
    plt.scatter(array_tsne[:, 0], array_tsne[:, 1], c=result, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=100, alpha=0.5)
    plt.show()


def clustering_dbscan(array_tsne):
    dbscan = DBSCAN(eps=1, min_samples=5)
    result = dbscan.fit_predict(array_tsne)
    plt.scatter(array_tsne[:, 0], array_tsne[:, 1], c=result, s=20, cmap='viridis')
    plt.show()


def clustering_affinity_propagation(array_tsne):
    ap = AffinityPropagation()
    ap.fit(array_tsne)
    result =ap.predict(array_tsne)
    plt.scatter(array_tsne[:, 0], array_tsne[:, 1], c=result, s=20, cmap='viridis')
    plt.show()


def exec_task(array_tsne):
    clustering_kmeans(array_tsne)
    clustering_dbscan(array_tsne)
    clustering_affinity_propagation(array_tsne)
