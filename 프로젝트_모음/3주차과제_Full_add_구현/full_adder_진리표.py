import numpy as np
import matplotlib.pyplot as plt

# FULL_Adder 함수 정의
def FULL_Adder(A, B, Cin):
    sum_bit = (A ^ B) ^ Cin
    cout = (A & B) | ((A ^ B) & Cin)
    return sum_bit, cout

# full adder의 진리표를 그리는 함수
def plot_full_adder_truth_table():
    A_vals = [0, 0, 1, 1, 0, 0, 1, 1]
    B_vals = [0, 1, 0, 1, 0, 1, 0, 1]
    Cin_vals = [0, 0, 0, 0, 1, 1, 1, 1]
    S_vals = []
    Cout_vals = []

    for A, B, Cin in zip(A_vals, B_vals, Cin_vals):
        S, Cout = FULL_Adder(A, B, Cin)
        S_vals.append(S)
        Cout_vals.append(Cout)

    plt.figure(figsize=(8, 6))
    plt.subplot(2, 1, 1)
    plt.title('Sum (S) Output')
    plt.xlabel('Input Combination')
    plt.ylabel('Sum')
    plt.xticks(np.arange(len(A_vals)), [f"{A},{B},{Cin}" for A, B, Cin in zip(A_vals, B_vals, Cin_vals)])
    plt.stem(range(len(S_vals)), S_vals, use_line_collection=True)

    plt.subplot(2, 1, 2)
    plt.title('Carry-out (Cout) Output')
    plt.xlabel('Input Combination')
    plt.ylabel('Cout')
    plt.xticks(np.arange(len(A_vals)), [f"{A},{B},{Cin}" for A, B, Cin in zip(A_vals, B_vals, Cin_vals)])
    plt.stem(range(len(Cout_vals)), Cout_vals, use_line_collection=True)

    plt.tight_layout()
    plt.show()

# full adder 진리표 그리기
plot_full_adder_truth_table()

