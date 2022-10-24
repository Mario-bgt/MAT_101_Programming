def collatz(num):
    lyst = []
    while True:
        if num == 1:
            lyst.append(num)
            return lyst
        else:
            lyst.append(num)
            if num % 2 == 0:
                num = num / 2
            else:
                num = 3*num + 1


print(collatz(33))