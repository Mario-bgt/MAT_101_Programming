# Exercise 1

def gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd(b, a%b)

a = 0
b = 4

print(gcd(a, b))
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

# Exercise 2




def index_of_L():
    if L == []:
        return None
    else:
        return (L.index(t))

L = [5, 6, 7, 4, 3, 6, 0, 75, 3]
t = 0

print(index_of_L())


# Exercis 3

def score(s):
    if s < 0:
        return s == 'achieved negative points'
    elif s > 60:
        return s == 'achieved more points than the maximum'
    elif 55 < s <= 60:
        return s == 6.0
    elif 50 < s <= 55:
        return s == 5.5
    elif 45 < s <= 50:
        return s == 5.0
    elif 40 < s <= 45:
        return s == 4.5
    elif 35 < s <= 40:
        return  s == 4.0
    elif 0 < s <= 35:
        return s == 'failed attempt'

print(score(60))



def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result

for n in range(1, 11):
    print("phi(", n, ") = ", phi(n), sep="")







