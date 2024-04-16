# Oppg 5 - Egen oppgave
# I denne oppgaven skal du utfordre brukeren i hoderegning!
# Tilby brukeren forskjellige matteoppgaver, ta svar som input
# For eksempel addisjon, potens, pythagoras
# Tilby også et par vanskelighetsgrader. Hvis bruker gir feil svar
# gi de tilbakemelding med avvik i prosent fra løsningen. 

# Dette programmet gir brukeren hoderegningsoppgaver i 

# a = første ledd i oppgave
# b = andre ledd i oppgave
# c = løsning
# svar = brukers input forslag på løsning
# start = hvilken type oppgave bruker ønsker
# grad = vanskelighetsgrad bruker ønsker

# Starter med å definere funksjonene som gjør kalkulasjonene
# (All min historie med python er matterelatert, nå skal alle få lide) 
def prosent(c, svar):
    # Siden jeg vile ha avviket av brukerens forslag som prosent av løsningen starter
    # vi med å regne ut hva det er, fulgt av å ta absoluttverdien. 
    # Slik blir resultatet det samme enten brukers svar er for høyt eller lavt
    # Dette er også funksjonen som sjekker og gir tilbakemelding hvorvidt de hadde riktig eller galt. 
   
    if c == svar: 
            print('Gratulerer, det er helt riktig!')
    # Sjekker om bruker ga riktig svar, og sier i så fall det.
  
    else:
        p = (1-svar/c)*100# Svar som prosent
        p = (p**2)**(1/2) # Absoluttverdi
        print(f'Nesten! Du var {p:.2f} % unna! Prøv igjen!')
    # Hvis bruker ikke ga riktig svar regner den ut prosenten og forteller hvor 
    # langt unna bruker var pluss en liten motiverende oppfordring. 

# Her følger funksjonene som løser matteproblemene. Litt mer fleksibelt å 
# lage de som funksjoner mtp vanskelighetsgradene. I stedet for å skrive de 
# om og om og om igjen kan du bare la de ta argumenter for å endre det du sender gjennom.  
def addisjon(a, b, svar):
    c = a + b
    prosent(c, svar)
    # Enkel funksjon som beregner summen av argumentene.

def potens(a, b, svar):
    c = a**b
    prosent(c, svar)
    # Beregner ene argumentet opphøyd i det andre.

def pythagoras(a, b, svar):
    c = (a**2 + b**2)**(1/2) # Pythagoras teorem
    prosent(c, svar)
    # Beregner hypotenusen når argumentene er kateter. 

# Når jeg kaller på quiz-funksjonen har jeg laget en if-test for input til å filtrere ut
# svar som ikke gir mening for scriptet, men slang med en liten "else" inni funksjonen i tilfelle
# noe dusteinput skulle klare å snike seg inn lell. 
def quiz(start, grad):
    # Funksjonen tar input fra bruker som argumenter. 
    # Sjekker først brukerens input for å velge hva slags oppgave de vil løse 
    if start == '1': 
        # Quiz 1 er for addisjon
        if grad == '1': 
            a = 49
            b = 58
        elif grad == '2': 
            a = 5689
            b = 2394
        elif grad == '3':
            a = 45687
            b = 56406
        else: 
            print('!!ERROR!!')
            return
        # Foretar en serie if/elif-tester for å sjekke hvilken vanskelighetsgrad bruker ønsker.
        # Basert på input fra bruker blir variablene tilegnet verdier vi sender til addisjon()        
        
        svar = int(input(f'Hva er {a} + {b}?\n'))
        # Leser brukeren sin input. Konverterer til integer fordi vi bare driver med heltall.
        
        addisjon(a, b, svar)
        # Kaller på funksjonen for addisjon og serverer variablene basert på vanskelighetsgrad
        # og brukers svar som argumenter. 

    elif start == '2':
        # Quiz 2 er for potenser
        if grad == '1':
            a = 4
            b = 3
        elif grad == '2':
            a = 11
            b = 5
        elif grad == '3': 
            a = 19
            b = 7
        else: 
            print('!!ERROR!!')
            return
        # Foretar en serie if/elif-tester for å sjekke hvilken vanskelighetsgrad bruker ønsker. 
        # Basert på input fra bruker blir variablene tilegnet verdier vi sender til potens()

        svar = int(input(f'Hva er {a} ^ {b}?\n'))
        # Leser brukeren sin input. Konverterer til integer fordi vi bare driver med heltall. 

        potens(a, b, svar)
        # Kaller på funksjonen for potens og serverer variablene basert på vanskelighetsgrad
        # og brukers svar som argumenter.

    elif start == '3':
        if grad == '1':
            a = 3
            b = 5
        elif grad == '2':
            a = 12
            b = 16
        elif grad == '3':
            a = 18
            b = 24
        else:
            print('!!ERROR!!')
            return
        # Foretar en serie if/elif-tester for å sjekke hvilken vanskelighetsgrad bruker ønsker. 
        # Basert på input fra bruker blir variablene tilegnet verdier vi sender til pythagoras()

        svar = int(input(f'Hva er Hypotenus når første katet er {a} og andre er {b}?\n'))
        # Leser brukeren sin input. Konverterer til integer fordi jeg er lat og valgte pythagorastall,
        # så vi bare driver med heltall. 

        pythagoras(a, b, svar)
        # Kaller på funksjonen for pythagoras og serverer variablene basert på vanskelighetsgrad
        # og brukers svar som argumenter.

print('Hei, og velkommen til matteprøve!')
print('Her er det hoderegning som gjelder')
print('Hvis du svarer feil vil du få tilbakemelding som prosent i avvik fra svaret')
print('Hva vil du ha prøve i?')
print('(Skriv et tall for å velge)')
# Flere printekommandoer etter hverandre fordi det bllir mindre rotete enn \n, som vi ser nå straks

start = input(' 1. Addisjon\n 2. Potenser\n 3. Pythagoras\n')
# Trenger bare strenger her. Tilegner "start"-variabelen med hvilken type oppgave bruker ønsker.
# Legger inn en if-test etterpå som sender bruker ut om de ikke oppfører seg. 

if start == '1' or start == '2' or start == '3':
    grad = input('Velg vanskelighetsnivå:\n 1. Lett\n 2. Middels\n 3. Vanskelig\n(Skriv et tall for å velge)\n')
    # Legger inn en if-test bare for å filtrere ut dårlig input, mindre knot for quiz()-funksjonen
    # Hvis bruker sender inn akseptert input for valg av oppgavetype blir de sendt videre til vanskelighetsgrad. 

    if grad == '1' or grad == '2' or grad == '3':
    #Enda en liten if-test for å filtrere ut dårlig input. Hvis akseptert blir quizen satt igang
    
        quiz(start, grad)
    # Kaller på quizen selv og gir den argumentene slik de ble definert etter brukers input. 
    # quiz() sjekker først hvilken oppgave brukeren ønsker, og så vanskelighetsgraden.

    else:
     print('Ikke et gyldig alternativ, start på nytt!')
else: 
    print('Ikke et gyldig alternativ, start på nytt!')
# Hvis bruker ikke skriver inn 1, 2 eller 3 som er alternativene blir de sendt ut og bedt om å starte på nytt. 