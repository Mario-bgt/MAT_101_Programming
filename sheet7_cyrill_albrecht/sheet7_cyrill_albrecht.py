import numpy as np


# Exercise 1a
lst1 = [1, 2, 3]
lst2 = [1.68, 2.71, 3.14]
array_11 = np.array(lst1)
array_12 = np.array(lst2)
# Exercise 1b
print(array_11 + array_12)
# Exercise 1c
print(array_11 * array_12)
# Exercise 1d
print(array_11 / 5)
# Exercise 1e
print(array_12 ** 2)
# Exercise 1f
print(np.concatenate((array_11, array_12)))
# Exercise 1g
print(np.concatenate((array_11[1:], array_12[:2])))


# Exercise 2a
array_21 = np.array(np.arange(4))
print(array_21)
# Exercise 2b
array_22 = np.array(np.linspace(0, 1, 4))
print(array_22)
# Exercise 2c
print(np.linalg.norm(array_22))
# Exercise 2d
print(np.dot(array_21, array_22))
# Exercise 2e
print(np.outer(array_21, array_22))


# Exercise 3a
matrix_3_3 = np.ones((3, 3))
print(matrix_3_3)
# Exercise 3b
identity_matrix = np.eye(3)
print(identity_matrix)
# Exercise 3c
print(identity_matrix + matrix_3_3)
# Exercise 3d
print(identity_matrix * ([7, 11, 2022]))
# Exercise 3e
matrix_func = np.block([
    [np.eye(2), np.full((2, 2), 4)],
    [np.zeros((2, 2)), np.array([19, 2])*np.eye(2)]])
print(matrix_func)