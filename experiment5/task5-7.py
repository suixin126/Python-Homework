import numpy as np

# 创建一个3x3的矩阵，矩阵的元素为1到9的整数
matrix1 = np.arange(1, 10).reshape(3, 3)

# 创建一个同样大小的矩阵，元素为9到1的整数
matrix2 = np.arange(9, 0, -1).reshape(3, 3)

# 打印矩阵验证
print("矩阵1:")
print(matrix1)
print("矩阵2:")
print(matrix2)

# 计算这两个矩阵的和并打印结果
sum_matrix = matrix1 + matrix2
print("矩阵和:")
print(sum_matrix)

# 计算这两个矩阵的差并打印结果
diff_matrix = matrix1 - matrix2
print("矩阵差:")
print(diff_matrix)

# 计算这两个矩阵的元素级乘积（即对应位置的元素相乘）并打印结果
elementwise_product = matrix1 * matrix2
print("元素级乘积:")
print(elementwise_product)

# 计算这两个矩阵的点积（矩阵乘法）并打印结果
dot_product = np.dot(matrix1, matrix2.T)  # 第二个矩阵需要转置，因为它们是方阵
print("矩阵点积:")
print(dot_product)