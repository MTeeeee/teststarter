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

    def add_paper(self):
        if self.maximal_voll == False and self.umgedreht == False:
            self.fuellstand += 1
            if self.leer == True:
                self.leer = False

            if self.fuellstand == 100:
                self.maximal_voll = True
        elif self.maximal_voll == True and self.umgedreht == False:
            print("Papierkorb ist voll! Bitte leeren.")

    def papierkorb_leeren(self):
        if self.maximal_voll == True and self.umgedreht == False:
            self.maximal_voll = False
            self.leer = True
            self.fuellstand = 0
        elif self.maximal_voll == False and self.umgedreht == False:
            print("Der Papierkorb ist bereits leer.")

    def papierkorb_drehen(self):
        if self.leer == True:
            self.umgedreht = True
            print("Der Papierkorb ist jetzt umgedreht.")
        else:
            print("Der Papierkorb ist nicht leer, bitte erst leeren!")

    def trommel_solo(self):
        if self.umgedreht == True:
            print("""
            TROMMELSOLOOOO!!!!
            BUM BUM BUMBUMBUM
            BADA BADA BUMBUMBUM
            Yeeeeaaaaaahhh!!!!!11einelf
            """)
