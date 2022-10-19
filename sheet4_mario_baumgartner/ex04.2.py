##### Part a #####
def collatz(num):
    res = []
    while True:
        if num == 1:
            res.append(num)
            return res
        else:
            res.append(num)
            if num % 2 == 0:
                num = num / 2
            else:
                num = 3*num + 1


##### Part b #####
cache = {1: 1}


def collatz_bonus(n):
    path = [n]
    while n not in cache:
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
        path.append(n)
    for i, m in enumerate(reversed(path)):
        cache[m] = cache[n] + i
    return cache[path[0]]


longest_list = max(range(1, 10**4), key=collatz_bonus)
lenght = len(collatz(longest_list))
print(f'The longest list with numbers under 10e4 was achieved with {longest_list} and has exactly {lenght} objects')
