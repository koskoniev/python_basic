def common_elements():
    set_3 = set()   # create 1st list
    for i in range(1, 99):
        if i % 3 == 0:
            set_3.add(i)

    set_5 = set()   # create 2nd list
    for i in range(1, 99):
        if i % 5 == 0:
            set_5.add(i)

    return set_3.intersection(set_5)


print(common_elements())
