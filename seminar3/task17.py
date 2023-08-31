# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
import random


arr = [random.randint(-10, 10) for _ in range(10)]

print(arr)
print(len(set(arr)))