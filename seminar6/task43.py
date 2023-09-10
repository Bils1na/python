from random import randint
# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:               Вывод:
# 1 2 3 2 3           2

def find_pairs(nums):
    result = [nums.count(i)//2 for i in range(len(nums)) if nums.count(i) > 1]

    return sum(result)

print(numbers:= [randint(1, 6) for _ in range(8)])
print(find_pairs(numbers))