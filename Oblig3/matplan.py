# Oppgave 4: Matplan
# Dette programmet har en ordbok som inneholder navn på fire beboere 
# i et sykehjem og hver deres frokoster, luncher og middager. 
# Det lages så en funksjon som først lister navnet på alle beboerne
# for så å be brukeren om å skrive et av de. 
# Programmet printer så matplanen deres.

bebmat = {'Hjørdis':['Brødskiver', 'Pannekaker', 'Fiskekaker'],\
    'Diana':['Havregrøt', 'Fruktsalat', 'Lapskaus'],\
    'Henning':['Frokostblanding', 'Potetlefser', 'Grønnsakssuppe'],\
    'Lyder':['Rundstykker', 'Potetsuppe', 'Gryterett']}
# Definerer først ordboken med navnene på beboerne som nøkkelord
# og måltidene deres, i rekkefølge, i en liste som innholdsverdi.

def matplan():
    beblis = list(bebmat)
    # Definerer funksjonen matplan, konverterer ordboken til en liste
    # som gjør det enklere å liste bare nøklene. 
    
    print(f'Her på sykehjemmet bor {beblis[0]}, {beblis[1]}, {beblis[2]} og {beblis[3]}.')
    navn = input('Hvem sin matplan ønsker du å se?\n(Husk stor forbokstav)\n')
    # Printer navnet på beboerne, men kaller på de via indekser. 
    # Litt mer smidig skulle vi ønske å endre på ordboken/listen
    # Ber så om input og lagrer det som en streng i variabelen "navn".
    
    if navn in beblis: 
        print(f'{navn} spiser {bebmat[navn][0]} til frokost, {bebmat[navn][1]} til middag, og {bebmat[navn][2]} til kvelds.')
        # Liten if-test for å sjekke om navnet er i registeret. 
        # I hvis tilfelle blir navnet deres pluss deres foretrukne
        # retter til frokost, lunch og middag skrevet ut. 
    
    elif navn not in beblis:
        print(f'Beklager, vi finner ikke {navn} i våre registre. Brukte du stor forbokstav?')
        # Hvis navnet ikke er i registeret er det ikke så mye
        # info om de å hente, og vi får en feilmelding. 

    else:
        print('!!ERROR!!')
        # Aner ikke hvordan du skulle fått denne feilen, men
        # jeg slang den med lell. 

matplan()
# Kaller funksjonen

"""
Jeg er klar over at jeg kunne behandlet input litt bedre, tillatt 
bruker å skrive i lowercase for så å konvertere første karakter
i en streng til stor bokstav, men orker ikke akkurat nå.  

Oppgave 4.3

a. Ordbok eller mengde.
Hadde det vært av interesse å ha brukerens faktiske navn koblet
til brukernavnet hadde ordbok vært mest interessant. 
Hvis ikke kunne vi brukt mengde, da det kun skal være unike brukernavn.

b. Ordbok
Her vil definitivt at to elementer skal være koblet i en liste, 
og er da ordboken skinner klarest. 

c. Liste
Hvis det kun skulle vært en liste av navn på rekke er det liste
som gjelder, for her kan samme navn dukke opp igjen. 

d. Ordbok
Igjen, veldig interessert i å koble to elementer sammen, vite 
hvem som har hvilke allergier, spesielt for å kunne slå opp. 

"""