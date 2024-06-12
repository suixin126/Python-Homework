import numpy as np


# 创建一个 6x6 的数组，边框为 1，内部为 0
def create_border_array(size):
    arr = np.zeros((size, size), dtype=int)  # 创建一个全是 0 的数组
    arr[0, :], arr[-1, :] = 1, 1  # 设置第一行和最后一行为 1
    arr[:, 0], arr[:, -1] = 1, 1  # 设置第一列和最后一列为 1
    return arr


# 验证数组的边框是否都是 1，内部是否都是 0
def verify_border_array(arr):
    size = arr.shape[0]  # 获取数组的大小
    # 检查边框是否都是 1
    border_is_one = np.all(arr[0, :] == 1) and np.all(arr[-1, :] == 1) and \
                    np.all(arr[:, 0] == 1) and np.all(arr[:, -1] == 1)
    # 检查内部是否都是 0
    internal_is_zero = np.all(arr[1:-1, 1:-1] == 0)
    return border_is_one and internal_is_zero


# 创建 6x6 数组
border_array = create_border_array(6)

# 打印整个数组
print("数组:")
print(border_array)

# 验证数组并打印结果
verification_result = verify_border_array(border_array)
print("数组的边框是否都是 1，内部是否都是 0:", verification_result)