# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите 
# минимальное число монеток, которые 
# нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же 
# стороной. Выведите минимальное количество 
# монет, которые нужно перевернуть
import random

def fill_coins(length):
    coin_choice = ["О", "Р"]
    result = ""

    for i in range(length):
        result += random.choice(coin_choice)

    return result

def min_flips(coins):
    min_O = coins.count("О")
    min_P = coins.count("Р")

    return min(min_O, min_P)

number_coins = int(input("Введите количество монет >> "))
coins = fill_coins(number_coins)

print(f"""Если монетки лежат в порядке - {coins}, 
тогда необходимо минмальное количество поворотом - {min_flips(coins)}""")