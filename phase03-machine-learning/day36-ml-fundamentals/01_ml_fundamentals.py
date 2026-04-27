#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 36: 机器学习基础概念

本文件包含机器学习基础概念的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, make_classification, make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 机器学习概述
print("=== 1. 机器学习概述 ===")

print("机器学习是人工智能的一个分支，通过算法让计算机从数据中学习并做出预测或决策。")
print("主要类型包括：")
print("1. 监督学习：从标记数据中学习")
print("2. 无监督学习：从未标记数据中学习")
print("3. 强化学习：通过与环境交互学习")
print("4. 半监督学习：结合标记和未标记数据")

# 2. 数据准备
print("\n=== 2. 数据准备 ===")

# 2.1 加载示例数据集
print("\n2.1 加载示例数据集")

# 加载鸢尾花数据集
iris = load_iris()
X_iris, y_iris = iris.data, iris.target
print(f"鸢尾花数据集形状: X={X_iris.shape}, y={y_iris.shape}")
print(f"特征名称: {iris.feature_names}")
print(f"类别名称: {iris.target_names}")

# 创建分类数据集
X_class, y_class = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
print(f"\n分类数据集形状: X={X_class.shape}, y={y_class.shape}")

# 创建回归数据集
X_reg, y_reg = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
print(f"\n回归数据集形状: X={X_reg.shape}, y={y_reg.shape}")

# 2.2 数据分割
print("\n2.2 数据分割")

# 分割鸢尾花数据集
X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)
print(f"训练集形状: X={X_train.shape}, y={y_train.shape}")
print(f"测试集形状: X={X_test.shape}, y={y_test.shape}")

# 3. 监督学习示例
print("\n=== 3. 监督学习示例 ===")

# 3.1 线性回归
print("\n3.1 线性回归")

# 创建简单的线性回归数据
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = 2 * x + 1 + np.random.randn(100) * 2

# 重塑数据
X = x.reshape(-1, 1)

# 分割数据
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
model = LinearRegression()
model.fit(X_train_reg, y_train_reg)

# 预测
y_pred = model.predict(X_test_reg)

# 评估
mse = mean_squared_error(y_test_reg, y_pred)
print(f"线性回归 MSE: {mse:.4f}")
print(f"回归系数: {model.coef_[0]:.4f}")
print(f"截距: {model.intercept_:.4f}")

# 可视化
plt.figure(figsize=(10, 6))
plt.scatter(X_test_reg, y_test_reg, label='真实值')
plt.plot(X_test_reg, y_pred, 'r-', label='预测值')
plt.title('线性回归示例')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('linear_regression_example.png')
plt.show()
print("线性回归示例已保存为 linear_regression_example.png")

# 3.2 逻辑回归
print("\n3.2 逻辑回归")

# 分割分类数据集
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X_class, y_class, test_size=0.2, random_state=42)

# 训练模型
model = LogisticRegression()
model.fit(X_train_clf, y_train_clf)

# 预测
y_pred_clf = model.predict(X_test_clf)

# 评估
accuracy = accuracy_score(y_test_clf, y_pred_clf)
print(f"逻辑回归准确率: {accuracy:.4f}")

# 4. 无监督学习示例
print("\n=== 4. 无监督学习示例 ===")

# 4.1 K-means聚类
print("\n4.1 K-means聚类")

from sklearn.cluster import KMeans

# 创建聚类数据
np.random.seed(42)
X_cluster = np.vstack([
    np.random.normal(0, 1, (100, 2)),
    np.random.normal(5, 1, (100, 2)),
    np.random.normal(10, 1, (100, 2))
])

# 训练K-means模型
kmeans = KMeans(n_clusters=3, random_state=42)
y_cluster = kmeans.fit_predict(X_cluster)

# 可视化
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_cluster[:, 0], y=X_cluster[:, 1], hue=y_cluster, palette='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', s=200, color='r')
plt.title('K-means聚类示例')
plt.xlabel('特征1')
plt.ylabel('特征2')
plt.savefig('kmeans_example.png')
plt.show()
print("K-means聚类示例已保存为 kmeans_example.png")

# 4.2 主成分分析
print("\n4.2 主成分分析")

from sklearn.decomposition import PCA

# 应用PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_iris)

# 可视化
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y_iris, palette='viridis')
plt.title('PCA降维示例')
plt.xlabel('主成分1')
plt.ylabel('主成分2')
plt.savefig('pca_example.png')
plt.show()
print("PCA降维示例已保存为 pca_example.png")

# 5. 模型评估
print("\n=== 5. 模型评估 ===")

from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

# 计算分类模型的评估指标
precision = precision_score(y_test_clf, y_pred_clf)
recall = recall_score(y_test_clf, y_pred_clf)
f1 = f1_score(y_test_clf, y_pred_clf)
conf_matrix = confusion_matrix(y_test_clf, y_pred_clf)

print(f"准确率: {accuracy:.4f}")
print(f"精确率: {precision:.4f}")
print(f"召回率: {recall:.4f}")
print(f"F1分数: {f1:.4f}")
print(f"混淆矩阵:\n{conf_matrix}")

