import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 读取文件
data = pd.read_csv('../../task3_source/ETTh1.csv')
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
# data_year.to_excel('../task3_source/data_year.xlsx')

# 首先，我们需要将多级索引的列名展平
data_year.columns = [f"{var}_{stat}" if stat != "" else var for var, stat in data_year.columns]

# 现在，我们可以使用melt函数将数据重塑为长格式
data_year_long = data_year.melt(id_vars=['year'],
                                var_name='variable',
                                value_name='value')

# 接下来，我们需要将'variable'列中的字符串拆分为有效负载类型和统计量
# 例如，'HUFL_mean' 拆分为 'HUFL' 和 'mean'
data_year_long[['load_type', 'statistic']] = data_year_long['variable'].str.split('_', expand=True)

# 删除原始的'variable'列
data_year_long.drop(columns=['variable'], inplace=True)

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 使用seaborn的catplot绘制多柱状图
g = sns.catplot(data=data_year_long, x='year', y='value', hue='statistic', col='load_type',
                kind='bar', palette='muted', height=5, aspect=.7)

# 添加标题和图例
g.set_titles("{col_name} {col_var}")
g.set_xlabels("年份")
g.set_ylabels("值")

# 调整子图间距和大小
g.fig.tight_layout(w_pad=3)

# 显示图形
plt.show()