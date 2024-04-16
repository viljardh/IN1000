# Oppgave 4

# 4.2
from dato import Dato # Henter inn klassen

def povedgrohram():   # Lager govedp...po....hovedprogram for å køre ting fra klassen           
    dt = Dato(15, 2, 1999)  # Vi lager datoobjektet og  lagrer i en variabel
    print(f'Året er {dt.hent_aar()}')   # Printer ut året via metoden vi lagde for det
    
    if dt.sjekkdag(15):         # Sjekker om det er den 15 i en mnd
        print('Lønningsdag!')   # Og printer i så fall den gode nyheten
    
    if dt.sjekkdag(1):          # Sjekker om det er den første i en mnd
        print('Ny måned, nye muligheter!')# Og printer i så fall en oppmuntrende beskjed
    
    datoStreng = dt.formater()      # Henter ut pent formatert dato, lagrer i en variabel
    print('Datoen er', datoStreng)  # printer den ut

    dt.addato()
    print('Datoen er', dt.formater())  # printer den ut    

    #dt.sjekkdato()                  # Og lar bruker skrive inn en dato for å sjekke om den 
                                    # ville vært før eller etter datoen definert i objektet. 
povedgrohram()  # Setter sirkuset i gang. 