def isPalindrome(arg):
    print(type(arg))
    if type(arg) is not str and type(arg) is not int:
        print("Parameter 'arg' as value '" + str(arg) + "' of type "
              + str(type(arg)) + " but should be of type int or string.")
        return None
    if type(arg) is int and arg < 0:
        print("Parameter 'arg' has value '" + str(arg) + "' but should be positive.")
        return None
    arg = str(arg).lower()
    return arg == arg[::-1]


print(isPalindrome('Lager-regal'))
print(isPalindrome(0.34))
print(isPalindrome(1337331))
