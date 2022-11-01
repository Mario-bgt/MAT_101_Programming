def is_isogram(phrase):
    phrase = phrase.lower()
    phrase = phrase.replace(' ', '')
    check_lyst = []
    for i in phrase:
        if i in check_lyst:
            return False
        else:
            check_lyst.append(i)
    return True


print(is_isogram('Dermatoglyphics'))
print(is_isogram('Abba'))
print(is_isogram('MOose'))
print(is_isogram('Ambidextrous'))
print(is_isogram('The big dwarf only jumps'))
