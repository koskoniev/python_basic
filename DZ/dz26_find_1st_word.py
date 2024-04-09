def first_word(text):
    """ Пошук першого слова """
    def get_list(my_text):
        return my_text.replace(",", " ").replace(".", " ").strip(" ").split(" ")

    def gen(getlist):
        yield getlist[0]

    lst = gen(get_list(text))
    return next(lst)


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
