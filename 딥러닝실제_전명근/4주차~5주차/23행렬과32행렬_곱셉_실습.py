import numpy as np

# 주어진 숫자를 이용하여 2x3 행렬 A와 3x2 행렬 B 생성
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# 두 행렬의 곱 계산
result = np.dot(A, B)

print("A와 B의 곱:")
print(result)
