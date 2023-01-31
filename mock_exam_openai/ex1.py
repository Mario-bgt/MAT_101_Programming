import numpy as np


# Part a)
def find_indices(l, s):
    if s == "positive":
        return [i for i, x in enumerate(l) if x > 0]
    elif s == "negative":
        return [i for i, x in enumerate(l) if x < 0]
    else:
        print("Invalid input for string s. Please enter 'positive' or 'negative'.")
        return


l = [1, -2, 3, -4, 5]
s = "negative"
v = find_indices(l, s)
print(v)
# Output: [1, 3]


# Part b)
def find_indices_matrix(M, s, t):
    if s == "bigger":
        return [[i, j] for i, row in enumerate(M) for j, val in enumerate(row) if val > t]
    elif s == "smaller":
        return [[i, j] for i, row in enumerate(M) for j, val in enumerate(row) if val < t]
    else:
        print("Invalid input for string s. Please enter 'bigger' or 'smaller'.")
        return


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = "smaller"
t = 5
v = find_indices_matrix(M, s, t)
print(v)
# Output: [[0, 0], [0, 1], [1, 0], [2, 0], [2, 1]]

# Part c)


def modify_3d_array(M):
    Q = np.zeros(M.shape)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            for k in range(M.shape[2]):
                if M[i, j, k] > 0.5:
                    Q[i, j, k] = np.power(M[i, j, k], 1/3)
                elif M[i, j, k] >= -0.5 and M[i, j, k] <= 0.5:
                    Q[i, j, k] = M[i, j, k]
                else:
                    Q[i, j, k] = np.power(M[i, j, k], 2)
    return Q
