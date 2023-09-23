# Задача ДОП по желанию Сделать свой локальный чат-бот аналогично приложенной записи.
from random import *
import json



def save():
    with open("movies.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(movies, ensure_ascii=False))
    print("Movies succecful saved in movies.json")

def load(lst):
    with open("movies.json", "r", encoding="utf-8") as fh:
            lst = json.load(fh)
    return lst

movies = []
movies.append("Matrix")
movies.append("Solaris")
movies.append("Lord of the Rings")
movies.append("Texas Chainsaw Masacre")

while True:
    command = input("Enter command >> ")
    if command == "/start":
        print("Bot starts its work.")
    elif command == "/stop":
        print("Bot has stoped.")
        break
    elif command == "/all":
        print("This is current list of movies.")
        print(movies)
    elif command == "/add":
        t = input("Enter name of movie >> ")
        movies.append(t)
        print("Movie has added in list.")
    elif command == "/help":
        print("Here is something guide.")
    elif command == "/delete":
        t = input("Enter name of movie >> ")
        # if t in movies:
        #     movies.remove(t)
        #     print("Movie has deleted from list.")
        # else:
        #     print("This movie is not in this list.")
        try:
            movies.remove(t)
            print("Movie has deleted from list.")
        except:
            print("This movie is not in this list.")
    elif command == "/random":
        # rnd = randint(0, len(movies) - 1)
        print(f"Random movie in your list => {choice(movies)}")
    elif command == "/save":
        save()
    elif command == "/load":
        movies = load(movies)
        print("Movies has succesful loaded.")
    else:
        print("Unknown command. You can recieve help by command /help.")