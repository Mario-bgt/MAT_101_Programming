def digital_root(n):
    while True:
        if len(str(n)) == 1:
            return n
        temp = 0
        for i in range(len(str(n))):
            temp = temp + int(str(n)[i])
        n = temp


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
