import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return 2*x**2 + 4*x*y + 5*y**2 - 6*x + 2*y + 10

def dx(x, y):
    return 4*x + 4*y - 6

def dy(x, y):
    return 4*x + 10*y + 2

xi = np.linspace(-5, 20, 100)
yi = np.linspace(-6, 6, 100)
X, Y = np.meshgrid(xi, yi)
Z = f(X, Y)

xj = np.linspace(-5, 20, 13)
yj = np.linspace(-6, 6, 7)
X1, Y1 = np.meshgrid(xj, yj)
Dx = dx(X1, Y1)
Dy = dy(X1, Y1)

plt.figure(figsize=(10, 5))
plt.contour(X, Y, Z, levels=np.logspace(0, 3, 10))
plt.quiver(X1, Y1, Dx, Dy, color='red', scale=500, minshaft=4)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
