# exersice 1)
a = 3
b = 15


def gcd(a, b):
    """
    :param a:
        int
    :param b:
        int
    :return:
        the greatest common divisor among a and b
    """
    if a == b == 0:
        return 0
    elif b == 0:
        return abs(a)
    elif a == 0:
        return abs(b)
    else:
        return gcd(b, a % b)


greatestCommonDivisor = gcd(a, b)


def lcm(a, b):
    """
    :param a:
        int
    :param b:
        int
    :return:
        the lowest common multiple of a and b
    """
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return (a / gcd(a, b)) * b


leastCommonMultiple = lcm(a, b)
print(greatestCommonDivisor, leastCommonMultiple)
