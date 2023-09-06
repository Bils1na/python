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

def game_output(r1, r2, r3):
    print(" | ".join(r1))
    print(" | ".join(r2))
    print(" | ".join(r3))

def player_turn(r1, r2, r3, char):
    while True:
        turn = list(input("Your turn, enter number of row and column >> ").split())

        if int(turn[0]) == 1:
            if r1[int(turn[1]) - 1] == " ":
                r1[int(turn[1]) - 1] = char
                return r1
            
        if int(turn[0]) == 2:
            if r2[int(turn[1]) - 1] == " ":
                r2[int(turn[1]) - 1] = char
                return r2
            
        if int(turn[0]) == 3:
            if r3[int(turn[1]) - 1] == " ":
                r3[int(turn[1]) - 1] = char
                return r3

def bot_turn(r1, r2, r3, char):
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
        
        if turn[0] == 2:
            if r2[int(turn[1]) - 1] == " ":
                r2[int(turn[1]) - 1] = char
                return r2
            
        if turn[0] == 3:
            if r3[int(turn[1]) - 1] == " ":
                r3[int(turn[1]) - 1] = char
                return r3
                
def check_endgame(r1, r2, r3, flag):
    # draw    
    if " " not in r1 and " " not in r2 and " " not in r3:
        flag = 2

    # row
    if (r1[0] == r1[1] and r1[1] == r1[2]) and " " not in r1:
        flag = 1  
    if (r2[0] == r2[1] and r2[1] == r2[2]) and " " not in r2:
        flag = 1
    if (r3[0] == r3[1] and r3[1] == r3[2]) and " " not in r3:
        flag = 1
        
    # column
    if (r1[0] == r3[0] and r2[0] == r3[0]) and " " not in r3[0]:
        flag = 1
    if (r1[1] == r3[1] and r2[1] == r3[1]) and " " not in r3[1]:
        flag = 1 
    if (r1[2] == r3[2] and r2[2] == r3[2]) and " " not in r3[2]:
        flag = 1
        
    # diagonal
    if (r1[0] == r3[2] and r2[1] == r3[2]) and " " not in r3[2]:
        flag = 1   
    if (r1[2] == r3[0] and r2[1] == r3[0]) and " " not in r3[0]:
        flag = 1
     
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
        round = 0
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
        round = 1
        print("")