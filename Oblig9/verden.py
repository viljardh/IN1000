# Oppgave 3

# Denne klassen lager og holder styr på tid og rom rutenettet og cellene befinner seg i. 
# Den kaller de frem og oppdaterer de, og binder sammen hele suppa sålangt. 

from rutenett import Rutenett

class Verden:

    def __init__(self, rader, kolonner):            # Klassen initialiseres med antall rader og kolonner
        self._rutenett = Rutenett(rader, kolonner)  # Og vi tegner da opp rutenettet med gitte parametre
        self._rutenett.fyll_med_tilfeldige_celler() # Fyller den så opp med celler som har 1/3 sjanse for å leve
        self._rutenett.koble_celler()               # Kobler de sammen så de vet hvem som er hvor
        self._generasjonsnummer = 0                 # Vi er da i 0-te generasjon som skal telles oppover

    def tegn(self):                     # Initialiserer en metode som 
        self._rutenett.tegn_rutenett()  # kaller på metoden fra rutenett sånn at vi kan se
        print('Generasjon:', self._generasjonsnummer, '- Antall levende celler:', self._rutenett.antall_levende())
        # Pluss litt smakstekst sånn at vi har litt interessant data. 

    def oppdatering(self):                          # This is where the magic happens
        list = self._rutenett.hent_alle_celler()    # Legger alle celleobjektene i rutenettet på rekke og rad i en liste
        for i in list:                              # Itererer over hele
            i.tell_levende_naboer()                 # Sørger for at cellene vet hvor mange naboer de har
        for i in list:                              # Når det er gjort
            i.oppdater_status()                     # Oppdaterer hver celle sin status etter antall naboer
        self._generasjonsnummer += 1                # Inkrementerer telleren 