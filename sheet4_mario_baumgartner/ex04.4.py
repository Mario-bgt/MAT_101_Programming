from math import pi


def approxPi(epsilon):
    res = 0
    n = 0
    while True:
        res += ((-1) ** n) / (2 * n + 1)
        if abs(4 * res - pi) < epsilon:
            return [n, 4*res, pi]
        n += 1


Pi = approxPi(1e-6)
print(Pi)
