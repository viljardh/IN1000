# Oppgave 2

# Denne klassen lager et rutenett for cellene å boltre seg i, og metoder som bestemmer 
# hvor i verden de befinner seg og hva som finnes rundt de sånn at de vet hva de skal gjøre.
# Gir oss verktøy til å behandle og organisere cellene. 
# Denne klassen vil også printe hvordan rutenettet ser ut.
# Jeg vil også uttrykke misnøye over at det går på form "rader x kolonner"
# Burde vært "kolonner x rader" fordi xy-koordinatsystem. Jeg vet at når man printer
# så går det som en scanline rad x kolonne, men allikevel. 

from random import randint  # Henter muligheten for å lage et tilfeldig tall
from celle import Celle     # Henter muligheten til å lage celler og manipulere de

class Rutenett:

    def __init__(self, rader, kolonner):    # Initialiserer rutenettet med ønsket antall rader og kolonner
        self._ant_rader = rader             # Lager initialverdier av de, de vil komme nyttig med
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett() # Lager også instansvariabel av rutenettet selv, som vi skal lage...

    def _lag_tomt_rutenett(self):       #..nå!
        l = []                          # Lager en tom liste 
        for i in range(self._ant_rader):# og legger inn "i" antall rader
            l.append(self._lag_tom_rad())# som vi lager i neste metode
        return l                        # lista kommer godt med, så den returnerer vi 

    def _lag_tom_rad(self):
        l = []                          # lager en midlertidig tom en 
        for i in range(self._ant_kolonner):# lager kolonner vi skal smekke inn i radene
            l.append(None)              # som skal være tomme slik at vi kan fylle de
        return l                        # og returnerer den slik at vi har den med videre.

    def fyll_med_tilfeldige_celler(self):         # en metode som gjør stort sett det den sier den skal
        for rad in range(self._ant_rader):        # for rad antall rader
            for kol in range(self._ant_kolonner): # og kol antall kolonner
                self.lag_celle(rad, kol)          # lager vi en celle i oppgitt koordinat. 

    def lag_celle(self, rad, kol):          # Denne metoden lager en celle, og plopper de i rutenettet gitt koordinatene
        celle = Celle()                     # Lager et objekt og en peker til objektet
        sjanse = randint(1, 3)              # Lager et tilfeldig heltall mellom 1 og 3
        if sjanse == 1:                     # Hvis det er en bra random er det 1/3 sjanse for at den blir 1
            celle.sett_levende()            # I hvis tilfelle cellen er i live
            self._rutenett[rad][kol] = celle# og plopper den inn i rutenettet gitt koordinatene
        else:
            self._rutenett[rad][kol] = celle# Igjen, jeg hater at det er rad x kol. Jeg tror rutenettet mitt er feil vei. 

    def hent_celle(self, rad, kol):                 # Denne metoden henter en celle, og sjekker at den er "in bounds",
        if rad >= 0 and rad < self._ant_rader:      # altså at den er inni rutenettet som konstruert. 
            if kol >= 0 and kol < self._ant_kolonner:
                return self._rutenett[rad][kol]     # I så tilfelle returnerer den cellen som objekt
            else:
                return                              # Hvis ikke returnerer den None
        else:
            return
#    def hent_celle(self, rad, kol):
#        if rad in range(self._ant_rader) and kol in range(self._ant_kolonner):
#            return self._rutenett[rad][kol]

    def tegn_rutenett(self):                        # Metode for å tegne ut rutenettet
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n') # Rensker terminalen bra nok
        for rad in range(self._ant_rader):          # Itererer gjennom rader
            for kol in range(self._ant_kolonner):   # og kolonner
                c = self.hent_celle(rad, kol)       # henter ut celleobjektet på koordinatet
                print(c.hent_status_tegn(), end=' ') # og printer ut statustegnet, sørger for at de havner på linje
            print('\n', end=' ')                     # Linjen er printet ferdig, vi gjør et linjeskift. 
            # Igjen...skulle vært kolonner x rader. Jeg tror rutenettet mitt er feil vei, men pga hvordan 
            # testfunksjonene er konstruert er jeg nødt til å spille på lag. Hvem gjør sånt??


    def _sett_naboer(self, rad, kol):               # Her skal vi da fortelle cellen hva slags naboer den har
        celle = self.hent_celle(rad, kol)           # For å gjøre det må vi såklart ha en celle
        for i in range(-1, 2):                      # Sjekker de som er til høyre og venstre
            for j in range(-1, 2):                  # Og de som er over og under (følgelig de som er begge deler)
                                                    # Kun ett hakk, en celle i 1,1 bryr seg ikke om hva som skjer i 7,8
                if not (i == 0 and j == 0):         # men *ikke* cellen selv
                    if self.hent_celle(rad + i, kol + j) is not None: # sjekker at den er in-bounds og på rutenettet
                        celle.legg_til_nabo(self.hent_celle(rad + i, kol + j)) # og hvis den er innafor legger vi den i
                                                                               # cellen sin list over naboer
        
    def koble_celler(self):                         # Og nå skal vi sørge for at hver enkelt celle vet hva som er rundt seg
        for rad in range(self._ant_rader):          # Itererer over rader
            for kol in range(self._ant_kolonner):   # og kolonner
                self._sett_naboer(rad, kol)         # og setter nabo for alle cellene i rutenettet. 

    def hent_alle_celler(self):                     # Metode for å lage en plain liste over alle cellene
        list = []                                   # Lager tom liste
        for rad in range(self._ant_rader):          # Itererer over rader
            for kol in range(self._ant_kolonner):   # Og kolonner
                list.append(self.hent_celle(rad, kol))# Legger celleobjektet i lista
        return list                                 # Og returnerer listen 

    def antall_levende(self):                       # Metode for å gi oss antall levende celler i rutenettet
        c = 0                                       # Initaliserer telleren
        for rad in range(self._ant_rader):          # Itererer over rader
            for kol in range(self._ant_kolonner):   # og kolonner
                celle = self.hent_celle(rad, kol)   # Henter frem cellen med koordinatet vi er på 
                if celle.er_levende():              # Sjekker om den er levende
                    c += 1                          # Og inkrementerer telleren i så tilfelle
        return c                                    # Returnerer telleren
    