def sort_by_lowest(lyst):
    lyst.sort()
    return lyst


def no_doubles(lyst):
    res = []
    for val in lyst:
        if val not in res:
            res.append(val)
    return res


L_1 = [2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 2, 4, 3]
print(sort_by_lowest(L_1))
print(no_doubles(L_1))
