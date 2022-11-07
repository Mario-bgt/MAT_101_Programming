import numpy as np


# Exercise 1a
array_11 = np.array([1, 2, 3])
array_12 = np.array([1.68, 2.71, 3.14])
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
array_13 = np.concatenate((array_11, array_12))
array_13 = np.delete(array_13, ([0], [-1]))
print(array_13)


# Exercise 2a
array_21 = np.arange(4)
print(array_21)
# Exercise 2b
array_22 = np.linspace(0, 1, 4)
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
print(identity_matrix * matrix_3_3)
# Exercise 3d
print(identity_matrix * ([7, 11, 2022]))
# Exercise 3e