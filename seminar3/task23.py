import random
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

arr = [random.randint(-10, 10) for _ in range(5)]
count = 0

print(arr)

for x in range(1, len(arr)):
    if arr[x] > arr[x - 1]:
        count += 1

print(count)