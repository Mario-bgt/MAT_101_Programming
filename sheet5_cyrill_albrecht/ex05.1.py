def Reverse(lst):
    if type(lst) is not list:
        print("Parameter 'lyst' is of type '" + str(type(lyst)) + "' but should be of type 'list'.")
    else:
        lst = lst[::-1]
    return lst


lst = [10, 11, 12, 13, 14, 1]
print(Reverse(lst))
