import numpy as np

# 生成一个包含至少10个元素、元素值在0到100之间的随机整数数组
array = np.random.randint(0, 101, size=20)  # 注意：randint的第二个参数是不包含的，所以使用101来包含100

# 打印生成的数组
print("生成的数组:", array)

# 计算并打印平均值
average = np.mean(array)
print("平均值:", average)

# 找出并打印最大值和最小值
max_value = np.max(array)
min_value = np.min(array)
print("最大值:", max_value)
print("最小值:", min_value)

# 计算数组中所有偶数元素的和并打印结果
even_sum = np.sum(array[array % 2 == 0])
print("偶数元素之和:", even_sum)