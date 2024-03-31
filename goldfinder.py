field = list()

field.append([7])
field.append([5, 8])
field.append([9, 8, 2])
field.append([1, 3, 5, 6])
field.append([6, 2, 4, 4, 5])
field.append([9, 5, 3, 5, 5, 7])
field.append([7, 4, 6, 4, 7, 6, 8])
print(field)

loot = field[0][0]

i = 0
place = 0

while i < len(field) - 1:
    if field[i + 1][place] > field[i + 1][place + 1]:
        loot += field[i + 1][place]
    else:
        loot += field[i + 1][place + 1]
        place += 1
    print("place:", place, "loot:", loot)
    i += 1
