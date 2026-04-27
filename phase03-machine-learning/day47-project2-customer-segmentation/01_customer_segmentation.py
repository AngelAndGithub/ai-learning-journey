#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 47: 实战项目2 - 用户分群

本文件包含用户分群的实战项目代码
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 数据生成与加载
print("=== 1. 数据生成与加载 ===")

# 生成用户数据
np.random.seed(42)
n_samples = 1000

# 生成4个聚类的数据
X, y_true = make_blobs(n_samples=n_samples, n_features=5, centers=4, cluster_std=1.0, random_state=42)

# 转换为DataFrame
customer_data = pd.DataFrame(X, columns=['年龄', '收入', '消费金额', '购买频率', '忠诚度'])

# 添加一些噪声
customer_data['年龄'] = np.abs(customer_data['年龄'] * 5 + 20)  # 年龄在20-60之间
customer_data['收入'] = np.abs(customer_data['收入'] * 10000 + 30000)  # 收入在3-8万之间
customer_data['消费金额'] = np.abs(customer_data['消费金额'] * 1000 + 500)  # 消费金额在500-2000之间
customer_data['购买频率'] = np.abs(customer_data['购买频率'] * 10 + 1)  # 购买频率在1-15之间
customer_data['忠诚度'] = np.abs(customer_data['忠诚度'] * 0.5 + 0.5)  # 忠诚度在0-1之间

print(f"数据集形状: {customer_data.shape}")
print("\n数据前5行:")
print(customer_data.head())

# 数据描述性统计
print("\n数据描述性统计:")
print(customer_data.describe())

# 2. 数据可视化
print("\n=== 2. 数据可视化 ===")

# 特征分布
plt.figure(figsize=(15, 10))
for i, col in enumerate(customer_data.columns, 1):
    plt.subplot(2, 3, i)
    sns.histplot(customer_data[col], kde=True)
    plt.title(f'{col}分布')

plt.tight_layout()
plt.savefig('feature_distributions.png')
plt.show()
print("特征分布图已保存为 feature_distributions.png")

# 特征相关性热力图
plt.figure(figsize=(10, 8))
corr = customer_data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('特征相关性热力图')
plt.savefig('correlation_heatmap.png')
plt.show()
print("特征相关性热力图已保存为 correlation_heatmap.png")

# 3. 数据预处理
print("\n=== 3. 数据预处理 ===")

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(customer_data)

print(f"标准化后数据形状: {X_scaled.shape}")
print(f"标准化后数据均值: {X_scaled.mean(axis=0).round(4)}")
print(f"标准化后数据标准差: {X_scaled.std(axis=0).round(4)}")

# 4. K-means聚类
print("\n=== 4. K-means聚类 ===")

# 确定最佳K值
inertia = []
silhouette_scores = []
calinski_scores = []
davies_scores = []
K = range(2, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))
    calinski_scores.append(calinski_harabasz_score(X_scaled, kmeans.labels_))
    davies_scores.append(davies_bouldin_score(X_scaled, kmeans.labels_))

# 可视化肘部法则
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(K, inertia, 'o-')
plt.title('肘部法则')
plt.xlabel('K值')
plt.ylabel('惯性')

plt.subplot(2, 2, 2)
plt.plot(K, silhouette_scores, 'o-')
plt.title('轮廓系数')
plt.xlabel('K值')
plt.ylabel('轮廓系数')

plt.subplot(2, 2, 3)
plt.plot(K, calinski_scores, 'o-')
plt.title('Calinski-Harabasz指数')
plt.xlabel('K值')
plt.ylabel('CH指数')

plt.subplot(2, 2, 4)
plt.plot(K, davies_scores, 'o-')
plt.title('Davies-Bouldin指数')
plt.xlabel('K值')
plt.ylabel('DB指数')

plt.tight_layout()
plt.savefig('kmeans_metrics.png')
plt.show()
print("K-means评估指标图已保存为 kmeans_metrics.png")

# 使用最佳K值（4）
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)

# 5. DBSCAN聚类
print("\n=== 5. DBSCAN聚类 ===")

# 确定最佳eps值
from sklearn.neighbors import NearestNeighbors

neigh = NearestNeighbors(n_neighbors=5)
neigh.fit(X_scaled)
distances, indices = neigh.kneighbors(X_scaled)
distances = np.sort(distances, axis=0)
distances = distances[:, 4]

plt.figure(figsize=(10, 6))
plt.plot(distances)
plt.title('KNN距离图')
plt.xlabel('样本索引')
plt.ylabel('距离')
plt.savefig('dbscan_eps.png')
plt.show()
print("DBSCAN eps选择图已保存为 dbscan_eps.png")

# 使用DBSCAN
dbscan = DBSCAN(eps=1.0, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)

print(f"DBSCAN聚类结果: {np.unique(dbscan_labels)}")
print(f"噪声点数量: {np.sum(dbscan_labels == -1)}")

# 6. 层次聚类
print("\n=== 6. 层次聚类 ===")

# 生成层次聚类树
linkage_matrix = linkage(X_scaled, method='ward')

