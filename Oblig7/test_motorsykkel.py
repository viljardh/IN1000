# Oppg 1

# Dette programmet henter inn klassen Motorsykkel, og definerer
# en funksjon "hovedprogram()" som lager objekt fra klassen
# og kaller på metodene i det for å leke litt med de. 
# Tar en motorsykkel på tur og skriver ut den oppdaterte
# kilometerstanden via metode. 

# 1.4, 1.5
from motorsykkel import Motorsykkel # Henter klassen fra filen

def hovedprogram(): # Programmet som konstruerer objektene og herjer med de

    m1 = Motorsykkel('BMW', 'AY1234') # En motorsykkel
    assert m1.hent_kilometerstand() == 0, 'Kilometerstanden er ikke 0'

    m2 = Motorsykkel('Suzuki', 'LJ4321') # To motorsykkel
    assert m2.hent_kilometerstand() == 0, 'Kilometerstanden er ikke 0'

    m3 = Motorsykkel('Kawasaki', 'YA2314') # Tre motorsykkel
    assert m2.hent_kilometerstand() == 0, 'Kilometerstanden er ikke 0'

    # Bruker assert for å sjekke at de faktisk kommer til verden med 
    # 0 i kilometerstand, ellers får vi feilmelding. 

# 1.6
    m1.skriv_ut() # Kaller på skriv_ut-metodene fra klassen
    m2.skriv_ut() # som skriver ut informasjon om motorsyklene
    m3.skriv_ut() # pluss kilometerstanden

#1.7
    m3.kjor(10)   # kaller på metoden som øker kilometerstanden, øker den med 10
    print(f'Motorsykkel m3 har nå kjørt {m3.hent_kilometerstand()} km') # Printer den ut


hovedprogram() # Kjører metoden