# 可视化混淆矩阵
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='d')
plt.title('混淆矩阵')
plt.xlabel('预测标签')
plt.ylabel('真实标签')
plt.savefig('confusion_matrix.png')
plt.show()
print("混淆矩阵已保存为 confusion_matrix.png")

# 6. 过拟合与欠拟合
print("\n=== 6. 过拟合与欠拟合 ===")

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# 创建非线性数据
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.randn(100) * 0.1

# 重塑数据
X = x.reshape(-1, 1)

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练不同复杂度的模型
models = {
    '线性模型': LinearRegression(),
    '多项式模型(2次)': make_pipeline(PolynomialFeatures(2), LinearRegression()),
    '多项式模型(10次)': make_pipeline(PolynomialFeatures(10), LinearRegression()),
    '多项式模型(20次)': make_pipeline(PolynomialFeatures(20), LinearRegression())
}

# 评估模型
plt.figure(figsize=(12, 8))
plt.scatter(X_train, y_train, label='训练数据')
plt.scatter(X_test, y_test, label='测试数据', alpha=0.5)

x_range = np.linspace(0, 10, 1000).reshape(-1, 1)

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    y_pred_range = model.predict(x_range)
    
    mse_train = mean_squared_error(y_train, y_pred_train)
    mse_test = mean_squared_error(y_test, y_pred_test)
    
    print(f"{name}: 训练MSE={mse_train:.4f}, 测试MSE={mse_test:.4f}")
    
    plt.plot(x_range, y_pred_range, label=f"{name} (测试MSE={mse_test:.4f})")

plt.title('过拟合与欠拟合示例')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('overfitting_underfitting.png')
plt.show()
print("过拟合与欠拟合示例已保存为 overfitting_underfitting.png")

# 7. 交叉验证
print("\n=== 7. 交叉验证 ===")

from sklearn.model_selection import cross_val_score, KFold

# 使用5折交叉验证
kf = KFold(n_splits=5, shuffle=True, random_state=42)
model = LogisticRegression()
scores = cross_val_score(model, X_class, y_class, cv=kf, scoring='accuracy')

print(f"5折交叉验证准确率: {scores}")
print(f"平均准确率: {scores.mean():.4f}")
print(f"准确率标准差: {scores.std():.4f}")

# 8. 特征重要性
print("\n=== 8. 特征重要性 ===")

from sklearn.ensemble import RandomForestClassifier

# 训练随机森林模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_clf, y_train_clf)

# 获取特征重要性
feature_importance = model.feature_importances_

# 可视化特征重要性
plt.figure(figsize=(12, 6))
sorted_idx = np.argsort(feature_importance)[::-1]
plt.bar(range(X_train_clf.shape[1]), feature_importance[sorted_idx])
plt.title('特征重要性')
plt.xlabel('特征索引')
plt.ylabel('重要性')
plt.savefig('feature_importance.png')
plt.show()
print("特征重要性图已保存为 feature_importance.png")

# 9. 实际应用示例
print("\n=== 9. 实际应用示例 ===")

# 9.1 鸢尾花分类
print("\n9.1 鸢尾花分类")

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# 训练多个分类模型
models = {
    'KNN': KNeighborsClassifier(),
    'SVM': SVC(),
    '随机森林': RandomForestClassifier(n_estimators=100, random_state=42),
    '逻辑回归': LogisticRegression()
}

# 评估模型
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name} 准确率: {accuracy:.4f}")

# 9.2 波士顿房价预测
print("\n9.2 波士顿房价预测")

from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor

# 加载波士顿房价数据集
boston = load_boston()
X_boston, y_boston = boston.data, boston.target

# 分割数据
X_train_boston, X_test_boston, y_train_boston, y_test_boston = train_test_split(X_boston, y_boston, test_size=0.2, random_state=42)

# 训练回归模型
models = {
    '线性回归': LinearRegression(),
    '随机森林回归': RandomForestRegressor(n_estimators=100, random_state=42)
}

# 评估模型
for name, model in models.items():
    model.fit(X_train_boston, y_train_boston)
    y_pred = model.predict(X_test_boston)
    mse = mean_squared_error(y_test_boston, y_pred)
    rmse = np.sqrt(mse)
    print(f"{name} RMSE: {rmse:.4f}")

# 10. 机器学习工作流程
print("\n=== 10. 机器学习工作流程 ===")
print("1. 问题定义")
print("2. 数据收集")
print("3. 数据预处理")
print("4. 特征工程")
print("5. 模型选择")
print("6. 模型训练")
print("7. 模型评估")
print("8. 模型调优")
print("9. 模型部署")
print("10. 模型监控与维护")

# 11. 清理文件
print("\n=== 11. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['linear_regression_example.png', 'kmeans_example.png', 'pca_example.png',
                   'confusion_matrix.png', 'overfitting_underfitting.png', 'feature_importance.png']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n机器学习基础概念练习完成！")
