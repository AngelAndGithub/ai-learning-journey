#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 40: 深度学习基础

本文件包含深度学习基础概念的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD, Adam, RMSprop
from tensorflow.keras.losses import MeanSquaredError, BinaryCrossentropy, CategoricalCrossentropy
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 深度学习概述
print("=== 1. 深度学习概述 ===")

print("深度学习是机器学习的一个分支，使用多层神经网络来学习数据的表示。")
print("主要特点：")
print("1. 自动特征提取")
print("2. 能够学习复杂的非线性关系")
print("3. 需要大量数据和计算资源")
print("4. 适用于图像、语音、自然语言处理等复杂任务")

# 2. 神经网络基础
print("\n=== 2. 神经网络基础 ===")

# 2.1 感知器
print("\n2.1 感知器")

# 简单感知器实现
class Perceptron:
    def __init__(self, input_size, learning_rate=0.01):
        self.weights = np.random.randn(input_size) * 0.01
        self.bias = 0.0
        self.learning_rate = learning_rate
    
    def activate(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        return self.activate(np.dot(x, self.weights) + self.bias)
    
    def train(self, X, y, epochs=100):
        for epoch in range(epochs):
            for i in range(len(X)):
                prediction = self.predict(X[i])
                error = y[i] - prediction
                self.weights += self.learning_rate * error * X[i]
                self.bias += self.learning_rate * error

# 测试感知器
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # AND逻辑

perceptron = Perceptron(input_size=2)
perceptron.train(X, y, epochs=100)

print("感知器测试结果 (AND逻辑):")
for i in range(len(X)):
    print(f"输入: {X[i]}, 预测: {perceptron.predict(X[i])}, 真实: {y[i]}")

# 2.2 神经网络结构
print("\n2.2 神经网络结构")

# 创建一个简单的神经网络模型
model = Sequential([
    Dense(64, input_shape=(10,), activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

print("神经网络模型结构:")
model.summary()

# 3. 激活函数
print("\n=== 3. 激活函数 ===")

# 定义激活函数
x = np.linspace(-5, 5, 100)

# Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Tanh
def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

# ReLU
def relu(x):
    return np.maximum(0, x)

# Leaky ReLU
def leaky_relu(x, alpha=0.01):
    return np.maximum(alpha * x, x)

# 可视化激活函数
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, sigmoid(x))
plt.title('Sigmoid')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x, tanh(x))
plt.title('Tanh')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(x, relu(x))
plt.title('ReLU')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(x, leaky_relu(x))
plt.title('Leaky ReLU')
plt.grid(True)

plt.tight_layout()
plt.savefig('activation_functions.png')
plt.show()
print("激活函数可视化已保存为 activation_functions.png")

# 4. 损失函数
print("\n=== 4. 损失函数 ===")

# 4.1 回归损失函数
print("\n4.1 回归损失函数")

# 均方误差
mse = MeanSquaredError()
y_true = np.array([1.0, 2.0, 3.0])
y_pred = np.array([1.1, 2.2, 2.9])
print(f"均方误差: {mse(y_true, y_pred).numpy():.4f}")

# 4.2 分类损失函数
print("\n4.2 分类损失函数")

# 二元交叉熵
bce = BinaryCrossentropy()
y_true_binary = np.array([1, 0, 1])
y_pred_binary = np.array([0.9, 0.1, 0.8])
print(f"二元交叉熵: {bce(y_true_binary, y_pred_binary).numpy():.4f}")

# 多分类交叉熵
cce = CategoricalCrossentropy()
y_true_categorical = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
y_pred_categorical = np.array([[0.8, 0.1, 0.1], [0.1, 0.7, 0.2], [0.2, 0.2, 0.6]])
print(f"多分类交叉熵: {cce(y_true_categorical, y_pred_categorical).numpy():.4f}")

# 5. 优化器
print("\n=== 5. 优化器 ===")

# 常用优化器
optimizers = {
    'SGD': SGD(learning_rate=0.01),
    'Adam': Adam(learning_rate=0.001),
    'RMSprop': RMSprop(learning_rate=0.001)
}

print("常用优化器:")
for name, optimizer in optimizers.items():
    print(f"- {name}")

# 6. 模型训练
print("\n=== 6. 模型训练 ===")

# 6.1 二分类任务
print("\n6.1 二分类任务")

# 创建二分类数据集
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 标准化数据
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 创建模型
model = Sequential([
    Dense(64, activation='relu', input_shape=(20,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# 编译模型
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 训练模型
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=0)

# 评估模型
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"二分类模型 - 损失: {loss:.4f}, 准确率: {accuracy:.4f}")

# 可视化训练过程
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='训练损失')
plt.plot(history.history['val_loss'], label='验证损失')
plt.title('损失曲线')
plt.xlabel(' epoch')
plt.ylabel('损失')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='训练准确率')
plt.plot(history.history['val_accuracy'], label='验证准确率')
plt.title('准确率曲线')
plt.xlabel(' epoch')
plt.ylabel('准确率')
plt.legend()

plt.tight_layout()
plt.savefig('training_curve.png')
plt.show()
print("训练曲线已保存为 training_curve.png")

# 6.2 回归任务
print("\n6.2 回归任务")

# 创建回归数据集
X_reg, y_reg = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)

# 分割数据
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# 标准化数据
X_train_reg = scaler.fit_transform(X_train_reg)
X_test_reg = scaler.transform(X_test_reg)

# 创建模型
model_reg = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(32, activation='relu'),
    Dense(1)
])

