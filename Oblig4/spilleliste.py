# Oppg 5

# I denne oppgaven skal du lage et program som lar bruker
# lagre en spilleliste med sang som nøkkel og følgende som 
# innholdsverdi: Navn på artist, album, og sjanger.
# La brukeren skrive inn sanger og info til de ikke ønsker mer, 
# og så gi de muligheten til å søke opp basert på hva de husker 
# eller ønsker, dvs søke etter artist, artist eller sjanger. 
# Sorter resultatet slik at bruker får grei oversikt. 

# Dette programmet lar brukeren lagre en spilleliste av sanger
# med info i en ordbok. Deretter lar den brukeren søke opp sanger
# som fyller kriterier de søker med, om det er nøkkel eller verdi.

x = 'y'             # Setter initialverdi med utgangspunkt i at bruker
spilleliste = {}    # ønsker å lage en spilleliste.
while x == 'y':     # Mens bruker fortsatt vil legge til er løkka aktiv
    print('Skriv navnet på en sang du ønsker å legge til:')
    san = input('(Husk case sensitivity)\n')
    art = input('Hva heter artisten eller gruppen?\n')
    alb = input('Hvilket album er sangen fra?\n')
    sja = input('Hva slags sjanger er det?\n')
    # Lager strengvariable for å midlertidig lagre dataen

    spilleliste[san] = art, alb, sja
    # Bruker sangtittel som nøkkel da den har størst sjanse for å være unik
    # Hvis f.eks flere sanger av samme artist eller samme sjanger. 
    # Lager da ordliste som lagrer artist, album og sjanger som verdi.

    x = input('Ønsker du å skrive inn flere? \ny/n: ')
    # Sjekker om bruker vil legge til flere sanger. Hvis de skriver
    # noe annet enn "y" stopper løkka.

""" !!! TESTLISTE !!!
spilleliste = {'Epitaph':('King Crimson', 'In The Court Of The Crimson King', 'Prog'),\
            'Niwashi KING':('Susumu Hirasawa', 'Kyuusai No Gihou', 'Electronic'),\
            'Oddfellows':('Tomahawk', 'Oddfellows', 'Alternative'),\
            'Test':('Tomahawk', 'Oddfellows', 'Alternative'),\
            'Hong Kong':('Gorillaz', 'D-Sides', 'Fusion'),\
            'The River':('King Gizzard And The Lizard Wizard', 'Quarters!', 'Alternative'),\
            'Armee Der Tristen':('Rammstein', 'Zeit', 'Industrial'),\
            'Elektrik':('King Crimson', 'The Power To Believe', 'Prog'),\
            'Ghost Bridge':('Susumu Hirasawa', 'Kyuusai No Gihou', 'Electronic'),\
            'God Hates A Coward':('Tomahawk', 'Tomahawk', 'Experimental'),\
            'Alter Mann':('Rammstein', 'Herzeleid', 'Industrial'),\
            'Nuclear Fusion':('King Gizzard And The Lizard Wizard', 'Flying Microtonal Banana', 'Alternative'),\
            'Rammstein':('Rammstein', 'Herzeleid', 'Industrial'),\
            'Tattoo':('Rammstein', 'Rammstein', 'Industrial')}
"""
print('Hva ønsker du å høre på? Oppgi sang, artist, sjanger eller album')
inp = input('(Husk store bokstaver)\n') # Lar bruker skrive inn søketekst
# Jeg gjør det enkelt for meg selv og insisterer på riktig bruk av store 
# og små bokstaver. 

# OK denne ble ikke pen, men bær med meg
if inp in spilleliste:
    # Først sjekker den om det bruker søker på er en sangtittel i seg selv
    # Og skriver dermed ut en veldig sløvt formatert liten informasjonsrubrikk
    # med sanger som har den tittelen
    print('\n  Sangtittel: ', inp, '\n')
    print('      Artist:', spilleliste[inp][0])
    print('       Album:', spilleliste[inp][1])
    print('     Sjanger:', spilleliste[inp][2])
    print('             -                ')

    # Denne er her i tilfelle sangtittelen er den samme som sjangeren, album- eller bandnavn. 
    # Ulempen er at den sangen blir skrevet ut to ganger, men det får vi nesten overleve. 
    for i in spilleliste:# Henter da ut i som nøkkel og går gjennom verdiene der
        if inp in spilleliste[i]:# Og hvis det bruker søkte på ligger der, print ut info
                print('\n  Sangtittel: ', i,  '\n')
                print('      Artist:', spilleliste[i][0])
                print('       Album:', spilleliste[i][1])
                print('     Sjanger:', spilleliste[i][2])  
                print('             -                ')

else: # Hvis bruker ikke søker på sangtittel, må vi gå gjennom nøklene og sjekke
    for i in spilleliste:# Henter da ut i som nøkkel og går gjennom verdiene der
        if inp in spilleliste[i]:# Og hvis det bruker søkte på ligger der, print ut info
                print('\n  Sangtittel: ', i,  '\n')
                print('      Artist:', spilleliste[i][0])
                print('       Album:', spilleliste[i][1])
                print('     Sjanger:', spilleliste[i][2])
                print('             -                ')
