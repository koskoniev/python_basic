print("DZ6: Move the lase list element to the beginning of the list")

my_list = list()
# пробуем аппенд
my_list.append('1')
my_list.append('2')
my_list.append('3')
print(my_list)

# var 1 - используем поп() и отдельную переменную
movable = my_list.pop()
my_list.insert(0, movable)
print(my_list)
the_list = my_list.copy()

# var 2 - используем поп() без переменной
my_list.insert(0, my_list.pop())
print(my_list)

# var 3 - переменная, список[-1], лен(), дел (но чисто на посмотреть)
movable = my_list[len(my_list) - 1]     # [len(my_list) - 1] is the last element
del (my_list[-1])    # index [-1] is the last element
my_list.insert(0, movable)
print(my_list)
