def numerical_diff(f, x):
    h = 1e-4 # 아주 작은 값
    return (f(x + h) - f(x - h)) / (2 * h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

diff_at_5 = numerical_diff(function_1, 5)
print("x=5 일 때 미분 값:", diff_at_5)

diff_at_10 = numerical_diff(function_1, 10)
print("x=10 일 때 미분 값:", diff_at_10)
