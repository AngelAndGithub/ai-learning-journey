#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 46: 实战项目1 - 房价预测

本文件包含房价预测的实战项目代码
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 数据加载与探索
print("=== 1. 数据加载与探索 ===")

# 加载波士顿房价数据集
boston = load_boston()
X, y = boston.data, boston.target

# 转换为DataFrame
df = pd.DataFrame(X, columns=boston.feature_names)
df['PRICE'] = y

print(f"数据集形状: {df.shape}")
print(f"特征名称: {boston.feature_names}")
print(f"价格范围: {y.min():.2f} - {y.max():.2f}")
print(f"价格均值: {y.mean():.2f}")

# 数据概览
print("\n数据概览:")
print(df.head())

# 数据描述性统计
print("\n数据描述性统计:")
print(df.describe())

# 2. 数据可视化
print("\n=== 2. 数据可视化 ===")

# 价格分布
plt.figure(figsize=(10, 6))
sns.histplot(df['PRICE'], bins=30, kde=True)
plt.title('房价分布')
plt.xlabel('房价')
plt.ylabel('频率')
plt.savefig('price_distribution.png')
plt.show()
print("房价分布图已保存为 price_distribution.png")

# 特征相关性热力图
plt.figure(figsize=(12, 10))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('特征相关性热力图')
plt.savefig('correlation_heatmap.png')
plt.show()
print("特征相关性热力图已保存为 correlation_heatmap.png")

# 选择与价格相关性较高的特征进行可视化
corr_with_price = corr['PRICE'].sort_values(ascending=False)
print("\n与价格相关性排序:")
print(corr_with_price)

# 绘制相关性较高的特征与价格的散点图
top_features = corr_with_price.index[1:6]  # 排除价格本身

plt.figure(figsize=(15, 10))
for i, feature in enumerate(top_features, 1):
    plt.subplot(2, 3, i)
    sns.scatterplot(x=df[feature], y=df['PRICE'])
    plt.title(f'{feature} vs PRICE')
    plt.xlabel(feature)
    plt.ylabel('PRICE')

plt.tight_layout()
plt.savefig('top_features_scatter.png')
plt.show()
print("特征与价格散点图已保存为 top_features_scatter.png")

# 3. 数据预处理
print("\n=== 3. 数据预处理 ===")

# 检查缺失值
print("\n检查缺失值:")
print(df.isnull().sum())

# 特征标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
print(f"训练集形状: {X_train.shape}, {y_train.shape}")
print(f"测试集形状: {X_test.shape}, {y_test.shape}")

# 4. 模型训练与评估
print("\n=== 4. 模型训练与评估 ===")

# 定义模型
models = {
    '线性回归': LinearRegression(),
    'Ridge回归': Ridge(),
    'Lasso回归': Lasso(),
    'ElasticNet回归': ElasticNet(),
    '决策树回归': DecisionTreeRegressor(),
    '随机森林回归': RandomForestRegressor(),
    '梯度提升回归': GradientBoostingRegressor(),
    'SVR': SVR()
}

# 训练和评估模型
results = []
for name, model in models.items():
    # 交叉验证
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
    
    # 训练模型
    model.fit(X_train, y_train)
    
    # 预测
    y_pred = model.predict(X_test)
    
    # 计算评估指标
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results.append({
        '模型': name,
        '交叉验证R²': scores.mean(),
        '测试集MSE': mse,
        '测试集RMSE': rmse,
        '测试集MAE': mae,
        '测试集R²': r2
    })
    
    print(f"{name}: 交叉验证R² = {scores.mean():.4f}, 测试集R² = {r2:.4f}, 测试集RMSE = {rmse:.4f}")

# 结果排序
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('测试集R²', ascending=False)
print("\n模型性能排序:")
print(results_df)

# 5. 模型调优
print("\n=== 5. 模型调优 ===")

# 选择表现最好的模型进行调优（梯度提升回归）
print("调优梯度提升回归模型...")

param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.05, 0.1],
    'max_depth': [3, 4, 5],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(GradientBoostingRegressor(random_state=42), param_grid, cv=5, scoring='r2', n_jobs=-1)
grid_search.fit(X_train, y_train)

print(f"最佳参数: {grid_search.best_params_}")
print(f"最佳交叉验证分数: {grid_search.best_score_:.4f}")

# 评估调优后的模型
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)
mse_best = mean_squared_error(y_test, y_pred_best)
rmse_best = np.sqrt(mse_best)
r2_best = r2_score(y_test, y_pred_best)

print(f"\n调优后模型性能:")
print(f"MSE: {mse_best:.4f}")
print(f"RMSE: {rmse_best:.4f}")
print(f"R²: {r2_best:.4f}")

# 6. 特征重要性
print("\n=== 6. 特征重要性 ===")

# 获取特征重要性
feature_importance = best_model.feature_importances_
indices = np.argsort(feature_importance)[::-1]

print("特征重要性排序:")
for i, idx in enumerate(indices):
    print(f"{i+1}. {boston.feature_names[idx]}: {feature_importance[idx]:.4f}")

# 可视化特征重要性
plt.figure(figsize=(12, 6))
plt.bar(range(len(feature_importance)), feature_importance[indices])
plt.xticks(range(len(feature_importance)), [boston.feature_names[i] for i in indices], rotation=45)
plt.title('特征重要性')
plt.savefig('feature_importance.png')
plt.show()
print("特征重要性图已保存为 feature_importance.png")

# 7. 预测结果可视化
print("\n=== 7. 预测结果可视化 ===")

# 真实值 vs 预测值
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_best)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title('真实值 vs 预测值')
plt.xlabel('真实房价')
plt.ylabel('预测房价')
plt.savefig('prediction_vs_actual.png')
plt.show()
print("真实值 vs 预测值图已保存为 prediction_vs_actual.png")

# 残差图
residuals = y_test - y_pred_best
plt.figure(figsize=(10, 6))
plt.scatter(y_pred_best, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.title('残差图')
plt.xlabel('预测房价')
plt.ylabel('残差')
plt.savefig('residuals.png')
plt.show()
print("残差图已保存为 residuals.png")

# 8. 模型部署
print("\n=== 8. 模型部署 ===")

import joblib

# 保存模型
joblib.dump(best_model, 'house_price_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("模型已保存为 house_price_model.pkl")
print("标准化器已保存为 scaler.pkl")

# 加载模型
loaded_model = joblib.load('house_price_model.pkl')
loaded_scaler = joblib.load('scaler.pkl')

# 测试加载的模型
test_sample = X_test[0].reshape(1, -1)
predicted_price = loaded_model.predict(test_sample)
print(f"\n测试样本预测房价: ${predicted_price[0]:.2f}")
print(f"实际房价: ${y_test[0]:.2f}")

# 9. 项目总结
print("\n=== 9. 项目总结 ===")
print("1. 数据探索: 分析了波士顿房价数据集的基本特征和分布")
print("2. 数据可视化: 展示了房价分布和特征相关性")
print("3. 模型训练: 比较了多种回归模型的性能")
print("4. 模型调优: 使用网格搜索优化了梯度提升回归模型")
print("5. 特征重要性: 分析了影响房价的重要特征")
print("6. 模型评估: 评估了模型的预测性能")
print("7. 模型部署: 保存了模型和标准化器，可用于实际应用")

# 10. 清理文件
print("\n=== 10. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['price_distribution.png', 'correlation_heatmap.png', 'top_features_scatter.png',
                   'feature_importance.png', 'prediction_vs_actual.png', 'residuals.png',
                   'house_price_model.pkl', 'scaler.pkl']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n房价预测项目完成！")
