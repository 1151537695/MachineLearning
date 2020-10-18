import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df_Iris = pd.read_csv('Iris.csv')

# print(df_Iris.describe())
# print(df_Iris.Species.value_counts())

# sns.set()   # 初始化

X = df_Iris['Sepal.Length']
Y = df_Iris['Sepal.Width']


# # sns.relplot(x='Sepal.Length', y='Sepal.Width', hue='Species', style='Species', data=df_Iris)      # 根据花蕊长度和宽度
# # sns.relplot(x='Petal.Length', y='Petal.Width', hue='Species', style='Species', data=df_Iris)
#
# plt.title('SepalLengthCm and SepalWidthCm data analysize')
# plt.show()

# fig = plt.figure()
# plt.scatter(X, Y, s=10)


# load_data = np.mat(np.array([X, Y]))
# kMeans(load_data, 3)
#
# plt.show()


if __name__ == "__main__":
    x = np.array(X)
    y = np.array(Y)
    data_load = []
    for i in range(x.size):
        data_load.append((x[i], y[i]))
    estimator = KMeans(n_clusters=3)
    estimator.fit(data_load)
    label_pred = estimator.labels_
    centroids = estimator.cluster_centers_
    print(centroids.shape)
    plt.figure()
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red')
    plt.scatter(x, y, c=label_pred, alpha=0.5)
    plt.show()
