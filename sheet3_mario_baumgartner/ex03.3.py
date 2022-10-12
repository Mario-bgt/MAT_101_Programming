def is_leap_year(year):
    """
    takes an int “year” and returns whether that year is a leap year
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
    takes a list of ints “date” and returns how many days are between New Year and date in a non-leap year
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
    takes two lists of ints “start” and “end” and calculates how many days are between “start” and “end”.
    :param start:
        list [day, month, year]
    :param end:
        list [day, month, year]
    :return:
        int, amount of days between start and end
    """
    start_year = start[2] + 1
    end_year = end[2]
    res = 0
    while start_year < end_year:
        if is_leap_year(start_year):
            res += 366
            start_year += 1
        else:
            res += 365
            start_year += 1
    if is_leap_year(start[2]) and days_since_new_year(start[0:2]) > 59:
        res = res + 366 - days_since_new_year(start[0:2])
    else:
        res = res + 365 - days_since_new_year(start[0:2])
    if is_leap_year(end[2]) and days_since_new_year(end[0:2]) > 59:
        res = res + 1 + days_since_new_year(end[0:2])
    else:
        res = res + days_since_new_year(end[0:2])
    return res


if __name__ == '__main__':
    print(days_between([25, 12, 2022], [4, 1, 2023]))
