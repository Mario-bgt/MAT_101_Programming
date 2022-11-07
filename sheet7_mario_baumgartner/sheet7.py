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
print(array_11*array_12)
# Part d)
print(.2*array_11)
# Part f)
print(np.concatenate((array_11, array_12)))
# Part g)
print(np.concatenate((array_11[1:], array_12[:2])))
