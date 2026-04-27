#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 27: Matplotlib高级

本文件包含Matplotlib高级操作的练习代码
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 3D绘图
print("=== 3D绘图 ===")

# 1.1 3D散点图
print("\n1.1 3D散点图")
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 创建数据
x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)
colors = np.random.rand(100)
sizes = 100 * np.random.rand(100)

# 绘制3D散点图
ax.scatter(x, y, z, c=colors, s=sizes, alpha=0.5, cmap='viridis')
ax.set_title('3D散点图')
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')
ax.set_zlabel('Z轴')
plt.savefig('3d_scatter.png')
plt.show()
print("3D散点图已保存为 3d_scatter.png")

# 1.2 3D曲面图
print("\n1.2 3D曲面图")
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 创建数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# 绘制3D曲面图
surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
fig.colorbar(surf, ax=ax)
ax.set_title('3D曲面图')
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')
ax.set_zlabel('Z轴')
plt.savefig('3d_surface.png')
plt.show()
print("3D曲面图已保存为 3d_surface.png")

# 2. 高级自定义
print("\n=== 高级自定义 ===")

# 2.1 自定义颜色映射
print("\n2.1 自定义颜色映射")
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots(figsize=(12, 6))

# 创建自定义颜色映射
from matplotlib.colors import LinearSegmentedColormap
colors = [(0, 0, 1), (0, 1, 1), (0, 1, 0), (1, 1, 0), (1, 0, 0)]  # 蓝->青->绿->黄->红
cmap = LinearSegmentedColormap.from_list('custom_cmap', colors, N=256)

# 绘制带颜色映射的线条
line = ax.plot(x, y, color='blue', label='sin(x)')
scatter = ax.scatter(x, z, c=x, cmap=cmap, s=50)
colorbar = plt.colorbar(scatter, ax=ax)
colorbar.set_label('X值')

ax.set_title('自定义颜色映射')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)
plt.savefig('custom_cmap.png')
plt.show()
print("自定义颜色映射图已保存为 custom_cmap.png")

# 2.2 自定义坐标轴
print("\n2.2 自定义坐标轴")
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(0, 10, 100)
y = np.sin(x)

ax.plot(x, y)
ax.set_title('自定义坐标轴')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')

# 自定义坐标轴范围
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

# 自定义刻度
ax.set_xticks(np.arange(0, 11, 2))
ax.set_yticks([-1, -0.5, 0, 0.5, 1])

# 自定义刻度标签
ax.set_xticklabels(['0', '2π/5', '4π/5', '6π/5', '8π/5', '2π'])

ax.grid(True)
plt.savefig('custom_axes.png')
plt.show()
print("自定义坐标轴图已保存为 custom_axes.png")

# 2.3 子图布局
print("\n2.3 子图布局")
# 使用gridspec创建复杂布局
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(12, 10))
gs = GridSpec(3, 3, figure=fig)

# 第一个子图 - 占据第一行所有列
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(np.random.randn(100))
ax1.set_title('第一个子图')

# 第二个子图 - 占据第二行前两列
ax2 = fig.add_subplot(gs[1, :2])
ax2.hist(np.random.randn(100))
ax2.set_title('第二个子图')

# 第三个子图 - 占据第二行第三列和第三行第三列
ax3 = fig.add_subplot(gs[1:, 2])
ax3.scatter(np.random.randn(50), np.random.randn(50))
ax3.set_title('第三个子图')

# 第四个子图 - 占据第三行前两列
ax4 = fig.add_subplot(gs[2, :2])
ax4.bar(['A', 'B', 'C'], [1, 2, 3])
ax4.set_title('第四个子图')

plt.tight_layout()
plt.savefig('custom_layout.png')
plt.show()
print("自定义布局图已保存为 custom_layout.png")

# 3. 动画
print("\n=== 动画 ===")

# 3.1 基本动画
print("\n3.1 基本动画")
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], lw=2)

# 初始化函数
def init():
    line.set_data([], [])
    return line,

# 动画函数
def animate(i):
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x + i/10.0)
    line.set_data(x, y)
    return line,

# 创建动画
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# 保存动画
ani.save('sin_animation.mp4', writer='ffmpeg', fps=30)
plt.close()
print("动画已保存为 sin_animation.mp4")

# 4. 交互式绘图
print("\n=== 交互式绘图 ===")

# 4.1 鼠标事件
print("\n4.1 鼠标事件")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(np.random.randn(100))
ax.set_title('点击图表查看坐标')

