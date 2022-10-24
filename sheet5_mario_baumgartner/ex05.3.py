from time import perf_counter_ns as t


def while_sum(N):
    res = 0
    n = 1
    while n < N + 1:
        res += n
        n += 1
    return res


def for_sum(N):
    res = 0
    for val in range(N + 1):
        res += val
    return res


def gauss_summation(N):
    return (N * (N + 1)) / 2


x = 99501
start = t()
res = while_sum(x)
end = t()
time = end - start
print(f"It took {time} nanoseconds to compute while_sum(N), and the result is {res}.")
start = t()
res = for_sum(x)
end = t()
time = end - start
print(f"It took {time} nanoseconds to compute for_sum(N), and the result is {res}.")
start = t()
res = gauss_summation(x)
end = t()
time = end - start
print(f"It took {time} nanoseconds to compute guass_summation(N), and the result is {res}.")
start = t()
res = sum(range(1, x + 1))
end = t()
time = end - start
print(f"It took {time} nanoseconds to compute sum(range(1+N+1)), and the result is {res}.")

for number in range(1, 10 ** 5, 1000):
    start = t()
    res = while_sum(number)
    end = t()
    best_time = (end - start, 'while_sum', res)
    start = t()
    res = for_sum(number)
    end = t()
    if best_time[0] > (end - start):
        best_time = (end - start, 'for_sum', res)
    start = t()
    res = gauss_summation(number)
    end = t()
    if best_time[0] > (end - start):
        best_time = (end - start, 'gauss_summation', res)
    start = t()
    res = sum(range(1, number + 1))
    end = t()
    if best_time[0] > (end - start):
        best_time = (end - start, 'sum(range(1, N + 1))', res)
    print(f"To calculate {number} the best option is {best_time[1]}, with just {best_time[0]} nanoseconds, coming to {best_time[2]} as the result")
