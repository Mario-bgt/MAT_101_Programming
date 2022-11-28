import numpy as np
import matplotlib.pyplot as plt
import math


# Exercise 1a

def approx_e_limit(x, n):
    if n == 0:
        return 1
    return (1 + x / n) ** n


# Exercise 1b


def approx_e_sum(x, n):
    i = 0
    for k in range(n + 1):
        i = i + ((x ** k) / (math.factorial(k)))
    return i


# Exercise 1cd

def plot_e_approximations(x, k):
    x_values = np.arange(0, k + 1)
    y_values = []
    for i in x_values:
        y_values.append(math.exp(x))
    plt.plot(x_values, y_values, '-g', label='e')
    y_values = []
    for i in x_values:
        y_values.append(approx_e_limit(x, i))
    plt.plot(x_values, y_values, '-b', label='e_limit')
    y_values = []
    for i in x_values:
        y_values.append(approx_e_sum(x, i))
    plt.plot(x_values, y_values, '-y', label='e_sum')
    plt.title('approximation of e')
    plt.ylabel('e_approx')
    plt.xlabel('n')
    plt.grid()
    plt.legend()
    plt.savefig('Exercise1.pdf')
    plt.show()


plot_e_approximations(1, 10)


# Exercise 2a

def plot_subplots(x_min, x_max):
    x_values = np.arange(x_min, x_max)
    y_values = []
    for i in x_values:
        y_values.append(math.exp(i))
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.6, top=0.9, wspace=0.4)
    fig.suptitle("exp(x)", fontsize=15)
    axis1 = fig.add_subplot(2, 2, 1)
    axis1.plot(x_values, y_values, '-g')
    axis1.set(xlabel='x linear', ylabel='y linear')
    axis2 = fig.add_subplot(2, 2, 2)
    axis2.plot(x_values, y_values, '-r')
    axis2.set(xlabel='x log', ylabel='y linear', xscale='log')
    axis3 = fig.add_subplot(2, 2, 3)
    axis3.plot(x_values, y_values, '-b')
    axis3.set(xlabel='x linear', ylabel='y log', yscale='log')
    axis4 = fig.add_subplot(2, 2, 4)
    axis4.plot(x_values, y_values, '-c')
    axis4.set(xlabel='x log', ylabel='y log', xscale='log', yscale='log')
    plt.savefig('subplots_exp.pdf')
    plt.show()


plot_subplots(1, 100)


# Exercise 2b

def plot_subplots_part_b(x_min, x_max, grid, function):
    x_values = np.arange(x_min, x_max, 0.001)
    y_values = []
    for i in x_values:
        y_values.append(function(i))
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.6, top=0.9, wspace=0.4)
    fig.suptitle(str(function.__name__) + '(x)', fontsize=15)
    fig.suptitle("exp(x)", fontsize=15)
    axis1 = fig.add_subplot(2, 2, 1)
    axis1.plot(x_values, y_values, '-g')
    axis1.set(xlabel='x linear', ylabel='y linear')
    axis2 = fig.add_subplot(2, 2, 2)
    axis2.plot(x_values, y_values, '-r')
    axis2.set(xlabel='x log', ylabel='y linear', xscale='log')
    axis3 = fig.add_subplot(2, 2, 3)
    axis3.plot(x_values, y_values, '-b')
    axis3.set(xlabel='x linear', ylabel='y log', yscale='log')
    axis4 = fig.add_subplot(2, 2, 4)
    axis4.plot(x_values, y_values, '-c')
    axis4.set(xlabel='x log', ylabel='y log', xscale='log', yscale='log')
    if grid:
        axis1.grid()
        axis2.grid()
        axis3.grid()
        axis4.grid()
    plt.savefig('subplots_exp_part_b.pdf')
    plt.show()


plot_subplots_part_b(0.1, 10, True, np.cos)