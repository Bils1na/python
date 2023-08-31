import random
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

arr = [random.randint(-10, 10) for _ in range(5)]
k = 3

print(arr)

for i in range(len(arr) - k):
    t = arr.pop()
    arr.insert(0, t)

print(arr)
