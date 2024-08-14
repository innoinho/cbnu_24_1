def XOR(x1, x2):
    return x1 ^ x2 #배타적 논리합

def AND(x1, x2):
    return x1 & x2 #논리곱

def half_adder(A, B):
    S = XOR(A, B)
    C = AND(A, B)
    return S, C

def FULL_ADDer(A, B, Cin):
    S1, C1 = half_adder(A, B)
    S2, C2 = half_adder(S1, Cin)
    Cout = OR(C1, C2)
    return S2, Cout

# OR 게이트 함수
def OR(x1, x2):
    return x1 | x2 #논리합

# 테스트
print("FULL_ADDer(0, 0, 0):", FULL_ADDer(0, 0, 0))
print("FULL_ADDer(0, 0, 1):", FULL_ADDer(0, 0, 1))
print("FULL_ADDer(0, 1, 0):", FULL_ADDer(0, 1, 0))
print("FULL_ADDer(0, 1, 1):", FULL_ADDer(0, 1, 1))
print("FULL_ADDer(1, 0, 0):", FULL_ADDer(1, 0, 0))
print("FULL_ADDer(1, 0, 1):", FULL_ADDer(1, 0, 1))
print("FULL_ADDer(1, 1, 0):", FULL_ADDer(1, 1, 0))
print("FULL_ADDer(1, 1, 1):", FULL_ADDer(1, 1, 1))

