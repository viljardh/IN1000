# Oppgave 3

# I dette programmet lager vi klassen som organiserer et objektsom funker som 
# spilleliste. Vi lager en metode som kan lese musikkinfo fra en fil og lage
# sangobjekter i en spilleliste, og en metode som legger et sangobjekt i spillelisten.
# Ellers kan man fjerne sanger, spille sanger og søke etter sanger. 

from sang import Sang # Henter sang-klassen og dens metoder vi lagde i stad

class Spilleliste:      # Definerer spillelisteobjektet
    def __init__(self, listenavn):  # Initialiseres med et navn
        self._sanger = []           # Lager en tom spilleliste
        self._navn = listenavn      # Som får et navn

    def les_fil(self, filnavn):     # Definerer moteden som lager spilleliste fra fil
        for i in open(filnavn, 'r'):# Itererer gjennom linjene i filen
            l = i.strip().split(';')# Rensker dataen basert på formatet vi forventer
            self._sanger.append(Sang(l[1], l[0])) # Lager objekter av de og legger i spillelisten

    def legg_til_sang(self, ny_sang):# Definerer en metode som tar et sangobjekt som argument
        self._sanger.append(ny_sang) # Og legger det til i spillelisten
    
    def fjern_sang(self, sang):     # Definerer en metode som lar oss fjerne sanger
        self._sanger.remove(sang)   # Den tar objekt som argument, og fjerner det fra listen

    def spill_sang(self, sang):     # Tar et sangobjekt som parameter
        sang.spill()                # Kaller på Sang-klassen og "spiller den av"
    
    def spill_alle(self):           # Metode for å spille av alle sanger
        for i in self._sanger:      # Itererer over elementene i spillelisten
            i.spill()               # og spiller de av
    
    def finn_sang(self, tittel):    # Lager en metode for å søke i spillelisten etter tittel
        for i in self._sanger:      # Itererer gjennom spillelisten
            if i.sjekk_tittel(tittel):# Og sjekker etter tittelmatch
                return i            # Returnerer i så tilfelle sangobjekt som matcher
        return                      # Hvis ingen match returneres ingenting i form av Null

    def hent_artist_utvalg(self, artistnavn): # Metode for å hente alle sangene til en artist
        listArtist = []             # Initialiserer en tom liste
        for i in self._sanger:      # Blar gjennom spillelisten
            if i.sjekk_artist(artistnavn):# Sjekker om sangen har en artist det søkes etter
                listArtist.append(i)# og legger sangen i lista
        
        return listArtist           # som returneres når søket er ferdig. 