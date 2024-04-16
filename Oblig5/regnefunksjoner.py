# Oblig 5
# Dette programmet definerer noen enkle funksjoner
# som foretar matematiske operasjoner.
# De blir validert via "assert"-funksjonen, og til slutt
# kalt på med litt formatering. 

#Oppg 1

#1.1
def addisjon(a, b): # Definerer funksjonen til å ta to elementer
    return a + b    # Og returnerer summen

x = 5               # Definerer verdier til å sende inn
y = 6               # i funksjonen
# For deretter å kalle på funksjonen og printe resultatene. 
print(f'{x} + {y} = {addisjon(x, y)}')


#1.2
def subtraksjon(a, b):# Definerer funksjonen til å ta to elementer
    return a - b      # og returnerer ene trukket fra andre.

# Sjekker at det stemmer via "assert"-funksjonen
assert 6 == subtraksjon(9, 3)
assert 1 == subtraksjon(-1, -2)
assert -43332 == subtraksjon(-34567, 8765)

def divisjon(a, b): # Definerer funksojnen til å ta to elementer
    return a/b      # Returnerer divisor delt på divident.

# og sjekker om de også stemmer via "assert"
assert 3 == divisjon(6, 2)
assert 4 == divisjon(-8, -2)
assert -3 == divisjon(-12, 4)

#1.3
def tommerTilCm(antallTommer): # Definerer funksjonen til å ta kun et
    assert antallTommer > 0    # element, "asserter" at det er større 
    return antallTommer*2.54   # enn 0, og konverterer fra cm til tommer.

x = 10 # Setter en verdi, kaller på funksjonen, og printer med litt formatering.
print(f'{x} cm er {tommerTilCm(x):.2f} tommer.')

#1.4
def skrivBeregninger():     # Definerer printefunksjonen
    
    print('Utregninger:')   # Printer sånn at det ligner litt på forslag
    inpa = float(input('Skriv et tall: '))  # Tar to inputs
    inpb = float(input('Skriv et til: '))   # og konverterer til flyttall
    
    print('')               # Litt formatering
    
    # Printer ut med formatering hvor man kaller på funksjonene
    # gitt brukers input. 
    print(f'Resultat av summering: {addisjon(inpa, inpb):.1f}')
    print(f'Resultat av subtraksjon: {subtraksjon(inpa, inpb):.1f}')
    print(f'Resultat av divisjon: {divisjon(inpa, inpb):.1f}')
    
    print('') # Litt formatering
    
    print('Konvertering fra tommer til cm:')
    inpc = float(input('Skriv inn et tall:')) # Ber om input, lagrer som float
    print(f'{inpc} cm er {tommerTilCm(inpc):.2f} tommer.') # Printer og kaller på funksjon

#1.5
skrivBeregninger() # Kaller på funksjonen som gjør alle beregningene og ber om input