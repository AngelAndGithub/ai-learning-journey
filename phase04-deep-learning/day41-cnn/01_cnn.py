#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 41: 卷积神经网络

本文件包含卷积神经网络的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.datasets import mnist, cifar10
from sklearn.model_selection import train_test_split

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 卷积神经网络基础
print("=== 1. 卷积神经网络基础 ===")

print("卷积神经网络（CNN）是一种专门用于处理网格数据的深度学习模型，特别适合图像处理任务。")
print("主要组成部分：")
print("1. 卷积层（Convolutional Layer）: 提取局部特征")
print("2. 池化层（Pooling Layer）: 降维并保留重要特征")
print("3. 全连接层（Fully Connected Layer）: 分类或回归")
print("4. 激活函数: 引入非线性")

# 2. 卷积操作
print("\n=== 2. 卷积操作 ===")

# 简单的卷积操作示例
def convolution_example():
    # 创建一个3x3的输入
    input_data = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    # 创建一个2x2的卷积核
    kernel = np.array([
        [1, 0],
        [0, -1]
    ])
    
    # 执行卷积操作
    output = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            output[i, j] = np.sum(input_data[i:i+2, j:j+2] * kernel)
    
    print("输入:")
    print(input_data)
    print("\n卷积核:")
    print(kernel)
    print("\n输出:")
    print(output)

convolution_example()

# 3. 池化操作
print("\n=== 3. 池化操作 ===")

# 最大池化示例
def max_pooling_example():
    # 创建一个4x4的输入
    input_data = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    
    # 执行2x2最大池化
    output = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            output[i, j] = np.max(input_data[i*2:i*2+2, j*2:j*2+2])
    
    print("输入:")
    print(input_data)
    print("\n最大池化输出:")
    print(output)

max_pooling_example()

# 4. 构建CNN模型
print("\n=== 4. 构建CNN模型 ===")

# 4.1 加载MNIST数据集
print("\n4.1 加载MNIST数据集")

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 数据预处理
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0

# 独热编码
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

print(f"训练集形状: {x_train.shape}")
print(f"测试集形状: {x_test.shape}")

# 4.2 构建简单的CNN模型
print("\n4.2 构建简单的CNN模型")

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

print("CNN模型结构:")
model.summary()

# 5. 模型训练
print("\n=== 5. 模型训练 ===")

# 编译模型
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型
history = model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.2, verbose=1)

# 评估模型
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"MNIST测试准确率: {accuracy:.4f}")

# 6. 数据增强
print("\n=== 6. 数据增强 ===")

# 创建数据增强生成器
datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=False,
    fill_mode='nearest'
)

# 可视化数据增强效果
plt.figure(figsize=(10, 10))
for i, (x_batch, y_batch) in enumerate(datagen.flow(x_train[:1], batch_size=1)):
    plt.subplot(3, 3, i+1)
    plt.imshow(x_batch[0].reshape(28, 28), cmap='gray')
    plt.axis('off')
    if i >= 8:
        break
plt.suptitle('数据增强效果')
plt.savefig('data_augmentation.png')
plt.show()
print("数据增强效果已保存为 data_augmentation.png")

# 7. 高级CNN架构
print("\n=== 7. 高级CNN架构 ===")

# 7.1 LeNet-5
print("\n7.1 LeNet-5")

