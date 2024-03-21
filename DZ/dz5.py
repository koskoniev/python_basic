print("DZ5: List split")

# my_list = [1, 2, 3, 4, 5, 6]
# my_list = [1, 2, 3]
# my_list = [1, 2, 3, 4, 5]
my_list = [1]
# my_list = []

# тут определяем границу 1й части списка
if (len(my_list) % 2) == 0:
    # если длина 2х частей одинакова
    range_start = int(len(my_list) / 2)
else:
    # если длина частей не равна, то сдвигаем границу вправо
    range_start = int((len(my_list) / 2) + 1)

# тут определяем границу 2й части списка
range_end = len(my_list)

new_list = [my_list[0:range_start], my_list[range_start:range_end]]
print(new_list)
