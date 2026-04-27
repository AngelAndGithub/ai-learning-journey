#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 43: 生成对抗网络

本文件包含生成对抗网络的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, LeakyReLU, BatchNormalization, Reshape, Flatten, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.datasets import mnist
import time

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 生成对抗网络基础
print("=== 1. 生成对抗网络基础 ===")

print("生成对抗网络（GAN）是一种深度学习模型，由生成器和判别器组成。")
print("工作原理：")
print("1. 生成器（Generator）：生成假数据")
print("2. 判别器（Discriminator）：区分真实数据和假数据")
print("3. 两者通过对抗训练不断提高性能")
print("4. 最终生成器能够生成逼真的假数据")

# 2. 数据准备
print("\n=== 2. 数据准备 ===")

# 加载MNIST数据集
(x_train, _), (_, _) = mnist.load_data()

# 数据预处理
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_train = x_train.astype('float32')

# 标准化到[-1, 1]范围
x_train = (x_train - 0.5) * 2

print(f"MNIST数据集形状: {x_train.shape}")
print(f"数据范围: [{x_train.min():.2f}, {x_train.max():.2f}]")

# 3. 构建生成器
print("\n=== 3. 构建生成器 ===")

def build_generator(latent_dim):
    model = Sequential()
    
    # 输入层
    model.add(Dense(256, input_dim=latent_dim))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    
    model.add(Dense(512))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    
    model.add(Dense(1024))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    
    # 输出层
    model.add(Dense(28*28*1, activation='tanh'))
    model.add(Reshape((28, 28, 1)))
    
    return model

latent_dim = 100
generator = build_generator(latent_dim)
print("生成器模型结构:")
generator.summary()

# 4. 构建判别器
print("\n=== 4. 构建判别器 ===")

def build_discriminator(img_shape):
    model = Sequential()
    
    # 输入层
    model.add(Flatten(input_shape=img_shape))
    model.add(Dense(512))
    model.add(LeakyReLU(alpha=0.2))
    
    model.add(Dense(256))
    model.add(LeakyReLU(alpha=0.2))
    
    # 输出层
    model.add(Dense(1, activation='sigmoid'))
    
    return model

img_shape = (28, 28, 1)
discriminator = build_discriminator(img_shape)
discriminator.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5), metrics=['accuracy'])
print("判别器模型结构:")
discriminator.summary()

# 5. 构建GAN
print("\n=== 5. 构建GAN ===")

# 冻结判别器
 discriminator.trainable = False

# 输入噪声
z = Input(shape=(latent_dim,))

# 生成图像
img = generator(z)

# 判别生成的图像
valid = discriminator(img)

# 构建GAN
combined = Model(z, valid)
combined.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5))
print("GAN模型结构:")
combined.summary()

# 6. 训练GAN
print("\n=== 6. 训练GAN ===")

epochs = 100
batch_size = 64
sample_interval = 10  # 每10个epoch保存一次生成的图像

# 真实标签和假标签
valid = np.ones((batch_size, 1))
fake = np.zeros((batch_size, 1))

# 用于保存生成的图像
def sample_images(epoch):
    r, c = 5, 5
    noise = np.random.normal(0, 1, (r * c, latent_dim))
    gen_imgs = generator.predict(noise)
    
    # 反标准化
    gen_imgs = 0.5 * gen_imgs + 0.5
    
    fig, axs = plt.subplots(r, c)
    cnt = 0
    for i in range(r):
        for j in range(c):
            axs[i,j].imshow(gen_imgs[cnt, :,:,0], cmap='gray')
            axs[i,j].axis('off')
            cnt += 1
    fig.suptitle(f'Epoch {epoch}')
    plt.savefig(f'gan_generated_{epoch}.png')
    plt.close()

# 训练开始
train_start = time.time()

