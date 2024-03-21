lst = [0, 1, 7, 2, 4, 8]
# lst = [1, 3, 5]
# lst = [6]
# lst = []

summa = 0
if lst:
    for index, value in enumerate(lst):
        if index % 2 == 0:
            summa += value
    summa *= lst[-1]

print(summa)
