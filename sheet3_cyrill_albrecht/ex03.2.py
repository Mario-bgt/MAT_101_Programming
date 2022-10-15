def power(base, exponent):
    if type(base) is not int and not float:
        print("Parameter 'base' as value '" + str(base) + "' of type "
              + str(type(base)) + " but should be of type int or float.")
        return None
    if type(exponent) is not int:
        print("Parameter 'exponent' as value '" + str(exponent) + "' of type "
              + str(type(exponent)) + " but should be of type int.")
        return None
    if exponent < 0:
        print("Parameter 'exponent' has value '" + str(exponent) + "' but should be greater or equal to 0.")
        return None
    res = base
    for i in range(exponent - 1):
        res = res * base
    return res


def better_power(base, exponent):
    if type(base) is not int and not float:
        print("Parameter 'base' as value '" + str(base) + "' of type "
              + str(type(base)) + " but should be of type int or float.")
        return None
    if type(exponent) is not int:
        print("Parameter 'exponent' as value '" + str(exponent) + "' of type "
              + str(type(exponent)) + " but should be of type int.")
        return None
    if exponent < 0 and base == 0:
        print("This combination of parameters is not valid: Parameter 'exponent' has value '" + str(
            exponent) + "' and parameter 'base' hase value 0. ")
        return None
    if exponent == 0:
        return 1
    if exponent >= 0:
        res = base
        for i in range(exponent - 1):
            res = res * base
        return res
    else:
        res = base
        for i in range(abs(exponent) - 1):
            res = res * base
        return 1 / res
