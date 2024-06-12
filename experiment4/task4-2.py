import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 使用Seaborn库载入内置的titanic数据集
titanic = pd.read_csv('../../task4_source/titanic.csv')

# 将确实数据处理为0
titanic['Age'] = titanic['Age'].fillna(0)

# 绘制'age'列基于'class'列的小提琴图
sns.violinplot(x='Pclass', y='Age', data=titanic)

# 设置图表的基本属性（可选）
plt.title("Distribution of Passenger Age by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Age")

# 如果需要更详细的控制，可以添加箱形图的元素到小提琴图中
sns.boxplot(x='Pclass', y='Age', data=titanic, palette="dark", width=0.4)


# 将图像保存为PNG文件
plt.savefig('../../task4_source/passenger_age_by_class.png', dpi=300)  # 设置dpi以控制图像的分辨率

# 显示图表
plt.show()