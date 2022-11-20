# Funktionsdefinitionen
def verschiebung(zeichen, schluessel):
    zahl = ord(zeichen)
    neueZahl = zahl + schluessel
    if neueZahl > 90:
        neueZahl -= 26
    elif neueZahl < 65:
        neueZahl += 26
    

    neuesZeichen = chr(neueZahl)
    return neuesZeichen

def verschluesselung(text, schluessel):
    neuerText = ''
    for c in text:
        neuerText += verschiebung(c, schluessel)
    return neuerText

def entschluesselung(text, schluessel):
    return verschluesselung(text, -schluessel)

# Funktionsaufrufe
print(verschluesselung('ASTERIX', 3))
print(entschluesselung('DVWHULA', 3))
print(verschluesselung('EUREKA', 7))
print(entschluesselung('LBYLRH', 7))
