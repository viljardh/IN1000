# Oppg 3

# Dette programmet gjør ymse funksjoner i python, men failer
# som forklart på bunn. 

def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
#        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()

"""
Først defineres minFunksjon() som ikke tar argumenter, deretter
hovedprogram() som heller ikke tar argumenter. Den vil så forsøke 
å kjøre hovedprogrammet - a blir satt til å være 42, b blir satt til 0
Den printer så b til terminalen, altså 0, før den da setter b til å være
lik a som er 42 - b er nå 42. Nå kaller den på den første funksjonen som 
ble definert, og en for-løkke blir satt i gang. x in range to vil først
starte med x = 0. c blir da satt til lik 2 og printet ut til terminal. 
Deretter blir den inkrementert med 1, c nå lik 3, og b blir satt til 10.
Nå kommer en feil da a aldri har blitt definert, og programmet vil
avsluttes med feilmelding som sier nettopp det. 
"""