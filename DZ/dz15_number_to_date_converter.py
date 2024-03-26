# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

data = (0, 224930, 466289, 950400, 1209600, 1900800, 8639999, 22493, 7948799)
for value in data:
    _24 = 86400
    _hr = 24
    _sec = 3600
    _min = 60
    days, sec = divmod(value, _24)
    hr, sec = divmod(sec, _sec)
    mins, sec = divmod(sec, _min)
    # print(days, hr, mins, sec)
    dayqty = ''
    if str(days)[-1] == 1:
        dayqty = 'день'
    elif (int(str(days)[-1]) >= 2) and (int(str(days)[-1]) <= 4):
        dayqty = 'дні'
    elif int(str(days)[-1]) == 0 or int(str(days)[-1]) >= 5 and int(str(days)[-1]) <= 19:
        dayqty = 'днів'
    hr = str(hr).zfill(2)
    mins = str(mins).zfill(2)
    sec = str(sec).zfill(2)

    # print(days, dayqty, ',', hr, mins, sec)
    the_date = f'{days} {dayqty}, {hr}:{mins}:{sec}'
    print(the_date)
