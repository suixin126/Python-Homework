import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager

# 1、导入数据，计算每周油温的均值，绘制折线图和散点图。
# 读取文件
data = pd.read_csv('../task2_source/ETTh1.csv')
# 增加week列
data['week'] = 0
# 总周数
week = 1
# 遍历
i = 0
while i < data.shape[0]:
    if i % 168 == 0:
        week += 1
    if i == 4416:
        year = 2017
    if i == 13176:
        year = 2018
    data.loc[i, 'week'] = week - 1
    i += 1

# 周均值
data_week = data.groupby('week')['OT'].mean().reset_index()
# 保存
# data_week.to_excel('../task2_source/data_week.xlsx')

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# # 绘制折线图
plt.plot(data_week['week'], data_week['OT'], color='blue', marker='o', linestyle='-', markersize=6, label='周平均油温')
# 绘制散点图（其实和上面的折线图用的是同一组数据，但这里为了演示还是加上）
plt.scatter(data_week['week'], data_week['OT'], color='red', marker='x', s=60, label='每周油温读数')
# 添加标题、横纵坐标和图例信息
plt.title('周油温变化图')
plt.xlabel('周数')
plt.ylabel('油温 (°C)')
plt.legend()
# 展示
plt.show()