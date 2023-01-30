import matplotlib.pyplot as plt
import numpy as np


def suminum(n):
    PS = 0
    for indn in range(n+1):
        PS = PS + (-1) ** indn * 1 / (2 ** indn)
    return PS


x_val = [2, 4, 8, 16, 32]
y_val = [suminum(i) for i in x_val]
y_val2 = [2 / 3 for i in x_val]
plt.plot(x_val, y_val, '.r', label='A_n')
plt.plot(x_val, y_val2, '-g', label='f(x)=2/3')
plt.title('Plot of the first few 2**k values of the sum')
plt.ylabel('A_n')
plt.xlabel('x')
plt.grid()
plt.legend()
plt.savefig('plot_series.png')
plt.show()


def convergence_for(n):
    return abs(suminum(n)-2/3)


def convergence_while(epsilon):
    n = 0
    while True:
        if convergence_for(n) <= epsilon:
            return n
        n += 1
        if n > 1e5:
            print("couldn't compute in a reasonable time")
            return None

