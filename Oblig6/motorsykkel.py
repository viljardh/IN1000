# Oppg 1

# Dette programmet lager en klasse som er en enkel representasjon av en 
# motorsykkel, et par av dens kjennetegn og dens kilometerstand. 
# Man "lager" objektet med å oppgi merke og regnr, vil alltid 
# starte med 0 i kilometerstand. 

# 1.1
class Motorsykkel: # Definerer klassen

    def __init__(self, merke, reg): # Konstruktoren tar merke og regnr i form av streng
        self._kmstand = 0       # Den skulle alltid være 0 jmf oppgavetekst
        self._merke = merke     # Lager instansvariable for merke og reg
        self._reg = reg         # basert på parametre når man kaller på klassen

# 1.2
    def kjor(self, km):         # Metode som tar et heltall som input og 
        self._kmstand += km     # hever kilometerstanden deretter. 

# 1.3
    def hent_kilometerstand(self): # Metode som når kalles på returnerer
        return self._kmstand       # kilometerstanden som den er

# 1.6
    def skriv_ut(self):         # Metode som skriver ut info om motorsykkelen
        print(f'Merket er {self._merke}') # merke
        print(f'Kilometerstand er {self._kmstand}') # nåværende kilometerstand
        print(f'Registreringsnummer er {self._reg}\n') # og regnr

