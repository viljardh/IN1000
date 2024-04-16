# Oppgave 2

# Her definerer vi en klasse som lager et objekt "Sang" med artistnavn og sangtittel
# Lager deretter metoder som sjekker informasjon om sangene gjennom brukers input

class Sang:# Definerer klassen Sang
    def __init__(self, artist, tittel): 
        self._artist = artist   # Definerer instansvariablene basert
        self._tittel = tittel   # på hvordan objektet blir konstruert

    def __str__(self):
        return f'Nå spiller {self._tittel} av {self._artist}'
    
    def spill(self):    # Lager en metode som sier hvilken sang som blir splilt og av hvem
        print(f'Nå spiller {self._tittel} av {self._artist}')
    
    def sjekk_artist(self, navn):   # Lager metode som lar bruker sjekke artist
        navn = navn.split()         # Lager en liste over ordene i strengen, skilt av mellomrom
        artist = self._artist.split()# Samme for artisten
        for i in navn:              # Hvis noen av elementene i søkelisten 
            if i in artist:         # finnes i artistnavnet
                return True         # returnerer vi "True"
        return False                # Hvis ikke, returnerer vi "False"

    def sjekk_tittel(self, sjekkTittel): # Lager metode for å sjekke sangtittel
        return sjekkTittel.lower() == self._tittel.lower() # Og tvinger begge i lowercase, sjekke om de matcer

    def sjekk_artist_og_tittel(self, artist, tittel): # Sjekker om begge stemmer overens
        return self.sjekk_tittel(tittel) and self.sjekk_artist(artist) # og gjøres med å kalle på foregående metoder