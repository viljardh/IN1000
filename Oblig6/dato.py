# Oppg 4

# 1.1
class Dato: # Definerer klassen
    def __init__(self, ny_dag, ny_maaned, nytt_aar): # Initierer konstruktor med parametre
        self._dag = ny_dag          # Dag,
        self._maaned = ny_maaned    # måned, 
        self._aar = nytt_aar        # og år. 
    
    def hent_aar(self):     # Lager en metode som returnerer
        return self._aar    # verdien for år, heltall
    
    def formater(self):     # En metode som returnerer en pent formatert streng
        d = str(self._dag)  # Konverterer da dag, måned og år til streng
        m = str(self._maaned)
        a = str(self._aar)
        if len(d) == 1:     # Slenger på en 0 foran hvis 
            d = '0' + d     # 
        if len(m) == 1:     # måned
            m = '0' + m     #
        if len(a) == 1:     # og år
            a = '0' + a     # bare er ett tall, sånn at det ser penere ut

        return '.'.join([d, m, a[-2:]])  # Returnerer den formaterte datoen som streng
                                        # Bare interessert i de to siste tallene i året

    def sjekkdag(self, dato):       # Sjekker om datoen er den samme som parameteren til metoden
        return self._dag == dato    # og returnerer True/False ettersom

    def sjekkdato(self):            # Callback til Oblig 1
        inp = input('Skriv en dato på format DD.MM:\n')
        d1 = int(self._dag)         # Bare at jeg gjør det med int denne gangen
        m1 = int(self._maaned) 
        inp = inp.split('.')        # Og på mine egne premisser
        d2 = int(inp[0])
        m2 = int(inp[1])

        if m1 > m2:     # Hvis månedene er foskjellige er det åpenbart hvilken dato som er størst
            print('Datoen du oppga er tidligere!')
        elif m1 < m2:
            print('Datoen du oppga er senere!')
        elif m1 == m2:  # Hvis mnd er den samme må vi gjøre en sjekk på dagene
            if d1 == d2:# for å finne hvem som er større, eller om de er like
                print('Samme dato!')
            elif d1 < d2:
                print('Datoen du oppga er senere!')
            elif d1 > d2:
                print('Datoen du oppga er tidligere!')
    

    def addato(self):   # Jeg har nå trosset Tom Scott sitt råd og begitt meg ut på datokoding
        list31 = [1, 3, 5, 7, 8, 10] # Liste over mnd med 31 dager, sans desember
        list30 = [4, 6, 9, 11]  # Liste over mnd med 30 dager

        if self._maaned in list31: # Hvis måneden har 31 dager
            if self._dag < 31:     # og datoen til objektet er  mindre enn 31
                self._dag += 1     # kan vi bare slenge på en dag
            else:
                self._dag = 1      # Hvis datoen er siste dag i mnd starter vi en ny og setter dato til første 
                self._maaned += 1  # Og så inkrementerer måneden en gang
        
        elif self._maaned in list30:# Nøyaktig samme logikk her, bare for 30 dager
            if self._dag < 30:
                self._dag += 1
            else:
                self._dag = 1
                self._maaned += 1

        elif self._maaned == 2:    # Sjekker for februar 
            if self._aar % 4 == 0: # og skuddår, alle skuddår er delelig på fire
                if self._dag < 29: # og i så fall har feb 29 dager
                    self._dag += 1
                else:
                    self._dag = 1
                    self._maaned += 1
            else:
                if self._dag < 28:  # Ellers har den 28
                    self._dag += 1
                else:
                    self._dag = 1
                    self._maaned += 1

        elif self._maaned == 12:    # Er vi i slutten av året og slutten av mnd
                if self._dag < 31:
                    self._dag += 1
                else:
                    self._dag = 1   # Begynner et nytt år med en ny dag
                    self._maaned = 1
                    self._aar += 1  # Og pluss ett år
        # Dette kunne vært gjort enklere med en ordbok ellerno
        # men `\_(o.O)_/´