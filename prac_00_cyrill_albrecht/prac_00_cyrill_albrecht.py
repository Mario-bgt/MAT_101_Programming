import numpy as np
import matplotlib.pyplot as plt

def partial_sum(n):
    return sum([((-1)**k)/(2**k) for k in range(n+1)])

n_values = [2, 4, 8, 16, 32]
partial_sums = [partial_sum(n) for n in n_values]

plt.scatter(n_values, partial_sums)
plt.hlines(y=2/3, xmin=0, xmax=32, color='red')
plt.title('Convergence of Series')
plt.xlabel('n values')
plt.ylabel('Partial Sums')
plt.grid()
plt.savefig('plot_series.png')
plt.show()


def convergence_for(n):
    A = 2/3
    An = partial_sum(n)
    return abs(An - A)

def convergence_while(tolerance):
    n = 0
    A = 2/3
    error = 1
    while error > tolerance:
        An = partial_sum(n)
        error = abs(An - A)
        n += 1
    return n

def my_matrix(n, m):
    A = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                B = i + j
            else:
                B = i - j
            A[i][j] = (-1)**(i + j) * B
    return A

def symmetric_matrix(C):
    if len(C) == 0 or len(C) != len(C[0]):
        return False
    for i in range(len(C)):
        for j in range(i + 1, len(C[0])):
            if C[i][j] != C[j][i]:
                return False
    return True


def read_data(filename):
    x, y = [], []
    with open(filename, 'r') as f:
        header = f.readline() # skip header line
        for line in f:
            data = line.strip().split(',')
            x.append(float(data[1]))
            y.append(float(data[2]))
    return np.array(x), np.array(y)

def compute_derivative(x, y):
    dy = np.zeros(len(y))
    dy[0] = (y[1] - y[0]) / (x[1] - x[0])
    dy[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    for i in range(1, len(y) - 1):
        dy[i] = (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])
    return dy

def save_data(filename, x, y, dy):
    with open(filename, 'w') as f:
        f.write("Index, Abscissae, Approximated Derivative\n")
        for i, (xi, yi, d) in enumerate(zip(x, y, dy)):
            f.write("{},{},{}\n".format(i, xi, d))

def plot_data(x, y, dy):
    plt.plot(x, y, label='Function')
    plt.plot(x, dy, label='Approximated Derivative')
    plt.xlabel('Abscissae')
    plt.ylabel('Values')
    plt.title('Function and Approximated Derivative')
    plt.legend()
    plt.savefig('final plot.png')

if __name__ == '__main__':
    x, y = read_data('my_function.dat')
    dy = compute_derivative(x, y)
    save_data('my derivative.dat', x, y, dy)
    plot_data(x, y, dy)

def my_dictionary(l1, l2):
    if len(l1) != len(l2):
        print("Error: lists have different lengths.")
        return

    return dict(zip(l1, l2))
