import time
import functools


def decorated(fn, time_begin=time.time()):
    print(time_begin, decorated.__name__)
    data = dict()
    def wrapper(num):
        nonlocal data
        def get_res(n):
            return fn(n)
        result = get_res(num)
        delta = time.time() - time_begin

        data["result"] = result
        data["delta"] = delta

        return data["result"]
    # print(time.time() - time_begin)
    return wrapper
    # return decorated


num_fib = 29


@decorated
# @functools.lru_cache()
def fib(value):
    if value in (0, 1):
        return value
    else:
        return fib(value - 2) + fib(value - 1)


print(time.time(), "b")
print(fib(num_fib))
print(time.time(), "e")
