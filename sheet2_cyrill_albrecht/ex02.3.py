# Exercise 3

def score(s):
    if s < 0:
        return 'achieved negative points'
    elif s > 60:
        return 'achieved more points than the maximum'
    elif 55 < s <= 60:
        return 6.0
    elif 50 < s <= 55:
        return 5.5
    elif 45 < s <= 50:
        return 5.0
    elif 40 < s <= 45:
        return 4.5
    elif 35 < s <= 40:
        return 4.0
    elif 0 <= s <= 35:
        return 'failed attempt'


s = 60
grade = score(s)
print(grade)
