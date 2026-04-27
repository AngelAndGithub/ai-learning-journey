#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 40: 模型评估与调优

本文件包含模型评估与调优的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, load_boston, make_classification
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                           confusion_matrix, classification_report, roc_curve, auc,
                           mean_squared_error, mean_absolute_error, r2_score)
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 模型评估指标
print("=== 1. 模型评估指标 ===")

# 1.1 分类模型评估
print("\n1.1 分类模型评估")

# 加载鸢尾花数据集
iris = load_iris()
X_iris, y_iris = iris.data, iris.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)

# 标准化数据
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 训练分类模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)

# 计算评估指标
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

print(f"准确率: {accuracy:.4f}")
print(f"精确率: {precision:.4f}")
print(f"召回率: {recall:.4f}")
print(f"F1分数: {f1:.4f}")

# 混淆矩阵
print("\n混淆矩阵:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# 分类报告
print("\n分类报告:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 1.2 回归模型评估
print("\n1.2 回归模型评估")

# 加载波士顿房价数据集
from sklearn.datasets import load_boston
boston = load_boston()
X_boston, y_boston = boston.data, boston.target

# 分割数据
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_boston, y_boston, test_size=0.2, random_state=42)

# 标准化数据
X_train_reg = scaler.fit_transform(X_train_reg)
X_test_reg = scaler.transform(X_test_reg)

# 训练回归模型
model_reg = RandomForestRegressor(n_estimators=100, random_state=42)
model_reg.fit(X_train_reg, y_train_reg)
y_pred_reg = model_reg.predict(X_test_reg)

# 计算评估指标
mse = mean_squared_error(y_test_reg, y_pred_reg)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")

# 2. 交叉验证
print("\n=== 2. 交叉验证 ===")

from sklearn.model_selection import KFold, StratifiedKFold, LeaveOneOut, LeavePOut

# 2.1 K折交叉验证
print("\n2.1 K折交叉验证")

# K折交叉验证
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X_iris, y_iris, cv=kf, scoring='accuracy')
print(f"K折交叉验证准确率: {scores}")
print(f"平均准确率: {scores.mean():.4f}")
print(f"准确率标准差: {scores.std():.4f}")

# 分层K折交叉验证
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores_stratified = cross_val_score(model, X_iris, y_iris, cv=skf, scoring='accuracy')
print(f"\n分层K折交叉验证准确率: {scores_stratified}")
print(f"平均准确率: {scores_stratified.mean():.4f}")
print(f"准确率标准差: {scores_stratified.std():.4f}")

# 3. 超参数调优
print("\n=== 3. 超参数调优 ===")

# 3.1 网格搜索
print("\n3.1 网格搜索")

# 定义参数网格
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# 网格搜索
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

print("最佳参数:")
print(grid_search.best_params_)
print(f"最佳交叉验证分数: {grid_search.best_score_:.4f}")
print(f"测试集分数: {grid_search.score(X_test, y_test):.4f}")

# 3.2 随机搜索
print("\n3.2 随机搜索")

from scipy.stats import randint

# 定义参数分布
param_dist = {
    'n_estimators': randint(50, 200),
    'max_depth': [3, 5, 7, None],
    'min_samples_split': randint(2, 10),
    'min_samples_leaf': randint(1, 4)
}

# 随机搜索
random_search = RandomizedSearchCV(RandomForestClassifier(random_state=42), param_distributions=param_dist, n_iter=20, cv=5, scoring='accuracy', n_jobs=-1, random_state=42)
random_search.fit(X_train, y_train)

print("最佳参数:")
print(random_search.best_params_)
print(f"最佳交叉验证分数: {random_search.best_score_:.4f}")
print(f"测试集分数: {random_search.score(X_test, y_test):.4f}")

# 4. 模型选择
print("\n=== 4. 模型选择 ===")

# 比较不同分类模型
models = {
    '逻辑回归': LogisticRegression(),
    'K近邻': KNeighborsClassifier(),
    '决策树': DecisionTreeClassifier(),
    '随机森林': RandomForestClassifier(),
    'SVM': SVC()
}

print("分类模型比较:")
for name, model in models.items():
    scores = cross_val_score(model, X_iris, y_iris, cv=5, scoring='accuracy')
    print(f"{name}: {scores.mean():.4f} ± {scores.std():.4f}")

# 比较不同回归模型
regression_models = {
    '线性回归': LinearRegression(),
    'Ridge回归': Ridge(),
    'Lasso回归': Lasso(),
    '决策树回归': DecisionTreeRegressor(),
    '随机森林回归': RandomForestRegressor()
}

print("\n回归模型比较:")
for name, model in regression_models.items():
    scores = cross_val_score(model, X_boston, y_boston, cv=5, scoring='r2')
    print(f"{name}: {scores.mean():.4f} ± {scores.std():.4f}")

