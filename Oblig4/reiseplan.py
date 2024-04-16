# Oppgave 3

# Dette programmet tar input og lagrer de i tre lister
# for så å slå de sammen til én. Deretter lar den bruker
# kalle på elementer i den nye sammenslåtte listen
# via input, og sjekker at inputen er gyldig. 

# 3.1, 3.2
steder = []         # Definerer tre tomme lister
klesplagg = []      # Brukeren kan fylle med det
avreisedato = []    # De måtte ønske

for i in range(5): #Vil da gå over indeks 0-4
    steder.append(input('Skriv et reisemål:\n'))
    klesplagg.append(input('Skriv et klesplagg:\n'))
    avreisedato.append(input('Skriv en avreisedato:\n'))
    # Legger inn input fra bruker i hver sine lister fem ganger

"""
steder = ['Oslo', 'Volda', 'Andebu', 'Mo i Rana', 'Levanger']
klesplagg = ['Skjorte', 'Regnjakke', 'Softshelljakke', 'Vinterjakke', 'Sterkt Tau']
avreisedato = ['09.08.22', '02.04.34', '02.06.44', '23.02.40', '06.07.04']
""" # Testliste, vennligst ignorer.

# 3.3
reiseplan = [steder, klesplagg, avreisedato] # Slår sammen listene
# Vi har de en liste med tre elementer, hvert av hvis er en liste

# 3.4
for i in reiseplan: # Itererer over elementene i lista
    print(i)        # og printer de ut.

# 3.5

liste_indeks1 = int(input('Skriv et tall mellom 0 og 2\n'))
liste_indeks2 = int(input('Skriv et tall mellom 0 og 4\n'))
# Tar indeks som input fra bruker og lagrer til variable som heltall

if liste_indeks1 >= 0 and liste_indeks1 <= 2:           # Manuell sjekk
    if liste_indeks2 >= 0 and liste_indeks2 <= 4:       # På at alt er
        print(reiseplan[liste_indeks1][liste_indeks2])  # i rekkevidde
        # Hvis indeksene bruker oppga er i rekkevidde printer vi ut
        # elementet i lista med de indeksene
    else:
        print('Ikke gyldig input')
else:
    print('Ikke gyldig input')
# Ellers printer vi at det ikke er gyldig input. 
# Ideelt ville jeg tatt en if-test på input 1
# *før* vi ga input 2, men valgte å følge oppgave-
# teksten bokstavelig.
