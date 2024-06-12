import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1、导入数据，计算每周油温的均值，绘制折线图和散点图。
data = pd.read_csv('../../task3_source/ETTh1.csv')
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
# data_week.to_excel('../../task3_source/data_week.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用于正常显示负号

# 绘制散点图
plt.figure(figsize=(10,6))
sns.scatterplot(x='week',y='OT',data=data_week,color='blue', palette='viridis',marker='x',s=60,label='每周油温读数')

# 绘制折线图
sns.lineplot(x='week',y='OT',data=data_week,color='red', label='周平均油温',marker='o', markersize=6, linestyle='-')

# 添加标题、横纵坐标和图例信息
plt.title('周油温变化图',fontsize=16)
plt.xlabel('周数')
plt.ylabel('油温 (°C)')
plt.legend()

# 显示图表
plt.show()
