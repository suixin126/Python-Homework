import numpy as np


def generate_unique_random_array(length, min_value, max_value):
    # 确保最小值和最大值合理
    if min_value >= max_value:
        raise ValueError("最小值必须小于最大值")

        # 确保可选择的整数数量大于或等于数组长度
    if max_value - min_value + 1 < length:
        raise ValueError("指定范围内的整数数量不足以生成唯一数组")

        # 使用numpy.random.choice生成唯一随机数组
    return np.random.choice(np.arange(min_value, max_value + 1), length, replace=False)


# 获取用户输入
length = int(input("请输入数组的长度: "))
min_value = int(input("请输入随机数的最小值: "))
max_value = int(input("请输入随机数的最大值: "))

# 调用函数并打印结果
try:
    unique_random_array = generate_unique_random_array(length, min_value, max_value)
    print("生成的唯一随机数组:", unique_random_array)
except ValueError as e:
    print("错误:", e)