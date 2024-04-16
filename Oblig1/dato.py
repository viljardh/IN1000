# Oppgave 3: Problemløsning med beslutninger
# Dette programmet leser datoer bruker foreslår 
# og forteller hvorvidt de er etter hverandre eller like

d1 = int(input('Dato Dag1\n'))
m1 = int(input('Dato Mnd1\n'))

d2 = int(input('Dato Dag2\n'))
m2 = int(input('Dato Mnd2\n'))
#Inputs for datoene

if m1 < m2: 
    print('Riktig rekkefølge!')

elif m1 > m2:
    print('Feil rekkefølge!')

    # Hvis ene mnd er større enn det andre har det ikke
    # noe å si hva dagen er. Sjekker for det først. 

elif m1 == m2:  # Hvis mnd er den samme må vi gjøre en sjekk på dagene
    if d1 == d2:# for å finne hvem som er større, eller om de er like
        print('Samme dato!')

    elif d1 < d2:
        print('Riktig rekkefølge!')
    
    elif d1 > d2:
        print('Feil rekkefølge!')
# Kunne egentlig skrevet "else" istf en elif-sjekk, men ser tydeligere ut
# med elif IMO
# Er også klar over at jeg sammenligner strenger, men python forstår 
# tydeligvis fortsatt tall og dets størrelse i strengeformat. 
