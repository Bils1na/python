from random import randint
import time

def show_test(xyz: int) -> str:
    print(randint(1, xyz))
    print(time.time())
    return 1234

print(show_test(100))

# t = [True, False, False, True]

# left = t[0]

# for el in t:
#     left = left and el

# print(left)

# sp = [55, 111, True, 'sss', [55, 77, 88]]

# for i in range(len(sp)):
#     print(sp[i], end=" ")

# print(end = "\n")

# for el in sp:
#     print(el, end = " ")

# print(end = "\n")

# for item in enumerate(sp):
#     print(item)

# print(list(range(1000)))

