def reverse(lst):  # I think the exercise don't want me to do this, but it's an easy way
    if type(lst) is not list:
        print("Parameter 'lst' is of type '" + str(type(lst)) + "' but should be of type 'list'.")
    else:
        lst = lst[::-1]
    return lst


lst = [10, 11, 12, 13, 14, 1]
print(reverse(lst))


def reverse_2(lyst):
    if type(lyst) is not list:
        print("Parameter 'lyst' is of type '" + str(type(lyst)) + "' but should be of type 'list'.")
    for i in range(len(lyst)):
        last_item = lyst.pop()  # .pop() removes the last element and stores it in last_item.
        lyst.insert(i, last_item)  # .insert moves last_item to index i
    return lyst


lyst = [10, 11, 12, 13, 14, 1]
print(reverse_2(lyst))
