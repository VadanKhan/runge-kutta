import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x * np.sqrt(y)  # Example differential equation


def runge_kutta_4th_order(f, x0, y0, x_end, h):
    n = int((x_end - x0) / h)
    x = np.linspace(x0, x_end, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * k1)
        k3 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * k2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return x, y


# Initial conditions
x0 = 0
y0 = 1
x_end = 10
h = 0.1

# Solve the ODE
x, y = runge_kutta_4th_order(f, x0, y0, x_end, h)

# Plot the results
plt.plot(x, y, label='Runge-Kutta 4th Order')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solving ODE using Runge-Kutta 4th Order Method')
plt.legend()
plt.grid(True)
plt.show()
