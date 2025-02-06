import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_excel(r"C:\Users\HARESH PS\Downloads\archive (2)\Online Retail.xlsx")

df = df.drop_duplicates()
df = df.dropna()

df['TotalSpending'] = df['Quantity'] * df['UnitPrice']

features = df[['CustomerID', 'Quantity', 'TotalSpending']].groupby('CustomerID').sum()

scaler = StandardScaler()
scaled_data = scaler.fit_transform(features)

pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

# K-means clustering
kmeans = KMeans(n_clusters=4)  
clusters = kmeans.fit_predict(scaled_data)

features['cluster'] = clusters

plt.figure(figsize=(10, 7))
sns.scatterplot(x=pca_data[:, 0], y=pca_data[:, 1], hue=clusters, palette='viridis')
plt.title('Customer Segmentation')
plt.xlabel('PCA Feature 1')
plt.ylabel('PCA Feature 2')
plt.show()

cluster_analysis = features.groupby('cluster').mean()
print(cluster_analysis)

for cluster in cluster_analysis.index:
    print(f"Cluster {cluster}:")
    print(cluster_analysis.loc[cluster])
   
