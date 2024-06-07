import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 4.   对油温数据进行统计，绘制饼图。分为10个，将最大、最小区域分裂，并添加阴影效果。再加一列数据，绘制双环型图。
data = pd.read_csv('../task2_source/ETTh1.csv')
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 获取最大值和最小值
min_temp = data['OT'].min()
max_temp = data['OT'].max()
# 定义区间的数量和范围。将数据划分为10个等宽的区间
num_bins = 10
bin_width = (max_temp - min_temp) / num_bins
bin_edges = np.arange(min_temp, max_temp + bin_width, bin_width)
bin_counts, _ = np.histogram(data['OT'], bins=bin_edges)
# 这里我们简单地将最小和最大的两个区域合并到中间的两个区域
bin_counts[0] += bin_counts[1]  # 合并最小两个区域
bin_counts[-1] += bin_counts[-2]  # 合并最大两个区域
bin_counts = bin_counts[1:-1]  # 去掉合并后的区域
bin_edges = bin_edges[1:-1]  # 对应的边界也要更新
# 添加另一组数据用于双环型图
inner_data = np.random.rand(len(bin_counts)) * bin_counts  # 假设内圈数据是外圈数据的某个比例
# 绘制饼图
fig, ax = plt.subplots()
# 外圈饼图
ax.pie(bin_counts, radius=1,
       labels=[f'{int(edge)}-{int(next_edge)}' for edge, next_edge in zip(bin_edges[:-1], bin_edges[1:])],
       colors=plt.cm.Blues(np.linspace(0, 1, len(bin_counts))), autopct='%1.1f%%', shadow=True)
# 内圈饼图
ax.pie(inner_data, radius=0.7, labels=None, colors=plt.cm.Greens(np.linspace(0.5, 1, len(inner_data))),
       autopct='%1.1f%%', shadow=True)
# 设置标题
ax.set_title('油温数据统计')
# 确保饼图在画布中居中
ax.axis('equal')
plt.show()