plt.figure(figsize=(12, 8))
dendrogram(linkage_matrix, truncate_mode='lastp', p=20, leaf_rotation=45, leaf_font_size=10)
plt.title('层次聚类树')
plt.savefig('hierarchical_dendrogram.png')
plt.show()
print("层次聚类树已保存为 hierarchical_dendrogram.png")

# 使用层次聚类
agglomerative = AgglomerativeClustering(n_clusters=4, linkage='ward')
hierarchical_labels = agglomerative.fit_predict(X_scaled)

# 7. 聚类结果评估
print("\n=== 7. 聚类结果评估 ===")

# 评估K-means
print("K-means评估:")
print(f"轮廓系数: {silhouette_score(X_scaled, kmeans_labels):.4f}")
print(f"Calinski-Harabasz指数: {calinski_harabasz_score(X_scaled, kmeans_labels):.4f}")
print(f"Davies-Bouldin指数: {davies_bouldin_score(X_scaled, kmeans_labels):.4f}")

# 评估层次聚类
print("\n层次聚类评估:")
print(f"轮廓系数: {silhouette_score(X_scaled, hierarchical_labels):.4f}")
print(f"Calinski-Harabasz指数: {calinski_harabasz_score(X_scaled, hierarchical_labels):.4f}")
print(f"Davies-Bouldin指数: {davies_bouldin_score(X_scaled, hierarchical_labels):.4f}")

# 8. 聚类结果可视化
print("\n=== 8. 聚类结果可视化 ===")

# 使用PCA降维可视化
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(15, 5))

# K-means结果
plt.subplot(1, 3, 1)
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=kmeans_labels, palette='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', s=200, color='r')
plt.title('K-means聚类结果')

# DBSCAN结果
plt.subplot(1, 3, 2)
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=dbscan_labels, palette='viridis')
plt.title('DBSCAN聚类结果')

# 层次聚类结果
plt.subplot(1, 3, 3)
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=hierarchical_labels, palette='viridis')
plt.title('层次聚类结果')

plt.tight_layout()
plt.savefig('clustering_results.png')
plt.show()
print("聚类结果可视化已保存为 clustering_results.png")

# 9. 聚类结果分析
print("\n=== 9. 聚类结果分析 ===")

# 添加K-means聚类结果到数据框
customer_data['cluster'] = kmeans_labels

# 分析每个聚类的特征
cluster_analysis = customer_data.groupby('cluster').mean()
print("\n每个聚类的特征均值:")
print(cluster_analysis)

# 可视化每个聚类的特征
plt.figure(figsize=(15, 10))
for i, col in enumerate(customer_data.columns[:-1], 1):
    plt.subplot(2, 3, i)
    sns.boxplot(x='cluster', y=col, data=customer_data)
    plt.title(f'{col}按聚类分布')

plt.tight_layout()
plt.savefig('cluster_features.png')
plt.show()
print("聚类特征分布已保存为 cluster_features.png")

# 10. 客户分群描述
print("\n=== 10. 客户分群描述 ===")

# 分析每个聚类的特征，给出分群描述
clusters = cluster_analysis.index
for cluster in clusters:
    print(f"\n聚类 {cluster}:")
    print(f"  平均年龄: {cluster_analysis.loc[cluster, '年龄']:.1f}")
    print(f"  平均收入: {cluster_analysis.loc[cluster, '收入']:.0f}")
    print(f"  平均消费金额: {cluster_analysis.loc[cluster, '消费金额']:.0f}")
    print(f"  平均购买频率: {cluster_analysis.loc[cluster, '购买频率']:.1f}")
    print(f"  平均忠诚度: {cluster_analysis.loc[cluster, '忠诚度']:.2f}")
    print(f"  客户数量: {len(customer_data[customer_data['cluster'] == cluster])}")

# 11. 模型部署
print("\n=== 11. 模型部署 ===")

import joblib

# 保存模型
joblib.dump(kmeans, 'customer_segmentation_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("模型已保存为 customer_segmentation_model.pkl")
print("标准化器已保存为 scaler.pkl")

# 加载模型
loaded_model = joblib.load('customer_segmentation_model.pkl')
loaded_scaler = joblib.load('scaler.pkl')

# 测试新客户
new_customer = np.array([[35, 50000, 1200, 8, 0.7]])
new_customer_scaled = loaded_scaler.transform(new_customer)
predicted_cluster = loaded_model.predict(new_customer_scaled)
print(f"\n新客户预测聚类: {predicted_cluster[0]}")

# 12. 项目总结
print("\n=== 12. 项目总结 ===")
print("1. 数据生成: 创建了包含5个特征的用户数据")
print("2. 数据可视化: 分析了特征分布和相关性")
print("3. 聚类算法: 比较了K-means、DBSCAN和层次聚类")
print("4. 模型评估: 使用多种指标评估聚类效果")
print("5. 结果分析: 分析了每个客户群体的特征")
print("6. 模型部署: 保存了模型和标准化器，可用于新客户分群")

# 13. 清理文件
print("\n=== 13. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['feature_distributions.png', 'correlation_heatmap.png', 'kmeans_metrics.png',
                   'dbscan_eps.png', 'hierarchical_dendrogram.png', 'clustering_results.png',
                   'cluster_features.png', 'customer_segmentation_model.pkl', 'scaler.pkl']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n用户分群项目完成！")
