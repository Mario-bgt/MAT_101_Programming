def is_leap_year(year):
    if year % 4 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 400 == 0:
        return True
    else:
        return False


def days_since_new_year(date):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = 0
    res = 0
    while i < (date[1] - 1):
        res = res + days[i]
        i = i + 1
    res = res + date[0] - 1
    return res


def days_between(start, end):
    start_year = start[2] + 1
    end_year = end[2]
    res = 0
    while start_year < end_year:
        if is_leap_year(start_year):
            res = res + 366
            start_year = start_year + 1
        else:
            res = res + 365
            start_year = start_year + 1
    if is_leap_year(start[2]) and days_since_new_year(start[0:2]) > 59:
        res = res + 366 - days_since_new_year(start[0:2])
    else:
        res = res + 365 - days_since_new_year(start[0:2])
    if is_leap_year(end[2]) and days_since_new_year(end[0:2]) > 59:
        res = res + 1 + days_since_new_year(end[0:2])
    else:
        res = res + days_since_new_year(end[0:2])
    return res


print(days_between([15, 11, 1998], [26, 2, 2001]))
