def is_leap_year(year):
    """
    :param year:
        int
    :return:
        True if int is a leap year, False if int is not a leap year.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


def days_since_new_year(date):
    """
    :param date:
        list with [day, month]
    :return:
        int, amount of days since new year
    """
    monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = 0
    res = 0
    while i < (date[1] - 1):
        res += monthsDays[i]
        i += 1
    res += date[0] - 1
    return res


def days_between(start, end):
    start_year = start[2]
    end_year = end[2]
    
    return None
