def digital_root(n):
    if n < 10:
        return n
    n= n % 10 + digital_root(n//10)
    return digital_root(n)

print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
