import time
import functools


def dec(fn):

    def wrap(*args):
        start = time.time()
        # nonlocal start
        res = fn(*args)
        d = dict()
        dt = time.time() - start
        d["res"] = res
        d["time"] = dt
        return d
    return wrap


@dec
def fib(value):
    if value in (0, 1):
        return value
    else:
        return fib(value - 2) + fib(value - 1)


@dec
def f_prime(check_num):
    if check_num < 2 or check_num > 3 and ((check_num % 2 == 0) or (check_num > 10 and check_num % 5 == 0)):
        return False
    else:
        range_len = lambda l: l if (l < 10) else (l // 2 + 1)
        for divider in range(3, range_len(check_num), 2):
            if check_num % divider == 0:
                return False
    return True


# print(fib)
# f = dec(fib)
# print(fib.__name__)
print(fib(28))
# print(f_prime(99991))