for epoch in range(epochs):
    # --------------------- #
    #  训练判别器
    # --------------------- #
    
    # 选择随机批次的真实图像
    idx = np.random.randint(0, x_train.shape[0], batch_size)
    imgs = x_train[idx]
    
    # 生成随机噪声
    noise = np.random.normal(0, 1, (batch_size, latent_dim))
    
    # 生成假图像
    gen_imgs = generator.predict(noise)
    
    # 训练判别器
    d_loss_real = discriminator.train_on_batch(imgs, valid)
    d_loss_fake = discriminator.train_on_batch(gen_imgs, fake)
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
    
    # --------------------- #
    #  训练生成器
    # --------------------- #
    
    noise = np.random.normal(0, 1, (batch_size, latent_dim))
    
    # 训练生成器
    g_loss = combined.train_on_batch(noise, valid)
    
    # 打印进度
    if epoch % 10 == 0:
        print(f"Epoch {epoch}/{epochs} [D loss: {d_loss[0]:.4f}, acc: {d_loss[1]:.4f}] [G loss: {g_loss:.4f}]")
    
    # 保存生成的图像
    if epoch % sample_interval == 0:
        sample_images(epoch)

train_end = time.time()
print(f"训练完成，耗时: {train_end - train_start:.2f}秒")

# 7. 生成图像
print("\n=== 7. 生成图像 ===")

# 生成10x10的图像网格
r, c = 10, 10
noise = np.random.normal(0, 1, (r * c, latent_dim))
gen_imgs = generator.predict(noise)

# 反标准化
gen_imgs = 0.5 * gen_imgs + 0.5

fig, axs = plt.subplots(r, c, figsize=(10, 10))
cnt = 0
for i in range(r):
    for j in range(c):
        axs[i,j].imshow(gen_imgs[cnt, :,:,0], cmap='gray')
        axs[i,j].axis('off')
        cnt += 1
fig.suptitle('生成的MNIST图像')
plt.savefig('gan_generated_final.png')
plt.show()
print("生成的最终图像已保存为 gan_generated_final.png")

# 8. 条件GAN
print("\n=== 8. 条件GAN ===")

# 构建条件生成器
def build_conditional_generator(latent_dim, num_classes):
    # 输入噪声
    noise = Input(shape=(latent_dim,))
    # 输入标签
    label = Input(shape=(1,), dtype='int32')
    
    # 将标签嵌入为密集向量
    label_embedding = Flatten()(Embedding(num_classes, latent_dim)(label))
    
    # 组合噪声和标签
    model_input = tf.keras.layers.multiply([noise, label_embedding])
    
    # 生成器网络
    x = Dense(256)(model_input)
    x = LeakyReLU(alpha=0.2)(x)
    x = BatchNormalization(momentum=0.8)(x)
    
    x = Dense(512)(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = BatchNormalization(momentum=0.8)(x)
    
    x = Dense(1024)(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = BatchNormalization(momentum=0.8)(x)
    
    x = Dense(28*28*1, activation='tanh')(x)
    img = Reshape((28, 28, 1))(x)
    
    return Model([noise, label], img)

# 构建条件判别器
def build_conditional_discriminator(img_shape, num_classes):
    # 输入图像
    img = Input(shape=img_shape)
    # 输入标签
    label = Input(shape=(1,), dtype='int32')
    
    # 将标签嵌入为密集向量并重塑
    label_embedding = Flatten()(Embedding(num_classes, np.prod(img_shape))(label))
    flat_img = Flatten()(img)
    
    # 组合图像和标签
    model_input = tf.keras.layers.multiply([flat_img, label_embedding])
    
    # 判别器网络
    x = Dense(512)(model_input)
    x = LeakyReLU(alpha=0.2)(x)
    
    x = Dense(256)(x)
    x = LeakyReLU(alpha=0.2)(x)
    
    x = Dense(1, activation='sigmoid')(x)
    
    return Model([img, label], x)

# 导入Embedding层
from tensorflow.keras.layers import Embedding

num_classes = 10

# 构建条件GAN
c_generator = build_conditional_generator(latent_dim, num_classes)
c_discriminator = build_conditional_discriminator(img_shape, num_classes)
c_discriminator.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5), metrics=['accuracy'])

