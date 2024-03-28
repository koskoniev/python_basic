import string

# range_letters = input("Input range (a-z): ")
range_letters = 'g-G'

begin = string.ascii_letters.find(range_letters[0])
end = string.ascii_letters.find(range_letters[2]) + 1

# variant1
for i in range(begin, end):
    print(string.ascii_letters[i], end='')

# variant 2
# print()
# print(string.ascii_letters[string.ascii_letters.find(range_letters[0]):string.ascii_letters.find(range_letters[2]) + 1])
# print(begin:end)
