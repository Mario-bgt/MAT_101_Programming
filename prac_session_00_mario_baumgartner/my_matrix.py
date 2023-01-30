import numpy as np


def my_matrix(n, m):
    i_val = np.arange(1, n+1, 1)
    j_val = np.arange(1, m+1, 1)
    mat = []
    for i in i_val:
        if i % 2 == 0:
            line = [(-1) ** (i + j) * (i + j) for j in j_val]
        else:
            line = [(-1) ** (i + j) * (i - j) for j in j_val]
        mat.append(line)
    return mat


def symmetric_matrix(mat):
    for line in mat:
        for j in range(len(line)):
            if line[j] != line[::-1][j]:
                print('Not symmetric')
                return False
    print('Symmetric')
    return True


def my_extract(mat):
    """takes as input a matrix A and gives as output two matrices
    B and C made respectively by the even rows only and by the odd columns only of the matrix A.
    Consider 0 as an even number here.
    INPUT: matrix A
    OUTPUT: matrices B and C"""
    B = []
    C = []
    for i in range(len(mat)):
        if i % 2 == 0:
            B.append(mat[i])
    for j in range(len(mat[0])):
        if j % 2 == 1:
            C.append([line[j] for line in mat])
    return B, C
