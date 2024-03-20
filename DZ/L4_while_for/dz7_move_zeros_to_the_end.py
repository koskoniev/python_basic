lst = [0, 1, 0, 12, 3]
# lst = [0]
# lst = [1, 0, 13, 0, 0, 0, 5]
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

size = len(lst)
index = 0
while index < size:
    if lst[index] == 0:
        lst.append(lst.pop(index))
        size -= 1   # could be "continue" instead
    else:
        index += 1

print(lst)
