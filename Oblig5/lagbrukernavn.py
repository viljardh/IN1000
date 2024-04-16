# Oppg 2
# Dette programmet lager brukernavn og epost til en UiO-bruker
# basert på deres input i form av navn og fakultet. 

# 2.1
#def lagBrukernavn(navn):    # Lager først en funksjon som lager brukernavn
#    n = navn.lower().split()# av brukerens faktiske navn, som tas som input. 
#    bn = n[0] + n[-1][0]    # Deretter blir navnene delt opp og vi henter ut fornavn
#    return ''.join(bn)      # pluss første bokstav av etternavn for så å spleise de. 

# 2.1, 2.6
def lagBrukernavn(navn):
    n = navn.lower().split()
    bn = ''.join(n[0] + n[-1][0]) # likt som i 2.1 fram til og med hit
    c = 1                         # starter en teller på  plass 2, antar 1 er brukt
    while bn in bnepost:          # Så lenge brukernavnet er i listen fra før
        bn = bn + n[-1][c]        # så legger vi til neste bokstav fra siste navn i lista
        c += 1                    # inkrementerer telleren i tilfelle det heller ikke er unikt
    return bn                     # returnerer brukernavn
# Begrensingen her er hvis det er mer enn tre som heter Ole Aas.
# Spent å se hva UiO hadde gjort hvis det var mer enn seks Ole Aas som gikk her. 

# 2.2
def lagEpost(brnavn, suffix):# Tar brukernavn og suffix som input
    list = [brnavn, suffix]  # Lager liste av de bare for å slå de sammen
    return '@'.join(list)       # Spleiser listen med en "@" i mellom

# 2.3
def skrivUtEposter(dic):    # Denne funksjonen tar en ordbok med brukernavn som nøkkelverdi
    for i in dic:           # og epost som innhodsverdi, for så å printe de ut. 
        print(lagEpost(i, dic[i])) # Lager epost, printer den ut


# 2.4 
bnepost = {}         # Lager en tom liste til å inneholde infoen

#bnepost = {'viljarh':'viljarh@ifi.uio.no', 'aleksj':'aleksj@ifi.uio.no', 'viljarha':'', 'viljarhar':''}
# Testliste, vennligst ignorer

def printerino():    # Lager en funksjon for dette, tillater meg å gjøre rekursivt. 
    inp = 'y'        # Vet ikke om det er bedre enn "if true" men gjør det sånn her. 
    while inp == 'y':# Setter e initialverdi for å starte showet
        inp = input('Ønsker du å input brukernavn og fakultet, eller printe listen? i/p \n\'s\' for å gå ut av programmet\n')
        
        if inp == 'i':# Hvis bruker ønsker å legge inn info må de nesten få lov
            nimput = input('Hva er navnet ditt?\n')# Lagrer navnet i en streng
            bnavn = lagBrukernavn(nimput)          # Gjør om til brukernavn
            fklt = input('Skriv fakultet-suffixen din:\n')# lagrer suffixen i en annen
            bnepost[bnavn] = fklt   # Legger brukernavn og suffix i ordbok
            printerino()
            # Går tilbake til "hovedmenyen"

        elif inp == 'p':# Hvis bruker ønsker å printe ut ordboken sålangt
            skrivUtEposter(bnepost)# Kaller på funksjonen som printer den
            printerino()                  # og gir input iform av ordbok med nøkkel
            # Går tilbake til "hovedmenyen"

        elif inp == 's':            # Lar bruker gå ut av prosedyren
            print('Takk og farvel.')# med vennlige avskjedsord
        
        else: # Lar bruker starte på nytt hvis de har gjort noe gærent
            print('Ikke gyldig input, start på nytt.')
            printerino()

printerino()  # Kaller på funksjonen som lager og printer ordboken

# 2.5
def testbrukernavn():                   # Definerer testfunksjon
    navn = 'Viljar Drevland Hardersen'  # Lager navn til input for å teste brukernavnfunksjonen
    bnavn = 'viljardh'                  # Tester med mitt faktiske UiO-brukernavn
    assert bnavn == lagBrukernavn(navn), "Forventet brukernavn " + bnavn + " men fikk brukernavn " + lagBrukernavn(navn)
    # Sjekker om navnet er likt som forventet resultat, printer feilmelding hvis ikke. 


def testepost():                  # Definerer testfunksjon
    bnavn = 'viljardh'            # Lager navn til input for å teste epostfunksjon
    suffix = 'ifi.uio.no'         # Lager også suffix
    epost = 'viljardh@ifi.uio.no' # Sjekker om det passer min faktiske epost
    assert epost == lagEpost(bnavn, suffix), 'Forventet epost ' + epost + ' men fikk ' + lagEpost(bnavn, suffix)
    # Sjekker om den genererte eposten er lik som forventet, printer feilmelding hvis ikke

#testbrukernavn() # Tester brukernavn, printer feilmelding
#testepost()      # Skulle testet eposten, men kommer ikke så langt
                  # Men gitt inputen vil den gi riktig. 