import math


def quadratic_formula(a, b, c):
    radicand = b ** 2 - 4 * a * c
    sqrt = abs(radicand) ** .5
    if radicand > 0:  # real and different root
        return [(-b + sqrt) / (2 * a), (-b - sqrt) / (2 * a)]
    elif radicand == 0:
        return [-b / (2 * a), -b / (2 * a)]
    else:
        return [- b / (2 * a) + 1j * sqrt / (2 * a), - b / (2 * a) - 1j * sqrt / (2 * a)]


print(quadratic_formula(5, 4, 14))
