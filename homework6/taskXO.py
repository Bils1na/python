from random import randint
# Задача XO необязательная.
# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он 
# ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# Например,
# |     |  Х | 
# |     |  O |
# |     |  O |
# При ходе пользователя у надо спрашивать номер строки и столбца, 
# куда он хочет сделать ход

def create_field(r, c):
    for i in range(r):
        game_field.append([" "] * c)
        
def draw_field(coor, r, c, field, char):
    for i in range(r):
        if i == int(coor[0]) - 1:
            for j in range(c):
                if j == int(coor[1]) - 1:
                    field[i][j] = char
                    
    for i in field:
        print(f"{i[0]}|{i[1]}|{i[2]}")

def player_turn(r, c, field, char):
    while True:
        turn = list(input("Your turn, enter number of row and column >> ").split())
        
        if field[int(turn[0])-1][int(turn[1])-1] == " ":
            return draw_field(turn, r, c, field, char)

def bot_turn(r, c, field, char):
    print("Bot turn...")
    while True:
        turn = [randint(1, 3) for i in range(2)]

        for i in range(len(field)): # check win
            for j in range(len(field[i])):
                if field[i][j] == " ":
                    field[i][j] = char 
                    if check_endgame(field, GAME) == 1:
                        field[i][j] = " "
                        if field[i][j] == " ":
                            return draw_field([i+1, j+1], r, c, field, char)
                    else:
                        field[i][j] = " "

        for i in range(len(field)): # check lose
            for j in range(len(field[i])):
                if field[i][j] == " ":
                    field[i][j] = PLAYER
                    if check_endgame(field, GAME) == 1:
                        field[i][j] = " "
                        if field[i][j] == " ":
                            return draw_field([i+1, j+1], r, c, field, char)
                    else:
                        field[i][j] = " "

        if field[int(turn[0])-1][int(turn[1])-1] == " ": # random slot
            return draw_field(turn, r, c, field, char)          

def check_endgame(field, flag):
    if " " not in field[0] and " " not in field[1] and " " not in field[2]: # draw
        flag = 2
         
    for i in range(len(field)): # win
        if field[i][0] == field[i][1] and field[i][1] == field[i][2] and " " not in field[i]: # horizontal
            flag = 1
        if field[0][i] == field[2][i] and field[1][i] == field[2][i] and " " not in field[2][i]: # vertical
            flag = 1
        if field[1][1] == field[0][2 - i] and field[1][1] == field[2][i] and " " not in field[1][1]: # diagonal
            flag = 1  

    return flag


PLAYER = "X"
BOT = "O"
GAME = 0

rows = 3
columns = 3
game_field = []
create_field(rows, columns)
start = int(input("Choose who goes first (1 - you, 0 - bot) >> "))

if start == 0:
    PLAYER = "O"
    BOT = "X"

while True:
    if start == 1: # player
        player_turn(rows, columns, game_field, PLAYER)
        GAME = check_endgame(game_field, GAME)
        if GAME == 1:
            print("Player has won! Congratulations!")
            break
        if GAME == 2:
            print("Game over!")
            break
        start = 0
        print("")
    
    if start == 0: # bot
        bot_turn(rows, columns, game_field, BOT)
        GAME = check_endgame(game_field, GAME)
        if GAME == 1:
            print("Bot has won! You suck!")
            break
        if GAME == 2:
            print("Game over!")
            break
        start = 1
        print("")