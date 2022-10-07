from math import gcd


def phi(n):
    """
    :param n:
        int
    :return:
        int
        The amount of times 1 <= k <= n where gcd(k,n) == 1
    """
    euler = 0
    for i in range(n+1):
        if gcd(i+1, n) == 1:
            euler += 1
    return euler


eulerPhi = phi(1487)
print(eulerPhi)
