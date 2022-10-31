# Exercise 2a
def quadratic_formula(a, b, c):
    root = abs(b ** 2) - 4 * a * c
    sqrt = root ** 0.5
    if root > 0:
        return [(-b + sqrt) / (2 * a), (-b - sqrt) / (2 * a)]
    elif root == 0:
        return [-b / (2 * a), -b / (2 * a)]
    else:
        return [- b / (2 * a) + 1j * sqrt / (2 * a), - b / (2 * a) - 1j * sqrt / (2 * a)]


# Exercise 2b
# with b = 0

def quadratic_formula2(a, c):
    sqrt = abs(-c / a) ** 0.5
    if (-c / a) >= 0:
        return [sqrt, -sqrt]
    else:
        return [1j * sqrt, -1j * sqrt]


# with c = 0

def quadratic_formula3(a, b):
    return [0, -b / a]

print(quadratic_formula(1,0,1))