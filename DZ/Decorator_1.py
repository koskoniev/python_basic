import time
import functools


def dec(fn):
    def wrap(*args):
        start = time.time()
        res = fn(*args)
        print(time.time() - start)
        return res
    return wrap


@dec
def fib(value):
    if value in (1, 2):
        return 1
    else:
        return fib(value - 1) + fib(value - 2)


# print(fib)
# f = dec(fib)
# print(fib.__name__)
print(fib(29))
