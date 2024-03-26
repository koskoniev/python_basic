import string

range_letters = input("Input range (a-z): ")

for i in range(string.ascii_letters.find(range_letters[0]), string.ascii_letters.find(range_letters[2]) + 1):
    print(string.ascii_letters[i], end='')
