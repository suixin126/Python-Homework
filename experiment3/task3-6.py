import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 6.   从高有效负载数据这列中，选择任意连续7天的数据，绘制热力图
data = pd.read_csv('../../task2_source/ETTh1.csv')
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 获取目标数据
new_data = data.head(168)
# 重塑数据以适合热力图（7天，每天24个时间点）
heatmap_data = new_data['HUFL'].values.reshape(7, 24)
# 创建一个新的DataFrame用于热力图
heatmap_df = pd.DataFrame(heatmap_data, columns=[f'时间点_{i + 1}' for i in range(24)],
                          index=[f'天_{i + 1}' for i in range(7)])
# 绘制热力图
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_df, annot=True, cmap='viridis', fmt=".1f")
plt.title('高有效负载数据热力图')
plt.xlabel('时间点（每天24个）')
plt.ylabel('天数（共7天）')
plt.show()