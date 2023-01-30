import matplotlib.pyplot as plt
import numpy as np


def euler(func, a, b, y_a, N):
    y_val = [y_a]
    y_temp = y_a
    dt = (b - a) / N
    for i in range(N-1):
        y_temp += dt * func(y_temp)
        y_val.append(y_temp)
    return y_val, np.arange(a, b, dt)


def test_function(y):
    return y


y_20, x_20 = euler(test_function, 0, 5, 1, 20)
y_40, x_40 = euler(test_function, 0, 5, 1, 40)
y_100, x_100 = euler(test_function, 0, 5, 1, 100)
y_org = [np.e**t for t in x_100]
plt.plot(x_20, y_20, '-r', label='N=20')
plt.plot(x_40, y_40, '-g', label='N=40')
plt.plot(x_100, y_100, '-b', label='N=100')
plt.plot(x_100, y_org, '-m', label='f(x)=e^x')
plt.legend()
plt.ylabel('f(x)=e^x or some approximation')
plt.xlabel('x-values')
plt.title("y'=y approximated by euler")
plt.grid()
plt.show()
