# The following part belongs to exersice 3
def ex3():
    sentence = 'You are using Python right now'
    print(type(sentence))
    print(sentence[0])
    print(sentence[-7:])
    print(sentence[4:7])
    print(len(sentence))


# The following part belongs to exersice 4
def ex4():
    array = [1, 'abc', [3.14], 2]
    print(type(array))
    print(array[2])
    names = ['Mario', 'Baumgartner']
    concatenated = array + names
    print(len(concatenated))


if __name__ == '__main__':
    ex3()
    # ex4()  # uncomment to run ex4
