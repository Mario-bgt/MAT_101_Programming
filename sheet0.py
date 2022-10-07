def find_min_and_idx(lyst):
    idx, idxmin = 0, 0
    while idx < len(lyst):
        if lyst[idxmin] > lyst[idx]:
            idxmin = idx
        idx += 1
    return idxmin, lyst[idxmin]


lyst = [1, 2, 3, 4, -1, 5, 8]
print(find_min_and_idx(lyst))
