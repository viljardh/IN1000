# Oppg1

# Dette programmet gjør litt bøy og tøy med funksjoners returverdi
# Først en enkel addisjon, så gir bruker mulighet til å sjekke hvor
# ofte en bokstav forekommer i en streng. 

# 1.1
def adder(a, b):    # Definerer funksjonen og krever to argumenter
    return a+b      # Legger sammen argumentene og gir de som output

print(f'4 + 7 = {adder(4, 7)} og 654564 + 789653 = {adder(654564, 789653)}')
# Ufin men effektiv liten print av et par resultater av funksjonen

# 1.2 og 1.3
inps = input('Skriv noe, faceroll, samme hva: \n')
inpc = input('Skriv et tegn: \n')
# Ber om hhv streng og enkel karakter som input

def tellForekomst(minTekst, minBokstav):
    c = 0                   # Starter en teller
    for i in minTekst:      # Itererer over elementene i strengen
        if i == minBokstav: # Sjekker om gitt karakter er en del av strengen
            c += 1          # Inkrementerer telleren i hvis tilfelle
    return c                # Returnerer tellern

print(f'{inpc} forekommer {tellForekomst(inps, inpc)} ganger i strengen du oppgav.')
# Printer ut brukers bokstav og hvor mange ganger den forekommer i strengen