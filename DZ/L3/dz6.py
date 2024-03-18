print("DZ6: Move the lase list element to the beginning of the list")

# my_list = [12, 3, 4, 10]
# my_list = [1]
my_list = []
# my_list = [12, 3, 4, 10, 8]
print(my_list)

if my_list:
    my_list.insert(0, my_list.pop())

print(my_list)
