# import string
# import keyword
import time

ms1 = time.time()
print(ms1)

i = 1
while i < 1000000:
    i += i

print(i)
ms2 = time.time()
print(ms2)
print(ms2 - ms1)
