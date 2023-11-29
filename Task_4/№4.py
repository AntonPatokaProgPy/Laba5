import numpy as np
import matplotlib.pyplot as plt

def equation(x, y):
    return ((x**2 + y**2 - 1)**3) - (x**2)*(y**3)

x = np.linspace(-2, 2, 1000)
y = np.linspace(-2, 2, 1000)

X, Y = np.meshgrid(x, y)
Z = equation(X, Y)

plt.contour(X, Y, Z, levels=[0], colors='blue')
plt.title('График уравнения ((x^2 + y^2 – 1)^3) – (x^2)*(y^3) = 0')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
