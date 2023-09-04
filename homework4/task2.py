# задача 2 необязательная. Напишите программу, 
# которая получает целое число и возвращает его двоичное, 
# восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к 
# разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции

def invert_number(dec_number, format):
    result = ""

    while dec_number >= 1:
        result += str(dec_number % format)
        dec_number //= format
    
    return result[::-1]

OCT = 8
BIN = 2

number = int(input("Enter number >> "))
bin_number = invert_number(number, BIN)
oct_number = invert_number(number, OCT)

print(f"dec = {number}, bin = {bin_number}, oct = {oct_number}")