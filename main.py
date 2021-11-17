import os

SCHERMBREEDTE = 54
MAX_WOORD_LENGTE = 20
DELETE = 'd'
EXTENSIE = '.wrd'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '='
SCHERMBREEDTE = 80
SCHERMHOOGTE = 40
STANDAARD_LIJST = 'n'
STOPPEN = 'q'
TOEVOEGEN = 't'

woord = "vlieger"
vertaling = "kite"

def print_regel(regel):
  # Haal 4 karakters van schermbreedte af: '| ' en ' |'
  print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))



def leeg_scherm():
    os.system("clear")

def lees_woordenlijst(bestandsnaam):
    with open('bestandsnaam') as f:
        bestandsdata = f.read()

def print_menu(lijstnaam):
    print("Type " + STANDAARD_LIJST + " in om een nieuwe woordenlijst te maken")
    print("Type " + KIES_LIJST + " in om een lijst te kiezen")
    print("Type "+ TOEVOEGEN + " in om een woord aan de woordenlijst toe te voegen")
    print("Type "+ STOPPEN + " in om het programma te stoppen")

def nieuwe_lijst_naam():
    lijst_naam_keuze = input("Type een naam in: ")
    return lijst_naam_keuze

def voeg_woorden_toe(woordenlijst, lijst_naam_keuze):
    print("Type Q in om te stoppen")
    doorgaan = True
    while doorgaan == True:
        woord_toevoegen = input("Type een woord in: ")
        if woord_toevoegen == "Q":
            doorgaan = False
        else:
            f = open(lijst_naam_keuze, "a")
            f.write(woord_toevoegen + "\n")
            f.close()


def main():
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))
    filename = ''
    doorgaan = True
    while doorgaan == True:
        print_regel("heyyy")
        print_menu("hallo")
        menu_keuze = input(": ")
        if menu_keuze == STANDAARD_LIJST:
            filename = nieuwe_lijst_naam()
            
            f = open(filename, "w")
            f.close()
            print("Woordenlijst is gemaakt!")
            
        
        if menu_keuze == TOEVOEGEN:
            print("hey")
            
            voeg_woorden_toe("2", filename)
        


main()