# 编译模型
model_reg.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# 训练模型
history_reg = model_reg.fit(X_train_reg, y_train_reg, epochs=50, batch_size=32, validation_split=0.2, verbose=0)

# 评估模型
loss_reg, mae_reg = model_reg.evaluate(X_test_reg, y_test_reg, verbose=0)
print(f"回归模型 - 损失: {loss_reg:.4f}, MAE: {mae_reg:.4f}")

# 7. 模型评估
print("\n=== 7. 模型评估 ===")

# 7.1 分类模型评估
print("\n7.1 分类模型评估")

from sklearn.metrics import confusion_matrix, classification_report

# 预测
y_pred = model.predict(X_test)
y_pred_classes = (y_pred > 0.5).astype(int)

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred_classes)
print("混淆矩阵:")
print(cm)

# 分类报告
print("分类报告:")
print(classification_report(y_test, y_pred_classes))

# 7.2 回归模型评估
print("\n7.2 回归模型评估")

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 预测
y_pred_reg = model_reg.predict(X_test_reg)

# 评估指标
mse = mean_squared_error(y_test_reg, y_pred_reg)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

print(f"回归模型评估:")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")

# 8. 过拟合与正则化
print("\n=== 8. 过拟合与正则化 ===")

# 创建过拟合示例
X_overfit, y_overfit = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)
X_train_overfit, X_test_overfit, y_train_overfit, y_test_overfit = train_test_split(X_overfit, y_overfit, test_size=0.2, random_state=42)

# 无正则化模型
model_overfit = Sequential([
    Dense(128, activation='relu', input_shape=(20,)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model_overfit.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history_overfit = model_overfit.fit(X_train_overfit, y_train_overfit, epochs=100, batch_size=8, validation_split=0.2, verbose=0)

# 带dropout正则化的模型
model_regularized = Sequential([
    Dense(128, activation='relu', input_shape=(20,)),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(32, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model_regularized.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history_regularized = model_regularized.fit(X_train_overfit, y_train_overfit, epochs=100, batch_size=8, validation_split=0.2, verbose=0)

# 可视化过拟合与正则化
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history_overfit.history['accuracy'], label='训练准确率 (无正则化)')
plt.plot(history_overfit.history['val_accuracy'], label='验证准确率 (无正则化)')
plt.plot(history_regularized.history['accuracy'], label='训练准确率 (带正则化)')
plt.plot(history_regularized.history['val_accuracy'], label='验证准确率 (带正则化)')
plt.title('过拟合与正则化对比')
plt.xlabel(' epoch')
plt.ylabel('准确率')
plt.legend()

plt.tight_layout()
plt.savefig('overfitting_regularization.png')
plt.show()
print("过拟合与正则化对比已保存为 overfitting_regularization.png")

# 9. 实际应用示例
print("\n=== 9. 实际应用示例 ===")

# 9.1 手写数字识别
print("\n9.1 手写数字识别")

from tensorflow.keras.datasets import mnist

# 加载数据
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 数据预处理
x_train = x_train.reshape(-1, 28*28) / 255.0
x_test = x_test.reshape(-1, 28*28) / 255.0

# 独热编码
encoder = OneHotEncoder()
y_train = encoder.fit_transform(y_train.reshape(-1, 1)).toarray()
y_test = encoder.transform(y_test.reshape(-1, 1)).toarray()

# 创建模型
model_mnist = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(10, activation='softmax')
])

# 编译模型
model_mnist.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型
history_mnist = model_mnist.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2, verbose=0)

# 评估模型
loss_mnist, accuracy_mnist = model_mnist.evaluate(x_test, y_test, verbose=0)
print(f"手写数字识别模型准确率: {accuracy_mnist:.4f}")

# 10. 深度学习框架
print("\n=== 10. 深度学习框架 ===")
print("1. TensorFlow: Google开发，功能全面，生态系统丰富")
print("2. PyTorch: Facebook开发，动态计算图，易于调试")
print("3. Keras: 高级API，可运行在TensorFlow、Theano或CNTK上")
print("4. MXNet: 亚马逊支持，高效的分布式训练")
print("5. Caffe: 卷积神经网络库，适合计算机视觉任务")

# 11. 清理文件
print("\n=== 11. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['activation_functions.png', 'training_curve.png', 'overfitting_regularization.png']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n深度学习基础练习完成！")
