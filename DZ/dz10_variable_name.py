import string
import keyword

word = input("Variable name: ")

if (word in keyword.kwlist
        or word[0].isdigit()
        or any(punc in word for punc in string.punctuation.replace('_', ''))
        or any(up in word for up in string.ascii_uppercase)
        or any(sp in word for sp in string.whitespace)
        or (word.count('_') == len(word) and len(word) > 1)):
    print(word, False)
else:
    print(word, True)
