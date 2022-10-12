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
    """
    :param start:
        list [day, month, year]
    :param end:
        list [day, month, year]
    :return:
        int, amount of days between start and end
    """
    start_year = start[2]+1
    end_year = end[2]
    res = 0
    while start_year < end_year:
        if is_leap_year(start_year):
            res += 366
            start_year += 1
        else:
            res += 365
            start_year += 1
    if is_leap_year(start[2]) and days_since_new_year([start[0:2]]) > 59:
        res = res + 1 +

    return res
