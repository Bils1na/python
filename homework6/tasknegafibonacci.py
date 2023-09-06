# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

def negafibonacci(num):
    num1 = 0
    num2 = 1
    num3 = num1 + num2
    result = [-num3, -num2, num1, num2, num3]
    
    if num == 0:
        result = [num1]
        return result
    
    if num == 1:
        result = [-num2, num1, num2]
        return result
    
    for i in range(2, num):
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        
        result.append(num3)
        result.insert(0, -num3)
        
    return result


number = int(input("Enter number >> "))
print(negafibonacci(number))