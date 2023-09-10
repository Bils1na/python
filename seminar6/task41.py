from random import randint
# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:          Ввод:
# 5              5
# 1 2 3 4 5      1 5 1 5 1
# Вывод:         Вывод:
# 1              2
# (каждое число вводится с новой строки)

number = int(input("Enter number >> "))
numbers = [randint(1, 10) for x in range(number)] 

print(numbers)
# print(sum([1 for x in range(-1, number-1) if numbers[x] > numbers[x-1] and numbers[x] > numbers[x+1]]))
print(len([x for x in range(-1, number-1) if numbers[x-1] < numbers[x] > numbers[x+1]]))