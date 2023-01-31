# Part a)

def find_indices(l, s):
    """
    Code a function which takes as input a list of numbers l and a string s and returns as output
    another list v. If the string s is equal to 'positive', it returns the list of the indices of the
    positive elements in the input list l; if the string s is equal to 'negative', it returns the list
    of the indices of the negative elements in the input list l; for any other value of the string s
    the execution is stopped.
    """
    if s != "positive" and s != "negative":
        print("Invalid input for string s. Please enter 'positive' or 'negative'.")
        return
    if s == "positive":
        return [i for i, x in enumerate(l) if x > 0]
    else:
        return [i for i, x in enumerate(l) if x < 0]

