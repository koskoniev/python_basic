import random

lst = []
for i in range(random.randint(3, 10)):
    lst.append(random.randint(0, 99))
print(lst)

new_list = []
index = 0
while index < len(lst):
    if (index == 0) or (index == 2):    # taking elements 1 и 3
        new_list.append(lst[index])
    index += 1
new_list.append(lst[-2])    # adding element -2

print(new_list)
