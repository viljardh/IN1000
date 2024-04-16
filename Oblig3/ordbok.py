# Oppgave 2: Ordbok
# Dette programmet tar for seg en ordbokliste over varer
# med deres pris, definerer så en funksjon som bruker
# kan kalle på for å legge til varer og deres pris i ordboken

varer = {'melk':14.9, 'brød':24.9, 'yoghurt':12.9, 'pizza':39.90}
print(varer)
# Definerer og printer ut ordboken med nøkler og innholdsverdier

def nyvare(): # Definerer funksjon fordi jeg ville
    v = input('Hviken vare ønsker du å legge til?\n')
    p = float(input('- og hvilken pris ønsker du å gi den?\n'))
    # Tilegner foreslått varenavn til variabel v som streng 
    # og tilegner foreslått pris til variabel p som flyttall

    varer[v] = p
    # Legger foreslått vare og tilhørende pris til i ordlisten

nyvare()
nyvare()
# Kaller på funksjonen to ganger for å legge til to nye elementer

print(varer)
# Skriver ut den modifiserte ordboken