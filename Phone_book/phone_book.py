# Phone book application

# on initialise de dictionnaire
result = {}

while True:
    
    # on demande à l'utlisateur de faire un choix
    ask = input("command (1 search, 2 add, 3 quit):")

    # on faire la recherche
    if ask == "1":

        name = input("name:")
        
        if name not in result:
            print("no number")
        else:
            print(result[name])


    elif ask == "2":
        name = input("name:")
        number = input("number:")

        result[name] = number
        print("ok!")

    elif ask == "3":
        break


print("quitting...")
