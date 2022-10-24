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


print(collatz(42))
