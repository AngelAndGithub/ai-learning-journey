#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 34: 数学基础-线性代数

本文件包含线性代数基础的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. 向量基础
print("=== 1. 向量基础 ===")

# 1.1 向量创建
print("\n1.1 向量创建")

# 行向量
v1 = np.array([1, 2, 3])
print(f"行向量 v1: {v1}")
print(f"v1 形状: {v1.shape}")

# 列向量
v2 = np.array([[1], [2], [3]])
print(f"\n列向量 v2:\n{v2}")
print(f"v2 形状: {v2.shape}")

# 1.2 向量运算
print("\n1.2 向量运算")

# 向量加法
v3 = np.array([4, 5, 6])
print(f"v1: {v1}")
print(f"v3: {v3}")
print(f"v1 + v3: {v1 + v3}")

# 向量减法
print(f"v1 - v3: {v1 - v3}")

# 向量标量乘法
print(f"v1 * 2: {v1 * 2}")

# 向量点积
print(f"v1 · v3: {np.dot(v1, v3)}")

# 向量长度
print(f"v1 长度: {np.linalg.norm(v1)}")

# 向量夹角
cos_theta = np.dot(v1, v3) / (np.linalg.norm(v1) * np.linalg.norm(v3))
theta = np.arccos(cos_theta)
print(f"v1 和 v3 的夹角: {np.degrees(theta):.2f} 度")

# 1.3 向量可视化
print("\n1.3 向量可视化")

# 2D向量
plt.figure(figsize=(8, 6))
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
plt.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='b', label='v3')
plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('2D向量可视化')
plt.legend()
plt.savefig('vector_2d.png')
plt.show()
print("2D向量可视化已保存为 vector_2d.png")

# 3D向量
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='v1')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='b', label='v3')
ax.set_xlim([0, 7])
ax.set_ylim([0, 7])
ax.set_zlim([0, 7])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D向量可视化')
ax.legend()
plt.savefig('vector_3d.png')
plt.show()
print("3D向量可视化已保存为 vector_3d.png")

# 2. 矩阵基础
print("\n=== 2. 矩阵基础 ===")

# 2.1 矩阵创建
print("\n2.1 矩阵创建")

# 2x3矩阵
A = np.array([[1, 2, 3], [4, 5, 6]])
print(f"矩阵 A:\n{A}")
print(f"A 形状: {A.shape}")

# 3x2矩阵
B = np.array([[7, 8], [9, 10], [11, 12]])
print(f"\n矩阵 B:\n{B}")
print(f"B 形状: {B.shape}")

# 单位矩阵
I = np.eye(3)
print(f"\n3x3单位矩阵 I:\n{I}")

# 零矩阵
Z = np.zeros((2, 3))
print(f"\n2x3零矩阵 Z:\n{Z}")

# 2.2 矩阵运算
print("\n2.2 矩阵运算")

# 矩阵加法
C = np.array([[2, 0, 1], [3, 1, 0]])
print(f"矩阵 A:\n{A}")
print(f"矩阵 C:\n{C}")
print(f"A + C:\n{A + C}")

# 矩阵标量乘法
print(f"\nA * 2:\n{A * 2}")

# 矩阵乘法
print(f"\n矩阵 A:\n{A}")
print(f"矩阵 B:\n{B}")
print(f"A @ B:\n{A @ B}")
print(f"np.dot(A, B):\n{np.dot(A, B)}")

# 矩阵转置
print(f"\nA 的转置:\n{A.T}")

# 矩阵行列式
D = np.array([[1, 2], [3, 4]])
print(f"\n矩阵 D:\n{D}")
print(f"D 的行列式: {np.linalg.det(D)}")

# 矩阵逆
print(f"\nD 的逆矩阵:\n{np.linalg.inv(D)}")

# 2.3 矩阵的秩
print("\n2.3 矩阵的秩")
print(f"矩阵 A 的秩: {np.linalg.matrix_rank(A)}")
print(f"矩阵 B 的秩: {np.linalg.matrix_rank(B)}")
print(f"矩阵 D 的秩: {np.linalg.matrix_rank(D)}")

# 3. 线性方程组
print("\n=== 3. 线性方程组 ===")

# 3.1 求解线性方程组
print("\n3.1 求解线性方程组")

# 方程组: 2x + y = 5, x + y = 3
A = np.array([[2, 1], [1, 1]])
b = np.array([5, 3])
x = np.linalg.solve(A, b)
print(f"方程组的解: x = {x[0]}, y = {x[1]}")

# 验证解
print(f"验证: 2x + y = {2*x[0] + x[1]}")
print(f"验证: x + y = {x[0] + x[1]}")

# 3.2 矩阵的特征值和特征向量
print("\n3.2 矩阵的特征值和特征向量")

E = np.array([[2, -1], [-1, 2]])
eigenvalues, eigenvectors = np.linalg.eig(E)
print(f"矩阵 E:\n{E}")
print(f"特征值: {eigenvalues}")
print(f"特征向量:\n{eigenvectors}")

# 4. 奇异值分解
print("\n=== 4. 奇异值分解 ===")

# 4.1 SVD分解
print("\n4.1 SVD分解")

F = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
U, S, Vt = np.linalg.svd(F)
print(f"矩阵 F:\n{F}")
print(f"U 矩阵:\n{U}")
print(f"S 矩阵: {S}")
print(f"Vt 矩阵:\n{Vt}")

# 验证SVD分解
S_matrix = np.zeros(F.shape)
np.fill_diagonal(S_matrix, S)
F_reconstructed = U @ S_matrix @ Vt
print(f"\n重构矩阵:\n{F_reconstructed}")
print(f"重构误差: {np.linalg.norm(F - F_reconstructed)}")

