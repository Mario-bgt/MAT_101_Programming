from time import perf_counter_ns


def while_sum(N):
    res = 0
    i = 1
    while i < N + 1:
        res = res + i
        i = i + 1
    return res


def for_sum(N):
    res = 0
    for i in range(N + 1):
        res = res + i
    return res


def gauss_summation(N):
    return (N * (N + 1)) / 2


N = 10000
start = perf_counter_ns()
res = while_sum(N)
end = perf_counter_ns()
time = end - start
print(f"It took {time} nanoseconds to compute while_sum(N), and the result is {res}.")


start = perf_counter_ns()
res = for_sum(N)
end = perf_counter_ns()
time = end - start
print(f"It took {time} nanoseconds to compute for_sum(N), and the result is {res}.")


start = perf_counter_ns()
res = gauss_summation(N)
end = perf_counter_ns()
time = end - start
print(f"It took {time} nanoseconds to compute guass_summation(N), and the result is {res}.")


start = perf_counter_ns()
res = sum(range(1, N + 1))
end = perf_counter_ns()
time = end - start
print(f"It took {time} nanoseconds to compute sum(range(1+N+1)), and the result is {res}.")


print("The gauss_summation will always be the fastest way to compute the Sum")