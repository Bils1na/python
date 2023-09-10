from random import randint
# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                             Вывод:
# 7                                 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1                    (каждое число вводится с новой строки)


number_a = int(input("Enter first number >> "))
number_b = int(input("Enter second number >> "))
numbers_a = [randint(1, 12) for _ in range(number_a)]
numbers_b = [randint(1, 12) for _ in range(number_b)]
print(f"First list - {numbers_a}, second list - {numbers_b}")
print([x for x in numbers_a if x not in set(numbers_b)])