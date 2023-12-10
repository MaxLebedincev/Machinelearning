import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


def search_optimal_clusters(array):
    inertia = []
    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, random_state=1, n_init=10).fit(array)
        inertia.append(np.sqrt(kmeans.inertia_))
    plt.plot(range(1, 10), inertia, marker='s')
    plt.xlabel('$k$')
    plt.ylabel('$J(C_k)$')
    plt.title('Нахождения оптимального кол-ва кластеров')
    plt.show()


def grouping(array):
    # объединение(проекция) признаков и приведению к 2д типу
    tsne = TSNE()
    array_tsne = tsne.fit_transform(array)
    plt.plot(array_tsne[:, 0], array_tsne[:, 1], 'bo')
    plt.title('Группировка элементов')
    plt.show()
    return array_tsne


def exec_task(array):
    search_optimal_clusters(array)
    array_tsne = grouping(array)
    return array_tsne
