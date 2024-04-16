# Oppgave 3 - Billettpris
# Denne oppgaven ber bruker skrive inn en alder
# og svarer med hvor mye billetten vil koste

def pris(): # Definerer funksjonen som gjør jobben for oss
    alder = int(input('Skriv en alder\n')) # Konverterer input til heltall
    billettpris = 0     # Definerer variabelen "billettpris" og gir den verdi 0

    if alder < 0:
        print('Ugyldig alder, prøv igjen')
        return
    # Liten sjekk bare for å luke ut negative tall. 

    elif alder <= 17:       # Sjekker om alderen er 17 eller mindre, går ellers videre
        billettpris = 30    # I hvis tilfelle blir billettpris tilegnet verdien 30

    elif alder < 63:        # Sjekker om alderen er mindre enn 63 hvis den er over 17
        billettpris = 50    # I så fall blir billettprisen 50. Hvis ikke, går den videre.

    elif alder >= 63:       # Sjekker om alderen er 63 eller eldre
        billettpris = 35    # I så tilfelle blir billettprisen 35

    else: 
        print('!!ERROR!!')  # Backupfeilmelding. 
        return
        
    print(f'Når din alder er {alder} blir billettprisen {billettpris} kroner.')
    # Printer en liten beskjed med alder og billettpris.

pris()
# Kjører funksjonen

# Prosedyren min fungerer etter alt jeg ser helt ok?
# Hadde jeg fulgt oppgaveteksten og implementert logikken
# direkte som det stod skulle elif alder < 63 egentlig vært
# elif alder > 17, og da hadde den aldri kommet lengre enn der. 
# Skulle gjerne gjort en sjekk på at inputen kun inneholder
# tall og gitt en mer beskrivende feilmelding, men usikker på 
# hvordan jeg skulle gått frem der. 