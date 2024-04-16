# Oppg 4

# Dette programmet har to funksjoner - først antele() som tar
# en streng eller en liste/mengde strenger og forteller hvor
# mange elementer det er i den, dvs for strenger antall bokstaver
# og for lister/mengder antall elementer. 
# Deretter defineres en funksjon som, gitt en setning, finner ut
# hvor mange unike ord det er og hvor ofte de forekommer, returnert
# som en ordbok.
# Til slutt inviteres brukeren til å skrive sin egen setning, 
# og det vil da skrives ut hvor hvor mange ord og unike ord
# setningen har, i tillegg til hvor ofte hvert ord forekommer.

# 4.1
def antele(ord):    # Definerer funksjonen "antall elementer"
    c = 0           # Initialverdi for telleren er 0
    for i in ord:   # Itererer over elementene i input
        c += 1      # Inkrementerer teller
    return c        # Gir telleren som output

# 4.2
def antset(setn):         # Definerer funksjoner "antall ord i setning"
    bok = {}              # En tom ordbok vi kan fylle
    setn = setn.split(' ')# Lager en liste av alle ordene i setningen
    setu = set(setn)      # Og lager en mengde sånn at vi har en liste med kun unike elementer
    for i in setu:        # Vi itererer da over de *unike* elementene
        i = i.lower()     # (orker ikke styre med case)
        bok[i] = 0        # setter verdien til nøkkelen til null som initialverdi
        for j in setn:    # itererer så over hele setningen som den er (bare som en liste)
            j = j.lower()
            if i == j:    # og hvis ordet dukker opp vil vi inkrementere telleren i ordboka
                bok[i] += 1# og lagrer nøkkelen med antall ganger den dukker opp i setningen
    return bok            # Gir da ordboken med unike ord som nøkler og antall ganger de er der
                          # som verdi
# Jeg ser i ettertid at jeg kunne gjort det mye enklere siden ordbøker bare tar unike nøkler
# men lar det stå som det er. 

# 4.3

inp = input('Skriv en setning, vær kreativ!\n') # Hyggelig oppmuntring til å bruke programmet
inps = inp.split(' ')                           # Lager en liste over alle ordene i setningen
bok = antset(inp)                               # Og en ordbok som tar setningen som kaller på funksjonen 

print(f'Det er {antele(inps)} ord i setningen din, og {antele(set(inps))} av de er unike!')
# Printer litt info, kaller på funksjonen som teller antall elementer og konverterer til mengde
# for å gi antall unike

for k in bok: # Itererer da over nøklene i ordboken og skriver ut infoen. 
              # Lagt på litt ekstra flesk for å få utskrift som foreslått i oppgaveteksten, 
              # men ideen er at den printer ut nøkkelordet, kaller på ordboken for å få ut 
              # antall ganger det forekommer, og kaller på "antall elementer" for å finne 
              # ut hvor langt det er. Lagt inn et par if-tester for grammatikken sin skyld, 
              # orket ikke å mekke at den sjekker for tegn eller tall. Huff. 

    if antele(k) == 1: # Hvis ordet kun har en bokstav/ett tegn
        if bok[k] == 1: # Hvis ordet kun forekommer en gang
            print(f'Ordet "{k}" forekommer {bok[k]} gang og har {antele(k)} bokstav.')
        else:
            print(f'Ordet "{k}" forekommer {bok[k]} ganger og har {antele(k)} bokstav.')
    else:
        print(f'Ordet "{k}" forekommer {bok[k]} ganger og har {antele(k)} bokstaver.')
# Printefunksjonen printer da ordet, altså nøklen det itereres over, kaller på ordboken for å få
# antall forekomst da det er verdien, og kaller på tellefunksjonen for å si hvor mange bokstaver det er. 