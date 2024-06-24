import numpy as np

# 행렬 A와 B의 값 설정
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# 두 행렬의 곱 계산
result = np.dot(A, B)

print("A와 B의 곱:")
print(result)
