import numpy as np

# 创建一个形状为 (a, b) 的矩阵
a, b = 3, 4
matrix = np.arange(a * b).reshape(a, b)

# 使用 reshape 方法将其转换为 (a, b, 1) 的矩阵
new_matrix = matrix.reshape(a, b, 1)

print("原始矩阵:")
print(matrix)
print("变换后的矩阵:")
print(new_matrix)
