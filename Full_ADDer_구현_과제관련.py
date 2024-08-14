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
    S = XOR(x1, x2)            # S= sum_bit
    C = AND(x1, x2)            # C= carry
    return S, C
    
def FULL_Adder(A, B, Cin):
    S1, C1 = half_adder(A, B)
    S2, C2 = half_adder(S1, Cin)
    Cout = OR(C1, C2)
    return S2, Cout

print("FULL_Adder(0, 0, 0):", FULL_Adder(0, 0, 0))
print("FULL_Adder(0, 0, 1):", FULL_Adder(0, 0, 1))
print("FULL_Adder(0, 1, 0):", FULL_Adder(0, 1, 0))
print("FULL_Adder(0, 1, 1):", FULL_Adder(0, 1, 1))
print("FULL_Adder(1, 0, 0):", FULL_Adder(1, 0, 0))
print("FULL_Adder(1, 0, 1):", FULL_Adder(1, 0, 1))
print("FULL_Adder(1, 1, 0):", FULL_Adder(1, 1, 0))
print("FULL_Adder(1, 1, 1):", FULL_Adder(1, 1, 1), "\n") 

def full_adder_truth_table():
    print("<Full_Adder_진리표>")
    print("A  B  Cin    S  Cout")
    print("--------------------")
    for A in range(2):
        for B in range(2):
            for Cin in range(2):
                S, Cout = FULL_Adder(A, B, Cin)
                print(f"{A}  {B}   {Cin}     {S}    {Cout}")

# full_adder_truth_table 함수 호출
full_adder_truth_table()