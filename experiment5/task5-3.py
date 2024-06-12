import numpy as np


def create_range_array_with_numpy(start, end, step=1):
    # 确保步长是整数  
    if step == 0:
        raise ValueError("Step cannot be zero.")

        # 使用NumPy的arange函数创建数组
    return np.arange(start, end + 1, step, dtype=int)


# 获取用户输入
start = int(input("请输入开始整数: "))
end = int(input("请输入结束整数: "))
step = int(input("请输入步长（可选，默认为1）: "))

# 调用函数并打印结果  
result_array = create_range_array_with_numpy(start, end, step)
print("生成的数组:", result_array)