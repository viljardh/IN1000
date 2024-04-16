# Oppgave 1: Lister
# Dette programmet lager en liste av tre vilkårlige tall
# valgt av bruker (rgb-verdier for Microsoft sin mørkeblå)
# Deretter bruker vi "append"-funksjonen til å legge til et tall
# i listen etter den har blitt laget. 

# Deretter tar programmet fire navn fra brukeren og legger de 
# i en liste. Den sjekker så om et av navnene brukeren oppga
# er det samme som skaperen av programmet, og skriver så en 
# oppmuntrende beskjed. Hvis ikke, en litt mindre oppmuntrende beskjed. 

# Til sist gjør den noen listeoperasjoner - summen og produktet av 
# tallene i den første listen blir lagret i sin egen liste. Blir så 
# lagt til og fjernet igjen som oppgaveteksten ba om. 


# 1.1
list1 = [1, 36, 86]         # Definerer en liste med heltall
list1.append(2)             # Legger til 2 helt til sist
print(list1[0], list1[2])   # Indeks starter på 0 i python, så
                            # Her hentes første og tredje tall i lista

# 1.2
list2 = []                  # Definerer tom liste
print('Husk å skrive med stor forbokstav!\n')
n1 = input('Si et navn: \n')
n2 = input('- og et til\n')
n3 = input('- og et til\n')
n4 = input('- og et siste\n')
# Ber om fire navn og tilegner variable

list2.append(n1)
list2.append(n2)
list2.append(n3)
list2.append(n4)           
# Legger navnene inn på rekke i lista
# Kunne gjort det direkte, men synes
# dette er ryddigere

#1.3
if 'Viljar' in list2:       # Hendig funksjon i python som kan sjekke om
    print('Du husket meg!') # et element er i en liste
                            # I så tilfelle en oppmuntrende beskjed

elif 'Viljar' not in list2: # Hvis navnet mitt ikke er i listen bruker
    print('Glemte du meg?') # skrev, en litt mindre oppmuntrende beskjed

else:                       # Igjen, sånn backup-backup feilmelding
    print('Hvordan fikk du til dette?')

#1.4
s = sum(list1)      # Summerer alle elementene i en liste og lagrer til s
p = list1[0] * list1[1] * list1[2] * list1[3] # Ganger over alle elementene
# OK så dette var litt rart - math-modulen skal egentlig ha en funksjon
# som ganger over alle elementene. Den funket på laptopen min, men fikk 
# feilmelding da jeg prøvde å kjøre på UiO sin server om at den ikke eksisterte
# import math
# p = math.prod(list1)

list3 = [s, p]      # Lager en ny liste med sum og produkt som elementer

list4 = list1 + list3 # Konkatedralerer den originale og nye listen
list4.pop(-1)         # og lager en helt ny liste igjen.
list4.pop(-1)         # pop fjerner et element gitt index, og index 
print(list4)          # -1 er siste elementet. 
# Printer sluttproduktet. 