#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 38: 监督学习-回归

本文件包含监督学习回归算法的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston, make_regression, load_diabetes
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.pipeline import make_pipeline

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 数据准备
print("=== 1. 数据准备 ===")

# 1.1 加载数据集
print("\n1.1 加载数据集")

# 加载波士顿房价数据集
boston = load_boston()
X_boston, y_boston = boston.data, boston.target
print(f"波士顿房价数据集: X={X_boston.shape}, y={y_boston.shape}")
print(f"特征名称: {boston.feature_names}")

# 加载糖尿病数据集
diabetes = load_diabetes()
X_diabetes, y_diabetes = diabetes.data, diabetes.target
print(f"\n糖尿病数据集: X={X_diabetes.shape}, y={y_diabetes.shape}")
print(f"特征名称: {diabetes.feature_names}")

# 创建回归数据集
X_reg, y_reg = make_regression(n_samples=1000, n_features=10, n_informative=5, noise=0.1, random_state=42)
print(f"\n合成回归数据集: X={X_reg.shape}, y={y_reg.shape}")

# 1.2 数据预处理
print("\n1.2 数据预处理")

# 标准化数据
scaler = StandardScaler()
X_boston_scaled = scaler.fit_transform(X_boston)
X_diabetes_scaled = scaler.fit_transform(X_diabetes)
X_reg_scaled = scaler.fit_transform(X_reg)

# 分割数据
X_train_boston, X_test_boston, y_train_boston, y_test_boston = train_test_split(X_boston_scaled, y_boston, test_size=0.2, random_state=42)
X_train_diabetes, X_test_diabetes, y_train_diabetes, y_test_diabetes = train_test_split(X_diabetes_scaled, y_diabetes, test_size=0.2, random_state=42)

print(f"波士顿房价训练集: {X_train_boston.shape}, 测试集: {X_test_boston.shape}")
print(f"糖尿病训练集: {X_train_diabetes.shape}, 测试集: {X_test_diabetes.shape}")

# 2. 回归算法
print("\n=== 2. 回归算法 ===")

# 2.1 线性回归
print("\n2.1 线性回归")

lr = LinearRegression()
lr.fit(X_train_boston, y_train_boston)
y_pred_lr = lr.predict(X_test_boston)

mse_lr = mean_squared_error(y_test_boston, y_pred_lr)
rmse_lr = np.sqrt(mse_lr)
mae_lr = mean_absolute_error(y_test_boston, y_pred_lr)
r2_lr = r2_score(y_test_boston, y_pred_lr)

print(f"线性回归 - MSE: {mse_lr:.4f}, RMSE: {rmse_lr:.4f}, MAE: {mae_lr:.4f}, R²: {r2_lr:.4f}")

# 2.2 岭回归
print("\n2.2 岭回归")

ridge = Ridge(alpha=1.0)
ridge.fit(X_train_boston, y_train_boston)
y_pred_ridge = ridge.predict(X_test_boston)

mse_ridge = mean_squared_error(y_test_boston, y_pred_ridge)
rmse_ridge = np.sqrt(mse_ridge)
mae_ridge = mean_absolute_error(y_test_boston, y_pred_ridge)
r2_ridge = r2_score(y_test_boston, y_pred_ridge)

print(f"岭回归 - MSE: {mse_ridge:.4f}, RMSE: {rmse_ridge:.4f}, MAE: {mae_ridge:.4f}, R²: {r2_ridge:.4f}")

# 2.3 Lasso回归
print("\n2.3 Lasso回归")

lasso = Lasso(alpha=0.1)
lasso.fit(X_train_boston, y_train_boston)
y_pred_lasso = lasso.predict(X_test_boston)

mse_lasso = mean_squared_error(y_test_boston, y_pred_lasso)
rmse_lasso = np.sqrt(mse_lasso)
mae_lasso = mean_absolute_error(y_test_boston, y_pred_lasso)
r2_lasso = r2_score(y_test_boston, y_pred_lasso)

