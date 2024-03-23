import string

value = (input("Enter text for hashtag: ")).title().replace(' ', '')

for char in value:
    for symbol in string.punctuation:
        if char == symbol:
            value = value.replace(char, '')
value = ('#' + value)[:140]

print(value)
