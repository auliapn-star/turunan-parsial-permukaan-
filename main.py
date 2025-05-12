import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x, y = sp.symbols('x y')
f = x**2 + y**2

df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

print("f(x, y) =", f)
print("∂f/∂x =", df_dx)
print("∂f/∂y =", df_dy)

# Visualisasi
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title("Permukaan z = x^2 + y^2")
plt.show()
