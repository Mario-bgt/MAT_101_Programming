import numpy as np
import matplotlib.pyplot as plt

#Exercise 1a

def get_indices_list(l, s):
    v = []
    if s == "positive":
        for i, val in enumerate(l):
            if val > 0:
                v.append(i)
    elif s == "negative":
        for i, val in enumerate(l):
            if val < 0:
                v.append(i)
    else:
        print("Invalid string input")
        return None
    return v

l = [1, 2, -3, -4, 5]
s = "negative"
v = get_indices_list(l, s)
print(v)

#Exercise 1b

def get_indices_matrix(M, s, t):
    v = []
    if s != "smaller" and s != "bigger":
        print("Invalid string input")
        return None
    for i in range(len(M)):
        for j in range(len(M[0])):
            if s == "bigger" and M[i][j] > t:
                v.append([i, j])
            elif s == "smaller" and M[i][j] < t:
                v.append([i, j])
    return v


M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s = "smaller"
t = 5
v = get_indices_matrix(M, s, t)
print(v)


#Exercise 1c


def modify_3d_ndarray(M):
    Q = np.zeros_like(M)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            for k in range(M.shape[2]):
                if M[i][j][k] > 0.5:
                    Q[i][j][k] = M[i][j][k]
                elif M[i][j][k] >= -0.5 and M[i][j][k] <= 0.5:
                    Q[i][j][k] = M[i][j][k]
                else:
                    Q[i][j][k] = np.power(M[i][j][k], 2)
    return Q

M = np.array([[[1, 0, -1], [2, 0, -2], [3, 0, -3]], [[4, 0, -4], [5, 0, -5], [6, 0, -6]], [[7, 0, -7], [8, 0, -8], [9, 0, -9]]])
v = modify_3d_ndarray(M)
print(v)

#Exercise 2a

def close_to_x(M, x, tol):
    Q = M.copy()
    indices = np.where(np.abs(Q - x) <= tol)
    Q[indices] = x
    return Q

M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = close_to_x(M, 5, 2)
print(v)

#Exercise 2b

def evaluate_function(f, a):
    v = np.zeros(len(a))
    for i, x in enumerate(a):
        v[i] = f(x)
    return v

def f(x):
    return x**2
a = np.array([1, 2, 3, 4, 5])

v= evaluate_function(f, a)
print(v)

#Exercise 2c

def convergence_sequence(a, epsilon):

    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        n = 2
        x_prev = a
        x = a **(1/n)
        while np.abs(x - x_prev) > epsilon:
            n += 1
            x_prev = x
            x = a **(1/n)
            if n > 10000:
                return "No convergence"
        return n

a = 2
epsilon = 0.0001
v = convergence_sequence(a, epsilon)
print(v)

#Exercise 3a


N = 5
Q = 100

x = np.linspace(0, 1, Q)

y = np.zeros((Q, N))
for j in range(N):
    y[:, j] = x**(j+1)

plt.plot(x, y)
plt.title('xj functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend([f'x{j+1}' for j in range(N)])
plt.grid()
plt.savefig('xj.png')
plt.show()
header = ','.join([f'x{j+1}' for j in range(N)])
np.savetxt('my_columns.dat', y, delimiter=',', header=header)

#Exercise 3b


y = np.loadtxt('my_columns.dat', delimiter=',', skiprows=1)

x = np.linspace(0, 1, y.shape[0])

plt.plot(x, y)
plt.title('xj functions')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend([f'x{j+1}' for j in range(y.shape[1])])
plt.show()

#Extra


def plot_xj(N, Q):
    x = np.linspace(0, 1, Q)

    y = np.zeros((Q, N))
    for j in range(N):
        y[:, j] = x**(j+1)

    plt.plot(x, y)
    plt.title('xj functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend([f'x{j+1}' for j in range(N)])
    plt.savefig('xj.png')

    header = ','.join([f'x{j+1}' for j in range(N)])
    np.savetxt('my_columns.dat', y, delimiter=',', header=header)

def read_plot_xj():
    y = np.loadtxt('my_columns.dat', delimiter=',', skiprows=1)

    x = np.linspace(0, 1, y.shape[0])

    plt.plot(x, y)
    plt.title('xj functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend([f'x{j+1}' for j in range(y.shape[1])])
    plt.show()






