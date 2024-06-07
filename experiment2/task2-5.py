import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 5.   对高无效负载、中间无效负载和低无效负载三列数据，绘制箱型图。
data = pd.read_csv('../task2_source/ETTh1.csv')
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 获取结果数据
new_data = data[['HULL','MULL','LULL']]
# 绘制箱型图
fig, ax = plt.subplots()
bp = ax.boxplot(new_data, patch_artist=True, labels=['高无效负载', '中间无效负载', '低无效负载'])
# 设置颜色
colors = ['lightblue', 'lightgreen', 'lightcoral']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
# 设置中文标题和坐标轴标签
ax.set_title('无效负载箱型图')
ax.set_xlabel('无效负载类型')
ax.set_ylabel('值')
# 添加图例
ax.set_xticklabels(['高', '中', '低'])
# 显示图形
plt.show()