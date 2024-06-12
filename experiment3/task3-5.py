import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 5.   对高无效负载、中间无效负载和低无效负载三列数据，绘制箱型图。
data = pd.read_csv('../../task3_source/ETTh1.csv')
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 获取结果数据
new_data = data[['HULL','MULL','LULL']]
# 使用Seaborn绘制箱型图
plt.figure(figsize=(10, 6))  # 设置图形大小
sns.boxplot(data=new_data)  # 绘制箱型图
sns.violinplot(data=new_data) # 绘制小提琴图
# 设置图形标题和轴标签
plt.title('无效负载箱型图')
plt.xlabel('无效负载类型')
plt.ylabel('值')
# 显示图形
plt.show()