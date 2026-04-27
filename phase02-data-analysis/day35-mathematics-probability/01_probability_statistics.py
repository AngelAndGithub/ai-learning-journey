#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 35: 数学基础-概率统计

本文件包含概率统计基础的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 概率基础
print("=== 1. 概率基础 ===")

# 1.1 概率计算
print("\n1.1 概率计算")

# 计算事件概率
def probability(event_outcomes, sample_space):
    """计算事件概率"""
    return len(event_outcomes) / len(sample_space)

# 示例：抛硬币
sample_space = {'H', 'T'}
event = {'H'}
print(f"抛硬币正面朝上的概率: {probability(event, sample_space)}")

# 示例：掷骰子
sample_space = {1, 2, 3, 4, 5, 6}
event = {2, 4, 6}  # 偶数
print(f"掷骰子得到偶数的概率: {probability(event, sample_space)}")

# 1.2 条件概率
print("\n1.2 条件概率")

# 示例：从两个盒子中取球
# 盒子A: 3红2蓝
# 盒子B: 2红3蓝

# 计算从盒子A中取出红球的概率
p_a = 0.5  # 选择盒子A的概率
p_red_given_a = 3/5  # 从盒子A中取出红球的概率
p_red = p_a * p_red_given_a + (1 - p_a) * 2/5  # 取出红球的总概率

print(f"从盒子A中取出红球的概率: {p_red_given_a}")
print(f"取出红球的总概率: {p_red}")

# 贝叶斯定理：已知取出红球，求来自盒子A的概率
p_a_given_red = (p_red_given_a * p_a) / p_red
print(f"已知取出红球，来自盒子A的概率: {p_a_given_red:.4f}")

# 2. 随机变量
print("\n=== 2. 随机变量 ===")

# 2.1 离散型随机变量
print("\n2.1 离散型随机变量")

# 示例：二项分布
n = 10  # 试验次数
p = 0.5  # 成功概率
binomial = stats.binom(n, p)

# 计算概率质量函数 (PMF)
x = np.arange(0, n+1)
pmf = binomial.pmf(x)

print("二项分布概率质量函数:")
for i, prob in enumerate(pmf):
    print(f"P(X={i}) = {prob:.4f}")

# 可视化二项分布
plt.figure(figsize=(10, 6))
plt.bar(x, pmf)
plt.title(f'二项分布 (n={n}, p={p})')
plt.xlabel('成功次数')
plt.ylabel('概率')
plt.savefig('binomial_distribution.png')
plt.show()
print("二项分布可视化已保存为 binomial_distribution.png")

# 2.2 连续型随机变量
print("\n2.2 连续型随机变量")

# 示例：正态分布
mu = 0  # 均值
sigma = 1  # 标准差
normal = stats.norm(mu, sigma)

# 计算概率密度函数 (PDF)
x = np.linspace(-4, 4, 100)
pdf = normal.pdf(x)

# 计算累积分布函数 (CDF)
cdf = normal.cdf(x)

print("正态分布概率密度函数:")
print(f"均值: {mu}")
print(f"标准差: {sigma}")
print(f"P(X < 0) = {normal.cdf(0):.4f}")
print(f"P(-1 < X < 1) = {normal.cdf(1) - normal.cdf(-1):.4f}")

# 可视化正态分布
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, pdf)
plt.title('正态分布 PDF')
plt.xlabel('x')
plt.ylabel('概率密度')

plt.subplot(1, 2, 2)
plt.plot(x, cdf)
plt.title('正态分布 CDF')
plt.xlabel('x')
plt.ylabel('累积概率')

plt.tight_layout()
plt.savefig('normal_distribution.png')
plt.show()
print("正态分布可视化已保存为 normal_distribution.png")

# 3. 统计量
print("\n=== 3. 统计量 ===")

# 3.1 描述性统计
print("\n3.1 描述性统计")

# 创建示例数据
np.random.seed(42)
data = np.random.normal(100, 15, 1000)

# 计算基本统计量
mean = np.mean(data)
median = np.median(data)
std = np.std(data)
var = np.var(data)
min_val = np.min(data)
max_val = np.max(data)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

print(f"均值: {mean:.2f}")
print(f"中位数: {median:.2f}")
print(f"标准差: {std:.2f}")
print(f"方差: {var:.2f}")
print(f"最小值: {min_val:.2f}")
print(f"最大值: {max_val:.2f}")
print(f"第一四分位数 (Q1): {q1:.2f}")
print(f"第三四分位数 (Q3): {q3:.2f}")
print(f"四分位距 (IQR): {iqr:.2f}")

# 可视化数据分布
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(data, kde=True)
plt.axvline(mean, color='r', linestyle='--', label=f'均值: {mean:.2f}')
plt.axvline(median, color='g', linestyle='--', label=f'中位数: {median:.2f}')
plt.title('数据分布')
plt.legend()

plt.subplot(1, 2, 2)
sns.boxplot(data)
plt.title('箱线图')

