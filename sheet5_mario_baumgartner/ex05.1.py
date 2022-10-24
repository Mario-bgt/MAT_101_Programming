def reverse(lyst):
    if type(lyst) is not list:
        print("Parameter 'lyst' is of type '" + str(type(lyst)) + "' but should be of type 'list'.")
        return None
    for i in range(len(lyst) // 2):
        lyst[i], lyst[-1 - i] = lyst[-1 - i], lyst[i]
    return lyst
