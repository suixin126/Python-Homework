import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager

# 读取文件
data = pd.read_csv('../task2_source/ETTh1.csv')
# 增加year列
data['year'] = 2016
# 年份
year = 2016
# 遍历
i = 0
while i < data.shape[0]:
    if i == 4416:
        year = 2017
    if i == 13176:
        year = 2018
    data.loc[i, 'year'] = year
    i += 1
# 2.   计算高有效负载、中间有效负载和低有效负载三列数据，按年份进行统计均值、最大值、最小值，使用多柱状图绘制展示。
data_year = data.groupby('year').agg({
    'HUFL': ['mean', 'max', 'min'],
    'MUFL': ['mean', 'max', 'min'],
    'LUFL': ['mean', 'max', 'min']
}).reset_index()
# 保存
# data_year.to_excel('../task2_source/data_year.xlsx')

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 重命名列以便绘图
data_year.columns = ['Year', 'High_Mean', 'High_Max', 'High_Min', 'Medium_Mean', 'Medium_Max', 'Medium_Min', 'Low_Mean',
                   'Low_Max', 'Low_Min']

# 3. 绘制多柱状图
# 准备索引和标签
years = data_year['Year']
labels = ['均值', '最大值', '最小值']
# 绘制高有效负载的柱状图
fig1, axs1 = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
# 绘制均值
axs1[0].bar(years, data_year['High_Mean'], label='高有效负载')
axs1[0].set_title('每年高有效负载的均值、最大值、最小值')
axs1[0].set_ylabel('均值')
axs1[0].legend()
# 绘制最大值
axs1[1].bar(years, data_year['High_Max'], label='高有效负载')
axs1[1].set_ylabel('最大值')
axs1[1].legend(loc='upper left')
# 绘制最小值
axs1[2].bar(years, data_year['High_Min'], label='高有效负载')
axs1[2].set_ylabel('最小值')
axs1[2].legend(loc='upper left')
axs1[2].set_xticks(years)
axs1[2].set_xticklabels(years, rotation=45)

# 绘制中有效负载的柱状图
fig2, axs2 = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
# 绘制均值
axs2[0].bar(years, data_year['Medium_Mean'], label='中有效负载')
axs2[0].set_title('每年中有效负载的均值、最大值、最小值')
axs2[0].set_ylabel('均值')
axs2[0].legend()
# 绘制最大值
axs2[1].bar(years, data_year['Medium_Mean'], label='中有效负载')
axs2[1].set_ylabel('最大值')
axs2[1].legend(loc='upper left')
# 绘制最小值
axs2[2].bar(years, data_year['Medium_Mean'], label='中有效负载')
axs2[2].set_ylabel('最小值')
axs2[2].legend(loc='upper left')
axs2[2].set_xticks(years)
axs2[2].set_xticklabels(years, rotation=45)

# 绘制低有效负载的柱状图
fig3, axs3 = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
# 绘制均值
axs3[0].bar(years, data_year['Low_Mean'], label='低有效负载')
axs3[0].set_title('每年低有效负载的均值、最大值、最小值')
axs3[0].set_ylabel('均值')
axs3[0].legend()
# 绘制最大值
axs3[1].bar(years, data_year['Low_Mean'], label='低有效负载')
axs3[1].set_ylabel('最大值')
axs3[1].legend(loc='upper left')
# 绘制最小值
axs3[2].bar(years, data_year['Low_Mean'], label='低有效负载')
axs3[2].set_ylabel('最小值')
axs3[2].legend(loc='upper left')
axs3[2].set_xticks(years)
axs3[2].set_xticklabels(years, rotation=45)
# 显示图形
plt.tight_layout()
plt.show()
