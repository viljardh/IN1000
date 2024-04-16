# Oppgave 5

# I denne oppgaven skal du lage en ordbok som har modellnavnet på en pistol
# som nøkkel, og IPSC-divisjonene den er godkjent i som innholdsverdi. 
# List modellene. Be bruker skrive inn en modell og en divisjon, og gi
# tilbakemelding hvorvidt den er godkjent eller ikke. 
# Hvis de skrive inn feil navn på modell eller divisjon, gi feilmelding.

# Dette programmet tar for seg en liste pistoler og divisjonene de er godkjente i. 
# Den ber bruker om et modellnavn og divisjon som input, sjekker den oppmot ordboken
# og gir tilbakemelding hvorvidt pistolen er godkjent i divisjonen bruker foreslår. 

pistlist = {'CZ SP-01':['Prod', 'Standard', 'Open'],\
            'Shadow2':['Prod', 'Standard', 'Open'],\
            'Glock 17':['Prod', 'Standard', 'Open'],\
            'BUL Trophy':['Classic', 'Standard', 'Open'],\
            'Kimber Target':['Classic', 'Standard', 'Open'],\
            'BUL SAS':['Standard', 'Open'],\
            'Browning Hi-Power':['Standard', 'Open'],\
            'CZ Czechmate':['Open'],\
            'STI DVC':['Standard', 'Open'],\
            'SVI Custom':['Open']}
# Definerer ordbok med vilkårlig valgte pistolmodeller som nøkkel og divisjonene
# de er godkjente i som innholdsverdi. 

modlist = list(pistlist)
divlist = ['Prod', 'Classic', 'Standard', 'Open']
# Lager liste av nøkkelordene pluss en liste med divisjonene i IPSC (forenklet)

print('Liste over modeller du kan velge mellom:') # Gir kontekst til hva som kommer

for pist in modlist:    # Printer alle nøklene på rams
    print(pist)         # dvs navnet på mo dellene bruker kan velge mellom.


def sjekk():            # Definerer en funksjon som tar modell og divisjon som input
                        # og sjekker om de går overens. Sjekker også om input
                        # gir mening
    mod = input('Hvilken modell? (Skriv presist navn!)\n')
    # Ber bruker skrive et modellnavn

    if mod in pistlist:
        # If-test for å sjekke om modellen er i listen over modeller vi tar for oss
        
        div = input('Vil du bruke den i Prod, Classic, Standard eller Open?\n')
        # I hvis tilfelle ber programmet brukeren om en divisjon

        if div in divlist:
            # Hvis divisjonen er i listen godkjente divisjoner går vi videre

            if div in pistlist[mod]:
                print(f'{mod} er godkjent til bruk i {div}!')
                # Sjekker om divisjonen er listet i innholdsverdien til modellen
                # og sier i så tilfelle fra.

            elif div not in pistlist[mod]:
                print(f'{mod} er ikke godkjent til {div}.')
                # Sjekker om divisjonen *ikke* er listet, i hvis tilfelle
                # den ikke er godkjent og sier så ifra.
                 
            else:
                print('!!ERROR!!')#Backupfeilmelding
        
        elif div not in divlist:
            print('Dette er ikke en gyldig divisjon.')
            return
            # Sjekker inputen. Hvis divisjonen bruker skriver ikke er listet
            # blir funksjonen avsluttet og bruker får tilbakemelding om hva 
            # som ble skrevet feil. 

        else:
            print('!!ERROR!!')#Backupfeilmelding
        
    elif mod not in pistlist:
        print('Dette er ikke en gyldig modell.')
        # Sjekker inputen. Hvis divisjonen bruker skriver ikke er listet
        # blir funksjonen avsluttet og bruker får tilbakemelding om hva 
        # som ble skrevet feil. 

    else: 
        print('!!ERROR!!')#Backupfeilmelding

sjekk() # Kjører funksjonen