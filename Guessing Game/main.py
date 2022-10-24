# Guessing Game
#
# In diesem Spiel gibt es eine geheime Zahl. Der Spieler muss diese Zahl in mehreren Schritten erraten.
# Um dem Ziel näher zu kommen, wird dem Spieler der Heinweis gegeben, ob sein Tip zu hoch oder zu niedrig war.
# Wenn der Spieler die geheime Zahl erraten hat, wird der Spieler gebührend gefeiert.

import random
import json
import os #für filesize check

from datetime import datetime
from helper import ensure_integer


# Constants
HELP_TEXT_GUESS_TO_HIGH = "Dein Tip ist leider zu hoch."
HELP_TEXT_GUESS_TO_LOW = "Dein Tip ist leider zu niedrig."
HELP_TEXT_WIN = "🎉 🎉 🎉 Gewonnen! 🎉 🎉 🎉"
HELP_TEXT_INTRO = """

# Begrüßungstext
print("")
print("Hallo Nutzer, wilkommen beim Guessing Game!")
print("Finde die geheime Zahl!")
print("Wenn du falsch liegst, bekommt du einen Tipp ob die Zahl höher oder niedriger ist.")
print("Aber Achtung, ich zähle mit wie viele Versuche du brauchst.")
print("Viel Glück!")

"""


# Variables
highscore_list = []
continue_playing = True


# Classes
class User:
    name = str
    highscore: int = 0

    def set_highscore(self, counter):
        if not self.highscore or counter < self.highscore:
            self.highscore = counter


# Functions
def old_highscore():
    #Falls noch nichts in der Json datei steht wirft json.load ein fehler
    #Deshalb davor schauen ob die Datei leer ist (Zeichen == 0)
    if(os.stat("highscore.json").st_size == 0):
        print("no previous highscores")
    else:
        with open('highscore.json', "r") as f:
            loadedScores = json.load(f)
            sortedScores = sorted(loadedScores, key=lambda k: k["count_guesses"])
            sortedScores = sortedScores[:5]     # Highscore auf die Top 5 begrenzen.
            print("\nDie aktuellen Highscores sind:\n")
            #Als Text printen
            #print(json.dumps(loadedScores)
            for score in sortedScores:
                print(str(score["name"]) + "\t\t" + str(score["count_guesses"]) + " Versuche \t\tDatum: " + str(score["time"]))


def save_new_highscore(user: User):
    """
    Saves a new highscore into our highscore list.
    """
    #Falls es noch nichts gibt -> Neues Objekt in array anlegen (damit wir appenden können wenn neue dazukommen)
    if(os.stat("highscore.json").st_size == 0):
        new_highscore = [{"count_guesses": user.highscore, "name": user.name, "time": datetime.now()}]
    else:
        with open('highscore.json', "r") as f:
            new_highscore = json.load(f)
        new_highscore.append({"count_guesses": user.highscore, "name": user.name, "time": datetime.now()})

    #highscore_list.append(new_highscore)
    #with open("highscore.txt", "a") as text_file:
    #    text_file.write(str(new_highscore) + "\n")
    with open("highscore.json", "w") as f: #w zum überschreiben, a zum appenden
        json.dump(new_highscore, f, default = str)
        

def ask_for_replay(user: User):
    """
    This function asks the user whether he/she wants to play again.
    """
    restart_game = input("Nochmal? j/n: ")
    if restart_game == "j":
        return True
    else:
        print("K, Bye!")
        save_new_highscore(user)
        return False


def display_welcome_message():
    """
    Displays a nice welcome message to user.
    """
    print(HELP_TEXT_INTRO)
    old_highscore()



def play(user: User):
    """
    Play the Game!
    """  
    SECRET_NUMBER = random.randint(1, 30)
    #SECRET_NUMBER = 5
    counter = 0

    while True:
        users_guess = ensure_integer(input("Bitte Zahl eingeben: "))
        counter += 1

        if users_guess == False:
            print("Das ist keine Zahl.")
            continue
        elif users_guess == SECRET_NUMBER:
            print(HELP_TEXT_WIN)
            user.set_highscore(counter)
            print(f"Dein aktuell bester Score: {user.highscore}")
            break
        elif users_guess < SECRET_NUMBER:
            print(HELP_TEXT_GUESS_TO_LOW)
        elif users_guess > SECRET_NUMBER:
            print(HELP_TEXT_GUESS_TO_HIGH)


# ###############################################
# # # Main
# ###############################################
if __name__ == "__main__": 
    display_welcome_message()


    print("\n====== Here comes a new challenger! ======\n")
    user = User()
    user.name = input("Bitte gib deinen Namen ein: ")
    print("")

    while continue_playing:
        play(user)

        if not ask_for_replay(user):
            break

print("==========================================================")
print(f"{user.name} deine beste Runde war {user.highscore} Versuche.")
old_highscore()