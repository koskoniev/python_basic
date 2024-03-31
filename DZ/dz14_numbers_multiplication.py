foo = input('Enter number: ')
res = None
while len(foo) > 1:
    res = 1
    for value in foo:
        res *= int(value)
        foo = str(res)
else:
    res = int(foo)
res = int(res)
print(res)
