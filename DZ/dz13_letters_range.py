import string

# range_letters = input("Input range (a-z): ")
range_letters = 'g-G'

# variant1
for i in range(string.ascii_letters.find(range_letters[0]), string.ascii_letters.find(range_letters[2]) + 1):
    print(string.ascii_letters[i], end='')

# variant 2
# print()
# print(string.ascii_letters[string.ascii_letters.find(range_letters[0]):string.ascii_letters.find(range_letters[2]) + 1])
