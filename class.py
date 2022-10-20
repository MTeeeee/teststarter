from operator import truediv
from pickle import PicklingError
from xmlrpc.client import boolean


class Papierkorb:
    farbe: str = "pink"
    form: str = "Zylinder"
    leer: bool = True
    maximal_voll: bool = False
    fuellstand: int = 0
    max_fuellstand: int = 100
    fremdkoerper: int = 0 
    umgedreht: bool = False

    def add_paper(self, fuellstand, leer, maximal_voll, umgedreht):
        if maximal_voll == False and umgedreht = False:
            fuellstand +=
            if leer == True:
                leer = False

            if fuellstand == 100:
                maximal_voll = True
        elif maximal_voll == True and umgedreht = False:
            print("Papierkorb ist voll! Bitte leeren.")

    def papierkorb_leeren(self, fuellstand, leer, maximal_voll, umgedreht):
        if maximal_voll == True and umgedreht = False:
            maximal_voll = False
            leer = True
            fuellstand = 0
        elif maximal_voll == False and umgedreht = False:
            print("Der Papierkorb ist bereits leer.")

    def papierkorb_drehen(self, leer, umgedreht):
        if leer == True:
            umgedreht = True
            print("Der Papierkorb ist jetzt umgedreht.")
        else:
            print("Der Papierkorb ist nicht leer, bitte erst leeren!")

    def trommel_solo(self, umgedreht):
        if umgedreht == True:
            print("""
            TROMMELSOLOOOO!!!!
            BUM BUM BUMBUMBUM
            BADA BADA BUMBUMBUM
            Yeeeeaaaaaahhh!!!!!11einelf
            """)
