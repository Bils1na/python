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
            
        # horizontal
        if r1[0] == r1[1] and r1[2] == " " and r1[0] != " ":
            r1[2] = "O"
            return r1
        if r1[0] == r1[2] and r1[1] == " " and r1[0] != " ":
            r1[1] = "O"
            return r1
        if r1[1] == r1[2] and r1[0] == " " and r1[1] != " ":
            r1[0] = "O"
            return r1
        
        if r2[0] == r2[1] and r2[2] == " " and r2[0] != " ":
            r2[2] = "O"
            return r2
        if r2[0] == r2[2] and r2[1] == " " and r2[0] != " ":
            r2[1] = "O"
            return r2
        if r2[1] == r2[2] and r2[0] == " " and r2[1] != " ":
            r2[0] = "O"
            return r2
        
        if r3[0] == r3[1] and r3[2] == " " and r3[0] != " ":
            r3[2] = "O"
            return r3
        if r3[0] == r3[2] and r3[1] == " " and r3[0] != " ":
            r3[1] = "O"
            return r3
        if r3[1] == r3[2] and r3[0] == " " and r3[1] != " ":
            r3[0] = "O"
            return r3

        # vertical
        if r1[0] == r3[0] and r2[0] == " " and r1[0] != " ":
            r2[0] = "O"
            return r2
        if r1[0] == r2[0] and r3[0] == " " and r1[0] != " ":
            r3[0] = "O"
            return r3
        if r2[0] == r3[0] and r1[0] == " " and r2[0] != " ":
            r1[0] = "O"
            return r1
        
        if r1[1] == r3[1] and r2[1] == " " and r1[1] != " ":
            r2[1] = "O"
            return r2
        if r1[1] == r2[1] and r3[1] == " " and r1[1] != " ":
            r3[1] = "O"
            return r3
        if r2[1] == r3[1] and r1[1] == " " and r2[1] != " ":
            r1[1] = "O"
            return r1
        
        if r1[2] == r3[2] and r2[2] == " " and r1[2] != " ":
            r2[2] = "O"
            return r2
        if r1[2] == r2[2] and r3[2] == " " and r1[2] != " ":
            r3[2] = "O"
            return r3
        if r2[2] == r3[2] and r1[2] == " " and r2[2] != " ":
            r1[2] = "O"
            return r1
        
        # diagonal
        if r1[0] == r2[1] and r3[2] == " " and r1[0] != " ":
            r3[2] = "O"
            return r3
        if r1[0] == r3[2] and r2[1] == " " and r1[0] != " ":
            r2[1] = "O"
            return r2
        if r2[1] == r3[2] and r1[0] == " " and r2[1] != " ":
            r1[0] = "O"
            return r1

        if r1[2] == r2[1] and r3[0] == " " and r1[2] != " ":
            r3[0] = "O"
            return r3
        if r1[2] == r3[0] and r2[1] == " " and r1[2] != " ":
            r2[1] = "O"
            return r2
        if r2[1] == r3[0] and r1[2] == " " and r2[1] != " ":
            r1[2] = "O"
            return r1

        # random slot
        if turn[0] == 1:
            if r1[int(turn[1]) - 1] == " ":
                r1[int(turn[1]) - 1] = char
                return r1
        
        if field[int(turn[0])-1][int(turn[1])-1] == " ":
            return draw_field(turn, r, c, field, char)              

def check_endgame(field, flag):
    # draw
    if " " not in field[0] and " " not in field[1] and " " not in field[2]:
        flag = 2
        
    # win    
    count = 2
    for i in range(len(field)):
        if field[i][0] == field[i][1] and field[i][1] == field[i][2] and " " not in field[i]:
            flag = 1
        if field[0][i] == field[2][i] and field[1][i] == field[2][i] and " " not in field[2][i]:
            flag = 1
        if field[1][1] == field[0][count] and field[1][1] == field[2][i] and " " not in field[1][1]:
            flag = 1
        count -= 1
     
    return flag


PLAYER = "X"
BOT = "O"

game = 0
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
round = int(input("Choose who goes first (1 - you, 0 - bot) >> "))

while True:
    # player
    if round == 1:
        player_turn(row1, row2, row3, PLAYER)
        game_output(row1, row2, row3)
        game = check_endgame(row1, row2, row3, game)
        if game == 1:
            print("Player has won! Congratulations!")
            break
        if game == 2:
            print("Game over!")
            break
        start = 0
        print("")
    
    # bot
    if round == 0:
        bot_turn(row1, row2, row3, BOT)
        game_output(row1, row2, row3)
        game = check_endgame(row1, row2, row3, game)
        if game == 1:
            print("Bot has won! You suck!")
            break
        if game == 2:
            print("Game over!")
            break
        start = 1
        print("")
