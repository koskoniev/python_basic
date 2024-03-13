# digit = int(input("Enter 5 number: "))
digit = 12345
pet = 10000
ter = 1000
sto = 100
ten = 10
one = 1
a, b = divmod(digit, ter)
c, d = divmod(b, sto)
e, f = divmod(a, ten)
g, h = divmod(d, ten)
print((h * pet) + (g * ter) + (c * sto) + (f * ten) + (e * one))
