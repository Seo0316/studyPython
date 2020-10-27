import numpy as np

mat1 = np.array([[1, 1], [2, 3]], dtype=float)
print("mat1:")
print(mat1)

print("type(mat1):", type(mat1))
print("mat1.shape:", mat1.shape)
print("mat1.dtype:", mat1.dtype)

mat2 = np.linalg.inv(mat1)
print("mat2 = np.linalg.inv(mat1)")
print(mat2)