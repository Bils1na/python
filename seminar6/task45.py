# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:             Вывод:
# 300               220 284

# def find_friendly_numbers(num):
#     result = []
    
#     for i in range(1, num+1):
#         nums_a = [x for x in range(1, i) if i / x % 1 == 0]
#         for j in range(i, num+1): 
#             nums_b = [x for x in range(1, j) if j / x % 1 == 0]

#             if sum(nums_a) == j and sum(nums_b) == i and i != j:
#                 result.append(i)
#                 result.append(j)

#     return result

def diff_num(num):
    return sum([i for i in range(1, num) if num % i == 0])

number = int(input("Enter number >> "))
res = [(diff_num(m), m) for m in range(number) if diff_num(diff_num(m)) == m and diff_num(m) > m]
# friendly_numbers = find_friendly_numbers(number)
# print(*friendly_numbers)
# for m in range(number):
#     n = diff_num(m)
#     if diff_num(n) == m and n > m:
#         res.append((n, m))
print(res)


