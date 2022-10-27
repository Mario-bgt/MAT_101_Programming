# Part a
def quadratic_formula(a, b, c):
    radicand = b ** 2 - 4 * a * c
    sqrt = abs(radicand) ** .5
    if radicand > 0:
        return [(-b + sqrt) / (2 * a), (-b - sqrt) / (2 * a)]
    elif radicand == 0:
        return [-b / (2 * a), -b / (2 * a)]
    else:
        return [- b / (2 * a) + 1j * sqrt / (2 * a), - b / (2 * a) - 1j * sqrt / (2 * a)]


# Part b
# If c = 0
def quadratic_formula_no_c(a, b):
    return [0, -b / a]


# if b = 0
def quadratic_formula_no_b(a, c):
    sqrt = abs(-c / a) ** .5
    if -c / a >= 0:
        return [sqrt, -sqrt]
    else:
        return [1j * sqrt, -1j * sqrt]
