import numpy as np
import matplotlib.pyplot as plt

def function_1(x):
    return 0.01*x**2 + 0.1*x

# x 값을 0.8부터 20.6까지 0.1 간격으로 20개 지정
x = np.arange(0.0, 20.0, 0.1)

# y 값을 함수 f(x)로 계산
y = function_1(x)

# x축 이름을 "x"로 설정
plt.xlabel("x")

# y축 이름을 "f(x)"로 설정
plt.ylabel("f(x)")

# 선 그래프를 그리기
plt.plot(x, y)

# 그래프를 표시
plt.show()

def numerical_diff(f, x):
    h = 1e-4 # 아주 작은 값
    return (f(x + h) - f(x - h)) / (2 * h)

diff_at_5 = numerical_diff(function_1, 5)
print("x=5 일 때 미분 값:", diff_at_5)

diff_at_10 = numerical_diff(function_1, 10)
print("x=10 일 때 미분 값:", diff_at_10)

