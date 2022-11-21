# Homework_3_Exercise_1
import math


def factorial(num):
    """
    Returns the factorial of "n".

    Prints a warning and returns None if "n" is negative or not an int.

    Input:
        n: int

    Output:
        result: int
    """
    # making sure "n" is an int
    if type(num) is not int:
        print("Parameter 'n' as value '" + str(num)
              + "' of type " + str(type(num)) + " but should be of type int.")
        return None

    # making sure "n" is positive
    if num < 0:
        print("Parameter 'n' as value '" + str(num)
              + "' but should be positive.")
        return None

    # preceeding to calculate n!
    result = 1  # defining the output variable

    # multiply result with every integer between "n" and 0
    while num > 0:
        result = result * num
        num = num - 1

    # returning the result
    return result


def sum_list(array):
    """
    Returns the sum of all ints and floats in the list "array".
    Elements of other types are ignored.

    Prints a warning and returns 0 if "array" is not of type list.
    Returns 0 if "array" is empty or contains no ints or floats.

    Input:
        array: list

    Output:
        result: float
    """
    # making sure "array" is a list
    if type(array) is not list:
        print("Parameter 'array' as value '" + str(array) + "' of type "
              + str(type(array)) + " but should be of type list.")
        return 0
    result = 0

    # calculating the sum over "array"
    for index in range(0, len(array)):
        # getting the next element in the list
        element = array[index]

        # need to skip elements that are neither int nor float
        if type(element) in [int, float]:
            # adding valid elements to the result
            result += element

    # returning the result
    return result


for i in range(14):
    print(i, factorial(i), math.factorial(i))

lyst1 = [1, 2, 4, 6]
lyst2 = [3, 2, 4, 6]
lyst3 = [5, 2, 4, 6]
print(sum_list(lyst1), sum(lyst1))
print(sum_list(lyst2), sum(lyst2))
print(sum_list(lyst3), sum(lyst3))
lyst4 = [0, 5, 5, 5]
lyst5 = ['hello', 2, 'two']
print(sum_list(lyst4), sum(lyst4))
print(sum_list(lyst5))