print(f"Lasso回归 - MSE: {mse_lasso:.4f}, RMSE: {rmse_lasso:.4f}, MAE: {mae_lasso:.4f}, R²: {r2_lasso:.4f}")

# 2.4 ElasticNet回归
print("\n2.4 ElasticNet回归")

elasticnet = ElasticNet(alpha=0.1, l1_ratio=0.5)
elasticnet.fit(X_train_boston, y_train_boston)
y_pred_enet = elasticnet.predict(X_test_boston)

mse_enet = mean_squared_error(y_test_boston, y_pred_enet)
rmse_enet = np.sqrt(mse_enet)
mae_enet = mean_absolute_error(y_test_boston, y_pred_enet)
r2_enet = r2_score(y_test_boston, y_pred_enet)

print(f"ElasticNet回归 - MSE: {mse_enet:.4f}, RMSE: {rmse_enet:.4f}, MAE: {mae_enet:.4f}, R²: {r2_enet:.4f}")

# 2.5 K近邻回归
print("\n2.5 K近邻回归")

knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train_boston, y_train_boston)
y_pred_knn = knn.predict(X_test_boston)

mse_knn = mean_squared_error(y_test_boston, y_pred_knn)
rmse_knn = np.sqrt(mse_knn)
mae_knn = mean_absolute_error(y_test_boston, y_pred_knn)
r2_knn = r2_score(y_test_boston, y_pred_knn)

print(f"K近邻回归 - MSE: {mse_knn:.4f}, RMSE: {rmse_knn:.4f}, MAE: {mae_knn:.4f}, R²: {r2_knn:.4f}")

# 2.6 支持向量回归
print("\n2.6 支持向量回归")

svr = SVR(kernel='rbf', C=1.0, gamma='scale')
svr.fit(X_train_boston, y_train_boston)
y_pred_svr = svr.predict(X_test_boston)

mse_svr = mean_squared_error(y_test_boston, y_pred_svr)
rmse_svr = np.sqrt(mse_svr)
mae_svr = mean_absolute_error(y_test_boston, y_pred_svr)
r2_svr = r2_score(y_test_boston, y_pred_svr)

print(f"SVR - MSE: {mse_svr:.4f}, RMSE: {rmse_svr:.4f}, MAE: {mae_svr:.4f}, R²: {r2_svr:.4f}")

# 2.7 决策树回归
print("\n2.7 决策树回归")

dt = DecisionTreeRegressor(max_depth=5, random_state=42)
dt.fit(X_train_boston, y_train_boston)
y_pred_dt = dt.predict(X_test_boston)

mse_dt = mean_squared_error(y_test_boston, y_pred_dt)
rmse_dt = np.sqrt(mse_dt)
mae_dt = mean_absolute_error(y_test_boston, y_pred_dt)
r2_dt = r2_score(y_test_boston, y_pred_dt)

print(f"决策树回归 - MSE: {mse_dt:.4f}, RMSE: {rmse_dt:.4f}, MAE: {mae_dt:.4f}, R²: {r2_dt:.4f}")

# 2.8 随机森林回归
print("\n2.8 随机森林回归")

rf = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train_boston, y_train_boston)
y_pred_rf = rf.predict(X_test_boston)

mse_rf = mean_squared_error(y_test_boston, y_pred_rf)
rmse_rf = np.sqrt(mse_rf)
mae_rf = mean_absolute_error(y_test_boston, y_pred_rf)
r2_rf = r2_score(y_test_boston, y_pred_rf)

print(f"随机森林回归 - MSE: {mse_rf:.4f}, RMSE: {rmse_rf:.4f}, MAE: {mae_rf:.4f}, R²: {r2_rf:.4f}")

# 2.9 梯度提升回归
print("\n2.9 梯度提升回归")

gb = GradientBoostingRegressor(n_estimators=100, max_depth=3, random_state=42)
gb.fit(X_train_boston, y_train_boston)
y_pred_gb = gb.predict(X_test_boston)

