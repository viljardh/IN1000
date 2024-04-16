# Oppgave 1

# Denne klassen lar oss lage et celleobjekt. Det kan ha status "levende" eller "doed", har en liste over naboer
# og et tall som sier hvor mange av de som er levende. Dette er ting som nødvendigvis vil måtte endre seg
# og vi lager metoder deretter. 

class Celle:
    # Konstruktører do what they scooby dooby do
    def __init__(self):         # Initialiserer celleobjektet
        self._status = 'doed'   # Er i utgangspunktet død, skal i utgangspunktet bare være med for å skape rutenettet
        self._naboer = []       # Og har ingen naboer
        self._ant_levende_naboer = 0 # Ikke levende heller
    
    def sett_doed(self):        # Metode for å endre status
        self._status = 'doed'   # til "død"

    def sett_levende(self):     # Og en til 
        self._status = 'levende'# for å vekke til live

    def legg_til_nabo(self, nabo): # Metode for å legge en celle til som nabo
        self._naboer.append(nabo)  # i en liste vi initialiserte i begynnelsen

    def er_levende(self):           # Sjekker om vi er i live, returnerer True eller False deretter
        return self._status == 'levende'

    def hent_status(self):
        # Jeg ser for meg hva denne skulle gjort, men trengte den ikke, så den uteblir.
        pass

    def hent_status_tegn(self):     # Denne metoden returnerer et tegn vi kan printe til konsollen 
        if self.er_levende():       # for å vise hvorvidt en celle er i live eller død. Sjekker med if-test.
            return 'O' 
            #return '█' #er kulere 
        else:
            return '.' 
            #return '░' #men akk

    def tell_levende_naboer(self):      # Antall levende naboer er viktig å vite for hvorvidt en celle skal dø
        self._ant_levende_naboer = 0    # leve eller komme til live. Men må resette telleren, ellers har vi plutselig 20. 
        for i in self._naboer:          # Går gjennom listen med naboer
            if i.er_levende():          # Sjekker om de lever
                self._ant_levende_naboer += 1   # Og oppdaterer instansvariabelen som holder koll på ant. levende naboer
    
    def ant_levende_naboer(self):       # Metode som returnerer antall levende nabo som heltall
        return self._ant_levende_naboer

    def oppdater_status(self):          # Oppdaterer status basert på antall naboer as per the rules 
        if self.er_levende():           # Hvis den er levende og har mindre enn to eller mer enn tre
            if self._ant_levende_naboer < 2 or self._ant_levende_naboer > 3:
                self.sett_doed()        # Dør den
            
        else:                           # Ellers vil den nødvendigvis være død
            if self._ant_levende_naboer == 3:
                self.sett_levende()     # Og hvis den har eksakt tre naboer, kommer den til live