# import time
#
#
# class Light:
#     def __init__(self):
#         self.switch = False
#
#     def on(self):
#         self.switch = True
#         print("Light ON")
#
#     def off(self):
#         self.switch = False
#         print("Light OFF")
#
#     def status(self):
#         return self.switch
#
#     def switch(self) -> None:
#         if self.status():
#             self.off()
#         else:
#             self.on()
#
#
# l = Light()
# print(l.status())
# l.switch
#
# # for i in range(7):
# #     # if l.status():
# #     l.switch()
# #     # else:
# #     #     l.on()
# #     time.sleep(0.5)
# end = 11
# num = 3
# for i in range(2, num // 2 + 1):
#     if num % i != 0:
#         # num = i
#         print(i, num)
#     else:
#         print(i, num, "else")

# print(5//2)
# print(5//2 + 1)

# for i in range(9):
#     if i & 0:
#         print(bin(i))
#         print(i, 'even')
#     else:
#         print(i, 'odd')
#         print(bin(i))

# def is_even(number):
#     s = str(number)[-1]
#     print(s)
#     # if int(s[-1]) in (0, 2, 4, 6, 8):
#     if s[-1] in ("24680"):
#         return True
#     else:
#         return False


# print(is_even(2494563894038**2))
# print(is_even(1056897**2))
# # print(is_even(24945638940387**3))
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
# print('OK')

# print(int(b))
# print(b & 0b1)

# def is_even(number):
#     if number & 1:
#         return False
#     else:
#         return True
#     # return bool(number & 0)
#
#
# # print(is_even(2494563894038**2))
# # print(is_even(1056897**2))
# # print(is_even(24945638940387**3))
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
# print('OK')

from inspect import isgenerator


def prime_generator(end):
    num = 2
    i = 2
    while i < end:
        yield num
        i += 1
        for j in range(2, i):
            if i % j in range(2, i):
                i += 1
            else:
                num = i


# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print(list(prime_generator(10)))
# print(list(prime_generator(15)))
# print(list(prime_generator(29)))
# print('Ok')
#
# # l = list()
# num = 2
# end = 29
# # l.append(num)
# # print(l)
# for i in range(2, end+1):
#     for j in range(2, i):
#         if i % j == 0:
#             num += 1
#         else:
#             num = i
#             num += 1
#             # print(num)
#     print(num)

def fp(*args):
    print(*args)


fp(2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