# 鼠标点击事件处理函数
def onclick(event):
    print(f'点击位置: x={event.xdata}, y={event.ydata}')

# 连接鼠标事件
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.savefig('interactive_plot.png')
plt.close()
print("交互式绘图已保存为 interactive_plot.png")

# 5. 实际应用示例
print("\n=== 实际应用示例 ===")

# 5.1 时间序列分析
print("\n5.1 时间序列分析")
# 创建时间序列数据
dates = pd.date_range('2020-01-01', periods=365, freq='D')
values = np.random.randn(365).cumsum() + 100

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(dates, values)
ax.set_title('时间序列数据')
ax.set_xlabel('日期')
ax.set_ylabel('值')

# 添加滚动条
from matplotlib.widgets import Slider

# 创建滚动条
ax_slider = plt.axes([0.2, 0.02, 0.65, 0.03])
slider = Slider(ax_slider, 'Month', 1, 12, valinit=6, valstep=1)

# 滚动条更新函数
def update(val):
    month = int(slider.val)
    start_date = pd.Timestamp(f'2020-{month:02d}-01')
    end_date = start_date + pd.DateOffset(months=1)
    ax.set_xlim(start_date, end_date)
    fig.canvas.draw_idle()

# 连接滚动条事件
slider.on_changed(update)

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('time_series.png')
plt.close()
print("时间序列分析图已保存为 time_series.png")

# 5.2 多数据系列可视化
print("\n5.2 多数据系列可视化")
# 创建多数据系列
categories = ['A', 'B', 'C', 'D', 'E']
series1 = [23, 45, 56, 78, 34]
series2 = [12, 34, 45, 67, 23]
series3 = [34, 56, 67, 89, 45]

fig, ax = plt.subplots(figsize=(12, 6))

# 绘制堆叠柱状图
bottom = np.zeros(len(categories))
for i, series in enumerate([series1, series2, series3]):
    ax.bar(categories, series, bottom=bottom, label=f'系列{i+1}')
    bottom += series

ax.set_title('堆叠柱状图')
ax.set_xlabel('类别')
ax.set_ylabel('值')
ax.legend()
plt.savefig('stacked_bar.png')
plt.show()
print("堆叠柱状图已保存为 stacked_bar.png")

# 5.3 饼图进阶
print("\n5.3 饼图进阶")
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 20, 25, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
explode = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                  autopct='%1.1f%%', shadow=True, startangle=90)

# 自定义文本样式
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)

ax.set_title('高级饼图')
ax.axis('equal')
plt.savefig('advanced_pie.png')
plt.show()
print("高级饼图已保存为 advanced_pie.png")

# 5.4 雷达图
print("\n5.4 雷达图")
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    """创建雷达图投影"""
    # 计算角度
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)
    theta += np.pi/num_vars
    
    def draw_poly_frame(self, ax, rmax):
        verts = unit_poly_verts(theta, rmax)
        return plt.Polygon(verts, closed=True, edgecolor='k')
    
    def unit_poly_verts(theta, r=1):
        x0, y0, r = [0.5] * 3
        verts = [(r*np.cos(t) + x0, r*np.sin(t) + y0) for t in theta]
        return verts + [verts[0]]
    
    class RadarAxes(PolarAxes):
        name = 'radar'
        draw_frame = draw_poly_frame
        
    register_projection(RadarAxes)
    return theta

# 创建雷达图
data = {
    'categories': ['A', 'B', 'C', 'D', 'E'],
    'series1': [0.8, 0.6, 0.9, 0.7, 0.85],
    'series2': [0.7, 0.8, 0.6, 0.9, 0.75]
}

N = len(data['categories'])
theta = radar_factory(N, frame='polygon')

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='radar'))
ax.set_title('雷达图', size=16, weight='bold', position=(0.5, 1.1))

# 绘制数据
ax.plot(theta, data['series1'], color='blue', label='系列1')
ax.fill(theta, data['series1'], facecolor='blue', alpha=0.25)
ax.plot(theta, data['series2'], color='red', label='系列2')
ax.fill(theta, data['series2'], facecolor='red', alpha=0.25)

# 设置标签
ax.set_xticks(theta)
ax.set_xticklabels(data['categories'])
ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'])
ax.set_ylim(0, 1)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.savefig('radar_chart.png')
plt.show()
print("雷达图已保存为 radar_chart.png")

print("\nMatplotlib高级练习完成！")
