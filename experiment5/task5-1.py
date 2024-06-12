import numpy as np

# 创建一个未初始化的数组，维度为 3×4 数据类型为 float64
uninitialized_array = np.empty((3, 4), dtype=np.float64)

# 创建一个维度为 5×5，所有元素初始化为 0 的数组
zero_array = np.zeros((5, 5))

# 创建一个维度为 2×3×2，所有元素初始化为 1 的数组
ones_array = np.ones((2, 3, 2))

# 创建一个维度为 4×4，数据类型为 int32，并将所有元素初始化为 7 的数组
seven_array = np.full((4, 4), 7, dtype=np.int32)

# 打印
print("Uninitialized array (filled with random values of type float64):")
print(uninitialized_array)
print("\nZero array:")
print(zero_array)
print("\nOnes array:")
print(ones_array)
print("\nSeven array (int32):")
print(seven_array)