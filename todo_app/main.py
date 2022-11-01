# todo_app
'''Entwickle eine App, mit der man ToDos verwalten kann. Die App soll über die Konsole verwendet werden können. 

Die App soll folgende Funktionen beinhalten (Akzeptanzkriterien):
    Datenbankverbindung zu einer sqlite Datenbank
    Verwendung von sqlalchemy
    Nutzereingabe: Hinzufügen einer neuen ToDo
    Nutzereingabe: Löschen einer ToDo
    Nutzereingabe: Erledigen einer ToDo
    Wenn eine ToDo "erledigt" ist, soll die ToDo auf "erledigt" gesetzt werden (boolean)
    Die ToDos können ein "zu Erledigen" Datum haben
    Nutzereingabe: Zeige die ToDos, die heute erledigt werden müssen
    Nutzereingabe: Auflisten der ToDos, die noch zu erledigen sind


Wie sehen ToDo Apps aus? Hier seht ihr ein Beispiel einer App mit graphischer Oberfläche: https://todomvc.com/examples/typescript-angular/#/.
'''

# imports

#from asyncio import constants
#from ctypes.wintypes import BOOL
#from email.policy import default
#from msilib.schema import Class
#from xmlrpc.client import Boolean
from rich.console import Console
from rich.table import Table

from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Date
from datetime import date
import datetime
#from sqlalchemy.types import Boolean, Date, DateTime, Float, Integer, Text, Time, Interval


# # # ######################################################
# # Do not touch!
# # Database Connection stuff!
# Erzeugen einer neuen Datenbank Engine
database = create_engine("sqlite:///todo.db")
# Basisklasse für Klassen
Base = declarative_base()

# Öffne Verbindung zur Datenbank
Session = sessionmaker(bind=database)
# Offene Verbindung zur Datenbank
session = Session()

# Rich Initialization
console = Console()
# # # ######################################################

class Task(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    task = Column(String)
    due_to = Column(Date)
    status = Column(Boolean, unique=False, default=False)



def initialize_database():
    """
    Initializes the database and creates all tables.
    See more here: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """
    Base.metadata.create_all(database)


# # # ###########################################
# # # Menu
# # # ###########################################
def show_menu():
    """
    Displays a menu.
    """

    MENU_TEXT = """
    Menu:
    - (F)ull list of tasks 
    - (T)odays tasks
    - (N)ot yet Done Tasks
    - (A)dd new task
    - (C)check off task
    - (D)elete task
    - (E)xit
    """
    print(MENU_TEXT)


def get_users_menu_input():
    menu_choice = input("Choose menu option: ").upper()

    if menu_choice == "T":
        list_todays_tasks()
    elif menu_choice == "F":
        list_all_tasks()
    elif menu_choice == "N":
        list_not_yet_done_tasks()
    elif menu_choice == "A":
        add_new_task()
    elif menu_choice == "C":
        check_off_task()
    elif menu_choice == "D":
        delete_task()    
    elif menu_choice == "E":
        console.print(f"Bye!", style="bold red")
        exit(1)


############################################################
### users choice ###
############################################################

def add_new_task():
    """
    Asks the user for the information about the new task. 
    Adds the task to the database.
    """
    print("Add a new task")
    input_task = input("Task?\t:")
    print("Due to?")
    input_due_to_year = input("Year?\t:")
    input_due_to_month = input("Month?\t:")
    input_due_to_day = input("Day?\t:")
    input_due_to = datetime.datetime(int(input_due_to_year), int(input_due_to_month), int(input_due_to_day))
    input_status = False
    new_task = Task(task=input_task, due_to=input_due_to, status=input_status)
    database_add_task(new_task)

def list_todays_tasks():
    tasks = database_todays_tasks()
    table = Table(show_header=True, header_style="bold green")
    table.add_column("ID", style="dim")
    table.add_column("To do")
    table.add_column("Due to")
    table.add_column("Done?")
    
    for task in tasks:
        table.add_row(str(task.id), task.task, str(task.due_to), str(task.status))

    console.print(table)

def list_not_yet_done_tasks():
    tasks = database_not_yet_done_tasks()
    table = Table(show_header=True, header_style="bold green")
    table.add_column("ID", style="dim")
    table.add_column("To do")
    table.add_column("Due to")
    table.add_column("Done?")
    
    for task in tasks:
        table.add_row(str(task.id), task.task, str(task.due_to), str(task.status))

    console.print(table)

def list_all_tasks():
    tasks = database_get_all_tasks()
    table = Table(show_header=True, header_style="bold green")
    table.add_column("ID", style="dim")
    table.add_column("To do")
    table.add_column("Due to")
    table.add_column("Done?")
    
    for task in tasks:
        table.add_row(str(task.id), task.task, str(task.due_to), str(task.status))

    console.print(table)

def check_off_task():
    task_id = int(input("Please enter the ID of the task: "))
    task = database_get_one_task(task_id)
    task_fields = {}
    task_fields["status"] = True

    console.print(f"Update Task {task.task} {task.due_to} {task.status}.", style="green")
    database_update_task(task, task_fields)    


def delete_task():    
    task_id = int(input("Please enter the ID of your task: "))
    task = database_get_one_task(task_id)
    console.print(f"Delete task {task.task} {task.due_to} {task.status}.", style="red")
    database_delete_task(task)

# # # ###########################################
# # # Database
# # # ###########################################
def database_add_task(task: Task):
    """
    Database command to add a new task.
    """
    session.add(task)
    session.commit()


def database_get_one_task(task_id: int):
    """
    Database command to get one friend by ID.
    """
    return session.query(Task).get(task_id)


def database_get_all_tasks():
    """
    Database command to get all tasks.
    `all_friends = session.query(Friend).all()` is a query call made with the sqlalchemy ORM. 
    The SQL query that is made is: `SELECT * FROM friends;`
    Alternative to this with raw sql:
    `all_friends_raw = session.execute("SELECT * FROM friends;").fetchall()`
    """
    return session.query(Task).all()

def database_todays_tasks():
    
    return session.query(Task).filter(Task.due_to == date.today()).all()

def database_not_yet_done_tasks():

    return session.query(Task).filter(Task.status == False).all()

def database_delete_task(task: Task):
    """
    Database command to delete a new friend.
    """
    session.delete(task)
    session.commit()


def database_update_task(task: Task, fields: dict):
    """
    Database command to update a friend.
    https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.update
    """
    session.query(Task).filter(Task.id == task.id).update(fields)
    session.commit()



############################################################
### main ### main ### main ###
############################################################
if __name__ == "__main__":
    initialize_database()

    while True:
        show_menu()
        get_users_menu_input()
