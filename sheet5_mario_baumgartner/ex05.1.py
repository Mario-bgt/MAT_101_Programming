# Part a
"""

1) let n = the rounded value for the middle of the length of the list
2) we switch the first with the last element of the list
3) we switch the second with the second last elementl of the list
4) and so on till we arrive at the middle (amount of switches from 1))
5) list is now reversed

"""


# Part b
def reverse(lyst):
    if type(lyst) is not list:
        print("Parameter 'lyst' is of type '" + str(type(lyst)) + "' but should be of type 'list'.")
        return None
    for i in range(len(lyst) // 2):
        lyst[i], lyst[-1 - i] = lyst[-1 - i], lyst[i]
    return lyst
