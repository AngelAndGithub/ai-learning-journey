#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 22: NumPy高级

本文件包含NumPy高级操作的练习代码
"""

import numpy as np

# 1. 向量化操作
print("=== 向量化操作 ===")

# 普通Python循环
print("\n1.1 普通Python循环")
import time

# 生成大数组
a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Python循环
start_time = time.time()
c = np.zeros_like(a)
for i in range(len(a)):
    c[i] = a[i] * b[i]
python_time = time.time() - start_time
print(f"Python循环时间: {python_time:.4f}秒")

# NumPy向量化操作
print("\n1.2 NumPy向量化操作")
start_time = time.time()
c = a * b
numpy_time = time.time() - start_time
print(f"NumPy向量化时间: {numpy_time:.4f}秒")
print(f"NumPy速度提升: {python_time / numpy_time:.2f}倍")

# 2. 索引高级操作
print("\n=== 索引高级操作 ===")

# 2.1 布尔索引
print("\n2.1 布尔索引")
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"原数组: {data}")
mask = data > 5
print(f"布尔掩码: {mask}")
print(f"布尔索引结果: {data[mask]}")

# 2.2 花式索引
print("\n2.2 花式索引")
data = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(f"原数组: {data}")
print(f"索引: {indices}")
print(f"花式索引结果: {data[indices]}")

# 二维数组花式索引
data_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n二维数组:\n{data_2d}")
row_indices = [0, 2]
col_indices = [1, 2]
print(f"行索引: {row_indices}")
print(f"列索引: {col_indices}")
print(f"花式索引结果: {data_2d[row_indices, col_indices]}")

# 3. 线性代数
print("\n=== 线性代数 ===")

# 3.1 矩阵运算
print("\n3.1 矩阵运算")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"矩阵A:\n{A}")
print(f"矩阵B:\n{B}")

# 矩阵乘法
print(f"\n矩阵乘法 (dot):\n{np.dot(A, B)}")
print(f"矩阵乘法 (@):\n{A @ B}")

# 矩阵转置
print(f"\n矩阵A转置:\n{A.T}")

# 矩阵求逆
print(f"\n矩阵A的逆:\n{np.linalg.inv(A)}")

# 矩阵行列式
print(f"\n矩阵A的行列式: {np.linalg.det(A)}")

# 特征值和特征向量
print(f"\n矩阵A的特征值和特征向量:")
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"特征值: {eigenvalues}")
print(f"特征向量:\n{eigenvectors}")

# 3.2 求解线性方程组
print("\n3.2 求解线性方程组")
# 方程组: 2x + y = 5, x + y = 3
A = np.array([[2, 1], [1, 1]])
b = np.array([5, 3])
x = np.linalg.solve(A, b)
print(f"解: x = {x[0]}, y = {x[1]}")

# 4. 随机数生成
print("\n=== 随机数生成 ===")

# 4.1 设置随机种子
print("\n4.1 设置随机种子")
np.random.seed(42)
print(f"设置种子后生成的随机数: {np.random.rand(5)}")
np.random.seed(42)
print(f"相同种子生成的随机数: {np.random.rand(5)}")

# 4.2 各种分布的随机数
print("\n4.2 各种分布的随机数")

# 均匀分布
uniform = np.random.uniform(0, 1, size=1000)
print(f"均匀分布均值: {np.mean(uniform):.4f}, 标准差: {np.std(uniform):.4f}")

# 正态分布
normal = np.random.normal(0, 1, size=1000)
print(f"正态分布均值: {np.mean(normal):.4f}, 标准差: {np.std(normal):.4f}")

# 泊松分布
poisson = np.random.poisson(lam=3, size=1000)
print(f"泊松分布均值: {np.mean(poisson):.4f}, 标准差: {np.std(poisson):.4f}")

# 二项分布
binomial = np.random.binomial(n=10, p=0.5, size=1000)
print(f"二项分布均值: {np.mean(binomial):.4f}, 标准差: {np.std(binomial):.4f}")

# 5. 广播高级应用
print("\n=== 广播高级应用 ===")

# 5.1 不同形状数组的广播
print("\n5.1 不同形状数组的广播")
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([10, 20, 30])
print(f"矩阵A:\n{A}")
print(f"数组B: {B}")
print(f"广播加法 A + B:\n{A + B}")

# 5.2 广播到更高维度
C = np.array([1, 2, 3])
D = np.array([[4], [5], [6]])
print(f"\n数组C: {C}")
print(f"数组D:\n{D}")
print(f"广播乘法 C * D:\n{C * D}")

# 6. 性能优化
print("\n=== 性能优化 ===")

# 6.1 使用视图而不是副本
print("\n6.1 使用视图而不是副本")
large_array = np.random.rand(1000000)
start_time = time.time()
# 创建副本
copy_array = large_array.copy()
copy_time = time.time() - start_time
print(f"创建副本时间: {copy_time:.4f}秒")

start_time = time.time()
# 创建视图
view_array = large_array.view()
view_time = time.time() - start_time
print(f"创建视图时间: {view_time:.4f}秒")

# 6.2 使用inplace操作
print("\n6.2 使用inplace操作")
array = np.random.rand(1000000)
start_time = time.time()
# 普通操作
array = array * 2
normal_time = time.time() - start_time

array = np.random.rand(1000000)
start_time = time.time()
# inplace操作
array *= 2
inplace_time = time.time() - start_time

print(f"普通操作时间: {normal_time:.4f}秒")
print(f"inplace操作时间: {inplace_time:.4f}秒")

# 7. 内存布局
print("\n=== 内存布局 ===")

# 7.1 C风格和F风格
print("\n7.1 C风格和F风格")
c_array = np.array([[1, 2, 3], [4, 5, 6]], order='C')
f_array = np.array([[1, 2, 3], [4, 5, 6]], order='F')
print(f"C风格数组:\n{c_array}")
print(f"F风格数组:\n{f_array}")
print(f"C风格内存布局: {c_array.flags.c_contiguous}")
print(f"F风格内存布局: {f_array.flags.f_contiguous}")

# 8. 实际应用示例
print("\n=== 实际应用示例 ===")

# 8.1 图像处理
print("\n8.1 图像处理")
# 创建一个简单的图像 (3x3像素，RGB)
image = np.zeros((3, 3, 3), dtype=np.uint8)
print(f"原始图像:\n{image}")

# 填充红色
image[:, :, 0] = 255
print(f"\n红色图像:\n{image}")

# 旋转图像
rotated = np.rot90(image)
print(f"\n旋转90度后的图像:\n{rotated}")

# 8.2 数据标准化
print("\n8.2 数据标准化")
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"原始数据:\n{data}")

# 计算均值和标准差
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
print(f"\n均值: {mean}")
print(f"标准差: {std}")

# 标准化
normalized = (data - mean) / std
print(f"\n标准化后的数据:\n{normalized}")

# 8.3 矩阵分解
print("\n8.3 矩阵分解")
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"原始矩阵:\n{A}")

# SVD分解
U, S, V = np.linalg.svd(A)
print(f"\nSVD分解:")
print(f"U矩阵:\n{U}")
print(f"S矩阵: {S}")
print(f"V矩阵:\n{V}")

# 8.4 随机抽样
print("\n8.4 随机抽样")
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# 无放回抽样
sample_without_replacement = np.random.choice(data, size=5, replace=False)
print(f"无放回抽样: {sample_without_replacement}")

# 有放回抽样
sample_with_replacement = np.random.choice(data, size=5, replace=True)
print(f"有放回抽样: {sample_with_replacement}")

print("\nNumPy高级练习完成！")
