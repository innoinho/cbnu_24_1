def XOR(x1, x2):
    return x1 ^ x2

def AND(x1, x2):
    return x1 & x2

def half_add(A, B):
    S = XOR(A, B)
    C = AND(A, B)
    print("S:", S, "C:", C)

half_add(0, 0)
half_add(0, 1)
half_add(1, 0)
half_add(1, 1)

