# Oppg 2

# Dette programmet lar brukeren skrive in en rems med tall
# frem til de skriver 0
# Disse tallene blir lagt til en liste, hele listen skrevet ut
# og så får vi vite summen av elementene i tillegg til 
# hvilket tall i listen som er størst og hvilket som er minst

# 2.1 og 2.2
x = 1           # Lager en vilkårlig ikkenull verdi for å starte
l = []          # En tom liste vi kan legge tallene i
while x != 0:   # Vil kjøre helt til noen skriver 0
    x = int(input('Skriv et heltall (Skriv 0 når du er ferdig)\n'))
    if x != 0:  # Jeg antok siden vi skulle ha minverdien at 0 
        l.append(x) # ikke skulle inkluderes i listen.
    elif input == 0:# Hvis brukeren skriver 0 
        break       # brytes løkka uten at 0 legges til
    else: 
        break       # bryter hvis noen prøver seg på tull

# 2.3
for i in l:     # Itererer over elementene i listen
    print(i)    # og printer de ut

# 2.4
def minSum(l):  # Definerer en funksjon som tar en liste som argument
    x = 0       # En startverdi
    for i in l: # Itererer over verdiene i lista
        x += i  # Legger de sammen i variabelen x
    return x    # Og returnerer summen av verdiene

print(f'Summen av tallene du oppga er {minSum(l)}')
# En liten forklarende beskjed

# 2.5 
min = l[0]      # Definerer en initialverdi som første element
for i in l:     # Itererer over elementene i listen
    if i < min: # Hvis det nye elementet er mindre enn det forrige minste
        min = i # erstatter vi variabelen med det nye minste elementet
print(f'Det minste tallet du oppgav var {min}')
# Printer ut minste element

max = l[0]      # Definerer en initialverdi som første element
for i in l:     # Itererer over elementene i listen
    if i > max: # Hvis det nye elementet er større enn det forrige
        max = i # erstatter vi variabelen med det nye største elementet
print(f'Det største tallet du oppgav var {max}')
# Printer ut største element