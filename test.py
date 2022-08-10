from kmeans import K_means
import pandas as pd
data=pd.read_csv("data3.csv")
KMeans=K_means(data)
KMeans.kmeans_fit(3)
print(data)








