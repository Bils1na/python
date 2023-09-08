# def calc1(a, b):
#     return a+b

# def calc2(a, b):
#     return a*b

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a + b, 5, 45)

# Task 1

# def even_square(func, nums):
#     return [func(x) for x in nums]

# def where(func, nums):
#     return [x for x in nums if func(x)]

# numbers = [1, 2, 3, 5, 8, 15, 23, 38]

# # result = [(i, i**2) for i in numbers if i % 2 == 0]
# # print(result)

# res = even_square(int, numbers)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(even_square(lambda x: (x, x**2), res))
# print(res)

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# data = '14 12 53 65 12 23'
# print(data)

# data = list(map(int, data.split()))
# print(data)

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# colors = ['red', '3161367', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# with open('file.txt', 'w') as data:
#     data.write("line 1\n")
#     data.write("line 2\n")

path = "file.txt"
data = open("file.txt", "r")
for line in data:
    print(line)
data.close()
