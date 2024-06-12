import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# （1）使用Seaborn库载入内置的titanic数据集
titanic = pd.read_csv('../../task4_source/titanic.csv')

# （4）设置图表的尺寸为宽10英寸、高6英寸。
plt.figure(figsize=(10, 6))  # 设置图形窗口的宽度为10英寸，高度为6英寸

# （2）使用countplot函数绘制一个图表，显示class列的每个类别的乘客数量
# 使用seaborn的countplot函数绘制class列的类别数量
sns.countplot(x='Pclass', data=titanic)

# （3）设置图表的基本属性，包括标题为"Titanic Passenger Classes"，x轴标签为"Passenger Class"，y轴标签为"Number of Passengers"。修改图表的颜色主题为深色模式。
# 设置seaborn的样式为darkgrid
sns.set_style("darkgrid")
# 设置图表的基本属性
plt.title("Titanic Passenger Classes")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")

# 显示图表
plt.show()