# 5. 过拟合与欠拟合
print("\n=== 5. 过拟合与欠拟合 ===")

# 创建合成分类数据
X, y = make_classification(n_samples=100, n_features=20, n_informative=5, n_redundant=15, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练不同深度的决策树
max_depths = [1, 2, 3, 5, 10, 20, None]
train_scores = []
test_scores = []

for depth in max_depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    train_scores.append(model.score(X_train, y_train))
    test_scores.append(model.score(X_test, y_test))

# 可视化过拟合与欠拟合
plt.figure(figsize=(10, 6))
plt.plot(max_depths, train_scores, label='训练准确率')
plt.plot(max_depths, test_scores, label='测试准确率')
plt.xlabel('最大深度')
plt.ylabel('准确率')
plt.title('决策树深度与过拟合关系')
plt.legend()
plt.savefig('overfitting_underfitting.png')
plt.show()
print("过拟合与欠拟合关系图已保存为 overfitting_underfitting.png")

# 6. 特征重要性
print("\n=== 6. 特征重要性 ===")

# 训练随机森林模型
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 获取特征重要性
feature_importance = rf.feature_importances_

# 排序
indices = np.argsort(feature_importance)[::-1]

print("特征重要性排序:")
for i, idx in enumerate(indices[:10]):
    print(f"{i+1}. 特征 {idx}: {feature_importance[idx]:.4f}")

# 可视化特征重要性
plt.figure(figsize=(12, 6))
plt.bar(range(10), feature_importance[indices[:10]])
plt.xticks(range(10), [f'特征 {i}' for i in indices[:10]])
plt.title('前10个重要特征')
plt.savefig('feature_importance.png')
plt.show()
print("特征重要性图已保存为 feature_importance.png")

# 7. ROC曲线和AUC
print("\n=== 7. ROC曲线和AUC ===")

# 创建二分类数据
X_binary, y_binary = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
X_train_bin, X_test_bin, y_train_bin, y_test_bin = train_test_split(X_binary, y_binary, test_size=0.2, random_state=42)

# 训练模型
model = LogisticRegression()
model.fit(X_train_bin, y_train_bin)
y_pred_proba = model.predict_proba(X_test_bin)[:, 1]

# 计算ROC曲线
fpr, tpr, thresholds = roc_curve(y_test_bin, y_pred_proba)
roc_auc = auc(fpr, tpr)

# 可视化ROC曲线
plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC曲线 (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('假阳性率')
plt.ylabel('真阳性率')
plt.title('ROC曲线')
plt.legend(loc="lower right")
plt.savefig('roc_curve.png')
plt.show()
print("ROC曲线已保存为 roc_curve.png")

# 8. 模型部署
print("\n=== 8. 模型部署 ===")

# 保存模型
import joblib

# 训练最终模型
final_model = RandomForestClassifier(n_estimators=100, random_state=42)
final_model.fit(X_train, y_train)

# 保存模型
joblib.dump(final_model, 'final_model.pkl')
print("模型已保存为 final_model.pkl")

# 加载模型
loaded_model = joblib.load('final_model.pkl')

# 测试加载的模型
accuracy = loaded_model.score(X_test, y_test)
print(f"加载的模型准确率: {accuracy:.4f}")

# 9. 实际应用示例
print("\n=== 9. 实际应用示例 ===")

# 9.1 模型评估与调优完整流程
print("\n9.1 模型评估与调优完整流程")

# 步骤1: 数据准备
print("步骤1: 数据准备")
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 步骤2: 模型选择
print("\n步骤2: 模型选择")
models = {
    '逻辑回归': LogisticRegression(),
    'K近邻': KNeighborsClassifier(),
    '随机森林': RandomForestClassifier()
}

for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    print(f"{name}: {scores.mean():.4f} ± {scores.std():.4f}")

# 步骤3: 超参数调优
print("\n步骤3: 超参数调优")
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)
print(f"最佳参数: {grid_search.best_params_}")
print(f"最佳交叉验证分数: {grid_search.best_score_:.4f}")

# 步骤4: 模型评估
print("\n步骤4: 模型评估")
best_model = grid_search.best_estimator
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"测试集准确率: {accuracy:.4f}")

# 步骤5: 模型部署
print("\n步骤5: 模型部署")
joblib.dump(best_model, 'iris_classifier.pkl')
print("模型已保存为 iris_classifier.pkl")

# 10. 清理文件
print("\n=== 10. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['overfitting_underfitting.png', 'feature_importance.png', 'roc_curve.png', 'final_model.pkl', 'iris_classifier.pkl']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n模型评估与调优练习完成！")
