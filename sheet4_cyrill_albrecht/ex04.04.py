from math import pi


def pi_approximation(epsi):
    res = 0
    n = 0
    while True:
        res = res + (((-1) ** n) / (2 * n + 1))
        if abs(4 * res - pi) < epsi:
            return [n, 4 * res, pi]
        n += 1


Pi = pi_approximation(0.00068)
print(Pi)
