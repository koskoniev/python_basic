import string

foo = "7654"
print(foo)
res = 1
_len = len(foo)
while _len - 1 > 1:
    for i in foo:
        num = int(i)
        res *= num
        foo = str(res)
        _len = len(foo)
print(res)
