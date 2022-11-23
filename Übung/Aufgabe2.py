# 2. Schreibt ein Programm, das Namen speichern und Ausgeben kann. 
# Die Namen sollen ganz simpel in einer Textdatei gespeichert werden. 
# Das Programm soll 2 Funktionalitäten haben: 
#   1. Zeige alle Namen und 
#   2. Füge Namen zur Textdatei hinzu. 
# Achtung: Doppelte Einträge sollen nicht eingetragen werden.

name_list = []

menu_text = """
(S)how All Names
(A)dd Name

"""

def add_name():
    read_names_from_file()
    new_name = input("Please enter the name you want to add: ")
    name_list.append(new_name)
    add_name_to_file(name_list)
    # if new_name == name_list:
    #     print("Name already exists")
    # else:
    #     name_list.append(new_name)
    #     add_name_to_file(name_list)


def add_name_to_file(new_name):
    
    name_file = open("name.txt", "w+")
    name_file.write(str(new_name))
    name_file.close()
    

def read_names_from_file():

    name_file = open("name.txt", "r+")
    name_list = name_file.read()
    name_file.close()
    return name_list

def show_names():

    name = read_names_from_file()
    print(f'''
    ##########

    {name}

    ##########''')

def menu():
    user_chioce = input("Please select an option: ").upper()
    
    if user_chioce == "S":
        show_names()
    elif user_chioce == "A":
        add_name()

################### main ################

while True:

    print(menu_text)
    menu()


