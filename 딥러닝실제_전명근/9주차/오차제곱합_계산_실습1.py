import numpy as np

y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])

def sum_squares_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)

SSE = sum_squares_error(y, t)
print("오차제곱합(SSE):", SSE)

y=[0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]

SSE = sum_squares_error(y, t)
print("오차제곱합(SSE):", SSE)

def cross_entropy_error(y,t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
cross_entropy_error(np.array(y), np.array(t))
                    
