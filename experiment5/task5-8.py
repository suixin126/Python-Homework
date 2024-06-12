import numpy as np

# 创建一个4x4的矩阵，元素为随机整数(1到100)
matrix = np.random.randint(1,101,size=(4, 4))
print("原始矩阵:")
print(matrix)

# 计算并打印矩阵的转置
transposed_matrix = matrix.T
print("矩阵的转置:")
print(transposed_matrix)

# 将矩阵沿水平方向翻转（即上下翻转）并打印结果
flipped_vertically = np.flipud(matrix)
print("上下翻转的矩阵:")
print(flipped_vertically)

# 将矩阵沿垂直方向翻转（即左右翻转）并打印结果
flipped_horizontally = np.fliplr(matrix)
print("左右翻转的矩阵:")
print(flipped_horizontally)

# 计算并打印矩阵的逆
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("矩阵的逆:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("矩阵不可逆")