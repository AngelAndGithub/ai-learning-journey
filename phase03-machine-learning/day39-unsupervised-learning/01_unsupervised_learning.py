#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 39: 无监督学习

本文件包含无监督学习算法的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, make_blobs, make_moons, load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering, Birch
from sklearn.decomposition import PCA, KernelPCA, TruncatedSVD
from sklearn.manifold import TSNE, Isomap, LocallyLinearEmbedding
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.neighbors import NearestNeighbors

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 数据准备
print("=== 1. 数据准备 ===")

# 1.1 加载数据集
print("\n1.1 加载数据集")

# 加载鸢尾花数据集
iris = load_iris()
X_iris, y_iris = iris.data, iris.target
print(f"鸢尾花数据集: X={X_iris.shape}, y={y_iris.shape}")

# 创建聚类数据集
X_blobs, y_blobs = make_blobs(n_samples=1000, n_features=2, centers=5, random_state=42)
print(f"\n聚类数据集: X={X_blobs.shape}, y={y_blobs.shape}")

# 创建月牙形数据集
X_moons, y_moons = make_moons(n_samples=500, noise=0.1, random_state=42)
print(f"\n月牙形数据集: X={X_moons.shape}, y={y_moons.shape}")

# 加载手写数字数据集
digits = load_digits()
X_digits, y_digits = digits.data, digits.target
print(f"\n手写数字数据集: X={X_digits.shape}, y={y_digits.shape}")

# 1.2 数据预处理
print("\n1.2 数据预处理")

# 标准化数据
scaler = StandardScaler()
X_iris_scaled = scaler.fit_transform(X_iris)
X_blobs_scaled = scaler.fit_transform(X_blobs)
X_moons_scaled = scaler.fit_transform(X_moons)
X_digits_scaled = scaler.fit_transform(X_digits)

# 2. 聚类算法
print("\n=== 2. 聚类算法 ===")

# 2.1 K-means聚类
print("\n2.1 K-means聚类")

# 确定最佳K值
inertia = []
silhouette = []
K = range(2, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_blobs_scaled)
    inertia.append(kmeans.inertia_)
    silhouette.append(silhouette_score(X_blobs_scaled, kmeans.labels_))

# 可视化肘部法则
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(K, inertia, 'o-')
plt.title('肘部法则')
plt.xlabel('K值')
plt.ylabel('惯性')

plt.subplot(1, 2, 2)
plt.plot(K, silhouette, 'o-')
plt.title('轮廓系数')
plt.xlabel('K值')
plt.ylabel('轮廓系数')

plt.tight_layout()
plt.savefig('kmeans_elbow.png')
plt.show()
print("K-means肘部法则图已保存为 kmeans_elbow.png")

# 使用最佳K值（5）
kmeans = KMeans(n_clusters=5, random_state=42)
y_kmeans = kmeans.fit_predict(X_blobs_scaled)

# 可视化聚类结果
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_blobs_scaled[:, 0], y=X_blobs_scaled[:, 1], hue=y_kmeans, palette='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', s=200, color='r')
plt.title('K-means聚类结果')
plt.savefig('kmeans_result.png')
plt.show()
print("K-means聚类结果已保存为 kmeans_result.png")

# 2.2 DBSCAN聚类
print("\n2.2 DBSCAN聚类")

# 确定最佳eps值
neigh = NearestNeighbors(n_neighbors=2)
neigh.fit(X_moons_scaled)
distances, indices = neigh.kneighbors(X_moons_scaled)
distances = np.sort(distances, axis=0)
distances = distances[:, 1]

plt.figure(figsize=(10, 6))
plt.plot(distances)
plt.title('KNN距离图')
plt.xlabel('样本索引')
plt.ylabel('距离')
plt.savefig('dbscan_eps.png')
plt.show()
print("DBSCAN eps选择图已保存为 dbscan_eps.png")

# 使用DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=5)
y_dbscan = dbscan.fit_predict(X_moons_scaled)

# 可视化聚类结果
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_moons_scaled[:, 0], y=X_moons_scaled[:, 1], hue=y_dbscan, palette='viridis')
plt.title('DBSCAN聚类结果')
plt.savefig('dbscan_result.png')
plt.show()
print("DBSCAN聚类结果已保存为 dbscan_result.png")

# 2.3 层次聚类
print("\n2.3 层次聚类")

# 凝聚层次聚类
agg = AgglomerativeClustering(n_clusters=5)
y_agg = agg.fit_predict(X_blobs_scaled)

