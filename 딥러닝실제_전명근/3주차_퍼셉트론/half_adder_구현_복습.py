import numpy as np

def XOR(x1, x2):
    s1 = NAND(x1, x2)  # NAND 게이트 호출
    s2 = OR(x1, x2)    # OR 게이트 호출
    y = AND(s1, s2)    # AND 게이트 호출
    return y

# NAND 게이트 정의
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # 가중치값
    b = 0.7                    # 편향값
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# OR 게이트 정의
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# AND 게이트 정의
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def half_adder(x1, x2):
    sum_bit = XOR(x1, x2)
    carry = AND(x1, x2)
    return sum_bit, carry

print(half_adder(0, 0))  # (0, 0)
print(half_adder(0, 1))  # (1, 0)
print(half_adder(1, 0))  # (1, 0)
print(half_adder(1, 1))  # (0, 1)

    
    