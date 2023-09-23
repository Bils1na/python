from time import time

# def how_long(func):
#     start = time()
#     func()
#     print(f"It spends {time() - start} sec")

# def create_list():
#     return [i for i in range(500000)]

# how_long(create_list)

# def calc_power(pow):
#     def calc_value(root):
#         return root ** pow
#     return calc_value

# print(calc_power(2)(2))

# square = calc_power(2)
# cube = calc_power(3)
# print(square(8))
# print(cube(2))

# square_2 = lambda x: x**2
# print(square_2(7))

# calc = {"+": lambda x,y: x + y,
#         "-": lambda x,y: x - y,
#         "*": lambda x,y: x * y,
#         "/": lambda x,y: x / y,
#         }

# def obrab(x, y, calc):
#     for key in calc:
#         print(calc[key](x,y))

# print(calc["*"](7, 4))
# print(calc["/"](7, 4))
# obrab(7, 4, calc)

sp = [7, 8, 11, -5, -9. -7]
sp2 = ["Ivan", "Kolya"]

# print(list(map(abs, sp)))
# print(*sp)
# # print(*map(abs, sp))
# print(*map(lambda item: -item, sp))
# print(*map(lambda item: item**2 if item > 0 else 0, sp))

# print(*filter(lambda item: item > 0, sp))

for item in zip(sp2, sp):
    print(item)