dt = dict.fromkeys(['d', 'h', 'm', 's', 'dn'], 0)
# dt['s'] = int(input("Enter seconds to convert: "))
dt['s'] = 100_000

_sec_24 = 86400
_hr_24 = 24
_sec_hr = 3600
_min_hr = 60

dt['d'], dt['s'] = divmod(dt['s'], _sec_24)
dt['h'], dt['s'] = divmod(dt['s'], _sec_hr)
dt['m'], dt['s'] = divmod(dt['s'], _min_hr)

if dt['d'] == 1 or (dt['d'] > 20 and int(str(dt['d'])[-1]) == 1):
    dt['dn'] = 'день'
elif ((int(str(dt['d'])[-1]) >= 2) and (int(str(dt['d'])[-1]) <= 4)) and (dt['d'] < 5 or dt['d'] > 20):
    dt['dn'] = 'дні'
else:
    dt['dn'] = 'днів'

hh = str(dt['h']).zfill(2)
mm = str(dt['m']).zfill(2)
ss = str(dt['s']).zfill(2)

the_date = f'{dt['d']} {dt['dn']}, {hh}:{mm}:{ss}'
print(the_date)
