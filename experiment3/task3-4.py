import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# 4.   对油温数据进行统计，绘制饼图。分为10个，将最大、最小区域分裂，并添加阴影效果。再加一列数据，绘制双环型图。
data = pd.read_csv('../../task3_source/ETTh1.csv')
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 统计油温数据
temperature_stats = pd.cut(data['OT'], bins=10).value_counts().sort_index()
# 添加另一组数据用于双环型图
temperature_stats2 = pd.cut(data['OT'], bins=20).value_counts().sort_index()
# 绘制饼图
plt.figure(figsize=(10, 6))
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # 添加阴影效果
temperature_stats.plot(kind='pie', autopct='%1.1f%%', explode=explode, shadow=True)
temperature_stats2.plot(kind='pie', autopct='%1.1f%%',radius=0.5,shadow=True)
plt.title('油温数据统计饼图', fontsize=16)
plt.ylabel('')  # 不显示y轴标签


plt.show()