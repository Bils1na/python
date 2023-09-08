from random import randint
# Задача FOOTBALL необязательная
# Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех команд.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Пример входа:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Выход будет:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

def fill_list_matches(num):
    teams = ["Спартак", "Зенит", "Локомотив", "ЦСКА", "Краснодар", "Динамо", "Уфа", "Торпедо", "Сатурн"]
    result = []
    
    for i in range(num):
        team_a = teams.pop(randint(0, len(teams)-1))
        team_b = teams.pop(randint(0, len(teams)-1))
        result.append(f"{team_a};{randint(0, 5)};{team_b};{randint(0, 5)}")    
        teams.append(team_a)
        teams.append(team_b)
        
    return result

def output_table(matches):
    text = [i.split(";") for i in matches]
    table = {}
    
    for i in text:
        for j in i:
            if not j.isdecimal():
                table[j] = table.get(j, [0, 0, 0, 0, 0])
                table[j][0] += 1
             
        if i[1] > i[3]:
            table[i[0]][1] += 1
            table[i[2]][3] += 1
        elif i[1] < i[3]: 
            table[i[2]][1] += 1
            table[i[0]][3] += 1
        else:
            table[i[0]][2] += 1
            table[i[2]][2] += 1
            
    for k, v in table.items():
        v[4] = v[1] * 3 + v[2] * 1
        print(f"{k}: {v[0]} {v[1]} {v[2]} {v[3]} {v[4]}")


number = int(input("Enter number >> "))
list_matches = fill_list_matches(number)

for i in list_matches:
    print(*i.split(";"))
print("")
output_table(list_matches)
