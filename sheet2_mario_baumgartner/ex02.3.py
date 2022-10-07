def find_grade(s):
    """
    :param s:
        int, your score
    :return:
        your grade
    """
    if s < 0 or s > 60:
        return 'Invalid input'
    elif s <= 35:
        return 'Failed attempt'
    elif s <= 40:
        return 4.0
    elif s <= 45:
        return 4.5
    elif s <= 50:
        return 5.0
    elif s <= 55:
        return 5.5
    elif s <= 60:
        return 6.0


grade = find_grade(58)
print(grade)
