# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.

number = int(input("Enter number >> "))
i = 0

while i < number:
    if 2 ** i < number:
        print(2 ** i)   
        i += 1
    else:
        break