plt.tight_layout()
plt.savefig('descriptive_statistics.png')
plt.show()
print("描述性统计可视化已保存为 descriptive_statistics.png")

# 3.2 相关性分析
print("\n3.2 相关性分析")

# 创建相关数据
x = np.linspace(0, 10, 100)
y1 = 2 * x + np.random.randn(100)
y2 = -x + np.random.randn(100)
y3 = np.random.randn(100)

# 计算相关系数
corr_xy1 = np.corrcoef(x, y1)[0, 1]
corr_xy2 = np.corrcoef(x, y2)[0, 1]
corr_xy3 = np.corrcoef(x, y3)[0, 1]

print(f"x 和 y1 的相关系数: {corr_xy1:.4f}")
print(f"x 和 y2 的相关系数: {corr_xy2:.4f}")
print(f"x 和 y3 的相关系数: {corr_xy3:.4f}")

# 可视化相关性
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.scatter(x, y1)
plt.title(f'正相关 (r={corr_xy1:.2f})')
plt.xlabel('x')
plt.ylabel('y1')

plt.subplot(1, 3, 2)
plt.scatter(x, y2)
plt.title(f'负相关 (r={corr_xy2:.2f})')
plt.xlabel('x')
plt.ylabel('y2')

plt.subplot(1, 3, 3)
plt.scatter(x, y3)
plt.title(f'无相关 (r={corr_xy3:.2f})')
plt.xlabel('x')
plt.ylabel('y3')

plt.tight_layout()
plt.savefig('correlation_analysis.png')
plt.show()
print("相关性分析可视化已保存为 correlation_analysis.png")

# 4. 假设检验
print("\n=== 4. 假设检验 ===")

# 4.1 t检验
print("\n4.1 t检验")

# 创建两组数据
group1 = np.random.normal(100, 15, 50)
group2 = np.random.normal(105, 15, 50)

# 独立样本t检验
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"t统计量: {t_stat:.4f}")
print(f"p值: {p_value:.4f}")

if p_value < 0.05:
    print("拒绝原假设，两组数据均值存在显著差异")
else:
    print("不拒绝原假设，两组数据均值无显著差异")

# 可视化两组数据
plt.figure(figsize=(10, 6))
sns.boxplot(data=[group1, group2], labels=['组1', '组2'])
plt.title('两组数据分布')
plt.savefig('t_test.png')
plt.show()
print("t检验可视化已保存为 t_test.png")

# 4.2 卡方检验
print("\n4.2 卡方检验")

# 创建列联表
data = [[10, 20, 30], [15, 25, 20]]
chi2, p, dof, expected = stats.chi2_contingency(data)
print(f"卡方统计量: {chi2:.4f}")
print(f"p值: {p:.4f}")
print(f"自由度: {dof}")
print(f"期望频数:\n{expected}")

if p < 0.05:
    print("拒绝原假设，两个变量存在显著关联")
else:
    print("不拒绝原假设，两个变量无显著关联")

# 5. 概率分布
print("\n=== 5. 概率分布 ===")

# 5.1 常见概率分布
print("\n5.1 常见概率分布")

# 泊松分布
lambda_ = 3
poisson = stats.poisson(lambda_)
x_poisson = np.arange(0, 10)
pmf_poisson = poisson.pmf(x_poisson)

# 指数分布
beta = 2
exponential = stats.expon(scale=beta)
x_exponential = np.linspace(0, 10, 100)
pdf_exponential = exponential.pdf(x_exponential)

# 均匀分布
uniform = stats.uniform(0, 10)
x_uniform = np.linspace(0, 10, 100)
pdf_uniform = uniform.pdf(x_uniform)

# 可视化各种分布
plt.figure(figsize=(15, 10))

plt.subplot(3, 2, 1)
plt.bar(x_poisson, pmf_poisson)
plt.title(f'泊松分布 (λ={lambda_})')
plt.xlabel('k')
plt.ylabel('P(X=k)')

plt.subplot(3, 2, 2)
plt.plot(x_exponential, pdf_exponential)
plt.title(f'指数分布 (β={beta})')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(3, 2, 3)
plt.plot(x_uniform, pdf_uniform)
plt.title('均匀分布 U(0, 10)')
plt.xlabel('x')
plt.ylabel('f(x)')

# 卡方分布
chi2_3 = stats.chi2(3)
x_chi2 = np.linspace(0, 15, 100)
pdf_chi2 = chi2_3.pdf(x_chi2)

plt.subplot(3, 2, 4)
plt.plot(x_chi2, pdf_chi2)
plt.title('卡方分布 (df=3)')
plt.xlabel('x')
plt.ylabel('f(x)')

# t分布
t_5 = stats.t(5)
x_t = np.linspace(-4, 4, 100)
pdf_t = t_5.pdf(x_t)

plt.subplot(3, 2, 5)
plt.plot(x_t, pdf_t)
plt.title('t分布 (df=5)')
plt.xlabel('x')
plt.ylabel('f(x)')

