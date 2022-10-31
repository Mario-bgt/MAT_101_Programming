from time import perf_counter_ns as t

# Part a)
def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Part b)
start = t()
res_19 = fibonacci_recursive(19)
end = t()
time_19 = (end - start) / 1e9
start = t()
res_38 = fibonacci_recursive(38)
end = t()
time_38 = (end - start) / 1e9
print(f"The value of F_19 is equal to {res_19} and it took {time_19} seconds to compute.")
print(f"The value of F_38 is equal to {res_38} and it took {time_38} seconds to compute.")
print(f"Notice that it took {time_38 - time_19} seconds longer to compute F_38.")


# Part c)
def fibonacci_iterative(n):
    a = 0
    b = 1
    for i in range(0, n):
        c = b
        b = a + b
        a = c
    return a


# Part d)
start = t()
res_40 = fibonacci_iterative(40)
end = t()
time_40 = (end - start) / 1e9
print(f"The value of F_40 is equal to {res_40} and it took {time_40} seconds to compute.")
print(f"Notice that it took {time_38 - time_40} seconds less to compute F_40 with iterative methode than it took to "
      f"compute F_38 with the recursive version")

# Part e)
n = 1
while True:
    fib1 = fibonacci_iterative(n)
    fib2 = fibonacci_iterative(n + 1)
    if fib2 / fib1 == (1 + 5 ** .5) / 2:
        print(n+1)
        break
    n += 1


# Part f)

