from inspect import isgenerator


def prime_generator(end):
    def is_prime(check_num):
        if check_num < 2 or check_num > 3 and ((check_num % 2 == 0) or (check_num > 10 and check_num % 5 == 0)):
            return False
        else:
            range_len = lambda l: l if (l < 10) else (l // 2 + 1)
            for divider in range(3, range_len(check_num), 2):
                if check_num % divider == 0:
                    return False
        return True


    for value in range(2, end + 1):
        if is_prime(value):
            yield value


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
