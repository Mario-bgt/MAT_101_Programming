import numpy as np


# Part a)
def my_occurrences(M, x):
    """
    Returns a list of the number of occurrences of x in each row of M.
    :param M: bidimensional ndarray of numbers
    :param x: int, scalar value
    :return: list, list of integers
    """
    # use list comprehension to iterate over rows of M
    return [np.count_nonzero(row == x) for row in M]


# Example usage
M = np.array([[1, 2, 3, 1], [4, 5, 1, 6], [0, 2, 5, 8], [1, 7, 8, 9]])
x = 1

occurrences = my_occurrences(M, x)
print(occurrences)
# Output: [2, 1, 0, 1]


# Part b)
def my_find(v, x, epsilon):
    """
    Returns the index of elements of v which are equal to x up to the tolerance epsilon.
    :param v: list of numbers
    :param x: scalar
    :param epsilon: tolerance
    :return: list of integers
    """
    # use list comprehension to iterate over rows of v
    return [i for i, vi in enumerate(v) if abs(vi - x) <= epsilon]


# Example usage
v = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
x = 1.0
epsilon = 0.5

indices = my_find(v, x, epsilon)
print(indices)
# Output: [0, 1, 2]
