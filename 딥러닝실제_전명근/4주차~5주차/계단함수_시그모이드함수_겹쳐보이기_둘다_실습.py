import numpy as np
import matplotlib.pyplot as plt

# 시그모이드 함수 정의
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 계단 함수 정의
def step_function(x):
    return np.array(x > 0, dtype=int)

# x 값 생성
x = np.arange(-5.0, 5.0, 0.1)

# 시그모이드 함수와 계단 함수의 값 계산
y_sigmoid = sigmoid(x)
y_step = step_function(x)

# 그래프 그리기
plt.plot(x, y_sigmoid, label='Sigmoid', linestyle='--')
plt.plot(x, y_step, label='Step', linestyle='-')
plt.title('Sigmoid vs. Step Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