# 可视化聚类结果
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_blobs_scaled[:, 0], y=X_blobs_scaled[:, 1], hue=y_agg, palette='viridis')
plt.title('层次聚类结果')
plt.savefig('hierarchical_result.png')
plt.show()
print("层次聚类结果已保存为 hierarchical_result.png")

# 2.4 BIRCH聚类
print("\n2.4 BIRCH聚类")

birch = Birch(n_clusters=5)
y_birch = birch.fit_predict(X_blobs_scaled)

# 可视化聚类结果
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_blobs_scaled[:, 0], y=X_blobs_scaled[:, 1], hue=y_birch, palette='viridis')
plt.title('BIRCH聚类结果')
plt.savefig('birch_result.png')
plt.show()
print("BIRCH聚类结果已保存为 birch_result.png")

# 3. 降维技术
print("\n=== 3. 降维技术 ===")

# 3.1 PCA
print("\n3.1 PCA")

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_digits_scaled)

print(f"PCA解释方差比: {pca.explained_variance_ratio_}")
print(f"累计解释方差比: {np.sum(pca.explained_variance_ratio_):.4f}")

# 可视化PCA结果
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y_digits, palette='viridis')
plt.title('PCA降维结果')
plt.savefig('pca_result.png')
plt.show()
print("PCA降维结果已保存为 pca_result.png")

# 3.2 t-SNE
print("\n3.2 t-SNE")

tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_digits_scaled[:500])  # 只使用部分数据加快计算

# 可视化t-SNE结果
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_tsne[:, 0], y=X_tsne[:, 1], hue=y_digits[:500], palette='viridis')
plt.title('t-SNE降维结果')
plt.savefig('tsne_result.png')
plt.show()
print("t-SNE降维结果已保存为 tsne_result.png")

# 3.3 Isomap
print("\n3.3 Isomap")

isomap = Isomap(n_components=2, n_neighbors=10)
X_isomap = isomap.fit_transform(X_digits_scaled[:500])

# 可视化Isomap结果
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_isomap[:, 0], y=X_isomap[:, 1], hue=y_digits[:500], palette='viridis')
plt.title('Isomap降维结果')
plt.savefig('isomap_result.png')
plt.show()
print("Isomap降维结果已保存为 isomap_result.png")

# 3.4 LLE
print("\n3.4 LLE")

lle = LocallyLinearEmbedding(n_components=2, n_neighbors=10, random_state=42)
X_lle = lle.fit_transform(X_digits_scaled[:500])

# 可视化LLE结果
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_lle[:, 0], y=X_lle[:, 1], hue=y_digits[:500], palette='viridis')
plt.title('LLE降维结果')
plt.savefig('lle_result.png')
plt.show()
print("LLE降维结果已保存为 lle_result.png")

# 4. 聚类评估
print("\n=== 4. 聚类评估 ===")

# 在鸢尾花数据集上评估不同聚类算法
print("在鸢尾花数据集上的聚类评估:")

algorithms = {
    'K-means': KMeans(n_clusters=3, random_state=42),
    'DBSCAN': DBSCAN(eps=0.5, min_samples=5),
    '层次聚类': AgglomerativeClustering(n_clusters=3),
    'BIRCH': Birch(n_clusters=3)
}

for name, algorithm in algorithms.items():
    labels = algorithm.fit_predict(X_iris_scaled)
    
    # 计算评估指标
    if len(set(labels)) > 1:  # 确保至少有两个聚类
        silhouette = silhouette_score(X_iris_scaled, labels)
        calinski_harabasz = calinski_harabasz_score(X_iris_scaled, labels)
        davies_bouldin = davies_bouldin_score(X_iris_scaled, labels)
        
        print(f"{name}:")
        print(f"  轮廓系数: {silhouette:.4f}")
        print(f"  Calinski-Harabasz指数: {calinski_harabasz:.4f}")
        print(f"  Davies-Bouldin指数: {davies_bouldin:.4f}")
    else:
        print(f"{name}: 只生成了一个聚类，无法计算评估指标")

# 5. 异常检测
print("\n=== 5. 异常检测 ===")

from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope

# 创建包含异常值的数据
np.random.seed(42)
X_normal = np.random.normal(0, 1, (1000, 2))
X_outliers = np.random.normal(5, 1, (50, 2))
X_anomaly = np.vstack([X_normal, X_outliers])
y_anomaly = np.zeros(1050, dtype=int)
y_anomaly[-50:] = 1  # 异常值标记为1