# 冻结判别器
c_discriminator.trainable = False

# 输入噪声和标签
noise = Input(shape=(latent_dim,))
label = Input(shape=(1,))

# 生成图像
img = c_generator([noise, label])

# 判别生成的图像
valid = c_discriminator([img, label])

# 构建条件GAN
c_combined = Model([noise, label], valid)
c_combined.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5))

print("条件GAN模型构建完成")

# 9. 训练条件GAN
print("\n=== 9. 训练条件GAN ===")

# 准备标签数据
y_train = np.zeros((x_train.shape[0], 1))
for i in range(x_train.shape[0]):
    # 这里简化处理，实际应该使用真实标签
    y_train[i] = i % 10

# 训练条件GAN
epochs = 50
batch_size = 64

for epoch in range(epochs):
    # --------------------- #
    #  训练判别器
    # --------------------- #
    
    # 选择随机批次的真实图像和标签
    idx = np.random.randint(0, x_train.shape[0], batch_size)
    imgs = x_train[idx]
    labels = y_train[idx]
    
    # 生成随机噪声
    noise = np.random.normal(0, 1, (batch_size, latent_dim))
    
    # 生成假图像
    gen_imgs = c_generator.predict([noise, labels])
    
    # 训练判别器
    d_loss_real = c_discriminator.train_on_batch([imgs, labels], valid)
    d_loss_fake = c_discriminator.train_on_batch([gen_imgs, labels], fake)
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
    
    # --------------------- #
    #  训练生成器
    # --------------------- #
    
    noise = np.random.normal(0, 1, (batch_size, latent_dim))
    
    # 训练生成器
    g_loss = c_combined.train_on_batch([noise, labels], valid)
    
    # 打印进度
    if epoch % 10 == 0:
        print(f"Epoch {epoch}/{epochs} [D loss: {d_loss[0]:.4f}, acc: {d_loss[1]:.4f}] [G loss: {g_loss:.4f}]")

# 10. 生成指定数字的图像
print("\n=== 10. 生成指定数字的图像 ===")

# 生成每个数字的图像
noise = np.random.normal(0, 1, (num_classes, latent_dim))
labels = np.arange(0, num_classes).reshape(-1, 1)

gen_imgs = c_generator.predict([noise, labels])

# 反标准化
gen_imgs = 0.5 * gen_imgs + 0.5

fig, axs = plt.subplots(2, 5, figsize=(10, 4))
for i in range(num_classes):
    axs[i//5, i%5].imshow(gen_imgs[i, :,:,0], cmap='gray')
    axs[i//5, i%5].set_title(f'数字: {i}')
    axs[i//5, i%5].axis('off')
plt.suptitle('条件GAN生成的指定数字')
plt.savefig('conditional_gan_generated.png')
plt.show()
print("条件GAN生成的图像已保存为 conditional_gan_generated.png")

# 11. GAN的应用
print("\n=== 11. GAN的应用 ===")
print("1. 图像生成: 生成逼真的图像、艺术作品")
print("2. 图像修复: 修复损坏的图像、填充缺失部分")
print("3. 图像转换: 风格迁移、超分辨率")
print("4. 数据增强: 为机器学习模型生成训练数据")
print("5. 文本到图像生成: 根据文本描述生成图像")
print("6. 视频生成: 生成逼真的视频序列")
print("7. 音频生成: 生成音乐、语音")

# 12. 清理文件
print("\n=== 12. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = []
for i in range(0, epochs, sample_interval):
    files_to_delete.append(f'gan_generated_{i}.png')
files_to_delete.extend(['gan_generated_final.png', 'conditional_gan_generated.png'])

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n生成对抗网络练习完成！")
