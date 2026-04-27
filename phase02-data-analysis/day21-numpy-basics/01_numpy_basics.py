#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 21: NumPy基础

本文件包含NumPy基础操作的练习代码
"""

import numpy as np

# 1. NumPy数组创建
print("=== NumPy数组创建 ===")

# 1.1 从Python列表创建
print("\n1.1 从Python列表创建")
a = np.array([1, 2, 3, 4, 5])
print(f"一维数组: {a}")
print(f"数组形状: {a.shape}")
print(f"数组类型: {a.dtype}")

# 二维数组
b = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n二维数组:\n{b}")
print(f"数组形状: {b.shape}")

# 1.2 使用内置函数创建
print("\n1.2 使用内置函数创建")

# 全0数组
zeros = np.zeros((2, 3))
print(f"全0数组:\n{zeros}")

# 全1数组
ones = np.ones((3, 2))
print(f"\n全1数组:\n{ones}")

# 单位矩阵
identity = np.eye(3)
print(f"\n单位矩阵:\n{identity}")

# 等差数列
arange = np.arange(0, 10, 2)
print(f"\n等差数列: {arange}")

# 等间隔数组
linspace = np.linspace(0, 1, 5)
print(f"\n等间隔数组: {linspace}")

# 1.3 随机数组
print("\n1.3 随机数组")

# 均匀分布随机数
random_uniform = np.random.rand(2, 3)
print(f"均匀分布随机数:\n{random_uniform}")

# 正态分布随机数
random_normal = np.random.randn(2, 3)
print(f"\n正态分布随机数:\n{random_normal}")

# 整数随机数
random_int = np.random.randint(0, 10, size=(2, 3))
print(f"\n整数随机数:\n{random_int}")

# 2. NumPy数组属性
print("\n=== NumPy数组属性 ===")
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"数组:\n{c}")
print(f"形状: {c.shape}")
print(f"维度: {c.ndim}")
print(f"元素数量: {c.size}")
print(f"数据类型: {c.dtype}")
print(f"每个元素字节大小: {c.itemsize}")
print(f"数组总字节大小: {c.nbytes}")

# 3. NumPy数组索引和切片
print("\n=== NumPy数组索引和切片 ===")
d = np.array([1, 2, 3, 4, 5])
print(f"原数组: {d}")
print(f"索引0: {d[0]}")
print(f"索引-1: {d[-1]}")
print(f"切片1:3: {d[1:3]}")
print(f"切片:3: {d[:3]}")
print(f"切片2:: {d[2:]}")

# 二维数组索引和切片
e = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n原数组:\n{e}")
print(f"索引(0,0): {e[0, 0]}")
print(f"索引(1,2): {e[1, 2]}")
print(f"切片行0:2, 列1:3:\n{e[0:2, 1:3]}")
print(f"切片所有行, 列0:2:\n{e[:, 0:2]}")

# 4. NumPy数组运算
print("\n=== NumPy数组运算 ===")
f = np.array([1, 2, 3])
g = np.array([4, 5, 6])

print(f"数组f: {f}")
print(f"数组g: {g}")
print(f"加法: {f + g}")
print(f"减法: {f - g}")
print(f"乘法: {f * g}")
print(f"除法: {f / g}")
print(f"幂运算: {f ** g}")

# 与标量运算
print(f"\n与标量运算:")
print(f"f + 2: {f + 2}")
print(f"f * 2: {f * 2}")

# 5. NumPy数学函数
print("\n=== NumPy数学函数 ===")
h = np.array([0, np.pi/2, np.pi])
print(f"原数组: {h}")
print(f"sin: {np.sin(h)}")
print(f"cos: {np.cos(h)}")
print(f"tan: {np.tan(h)}")

# 其他数学函数
print(f"\n其他数学函数:")
i = np.array([1, 4, 9])
print(f"原数组: {i}")
print(f"平方根: {np.sqrt(i)}")
print(f"指数: {np.exp(i)}")
print(f"对数: {np.log(i)}")

# 6. NumPy聚合函数
print("\n=== NumPy聚合函数 ===")
j = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"原数组:\n{j}")
print(f"求和: {np.sum(j)}")
print(f"按行求和: {np.sum(j, axis=0)}")
print(f"按列求和: {np.sum(j, axis=1)}")
print(f"平均值: {np.mean(j)}")
print(f"最大值: {np.max(j)}")
print(f"最小值: {np.min(j)}")
print(f"标准差: {np.std(j)}")
print(f"方差: {np.var(j)}")
print(f"中位数: {np.median(j)}")

# 7. NumPy数组变形
print("\n=== NumPy数组变形 ===")
k = np.array([1, 2, 3, 4, 5, 6])
print(f"原数组: {k}")
print(f"形状: {k.shape}")

# reshape
reshaped = k.reshape(2, 3)
print(f"\nreshape(2, 3):\n{reshaped}")

# flatten
flattened = reshaped.flatten()
print(f"\nflatten: {flattened}")

# ravel
raveled = reshaped.ravel()
print(f"\nravel: {raveled}")

# 8. NumPy数组连接
print("\n=== NumPy数组连接 ===")
l = np.array([[1, 2], [3, 4]])
m = np.array([[5, 6], [7, 8]])
print(f"数组l:\n{l}")
print(f"数组m:\n{m}")

# 水平连接
hstack = np.hstack((l, m))
print(f"\nhstack:\n{hstack}")

# 垂直连接
vstack = np.vstack((l, m))
print(f"\nvstack:\n{vstack}")

# 深度连接
dstack = np.dstack((l, m))
print(f"\ndstack:\n{dstack}")

# 9. NumPy数组分割
print("\n=== NumPy数组分割 ===")
n = np.array([1, 2, 3, 4, 5, 6])
print(f"原数组: {n}")

# 水平分割
hsplit = np.hsplit(n, 3)
print(f"\nhsplit: {hsplit}")

# 垂直分割
o = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(f"\n原数组:\n{o}")
vsplit = np.vsplit(o, 2)
print(f"vsplit:\n{vsplit}")

# 10. NumPy广播
print("\n=== NumPy广播 ===")
p = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
q = np.array([10, 20, 30])
print(f"数组p:\n{p}")
print(f"数组q: {q}")
print(f"广播运算 p + q:\n{p + q}")

# 11. 实际应用示例
print("\n=== 实际应用示例 ===")

# 计算欧几里得距离
def euclidean_distance(x, y):
    """计算欧几里得距离"""
    return np.sqrt(np.sum((x - y) ** 2))

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
distance = euclidean_distance(x, y)
print(f"欧几里得距离: {distance}")

# 计算矩阵乘法
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
product = np.dot(matrix1, matrix2)
print(f"\n矩阵乘法:\n{product}")

# 计算统计数据
np.random.seed(42)
data = np.random.randn(1000)
print(f"\n统计数据:")
print(f"均值: {np.mean(data)}")
print(f"标准差: {np.std(data)}")
print(f"最小值: {np.min(data)}")
print(f"最大值: {np.max(data)}")
print(f"25%分位数: {np.percentile(data, 25)}")
print(f"50%分位数: {np.percentile(data, 50)}")
print(f"75%分位数: {np.percentile(data, 75)}")

print("\nNumPy基础练习完成！")
