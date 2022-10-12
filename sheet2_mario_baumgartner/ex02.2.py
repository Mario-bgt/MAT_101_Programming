def find_idx_of_t(L, t):
    """
    :param L:
        List
    :param t:
        str, int, bool, float
    :return:
        int
        The index at which t is located in L. If t not in L; returns None
    """
    idx = 0
    if t not in L:
        return None
    idxres = 0
    while idx < len(L):
        if L[idx] == t:
            idxres = idx
        idx += 1
    return idxres


L = [1, 2, 5, 7, 2, 88, 2, 69, 0, 34, 'Cat', 'Dog', True, 3, 3.56, 9]
t = 2

idx = find_idx_of_t(L, t)
print(idx)
