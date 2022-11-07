from time import perf_counter_ns as time


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


start = time()
t_19 = fibonacci_recursive(19)
end = time()
time_19 = (end - start) / 1e9
start = time()
t_38 = fibonacci_recursive(38)
end = time()
time_38 = (end - start) / 1e9
print(f"To compute f19 = {t_19} it used {time_19} seconds")
print(f"To compute f38 = {t_38} it used {time_38} seconds")


def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


start = time()
t_40 = fibonacci_iterative(40)
end = time()
time_40 = (end - start) / 1e9
print(f"To compute f40 = {t_40} it used {time_40} seconds")

n = 1
while True:
    fibonacci1 = fibonacci_iterative(n)
    fibonacci2 = fibonacci_iterative(n + 1)
    if fibonacci2 / fibonacci1 == (1 + 5 ** 0.5) / 2:
        print(f"It took {n + 1} fibonacci numbers until its equal to the golden ratio")
        break
    n = n + 1

count_lyst = []


def fibonacci_recursive_counter(n):
    count_lyst.append(1)
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_recursive_counter(n - 1) + fibonacci_recursive_counter(n - 2)


print(fibonacci_recursive_counter(10), len(count_lyst))
