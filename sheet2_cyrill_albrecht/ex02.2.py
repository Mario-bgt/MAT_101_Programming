# Exercise 2


def index_of_t(L, t):
    i = 0
    if t not in L:
        return None
    j = 0
    while i < len(L):
        if t == L[i]:
            j = i
        i = i + 1
    return  j


L = [1, 2, 3, 4, 'dog', 2.3]
t = 2.3
idx = index_of_t(L, t)
print(idx)
