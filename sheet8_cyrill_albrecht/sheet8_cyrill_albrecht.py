import numpy as np


def fibonacciMatrix(n):
    a = np.block([[1, 1], [1, 0]])
    fibonacci_n = np.linalg.matrix_power(a, n) @ np.transpose(np.array([1, 0]))
    print(fibonacci_n)


fibonacciMatrix(101)


def monteCarloPi(N):
    circle_points = 0
    square_points = N
    for j in range(N):
        rand_x = np.random.uniform(-1, 1)
        rand_y = np.random.uniform(-1, 1)
        distance = np.sqrt(rand_x ** 2 + rand_y ** 2)
        if distance <= 1:
            circle_points += 1
    return 4 * (circle_points / square_points)


print(monteCarloPi(10000))

def monteCarloSphere(n, d):

    values = np.random.uniform(low=-1, high=1, size=(n, d))
    e = 0
    for j in values:
        if np.linalg.norm(j) <= 1:
            e = e + 1
    return np.power(2, d) * (e / n)


volume_3 = monteCarloSphere(10000, 3)
volume_4 = monteCarloSphere(10000, 4)
volume_10 = monteCarloSphere(10000, 10)
volume_100 = monteCarloSphere(10000, 100)
volume_300 = monteCarloSphere(10000, 300)
print(f"The volume of dimension 3 = {volume_3}, 4 = {volume_4}, 10 = {volume_10}, 100 = {volume_100}, 300 = {volume_300} ")


def sieveOfEratosthenes(n):
    lyst = np.arange(2, n + 1)
    p = 2
    primes = [2]
    while True:
        multiples = list(range(2 * p, n+1, p))
        temp_lyst = []
        for j in lyst:
            if j not in multiples:
                temp_lyst.append(j)
        lyst = temp_lyst
        min_lyst = []
        for i in lyst:
            if i > p:
                min_lyst.append(i)
        if len(min_lyst) == 0:
            return primes
        p = min(min_lyst)
        primes.append(p)


print(sieveOfEratosthenes(100))