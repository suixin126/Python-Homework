import random
import numpy as np

# 创建一个包含20个元素的列表，元素为随机生成的0到100之间的整数
random_list = [random.randint(0, 100) for _ in range(20)]
print("随机生成的列表:", random_list)

# 使用NumPy计算平均值
mean = np.mean(random_list)
print("平均值:", mean)

# 使用NumPy计算中位数
median = np.median(random_list)
print("中位数:", median)

# 使用NumPy计算标准差
std_dev = np.std(random_list)
print("标准差:", std_dev)

# 使用NumPy找出最大值和最小值
max_val = np.max(random_list)
min_val = np.min(random_list)
print("最大值:", max_val)
print("最小值:", min_val)

# 计算列表中所有偶数的总和
even_sum = sum(num for num in random_list if num % 2 == 0)
print("所有偶数的总和:", even_sum)