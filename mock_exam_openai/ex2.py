import numpy as np


# Part a)
def replace_elements(M, x, tol):
    Q = np.array(M)
    Q[np.abs(Q - x) <= tol] = x
    return Q


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 5
tol = 2
Q = replace_elements(M, x, tol)
print(Q)
# Output: [[1 2 5], [5 5 5], [5 8 9]]


# Part b)
def evaluate_function(f, a):
    v = [f(x) for x in a]
    return v


def f(x):
    return x**2

a = [1, 2, 3, 4, 5]
v = evaluate_function(f, a)
print(v)
# Output: [1, 4, 9, 16, 25]


# Part c)
def convergence(a, epsilon):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        n = 2
        x_prev = a
        x = a**(1/n)
        while abs(x - x_prev) > epsilon:
            n += 1
            x_prev = x
            x = a**(1/n)
            if n >= 10**6:
                print("The function did not converge.")
                return
        else:
            return n


a = 2
epsilon = 0.0001
print(convergence(a, epsilon))