# F分布
f_2_10 = stats.f(2, 10)
x_f = np.linspace(0, 5, 100)
pdf_f = f_2_10.pdf(x_f)

plt.subplot(3, 2, 6)
plt.plot(x_f, pdf_f)
plt.title('F分布 (df1=2, df2=10)')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.tight_layout()
plt.savefig('probability_distributions.png')
plt.show()
print("概率分布可视化已保存为 probability_distributions.png")

# 6. 统计推断
print("\n=== 6. 统计推断 ===")

# 6.1 置信区间
print("\n6.1 置信区间")

# 计算均值的95%置信区间
data = np.random.normal(100, 15, 100)
mean = np.mean(data)
std = np.std(data, ddof=1)
n = len(data)
t_value = stats.t.ppf(0.975, n-1)  # 95%置信水平
margin_of_error = t_value * (std / np.sqrt(n))
confidence_interval = (mean - margin_of_error, mean + margin_of_error)

print(f"样本均值: {mean:.2f}")
print(f"样本标准差: {std:.2f}")
print(f"95%置信区间: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")

# 6.2 中心极限定理
print("\n6.2 中心极限定理")

# 从均匀分布中采样
sample_size = 30
num_samples = 1000
sample_means = []

for _ in range(num_samples):
    sample = np.random.uniform(0, 10, sample_size)
    sample_means.append(np.mean(sample))

# 计算样本均值的分布
mean_sample_means = np.mean(sample_means)
std_sample_means = np.std(sample_means)

print(f"样本均值的均值: {mean_sample_means:.2f}")
print(f"样本均值的标准差: {std_sample_means:.2f}")
print(f"理论标准差 (σ/√n): {10/np.sqrt(12)/np.sqrt(sample_size):.2f}")

# 可视化中心极限定理
plt.figure(figsize=(10, 6))
sns.histplot(sample_means, kde=True)
plt.axvline(mean_sample_means, color='r', linestyle='--', label=f'样本均值: {mean_sample_means:.2f}')
plt.title('中心极限定理演示')
plt.xlabel('样本均值')
plt.ylabel('频率')
plt.legend()
plt.savefig('central_limit_theorem.png')
plt.show()
print("中心极限定理演示已保存为 central_limit_theorem.png")

# 7. 实际应用示例
print("\n=== 7. 实际应用示例 ===")

# 7.1 A/B测试
print("\n7.1 A/B测试")

# 模拟A/B测试数据
np.random.seed(42)
# 方案A: 转化率10%
sample_size_a = 1000
conversions_a = np.sum(np.random.binomial(1, 0.1, sample_size_a))

# 方案B: 转化率12%
sample_size_b = 1000
conversions_b = np.sum(np.random.binomial(1, 0.12, sample_size_b))

print(f"方案A: {conversions_a}/{sample_size_a} = {conversions_a/sample_size_a:.4f}")
print(f"方案B: {conversions_b}/{sample_size_b} = {conversions_b/sample_size_b:.4f}")

# 使用卡方检验
table = [[conversions_a, sample_size_a - conversions_a], [conversions_b, sample_size_b - conversions_b]]
chi2, p_value = stats.chi2_contingency(table)[:2]

print(f"卡方统计量: {chi2:.4f}")
print(f"p值: {p_value:.4f}")

if p_value < 0.05:
    print("拒绝原假设，两个方案的转化率存在显著差异")
else:
    print("不拒绝原假设，两个方案的转化率无显著差异")

# 7.2 质量控制
print("\n7.2 质量控制")

# 创建生产数据
np.random.seed(42)
# 正常生产过程的产品重量
weights = np.random.normal(100, 2, 100)

# 计算控制限
mean_weight = np.mean(weights)
std_weight = np.std(weights)
upper_control_limit = mean_weight + 3 * std_weight
lower_control_limit = mean_weight - 3 * std_weight

print(f"均值: {mean_weight:.2f}")
print(f"标准差: {std_weight:.2f}")
print(f"上控制限: {upper_control_limit:.2f}")
print(f"下控制限: {lower_control_limit:.2f}")

# 可视化控制图
plt.figure(figsize=(12, 6))
plt.plot(weights, 'o-')
plt.axhline(mean_weight, color='r', linestyle='--', label=f'均值: {mean_weight:.2f}')
plt.axhline(upper_control_limit, color='g', linestyle='--', label=f'上控制限: {upper_control_limit:.2f}')
plt.axhline(lower_control_limit, color='g', linestyle='--', label=f'下控制限: {lower_control_limit:.2f}')
plt.title('质量控制图')
plt.xlabel('样本')
plt.ylabel('重量')
plt.legend()
plt.savefig('control_chart.png')
plt.show()
print("质量控制图已保存为 control_chart.png")

# 8. 清理文件
print("\n=== 8. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['binomial_distribution.png', 'normal_distribution.png', 'descriptive_statistics.png',
                   'correlation_analysis.png', 't_test.png', 'probability_distributions.png',
                   'central_limit_theorem.png', 'control_chart.png']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n概率统计练习完成！")
