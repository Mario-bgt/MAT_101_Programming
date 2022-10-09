# Exercise 4
from math import gcd


def phi(n):
    i = 0
    for k in range(n+1):
        if 1 == gcd(k+1, n):
            i = i + 1
    return i


n = 1354
eulerPhi = phi(n)
print(eulerPhi)

