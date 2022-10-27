from rich.console import Console
from rich.table import Table

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import delete
from sqlalchemy import update



# # # ###########################################
# # Do not touch!
# # Database Connection stuff!
# Erzeugen einer neuen Datenbank Engine
database = create_engine("sqlite:///friendbook.db")
# Basisklasse für Klassen
Base = declarative_base()

# Öffne Verbindung zur Datenbank
Session = sessionmaker(bind=database)
# Offene Verbindung zur Datenbank
session = Session()

# Rich Initialization
console = Console()
# # # ###########################################

# classes -----------------------------------------------

class Friend(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    # Foreignkeys
    color_id = Column(Integer, ForeignKey("favorite_color.id"))


class FavoriteColor(Base):
    __tablename__ = "favorite_color"

    id = Column(Integer, primary_key=True)
    color = Column(String)


class Hobbies(Base):
    __tablename__ = "hobbies"

    id = Column(Integer, primary_key=True)
    hobby = Column(String)


class Friends_has_hobbies(Base):
    __tablename__ = "friends_has_hobbies"

    id = Column(Integer, primary_key=True)
    friends_id = Column(Integer, ForeignKey("friends.id"))
    hobbies_id = Column(Integer, ForeignKey("hobbies.id"))


class Music(Base):
    __tablename__ = "music"

    id = Column(Integer, primary_key = True)
    music = Column(String)


class Friends_has_music(Base):
    __tablename__ = "friends_has_music"

    id = Column(Integer, primary_key=True)
    friends_id = Column(Integer, ForeignKey("friends.id"))
    music_id = Column(Integer, ForeignKey("music.id"))    

'''
class Friends_has_firends(Base):
    _tablename_ = "friends_has_friends"

    id = Column(Integer, primary_key=True)
    friends_id = Column(Integer, ForeignKey("friends.id"))
    friends_id2 = Column(Integer, ForeignKey("friends.id"))
'''

# functions ------------------------------
MENU_TEXT = """

(A)dd new friend
(U)pdate friend
(D)elete friend
(L)ist all friends
(E)xit

"""


def initialize_database():
    """
    Initializes the database and creates all tables.

    See more here: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """
    Base.metadata.create_all(database)




def get_users_menu_input():
    menu_choice = input("Choose Menu Option: ").upper()

    if menu_choice == "A":
        add_new_friend()
     elif menu_choice == "U":
         update_friend()
    elif menu_choice == "D":
        delete_friend()
    elif menu_choice == "L":
        list_all_friends()
    elif menu_choice == "E":
        exit(1)


def list_all_friends():
    friends = database_get_all_friends()
    table = Table(show_header=True, header_style="bold green")
    table.add_column("ID", style="dim")
    table.add_column("First Name")
    table.add_column("Last Name")
    
    for friend in friends:
        table.add_row(str(friend.id), friend.first_name, friend.last_name)

    console.print(table)


def database_add_friend(friend: Friend):
    """
    Database command to add a new friend.
    """
    session.add(friend)
    session.commit()


def database_get_all_friends():
    """
    Database command to get all friends.
    """
   # all_friends = session.query(Friend).all()
   # all_friends = session.execute("SELECT * FROM friends;").fetchall()
   # wer_ist_jascha = session.execute("SELECT * From friends WHERE first_name = Jascha").fetchall()
    
    # print("")
    # print("First Name\tLast Name\tEmail")
    # print("")
    # for friend in all_friends:
    #     print(f"{friend.first_name}\t\t{friend.last_name}\t\t{friend.email}")
    return session.query(Friend).all()

def add_new_friend():
    """
    add a new friend
    """
    input_first_name = input("Please enter first Name: ")
    input_last_name = input("Please enter last Name: ")
    input_email = input("Please enter email: ")

    new_friend = Friend(email=input_email, first_name=input_first_name, last_name=input_last_name)
    database_add_friend(new_friend)


# def delete_friend():
#     friends = database_get_all_friends()
#     delete_id = input("Please enter the ID of the person you want to delete: ")
#     delete_id = int(delete_id)

#     deleted = delete(friends).where(friends.c.id == delete_id)
    
    
# def update_friend():
#     friends = database_get_all_friends()
#     update_id = input("Which ID do you want to update?: ")
#     update_what = input("What do you want to update? (first name / last name / email)")
#     old_value = input("Alte eingabe ")

#     if update_what == "first name":
#         stmt = (
#             update(friends)
#            .where(friends.c.first_name == "patrick")
#            .values(fullname="Patrick the Star")
#         )
#     print(stmt)
    
    



# # # ###########################################
# # # Main
# # # ###########################################
if __name__ == "__main__":
    initialize_database()

   
    # while True:
    #     ask_add_friend = input("add friend? y/n ")

    #     if  ask_add_friend == "y":
    #         add_new_friend()
    #     else:
    #         database_get_all_friends()
    #         exit(1)

    while True:

        print(MENU_TEXT)
        get_users_menu_input()


    # Example to list all friends
    