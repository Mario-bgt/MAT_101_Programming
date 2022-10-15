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
    while num >= 10:
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
    for index in range(1, len(array)):
        # getting the next element in the list
        element = array[index]

        # need to skip elements that are neither int nor float
        if type(element) in [int, float]:
            # adding valid elements to the result
            result += element

    # returning the result
    return result