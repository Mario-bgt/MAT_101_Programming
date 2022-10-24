def isPalindrome(arg):
    if type(arg) is not str and type(arg) is not int:
        print(f"Parameter isn't a string or integer. Parameter is a {type(arg)}")
        return None
    if type(arg) is int and arg < 0:
        print("Parameter 'arg' has value '" + str(arg) + "' but should be positive.")
        return None
    arg = str(arg).lower()
    return arg == arg[::-1]


print(isPalindrome('cyrill'))
print(isPalindrome('racecar'))
print(isPalindrome(1337))
