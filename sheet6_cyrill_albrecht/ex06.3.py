def is_isogram(word):
    word = word.lower()
    word = word.replace(' ', '')
    lst_check = []
    for i in word:
        if i in lst_check:
            return False
        else:
            lst_check.append(i)
    return True


print(is_isogram('Dermatoglyphics'))
print(is_isogram('Abba'))
print(is_isogram('MOose'))
print(is_isogram('Ambidextrous'))
print(is_isogram('The big dwarf only jumps'))