# 5. 主成分分析
print("\n=== 5. 主成分分析 ===")

# 5.1 PCA实现
print("\n5.1 PCA实现")

def pca(X, n_components):
    """主成分分析"""
    # 中心化
    X_mean = np.mean(X, axis=0)
    X_centered = X - X_mean
    
    # 计算协方差矩阵
    cov_matrix = np.cov(X_centered.T)
    
    # 计算特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    # 按特征值降序排序
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # 选择前n_components个主成分
    eigenvectors = eigenvectors[:, :n_components]
    
    # 投影
    X_pca = X_centered @ eigenvectors
    
    return X_pca, eigenvalues, eigenvectors, X_mean

# 创建示例数据
np.random.seed(42)
X = np.random.randn(100, 3)

# 应用PCA
X_pca, eigenvalues, eigenvectors, X_mean = pca(X, 2)
print(f"原始数据形状: {X.shape}")
print(f"PCA后数据形状: {X_pca.shape}")
print(f"特征值: {eigenvalues}")
print(f"解释方差比: {eigenvalues / np.sum(eigenvalues)}")

# 可视化PCA结果
plt.figure(figsize=(10, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.title('PCA降维结果')
plt.xlabel('主成分1')
plt.ylabel('主成分2')
plt.savefig('pca_result.png')
plt.show()
print("PCA降维结果已保存为 pca_result.png")

# 6. 线性代数在机器学习中的应用
print("\n=== 6. 线性代数在机器学习中的应用 ===")

# 6.1 线性回归
print("\n6.1 线性回归")

# 创建线性回归数据
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = 2 * x + 1 + np.random.randn(100) * 2

# 构造设计矩阵
X_design = np.vstack([x, np.ones(len(x))]).T

# 使用最小二乘法求解
coefficients = np.linalg.inv(X_design.T @ X_design) @ X_design.T @ y
slope, intercept = coefficients
print(f"线性回归系数: 斜率 = {slope:.2f}, 截距 = {intercept:.2f}")

# 预测
y_pred = X_design @ coefficients

# 可视化
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='数据点')
plt.plot(x, y_pred, 'r-', label='线性回归拟合')
plt.title('线性回归')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('linear_regression.png')
plt.show()
print("线性回归结果已保存为 linear_regression.png")

# 6.2 聚类分析
print("\n6.2 聚类分析")

# K-means聚类
def k_means(X, k, max_iters=100):
    """K-means聚类"""
    # 随机初始化聚类中心
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]
    
    for _ in range(max_iters):
        # 计算每个样本到聚类中心的距离
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        
        # 分配聚类
        labels = np.argmin(distances, axis=1)
        
        # 更新聚类中心
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        
        # 检查收敛
        if np.allclose(centroids, new_centroids):
            break
        
        centroids = new_centroids
    
    return labels, centroids

# 创建聚类数据
np.random.seed(42)
X1 = np.random.normal(0, 1, (50, 2))
X2 = np.random.normal(5, 1, (50, 2))
X_cluster = np.vstack([X1, X2])

# 应用K-means
labels, centroids = k_means(X_cluster, 2)

# 可视化
plt.figure(figsize=(10, 6))
plt.scatter(X_cluster[labels == 0, 0], X_cluster[labels == 0, 1], label='聚类0')
plt.scatter(X_cluster[labels == 1, 0], X_cluster[labels == 1, 1], label='聚类1')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, color='r', label='聚类中心')
plt.title('K-means聚类')
plt.xlabel('特征1')
plt.ylabel('特征2')
plt.legend()
plt.savefig('kmeans_clustering.png')
plt.show()
print("K-means聚类结果已保存为 kmeans_clustering.png")

# 7. 线性代数库的使用
print("\n=== 7. 线性代数库的使用 ===")

print("NumPy线性代数函数:")
print("1. np.linalg.dot(a, b) - 矩阵乘法")
print("2. np.linalg.inv(a) - 矩阵求逆")
print("3. np.linalg.det(a) - 计算行列式")
print("4. np.linalg.eig(a) - 计算特征值和特征向量")
print("5. np.linalg.svd(a) - 奇异值分解")
print("6. np.linalg.solve(a, b) - 求解线性方程组")
print("7. np.linalg.norm(a) - 计算向量或矩阵的范数")
print("8. np.linalg.matrix_rank(a) - 计算矩阵的秩")

# 8. 实际应用示例
print("\n=== 8. 实际应用示例 ===")

# 8.1 图像处理中的应用
print("\n8.1 图像处理中的应用")

# 创建一个简单的图像
image = np.zeros((100, 100))
image[25:75, 25:75] = 1  # 中间的白色正方形

# 添加噪声
noise = np.random.randn(100, 100) * 0.1
noisy_image = image + noise

# 使用SVD进行图像压缩
U, S, Vt = np.linalg.svd(noisy_image)

# 保留前k个奇异值
k = 10
S_k = np.zeros((k, k))
np.fill_diagonal(S_k, S[:k])
compressed_image = U[:, :k] @ S_k @ Vt[:k, :]

# 可视化
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('原始图像')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('带噪声的图像')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(compressed_image, cmap='gray')
plt.title(f'压缩后的图像 (k={k})')
plt.axis('off')

plt.tight_layout()
plt.savefig('image_compression.png')
plt.show()
print("图像处理结果已保存为 image_compression.png")

# 9. 清理文件
print("\n=== 9. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['vector_2d.png', 'vector_3d.png', 'pca_result.png', 'linear_regression.png', 'kmeans_clustering.png', 'image_compression.png']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n线性代数练习完成！")