lenet_model = Sequential([
    Conv2D(6, (5, 5), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(16, (5, 5), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(120, activation='relu'),
    Dense(84, activation='relu'),
    Dense(10, activation='softmax')
])

print("LeNet-5模型结构:")
lenet_model.summary()

# 7.2 构建更复杂的CNN模型
print("\n7.2 构建更复杂的CNN模型")

complex_model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    BatchNormalization(),
    Conv2D(32, (3, 3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    
    Conv2D(64, (3, 3), activation='relu'),
    BatchNormalization(),
    Conv2D(64, (3, 3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    
    Flatten(),
    Dense(512, activation='relu'),
    BatchNormalization(),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

print("复杂CNN模型结构:")
complex_model.summary()

# 8. CIFAR-10数据集上的应用
print("\n=== 8. CIFAR-10数据集上的应用 ===")

# 加载CIFAR-10数据集
(x_train_cifar, y_train_cifar), (x_test_cifar, y_test_cifar) = cifar10.load_data()

# 数据预处理
x_train_cifar = x_train_cifar / 255.0
x_test_cifar = x_test_cifar / 255.0

# 独热编码
y_train_cifar = tf.keras.utils.to_categorical(y_train_cifar, 10)
y_test_cifar = tf.keras.utils.to_categorical(y_test_cifar, 10)

print(f"CIFAR-10训练集形状: {x_train_cifar.shape}")
print(f"CIFAR-10测试集形状: {x_test_cifar.shape}")

# 构建CIFAR-10模型
cifar_model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# 编译模型
cifar_model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型
history_cifar = cifar_model.fit(x_train_cifar, y_train_cifar, epochs=10, batch_size=64, validation_split=0.2, verbose=1)

# 评估模型
loss_cifar, accuracy_cifar = cifar_model.evaluate(x_test_cifar, y_test_cifar, verbose=0)
print(f"CIFAR-10测试准确率: {accuracy_cifar:.4f}")

# 9. 模型评估与可视化
print("\n=== 9. 模型评估与可视化 ===")

# 9.1 训练曲线
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='训练准确率')
plt.plot(history.history['val_accuracy'], label='验证准确率')
plt.title('MNIST模型准确率')
plt.xlabel('epoch')
plt.ylabel('准确率')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history_cifar.history['accuracy'], label='训练准确率')
plt.plot(history_cifar.history['val_accuracy'], label='验证准确率')
plt.title('CIFAR-10模型准确率')
plt.xlabel('epoch')
plt.ylabel('准确率')
plt.legend()

plt.tight_layout()
plt.savefig('training_curves.png')
plt.show()
print("训练曲线已保存为 training_curves.png")

# 9.2 预测结果可视化
print("\n9.2 预测结果可视化")

# 在MNIST测试集上进行预测
predictions = model.predict(x_test)
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)

# 可视化预测结果
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"预测: {predicted_classes[i]}, 真实: {true_classes[i]}")
    plt.axis('off')
plt.suptitle('MNIST预测结果')
plt.savefig('mnist_predictions.png')
plt.show()
print("MNIST预测结果已保存为 mnist_predictions.png")

# 10. 特征图可视化
print("\n=== 10. 特征图可视化 ===")

# 获取中间层的输出
from tensorflow.keras.models import Model

# 创建一个新模型，输出前几个卷积层的特征图
layer_outputs = [layer.output for layer in model.layers[:6]]  # 前6层
feature_extractor = Model(inputs=model.input, outputs=layer_outputs)

# 选择一个样本图像
img = x_test[0]
img = np.expand_dims(img, axis=0)  # 添加批次维度

# 获取特征图
feature_maps = feature_extractor.predict(img)

# 可视化特征图
plt.figure(figsize=(12, 8))
layer_names = [layer.name for layer in model.layers[:6]]

for i, (name, feature_map) in enumerate(zip(layer_names, feature_maps)):
    if len(feature_map.shape) == 4:  # 只可视化卷积层和池化层
        n_features = feature_map.shape[-1]  # 特征图数量
        size = feature_map.shape[1]  # 特征图大小
        
        # 创建一个网格来显示特征图
        n_cols = min(8, n_features)
        n_rows = (n_features + n_cols - 1) // n_cols
        
        plt.subplot(len(layer_names), n_cols, i * n_cols + 1)
        plt.suptitle('特征图可视化')
        
        for j in range(min(n_features, 8)):
            plt.subplot(len(layer_names), n_cols, i * n_cols + j + 1)
            plt.imshow(feature_map[0, :, :, j], cmap='viridis')
            plt.title(f"{name} #{j+1}")
            plt.axis('off')

plt.tight_layout()
plt.savefig('feature_maps.png')
plt.show()
print("特征图可视化已保存为 feature_maps.png")

# 11. 实际应用示例
print("\n=== 11. 实际应用示例 ===")

# 11.1 图像分类
print("\n11.1 图像分类")
print("CNN广泛应用于图像分类任务，如:")
print("- 手写数字识别")
print("- 物体识别")
print("- 人脸识别")
print("- 医学图像诊断")

# 11.2 迁移学习
print("\n11.2 迁移学习")
print("使用预训练的CNN模型进行迁移学习:")
print("- VGG16/19")
print("- ResNet")
print("- Inception")
print("- MobileNet")

# 12. 清理文件
print("\n=== 12. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['data_augmentation.png', 'training_curves.png', 'mnist_predictions.png', 'feature_maps.png']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n卷积神经网络练习完成！")
