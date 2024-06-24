import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # 가중치
    b = 0.7  # 편향
    tmp = np.sum(w * x) + b  # 가중합에 편향을 더해줌
    if tmp <= 0:
        return 0
    else:
        return 1

# 각 입력에 대한 NAND 게이트의 결과 출력
print(NAND(0, 0))  # 출력: 1
print(NAND(1, 0))  # 출력: 1
print(NAND(0, 1))  # 출력: 1
print(NAND(1, 1))  # 출력: 0

