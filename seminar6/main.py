from random import randint
from easygui import *


def random_list(size):
    result = []
    for i in range(size):
        result.append(randint(-10, 10))
    return result


size = int(enterbox("Enter number >> "))
msgbox(str({str(i): randint(1, 100) for i in range(size)}))


# sp = [-5, 8, -9, 1, 7, 2]

# print([x for x in sp])
# print([x**2 for x in sp])
# print([x**2 if x > 0 else 0 for x in sp])

# print({str(x): x for x in sp})
# print({str(x): randint(1, 10) for x in range(10)})
# print({str(x): [x for x in sp] for x in range(10)})
# второй список на основе пенрвого, если элемент больше 0 то возвести в квадрат

# print(random_list(10))

# print([randint(1, 100) for i in range(10)])