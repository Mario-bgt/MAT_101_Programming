# Exercise 4
from math import gcd


def phi(n):
    i = 0
    for k in range(n):
        if 1 == gcd(k, n):
            i = i + 1
        return i


n = 2345
eulerPhi = phi(n)
print(eulerPhi)

