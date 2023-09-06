# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с 
# клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_sequence(first_elem, d, num):
    result = [first_element + (d * i) for i in range(num)]
    
    return result
    

first_element = int(input("Enter first element of sequence >> "))
step = int(input("Enter step >> "))
length = int(input("Enter length of sequence >> "))
numbers = arithmetic_sequence(first_element, step, length)

print(*numbers)