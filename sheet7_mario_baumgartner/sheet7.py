import numpy as np

# Exersice 1
# Part a)
lyst1 = [1, 2, 3]
lyst2 = [1.68, 2.71, 3.14]
array_11 = np.array(lyst1)
array_12 = np.array(lyst2)
# Part b)
print(array_11 + array_12)
# Part c)
print(array_11 * array_12)
# Part d)
print(.2 * array_11)
# Part e)
print(array_12**2)
# Part f)
print(np.concatenate((array_11, array_12)))
# Part g)
print(np.concatenate((array_11[1:], array_12[:2])))

# Exersice 2
# Part a)
array_21 = np.array(np.arange(4))
print(array_21)
# Part b)
array_22 = np.array(np.linspace(0, 1, 4))
print(array_22)
# Part c)
print(np.linalg.norm(array_22))
# Part d)
print(np.inner(array_21, array_22))
# Part e)
print(np.outer(array_21, array_22))

# Exersice 3
# Part a)
ones = np.ones((3, 3))
print(ones)
# Part b)
iden = np.eye(3)
print(iden)
# Part c)
print(ones + iden)
# Part d)
print(iden * [7, 11, 2022])
# Part e)
mat = np.block([
    [np.eye(2), np.full((2, 2), 4)],
    [np.zeros((2, 2)), np.array([19, 2])*np.eye(2)]])
print(mat)
