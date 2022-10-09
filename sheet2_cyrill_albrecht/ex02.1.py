# Exercise 1
a = 10
b = 12


def gcd(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return abs(b)
    elif b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)


greatestCommonDivisor = gcd(a, b)
print(greatestCommonDivisor)


def lcm(a, b):
    if b == 0:
        return 0
    else:
        lcm = (a * b) // gcd(a, b)
        return lcm


leastCommonMultiple = lcm(a, b)
print(leastCommonMultiple)
