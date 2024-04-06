def popular_words(text: str, words: list):
    dic = dict()
    text = text.lower().split(" ")
    for i in words:
        dic[i] = text.count(i)
    return dic


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
