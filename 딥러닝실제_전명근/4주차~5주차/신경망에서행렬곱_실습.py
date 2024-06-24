import numpy as np

# 주어진 숫자를 이용하여 1x2 행렬 X와 2x3 행렬 W 생성
X = np.array([[1, 2]])

W = np.array([[1, 3, 5],
              [2, 4, 6]])

# 두 행렬의 곱 계산
result = np.dot(X, W)

print("X와 W의 곱:")
print(result)
