from random import randint
# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

def fill_list(num):
    result = [randint(-10, 200) for i in range(num)]
    
    return result
    
def define_indexes(nums, num_a, num_b):
    result = []
    
    for i in range(len(nums)):
        if nums[i] > num_a and nums[i] < num_b:
            result.append(i)
            
    return result


number = int(input("Enter number of elements >> "))
number_a = int(input("Enter first number >> "))
number_b = int(input("Enter second number >> "))
numbers = fill_list(number)

print(numbers)
print(define_indexes(numbers, number_a, number_b))