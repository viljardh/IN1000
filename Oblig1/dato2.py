# Oppgave 3.3
# Dette programmet leser to datoer på format DD.MM 
# og sjekker om de er i rekkefølge

dato1 = input('Skriv en dato formatert som DDMM (f.eks 0705 for syvende mai) \n')
dato2 = input('Og enda en, samme format\n')
# Leser dato fra input

d1 = dato1[:len(dato1)//2]
m1 = dato1[len(dato1)//2:]
d2 = dato2[:len(dato2)//2]
m2 = dato2[len(dato2)//2:]
# Ikke veldig smidig, men det d1 og d2 henter ut de to første tegnene i strengene som blir
# punchet inn, mens m1 og m2 henter de to siste. len(dato) returnerer selvfølgelig 4
# fordi det er fire siffer vi ber om, delt på 2 er....2. Kunne selvfølgelig skrevet 
# dato[:2] for å få ut de to første eller dato[2:] for å få ut de to siste, men kan 
# i hvert fall late som jeg kan programmere...

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
# tydeligvis forts1tt tall og dets størrelse i strengeformat. 