mse_gb = mean_squared_error(y_test_boston, y_pred_gb)
rmse_gb = np.sqrt(mse_gb)
mae_gb = mean_absolute_error(y_test_boston, y_pred_gb)
r2_gb = r2_score(y_test_boston, y_pred_gb)

print(f"梯度提升回归 - MSE: {mse_gb:.4f}, RMSE: {rmse_gb:.4f}, MAE: {mae_gb:.4f}, R²: {r2_gb:.4f}")

# 2.10 AdaBoost回归
print("\n2.10 AdaBoost回归")

adaboost = AdaBoostRegressor(n_estimators=100, random_state=42)
adaboost.fit(X_train_boston, y_train_boston)
y_pred_adaboost = adaboost.predict(X_test_boston)

mse_adaboost = mean_squared_error(y_test_boston, y_pred_adaboost)
rmse_adaboost = np.sqrt(mse_adaboost)
mae_adaboost = mean_absolute_error(y_test_boston, y_pred_adaboost)
r2_adaboost = r2_score(y_test_boston, y_pred_adaboost)

print(f"AdaBoost回归 - MSE: {mse_adaboost:.4f}, RMSE: {rmse_adaboost:.4f}, MAE: {mae_adaboost:.4f}, R²: {r2_adaboost:.4f}")

# 3. 模型评估
print("\n=== 3. 模型评估 ===")

# 3.1 模型性能比较
print("\n3.1 模型性能比较")

models = {
    '线性回归': lr,
    '岭回归': ridge,
    'Lasso回归': lasso,
    'ElasticNet回归': elasticnet,
    'K近邻回归': knn,
    'SVR': svr,
    '决策树回归': dt,
    '随机森林回归': rf,
    '梯度提升回归': gb,
    'AdaBoost回归': adaboost
}

performance = {}
for name, model in models.items():
    y_pred = model.predict(X_test_boston)
    mse = mean_squared_error(y_test_boston, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test_boston, y_pred)
    performance[name] = {'MSE': mse, 'RMSE': rmse, 'R²': r2}

# 转换为DataFrame便于查看
import pandas as pd
performance_df = pd.DataFrame(performance).T
print("模型性能比较:")
print(performance_df.sort_values('R²', ascending=False))

# 3.2 交叉验证
print("\n3.2 交叉验证")

from sklearn.model_selection import KFold

kf = KFold(n_splits=5, shuffle=True, random_state=42)

print("5折交叉验证结果:")
for name, model in models.items():
    scores = cross_val_score(model, X_boston_scaled, y_boston, cv=kf, scoring='r2')
    print(f"{name}: {scores.mean():.4f} ± {scores.std():.4f}")

# 4. 超参数调优
print("\n=== 4. 超参数调优 ===")

from sklearn.model_selection import GridSearchCV

# 以梯度提升回归为例进行网格搜索
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2]
}

grid_search = GridSearchCV(GradientBoostingRegressor(random_state=42), param_grid, cv=5, scoring='r2', n_jobs=-1)
grid_search.fit(X_train_boston, y_train_boston)

print("梯度提升回归最佳参数:")
print(grid_search.best_params_)
print(f"最佳R²得分: {grid_search.best_score_:.4f}")

# 5. 特征重要性
print("\n=== 5. 特征重要性 ===")

# 随机森林特征重要性
feature_importance = rf.feature_importances_
feature_names = boston.feature_names

# 排序
indices = np.argsort(feature_importance)[::-1]

print("特征重要性排序:")
for i, idx in enumerate(indices):
    print(f"{i+1}. {feature_names[idx]}: {feature_importance[idx]:.4f}")

# 可视化特征重要性
plt.figure(figsize=(12, 6))
plt.bar(range(len(feature_importance)), feature_importance[indices])
plt.xticks(range(len(feature_importance)), [feature_names[i] for i in indices], rotation=45)
plt.title('特征重要性')
plt.savefig('feature_importance.png')
plt.show()
print("特征重要性图已保存为 feature_importance.png")

