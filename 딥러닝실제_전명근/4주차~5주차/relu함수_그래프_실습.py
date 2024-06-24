import numpy as np
import matplotlib.pyplot as plt

# ReLU 함수 정의
def relu(x):
    return np.maximum(0, x)

# x 값 생성
x = np.arange(-5.0, 5.0, 0.1)

# ReLU 함수의 값 계산
y_relu = relu(x)

# 그래프 그리기
plt.plot(x, y_relu, label='ReLU', linestyle='-')
plt.title('ReLU Function')
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.grid(True)
plt.show()
