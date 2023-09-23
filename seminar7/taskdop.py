# Необходимо напистаь программу для автоматического перевода различных валютных счетов в рублевые.
# Начальные данные программы это три рахличных списка - Фамилии владельцев счетов, указание валюты, 
# состояние счетов. Т.е. у Иголкина счет в евро и там лежит 50000, и так далее.
# Также вначале заданы отношения курса рубля к доллару и евро.

# surnames = []
# currency_name = []
# balances = [30000, 40000, 50000]
# dollar = 90
# euro = 99

# Вам необходимо написать функцию calc, которая на входе принимает только один аргумент, далее надо применить ее в комбинациях с map и zip
# На выходе программы должны быть три пары значений - фамилии владельцев счетов и состояние рублевого счета

def calc(people_money):
    # res = list(map(lambda x: (x[0], x[2]*dollar) if x[1] == "dollar" else (x[0], x[2]), people_money))
    res = people_money[1]
    if people_money[0] == "dollar":
        res *= dollar
    elif people_money[0] == "euro":
        res *= euro
    return res


surnames = ["Ivanov", "Karpov", "Igolkin"]
currency_name = ["ruble", "dollar", "euro"]
balances = [30000, 40000, 50000]
dollar = 90
euro = 99

# people_money = list(zip(currency_name, balances))
new_balances = list(map(calc, zip(currency_name, balances)))
# print(people_money)
# print(calc(people_money))
print(*zip(surnames, new_balances))