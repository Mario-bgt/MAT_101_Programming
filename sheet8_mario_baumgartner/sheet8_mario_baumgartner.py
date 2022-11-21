import numpy as np

"""Exersice 1"""


def fibonacciMatrix(n):
    A = np.array([[1, 1],
                  [1, 0]])
    fib_n = np.linalg.matrix_power(A, n) @ np.array([[1], [0]])
    return fib_n[1]


fib_101 = fibonacciMatrix(101)

print(f"The value for 101 is {fib_101} which is simply wrong. ")

"""Exersice 2"""


# Part a)
def monteCarloPi(n):
    values = np.random.uniform(low=-1, high=1, size=(n, 2))
    m = 0
    for j in values:
        if np.linalg.norm(j) <= 1:
            m += 1
    return (m / n) * 4


print(monteCarloPi(10000))


# Part b)
def monteCarloSphere(n, d):
    values = np.random.uniform(low=-1, high=1, size=(n, d))
    o = 0
    for j in values:
        if np.linalg.norm(j) <= 1:
            o += 1
    return np.power(2, d) * (o / n)


vol_3 = monteCarloSphere(10000, 3)
vol_4 = monteCarloSphere(10000, 4)
vol_10 = monteCarloSphere(10000, 10)
vol_100 = monteCarloSphere(10000, 100)
vol_300 = monteCarloSphere(10000, 300)
print(f"The volume of dimension 3 = {vol_3}, 4 = {vol_4}, 10 = {vol_10}, 100 = {vol_100}, 300 = {vol_300} ")
print(f"As expected the volume for dim 4 is the greatest and then decreases to 0 for dim getting bigger.")

"""Exersice 3"""


def sieveOfEratosthenes(n):
    lyst = np.arange(2, n + 1)
    p = 2
    primes = [2]
    while True:
        multiples = list(range(2 * p, n+1, p))
        lyst = [j for j in lyst if j not in multiples]
        min_lyst = [i for i in lyst if i > p]
        if len(min_lyst) == 0:
            return primes
        p = min(min_lyst)
        primes.append(p)


print(sieveOfEratosthenes(30))
