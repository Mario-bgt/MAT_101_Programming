# Homework_3_Exercise_1

def factorial(num):
    """
    Returns the factorial of "num".

    Prints a warning and returns None if "num" is negative or not an int.

    Input:
        num: int

    Output:
        result: int
    """
    # making sure "num" is an int
    if type(num) is not int:
        print("Parameter 'num' as value '" + str(num)
              + "' of type " + str(type(num)) + " but should be of type int.")
        return None

    # making sure "num" is positive
    if num < 0:
        print("Parameter 'num' as value '" + str(num)
              + "' but should be positive.")
        return None

    # preceeding to calculate num!
    result = 1  # defining the output variable

    # multiply result with every integer between "num" and 0
    while num > 0:  # num has to be bigger than 0 not 10
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
    for index in range(0, len(array)):  # it has to start at 0 otherwise the first Element won't be included
        # getting the next element in the list
        element = array[index]

        # need to skip elements that are neither int nor float
        if type(element) in [int, float]:
            # adding valid elements to the result
            result += element

    # returning the result
    return result


# Exercise 1a
correct1 = [15, 16, 17, 18, 19]
for i in correct1:
    print(i, factorial(i), factorial(i))
correct2 = ['dog', 14, 15]
for i in correct2:
    print(i, factorial(i), factorial(i))

correctlyst1 = [0, 2, 1]
print(sum_list(correctlyst1), sum(correctlyst1))
correctlyst2 = ['dog', 'cat', 1]
print(sum_list(correctlyst2))

# Exercise 1b
# These examples are wrong without the correction
L = [0, 1, 2, 3, 4, 5]
for i in L:
    print(i, factorial(i), factorial(i))

lyst1 = [1, 2, 3, 4]
lyst2 = [4, 1, 6, 200]
lyst3 = [5, 'dog', 3]
print(sum_list(lyst1), sum(lyst1))
print(sum_list(lyst2), sum(lyst2))
print(sum_list(lyst3))
