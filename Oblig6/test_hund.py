# Oppg 3

# Dette programmet henter inn klassen "Hund" og definerer 
# en funksjon som lager objektet og kaller på metoder
# i klassen som lar oss veie, mate og trimme den. 

# 3.2
from hund import Hund   # Henter klassen fra filen

def povedhogram():      # Lager et pove- hovedprogram for å kjøre metodene

    dawg = Hund(7, 55)  # Som min egen kjære hund, Madonna. 7 år og 55 kg. 

# 3.6
    dawg.spring()       # Trimmer henne litt, lykke til med det
    print(dawg.hent_vekt()) # Sjekker vekten

    dawg.spring()       # Og igjen
    print(dawg.hent_vekt())

    dawg.spis(2)        # Lar henne spise litt
    print(dawg.hent_vekt()) # Og sjekker vekten

    dawg.spis(2)        # Og igjen. 
    print(dawg.hent_vekt())

povedhogram()           # Kjører 