# 训练异常检测模型
print("异常检测模型评估:")

models = {
    'Isolation Forest': IsolationForest(contamination=0.05, random_state=42),
    'Elliptic Envelope': EllipticEnvelope(contamination=0.05, random_state=42)
}

for name, model in models.items():
    y_pred = model.fit_predict(X_anomaly)
    # 将-1（异常）转换为1，1（正常）转换为0
    y_pred = np.where(y_pred == -1, 1, 0)
    
    # 计算准确率
    accuracy = np.sum(y_pred == y_anomaly) / len(y_anomaly)
    print(f"{name} 准确率: {accuracy:.4f}")

# 可视化异常检测结果
plt.figure(figsize=(12, 5))

for i, (name, model) in enumerate(models.items()):
    y_pred = model.fit_predict(X_anomaly)
    
    plt.subplot(1, 2, i+1)
    plt.scatter(X_anomaly[y_pred == 1, 0], X_anomaly[y_pred == 1, 1], color='r', label='异常')
    plt.scatter(X_anomaly[y_pred == -1, 0], X_anomaly[y_pred == -1, 1], color='b', label='正常')
    plt.title(f'{name} 异常检测')
    plt.legend()

plt.tight_layout()
plt.savefig('anomaly_detection.png')
plt.show()
print("异常检测结果已保存为 anomaly_detection.png")

# 6. 实际应用示例
print("\n=== 6. 实际应用示例 ===")

# 6.1 客户分群
print("\n6.1 客户分群")

# 创建客户数据
np.random.seed(42)
customer_data = pd.DataFrame({
    'age': np.random.randint(18, 70, 1000),
    'income': np.random.normal(50000, 15000, 1000).astype(int),
    'spending': np.random.normal(5000, 1500, 1000).astype(int),
    'loyalty': np.random.uniform(0, 1, 1000)
})

# 标准化数据
customer_scaled = scaler.fit_transform(customer_data)

# 使用K-means进行客户分群
kmeans = KMeans(n_clusters=4, random_state=42)
customer_clusters = kmeans.fit_predict(customer_scaled)

# 可视化客户分群
pca = PCA(n_components=2)
customer_pca = pca.fit_transform(customer_scaled)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=customer_pca[:, 0], y=customer_pca[:, 1], hue=customer_clusters, palette='viridis')
plt.title('客户分群结果')
plt.savefig('customer_segmentation.png')
plt.show()
print("客户分群结果已保存为 customer_segmentation.png")

# 6.2 图像压缩
print("\n6.2 图像压缩")

from sklearn.datasets import load_sample_image

# 加载示例图像
china = load_sample_image("china.jpg")
china = china / 255.0  # 归一化

# 重塑图像为二维数组
height, width, channels = china.shape
china_reshaped = china.reshape(-1, channels)

# 使用K-means进行图像压缩
n_colors = 64
kmeans = KMeans(n_clusters=n_colors, random_state=42)
kmeans.fit(china_reshaped)

# 替换像素值为聚类中心
compressed = kmeans.cluster_centers_[kmeans.labels_]
compressed = compressed.reshape(height, width, channels)

# 可视化原始图像和压缩图像
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(china)
plt.title('原始图像')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(compressed)
plt.title(f'压缩图像 ({n_colors} 颜色)')
plt.axis('off')

plt.tight_layout()
plt.savefig('image_compression.png')
plt.show()
print("图像压缩结果已保存为 image_compression.png")

# 7. 无监督学习应用场景
print("\n=== 7. 无监督学习应用场景 ===")
print("1. 聚类分析: 客户分群、市场细分、异常检测")
print("2. 降维技术: 数据可视化、特征提取、噪声去除")
print("3. 异常检测: 欺诈检测、故障诊断、网络安全")
print("4. 关联规则学习: 购物篮分析、推荐系统")
print("5. 密度估计: 概率密度函数估计、异常检测")

# 8. 清理文件
print("\n=== 8. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['kmeans_elbow.png', 'kmeans_result.png', 'dbscan_eps.png', 'dbscan_result.png',
                   'hierarchical_result.png', 'birch_result.png', 'pca_result.png', 'tsne_result.png',
                   'isomap_result.png', 'lle_result.png', 'anomaly_detection.png', 'customer_segmentation.png',
                   'image_compression.png']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n无监督学习练习完成！")
