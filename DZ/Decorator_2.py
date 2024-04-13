# Декоратор должен проверять, что все аргументы декорируемой функции, больше нуля.
# Если они больше нуля, тогда возвращать результат функции.
# Если хотябы один агрумент меньше нуля, возвращать None.
def zero_check(fn):
    def wrapper(*args):
        if 0 in args:
            return None
        else:
            return fn(*args)
    return wrapper


@zero_check
def difference(*args):
    if len(args) > 0:
        return round(max(args) - min(args), 2)
    else:
        return 0


print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())
print('OK')
