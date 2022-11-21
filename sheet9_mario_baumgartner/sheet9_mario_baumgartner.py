import numpy as np
import matplotlib.pyplot as plt
import math

"""Exersice 1"""


# Part a)
def approx_e_limit(x, n):
    return (1 + x / n) ** n


# Part b)
def approx_e_sum(x, n):
    exp = 0
    for j in range(n + 1):
        exp += (x ** j) / math.factorial(j)
    return exp


# Part c,d)
def plot_e_approximations(x, k):
    x_values = np.arange(0, k + 1)
    y_values = [math.exp(x) for i in x_values]
    plt.plot(x_values, y_values, '-g', label='e')
    y_values = [approx_e_limit(x, i) for i in x_values]
    plt.plot(x_values, y_values, '-b', label='e_limit')
    y_values = [approx_e_sum(x, i) for i in x_values]
    plt.plot(x_values, y_values, '-y', label='e_sum')
    plt.title('approximations of e')
    plt.ylabel('e_approx')
    plt.xlabel('n')
    plt.legend()
    plt.grid()
    plt.savefig('approximate_e.pdf')
    plt.show()


plot_e_approximations(1, 10)

"""Exersice 2"""


# Part a)
def plot_subplots(x_min, x_max):
    x_values = np.arange(x_min, x_max, 1/(x_max-x_min))
    y_values = [math.exp(i) for i in x_values]
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.6, top=0.9, wspace=0.4)
    fig.suptitle("exp(x)", fontsize=15)
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(x_values, y_values, '-r')
    ax1.set(xlabel='x linear', ylabel='y linear')
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(x_values, y_values, '-g')
    ax2.set(xlabel='x log', ylabel='y linear', xscale='log')
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(x_values, y_values, '-b')
    ax3.set(xlabel='x linear', ylabel='y log', yscale='log')
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(x_values, y_values, '-y')
    ax4.set(xlabel='x log', ylabel='y log', xscale='log', yscale='log')
    plt.savefig('subplots_exp.pdf')
    plt.show()


plot_subplots(1, 100)


# Part b)
def plot_subplots_advanced(x_min, x_max, grid, function):
    x_values = np.arange(x_min, x_max, 1/(x_max-x_min))
    y_values = [function(i) for i in x_values]
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.6, top=0.9, wspace=0.4)
    fig.suptitle(str(function.__name__)+'(x)', fontsize=15)
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(x_values, y_values, '-r')
    ax1.set(xlabel='x linear', ylabel='y linear')
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(x_values, y_values, '-g')
    ax2.set(xlabel='x log', ylabel='y linear', xscale='log')
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(x_values, y_values, '-b')
    ax3.set(xlabel='x linear', ylabel='y log', yscale='log')
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(x_values, y_values, '-y')
    ax4.set(xlabel='x log', ylabel='y log', xscale='log', yscale='log')
    if grid:
        ax1.grid()
        ax2.grid()
        ax3.grid()
        ax4.grid()
    plt.savefig('subplots_advanced.pdf')
    plt.show()


plot_subplots_advanced(0.1, 10, True, np.cos)


