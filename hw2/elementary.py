import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage

def stats_analysis(data: pd.DataFrame) -> None:
    linkage_data = linkage(data, method="ward", metric="euclidean")

    print(np.prod(linkage_data.shape))

    dendrogram(linkage_data)

    plt.legend()
    plt.show()

    return

if __name__ == '__main__':
    data = pd.read_excel('data.xlsx', 'Kiddos')

    stats_analysis(data)
    