import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 3.   对油温数据，绘制直方图。自己按照最大、最小值划分区间。
data = pd.read_csv('../task2_source/ETTh1.csv')
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 获取最大值和最小值
min_temp = data['OT'].min()
max_temp = data['OT'].max()
# 定义区间的数量和范围。将数据划分为50个等宽的区间
num_bins = 50
bin_width = (max_temp - min_temp) / num_bins
bin_edges = np.arange(min_temp, max_temp + bin_width, bin_width)
# 绘制直方图
plt.hist(data['OT'], bins=bin_edges, alpha=0.7, rwidth=0.8, color='g')
# 设置标题和轴标签
plt.title('油温数据')
plt.xlabel('温度 (°C)')
plt.ylabel('频率')
# 显示网格和图形
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()