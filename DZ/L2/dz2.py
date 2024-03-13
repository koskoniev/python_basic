print("dz2")

num = int(input("Enter 4-digits number: "))
print("This is the number: ", num)

print("Variant 1")
print(num // 1000)
print((num - (num // 1000) * 1000) // 100)
print((num - ((num // 100) * 100)) // 10)
print(num - ((num // 10) * 10))

print("Variant 2")
n1, n2 = divmod(num, 1000)
n2, n3 = divmod(n2, 100)
n3, n4 = divmod(n3, 10)
print(n1, "\n", n2, "\n", n3, "\n", n4)
