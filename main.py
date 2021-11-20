#Gemaakt door Sami!

import os
import random

test = ''
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
STANDAARD_LIJST = 'EN-NED'
STOPPEN = 'q'
TOEVOEGEN = 't'
VERWIJDEREN = 'v'




def print_regel(regel):
  # Haal 4 karakters van schermbreedte af: '| ' en ' |'
  print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))

def print_header():
  
    print("="* SCHERMBREEDTE)
    print_regel("")

def print_footer():
    print_regel('')
    print("="*SCHERMBREEDTE)



def leeg_scherm():
    os.system("clear")



def overhoren(lijstnaam):
    filesize = os.path.getsize(lijstnaam)
    if filesize == 0:
        print('Er staat niks in de lijst dat ik kan overhoren.')
        input("Klik op Enter om door te gaan")
    else:
        f = open(lijstnaam)
        woorden_in_bestand = {}
        gaan = True
        

        for line in f:
            woord1, woord2 = line.strip('\n').split('=')
            woorden_in_bestand[woord1] = woord2
            print(woord1 + " " + woord2)
            

        f.close()
        while gaan == True:
            test = random.choice(list(woorden_in_bestand.keys()))
            leeg_scherm()
            print_header()
            print_regel('Vertaal het woord: '+test)
            print_footer()
            print('Type '+STOPPEN+" in om te stoppen")
            print("")
            vertaling = input("Uw vertaling: ")
            if vertaling in woorden_in_bestand.values():
                print("Dat is goed!")
                input("Klik op Enter om door te gaan")
            if vertaling not in woorden_in_bestand.values():
                print("Dat is fout")
                print("Het juiste antwoord was: "+ woorden_in_bestand[test])
                input("Klik op Enter om door te gaan")
            
            if vertaling == STOPPEN:
                gaan = False




    
def print_afscheid():
    leeg_scherm()
    print_header()
    print_regel("Dankuwel voor het gebruiken van dit programma!")
    print_regel("Ik hoop dat u nog een fijne dag/nacht heeft :)")
    print_footer()


def print_menu(lijstnaam):
    leeg_scherm()
    print_header()
    print_regel("Welkom bij het overhoorprogamma!")
    print_regel("De woorden lijst die nu geselecteerd is, is: "+ lijstnaam)
    print_regel("Type "+OVERHOREN+" in om de geselecteerde lijst te overhoren")
    print_regel("Type " + NIEUWE_LIJST + " in om een nieuwe woordenlijst te maken")
    print_regel("Type " + KIES_LIJST + " in om een lijst te kiezen")
    print_regel("Type "+ TOEVOEGEN + " in om een woordpaar aan de woordenlijst toe te voegen")
    print_regel("Type "+ STOPPEN + " in om het programma te stoppen")
    print_footer()

def nieuwe_lijst_naam():
    lijst_naam_keuze = input("Type een naam in: ")
    lijst_naam_keuze = lijst_naam_keuze + EXTENSIE
    return lijst_naam_keuze

def schrijf_woordenlijst(woordenlijst, lijst_naam):
    f = open(lijst_naam, 'a')
    for key, value in woordenlijst.items():
        f.write(key + SCHEIDER + value + "\n")
        
    f.close()
    woordenlijst.clear()


def voeg_woorden_toe(woordenlijst, lijstnaam):
    


    doorgaan = True
    while doorgaan == True:
        leeg_scherm()
        print("Type "+STOPPEN+ " in om te stoppen")
        woord_toevoegen = input("Type een woord in: ")
        woord_toevoegen2 = input("Type de vertaling van het woord in: ")
        
        if woord_toevoegen == STOPPEN:
            doorgaan = False
        else:
            print("wilt u de woordparen naar een bestand schrijven? ja/nee: ")
            wegschrijven = input(" ")
            if wegschrijven == "ja":
                woordenlijst[woord_toevoegen] = woord_toevoegen2
                schrijf_woordenlijst(woordenlijst, lijstnaam)
            elif wegschrijven == "nee":
                
                print("")
            elif wegschrijven == STOPPEN:
                doorgaan = False
            else:
                print("")
    


def main():
    f = open(STANDAARD_LIJST, 'w')
    f.close()
    
    woordenlijst = {}
    bestanden = []
    bestanden.append(STANDAARD_LIJST)
    filename = ''
    doorgaan = True
    lijstnaam = STANDAARD_LIJST
    
    while doorgaan == True:
        
        print_menu(lijstnaam)
        menu_keuze = input("Uw keuze:  ")
        if menu_keuze == NIEUWE_LIJST:
            
            filename = nieuwe_lijst_naam()
            
            f = open(filename, "w")
            f.close()
            bestanden.append(filename)
            print("Woordenlijst is gemaakt!")
            input("KLik op Enter om door te gaan")
            
        
        elif menu_keuze == TOEVOEGEN:
            
            zeker_weten = input('Weet u het zeker? De oude inhoud zal verloren gaan. ja/nee: ')
            if zeker_weten == 'ja':
                f = open(lijstnaam, 'w')
                f.close()
                voeg_woorden_toe(woordenlijst, lijstnaam)
            elif zeker_weten == 'nee':
                print('')
            else:
                print('Dat heb ik niet goed begrepen :(')
                input("Klik op Enter om door te gaan")
        elif menu_keuze == KIES_LIJST:
            leeg_scherm()
            print_header()
            print_regel("De huidige lijst is: "+lijstnaam)
            print_regel('De volgende woordenlijsten staan in de map: ')
            print_regel('')
            for i in bestanden:
                print_regel(i)
            print_regel('')
            print_regel("Voer hieronder de naam van de lijst die u wilt kiezen")
            print_regel("Voer "+STOPPEN+" in om te stoppen")
            print_footer()
            lijst_keuze = input("lijstnaam: ")
            if lijst_keuze in bestanden:
                lijstnaam = lijst_keuze
            else:
                print(lijst_keuze+' bestaat niet.')
                input('Klik op Enter om door te gaan')
        elif menu_keuze == OVERHOREN:
            overhoren(lijstnaam)
        
        elif menu_keuze == STOPPEN:
            print_afscheid()
            doorgaan = False

            

        
        
        


main()



