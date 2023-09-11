from random import choice 
from time import sleep

def choose_card(lst):
    card = lst.pop(lst.index(choice(lst)))
    return card

def check_score(score_a, score_b):
    return "Player has won!" if abs(score_a - BLACKJACK) < abs(score_b - BLACKJACK) else "Bot has won!"
    

BLACKJACK = 21

deck = [i for i in range(1, 11) for j in range(4) if i != 5]
player_score = 0
bot_score = 0

start = int(input("Do you want to play BlackJack? (1 - yes, 0 - no) >> "))
while True:
    
    if start == 1: # player
        player_score += choose_card(deck)
        if player_score == BLACKJACK:
            print("Player has won!")
            break
        print(f"Your score is {player_score}")
        turn = int(input("Do you want to take one more card?(1 - yes, 0 - no) >> "))
        if turn == 0:
            print(f"Your score is {player_score}\n")
            start = 2
        
    elif start == 2: # bot
        bot_score += choose_card(deck)
        print(f"Bot takes card, it score is {bot_score}")
        sleep(1)
        if bot_score + choose_card(deck) > BLACKJACK:
            print(check_score(player_score, bot_score))
            break

    else: # exit
        break
    
