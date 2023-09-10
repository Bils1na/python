# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change_qual(min, max, n):
    if n < 0:
        return 
    if numbers[n] == max:
        numbers[n] = min
    change_qual(min, max, n - 1)


number = int(input("Enter number >> "))
numbers = [1, 3, 3, 3, 4]

change_qual(min(numbers), max(numbers), len(numbers) - 1)
print(numbers)