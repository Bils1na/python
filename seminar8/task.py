# import sqlite3 as sq
import json

# con_name = sq.connect("names.db")
# cur_name = con_name.cursor()
# cur_name.execute("""
#                  """)

phonebook = {"Uncle Vanya": {"phones": ["+78002553535", "+78772562534"], "city": "Moscow", "status": "dead"}}

while True:
    command = input("Enter command >> ")

    if command == "/all": # Output list of numbers
        print("Here is current list of numbers\n")
        for k, v in phonebook.items():
            print(f"{k}: ")
            for k1, v1 in v.items():
                print(f"\t\t{k1}: {v1}")

    elif command == "/add": # Added a new contact
        name = input("Enter the name of the new contact >> ")
        if name in phonebook:
            print("This contact already exists")
        else:
            phones = []
            while True:
                num = input("Enter number >> ")
                if num == "quit":
                    break
                phones.append(num)
            city = input("Enter city of contact >> ")
            status = input("Enter status >> ")
            phonebook[name]= {"phones": phones, 
                              "city": city, 
                              "status": status,
                              }
        print("Number has succesful added into list")

    elif command == "/number": # i don't know
        name = input("Enter name of contact >> ")
        if name not in phonebook:
            print("This contact does not exist")
        else:
            phone = input("Enter number >> ")
            if phone in phonebook[name]['phones']:
                print("Number exists")
            else:
                phonebook[name]["phones"].append(phone)

    elif command == "/help": # guide
        print("There is something guide here")