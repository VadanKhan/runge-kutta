import numpy as np
import matplotlib.pyplot as plt

# Define the differential equations


def dx_dt(x, y):
    return (y - 1) * x


def dy_dt(x, y):
    return -x * y

# Runge-Kutta 4th Order Method for a system of two differential equations


def runge_kutta_4th_order_system(dx_dt, dy_dt, x0, y0, t_end, h):
    n = int(t_end / h)
    t = np.linspace(0, t_end, n + 1)
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0] = x0
    y[0] = y0

    for i in range(n):
        k1_x = h * dx_dt(x[i], y[i])
        k1_y = h * dy_dt(x[i], y[i])

        k2_x = h * dx_dt(x[i] + 0.5 * k1_x, y[i] + 0.5 * k1_y)
        k2_y = h * dy_dt(x[i] + 0.5 * k1_x, y[i] + 0.5 * k1_y)

        k3_x = h * dx_dt(x[i] + 0.5 * k2_x, y[i] + 0.5 * k2_y)
        k3_y = h * dy_dt(x[i] + 0.5 * k2_x, y[i] + 0.5 * k2_y)

        k4_x = h * dx_dt(x[i] + k3_x, y[i] + k3_y)
        k4_y = h * dy_dt(x[i] + k3_x, y[i] + k3_y)

        x[i + 1] = x[i] + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        y[i + 1] = y[i] + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6

    return t, x, y


# Initial conditions
x0 = 0.0001  # Approximate initial condition for x(0)
y0 = 2
t_end = 20
h = 0.0001

# Solve the system of ODEs
t, x, y = runge_kutta_4th_order_system(dx_dt, dy_dt, x0, y0, t_end, h)

# Plot the results
plt.plot(t, x, label=r'Intensity term x($\tau$): ($\frac{{dx}}{{d\tau}} = (y - 1)x$)')
plt.plot(t, y, label=r'Population Inversion Term y($\tau$): ($\frac{{dy}}{{d\tau}} = -xy$)')
plt.xlabel(r'time value term $\tau$')
plt.ylabel('Value')
plt.title('Solution of Q Switch (increase) Laser Pulse')
plt.legend(fontsize=8, loc='upper right')
plt.grid(True)
plt.show()
