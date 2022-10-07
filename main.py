import numpy as np


def salomes_theorem(number):
    begginer_number = number
    if number >= 100:
        number = 99
    if number % 11 == 0:
        return print(f'{begginer_number} does not converge to 9 cause its divisable by 11')
    n = 0
    while number != 9:
        new = str(number)[1] + str(number)[0]
        number = abs(number - int(new))
        n += 1
        if n >= 100:
            print(f'function did not terminate with {begginer_number}, even afer {n} tries')
            break
    print(f'{begginer_number} terminated to 9 after {n} loops!')

'''
for i in np.linspace(10, 199, 190):
    salomes_theorem(int(i))
'''



def marios_theorem(number):
    n = 0
    beggin = number
    while number != 4:
        if number % 2 == 1:
            number = number * 3 + 1
        else:
            number = number / 2
        n += 1
    print(f'We arrived at the 1, 2, 4 loop after {n} loops for the number {beggin}')


for i in np.linspace(1, 1000,1001):
    marios_theorem(int(i))