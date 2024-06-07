import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.gridspec import GridSpec

# 7 任选3列数据，绘制2行2列的多子图（其中第2行的数据一个子图，如下图所示）。三个子图应为不同类型的图。
data = pd.read_csv('../task2_source/ETTh1.csv')
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 创建一个figure
fig = plt.figure(figsize=(10, 6))
# 定义一个2行的网格，第一行2列，第二行1列
grid = GridSpec(2, 2, figure=fig, height_ratios=[2, 1])
grid.update(wspace=0.4, hspace=0.5)  # 调整子图之间的间距

# 第一个子图：柱状图（HUFL）
ax1 = fig.add_subplot(grid[0, 0])
ax1.bar(data.index, data['HUFL'], color='lightblue', label='HUFL')
ax1.set_title('HUFL柱状图')
ax1.set_xlabel('索引')
ax1.set_ylabel('值')
ax1.legend()

# 第二个子图：折线图（MUFL）
ax2 = fig.add_subplot(grid[0, 1])
ax2.plot(data.index, data['MUFL'], marker='o', color='lightgreen', linestyle='-', label='MUFL',markersize=1)
ax2.set_title('MUFL折线图')
ax2.set_xlabel('索引')
ax2.set_ylabel('值')
ax2.legend()

# 第三个子图：散点图（LUFL)，使其宽度占据整个窗体的宽度
# 通过gridspec的slice和span参数来实现跨列
ax3 = fig.add_subplot(grid[1, :])  # 这里的":"表示该子图跨越第二行的所有列
ax3.scatter(data.index, data['LUFL'], color='lightcoral', marker='x', label='LUFL')
ax3.set_title('LUFL散点图')
ax3.set_xlabel('索引')
ax3.set_ylabel('值')
ax3.legend()

# 设置中文字体和坐标轴刻度的正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号显示为方块的问题

# 显示图形
plt.show()