# 6. 多项式回归
print("\n=== 6. 多项式回归 ===")

# 创建简单的非线性数据
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.randn(100) * 0.1

# 重塑数据
X = x.reshape(-1, 1)

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练不同次数的多项式回归
degrees = [1, 2, 3, 5, 10]
plt.figure(figsize=(12, 8))
plt.scatter(X_train, y_train, label='训练数据')
plt.scatter(X_test, y_test, label='测试数据', alpha=0.5)

x_range = np.linspace(0, 10, 1000).reshape(-1, 1)

for degree in degrees:
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_pred_range = model.predict(x_range)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"多项式回归 (degree={degree}): MSE={mse:.4f}, R²={r2:.4f}")
    
    plt.plot(x_range, y_pred_range, label=f"degree={degree} (R²={r2:.3f})")

plt.title('多项式回归示例')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('polynomial_regression.png')
plt.show()
print("多项式回归示例已保存为 polynomial_regression.png")

# 7. 实际应用示例
print("\n=== 7. 实际应用示例 ===")

# 7.1 波士顿房价预测
print("\n7.1 波士顿房价预测")

# 使用最佳模型（梯度提升回归）
best_model = GradientBoostingRegressor(n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42)
best_model.fit(X_train_boston, y_train_boston)
y_pred = best_model.predict(X_test_boston)

# 评估
mse = mean_squared_error(y_test_boston, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test_boston, y_pred)
r2 = r2_score(y_test_boston, y_pred)

print(f"最佳模型性能 - MSE: {mse:.4f}, RMSE: {rmse:.4f}, MAE: {mae:.4f}, R²: {r2:.4f}")

# 可视化预测结果
plt.figure(figsize=(10, 6))
plt.scatter(y_test_boston, y_pred)
plt.plot([y_test_boston.min(), y_test_boston.max()], [y_test_boston.min(), y_test_boston.max()], 'r--')
plt.title('实际值 vs 预测值')
plt.xlabel('实际房价')
plt.ylabel('预测房价')
plt.savefig('prediction_vs_actual.png')
plt.show()
print("预测结果可视化已保存为 prediction_vs_actual.png")

# 7.2 糖尿病进展预测
print("\n7.2 糖尿病进展预测")

# 训练模型
model_diabetes = RandomForestRegressor(n_estimators=100, random_state=42)
model_diabetes.fit(X_train_diabetes, y_train_diabetes)
y_pred_diabetes = model_diabetes.predict(X_test_diabetes)

# 评估
mse_diabetes = mean_squared_error(y_test_diabetes, y_pred_diabetes)
rmse_diabetes = np.sqrt(mse_diabetes)
r2_diabetes = r2_score(y_test_diabetes, y_pred_diabetes)

print(f"糖尿病进展预测 - MSE: {mse_diabetes:.4f}, RMSE: {rmse_diabetes:.4f}, R²: {r2_diabetes:.4f}")

# 8. 回归算法选择指南
print("\n=== 8. 回归算法选择指南 ===")
print("1. 线性回归: 适用于线性关系，计算效率高")
print("2. 岭回归: 适用于多重共线性问题")
print("3. Lasso回归: 适用于特征选择")
print("4. ElasticNet回归: 结合L1和L2正则化")
print("5. K近邻回归: 适用于非线性关系，对异常值敏感")
print("6. SVR: 适用于高维数据，参数调优复杂")
print("7. 决策树回归: 适用于非线性关系，易于理解")
print("8. 随机森林回归: 适用于大多数问题，鲁棒性强")
print("9. 梯度提升回归: 精度高，但训练时间长")
print("10. AdaBoost回归: 适用于弱学习器的集成")

# 9. 清理文件
print("\n=== 9. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['feature_importance.png', 'polynomial_regression.png', 'prediction_vs_actual.png']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n监督学习-回归练习完成！")
