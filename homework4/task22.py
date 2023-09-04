from random import randint
# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в 
# порядке возрастания все те числа, которые встречаются в обоих наборах.
# # Пользователь вводит 2 числа. n — кол-во элементов первого 
# множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

def fill_list(length):
    result = [randint(1, 9) for i in range(length)]

    return result


length_a = int(input("Enter length 1 >> "))
length_b = int(input("Enter length 2 >> "))
numbers_a, numbers_b = fill_list(length_a), fill_list(length_b)
result_list = numbers_a + numbers_b

print(f"First list - {numbers_a}, second list - {numbers_b}")
print(f"Result - {set(result_list)}")