import numpy as np

# 生成一个包含至少15个元素、元素值在0到100之间的随机整数数组
array = np.random.randint(0, 101, size=15)

# 打印数组的第三个元素和倒数第三个元素
print("第三个元素:", array[2])  # 注意索引从0开始
print("倒数第三个元素:", array[-3])  # 负数索引从数组末尾开始计数

# 打印数组中前五个元素
print("前五个元素:", array[:5])

# 打印数组中最后五个元素
print("最后五个元素:", array[-5:])

# 打印数组中从第五个到第十个元素的切片（不包含第十一个元素）
print("从第五个到第十个元素的切片:", array[4:10])

# 判断数组中是否存在元素值大于50的元素，并打印结果
if np.any(array > 50):
    print("存在元素值大于50的元素")
else:
    print("不存在元素值大于50的元素")