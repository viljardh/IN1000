# Oppg 4 

# Dette programmet leser inn temperaturdata fra fil og organiserer de i en ordbok
# Deretter sammenligner den listen med rekordtemperaturer med en liste som inneholder
# temperaturer målt for et helt år, sier ifra og endrer i ordboken hvis det er ny 
# varmest temperatur. 

# 4.1
def makeDic(fnvn):              # Definerer funksjon: Tar filnavn som skal leses som input
    dic = {}                    # Lager en tom ordbok vi kan legge ting i
    for i in open(fnvn, 'r'):   # Itererer gjennom alle linjene i filen, read-only
        i = i.strip().split(',')# Behandler linjen sånn at vi får all dataen i en liste
        dic[i[0]] = float(i[1]) # Vet at index 0 i liten er mnd og index 1 er temperaturen
    return dic                  # Blir så lagt til i ordboken med mnd som nøkkel og temp som verdi
    # Returnerer ordboken med makstemperaturen pr mnd

maxMonth = makeDic('max_temperatures_per_month.csv') # Kaller på funksjonen som gir os ovennevnte ordbok
print(maxMonth) # Printer den ut

# 4.2 og 4.3
def varmDag(dic, fnvn):         # Denne funksjoen tar da en ordbok og et filnavn som skal leses som input
    for i in open(fnvn, 'r'):   # Går gjennom hver linje i filen, read only  
        i = i.strip().split(',')# Rensker input igjen, får pen liste med data
        temp = float(i[2])      # Temperaturen den aktuelle mnd har index 2, tredje element
        if temp > dic[i[0]]:    # Nøkkelen i ordboken er bestemt av linjen den er på i tekstfilen
            dic[i[0]] = temp    # Så den sjekker da temperaturen for den aktuelle mnd. Hvis temperaturen
                                # en måned i den nye listen er større enn den fra den vi lagde forrige oppgave
                                # blir ordboken oppdatert med den nye temperaturen. 

            #print(f'Ny varmerekord {i[1]} {i[0]}: Ny rekord er {temp} grader Celcius')
            #print(f'Gammel rekord var {dic[i[0]]}\n')
            # Printefunksjon for den forrige oppgaven
    return dic# Returnerer den oppdaterte ordboken

maxDaily = 'max_daily_temperature_2018.csv' # Gjør det litt ryddigere og lagrer filavnet som streng i en variabel
nyvarmestdag = varmDag(maxMonth, maxDaily)
print(nyvarmestdag)          # Kaller på funksjonen som lager den oppdaterte ordboken 

# 4.4
def skrivVarmDag(dic, fnavn): # Definerer funksjonen, tar ordbok og filnavn som arg
    nvd = open(fnavn, 'w')    # Åpner en blank fil med filnavnet gitt input
    for i in dic:             # Itererer over mnd i ordboken med varmeste dager
        nvd.write(i + ',' + str(dic[i]) + '\n') # Skriver de inn i tekstfilen  med formateringen
    nvd.close()               # Lukker txt-filen
skrivVarmDag(nyvarmestdag, 'nyvarmestdag.txt') # Kaller på og kjører funksjonen som skriver den
                                               # oppdaterte listen med varmeste temperaturer pr mnd

# 4.5
def varmebolge(fnavn):  # Definerer funksjonen, tar filnavn som input
    list = []
    for i in open(fnavn, 'r'):
        list.append(i.strip().split(','))
    # Finnes sikkert enklere måte å gjøre dette på via readlines eller noe, men orker ikke.
    # Lager en liste med all informasjonen heller. 

    c = 1 # Telleren starter på indeks 1 i dag, fordi jeg sjekker temperaturen forrige dag

    for i in range(1, len(list)-1): # Jeg jukset litt her, og antok det ikke var hetebølge 27-31 desember
        ptemp = float(list[i-1][2]) # Sjekker tempen fra dagen før nåværende indeks
        ctemp = float(list[i][2])   # Og tempen på "dagens" indeks
        if ptemp >= 25 and ctemp >= 25: # Hvis vi har to dager på rad med temp over 25 kan vi gå videre
            if c >= 5:                  # Hvis det har vært fem eller flere dager med hete må vi si ifra
                if float(list[i+1][2]) < 25: # Men kun hvis dagen etter nåværende indeks ikke er en del av bølgen
                    d1 = list[i-c]      # Starten av hetebølgen vil være dagens minus hvor mange dager det har vært hete
                    d2 = list[i]        # og slutten vil være nåværende dag, før neste som vil bli under 25 C
                    print(f'Det var hetebølge fra {d1[1]} {d1[0]} til {d2[1]} {d2[0]}')
                    c = 1           # Resetter telleren
                else:
                    c += 1            # Hvis neste dag ikke er under 25, er den over 25, og hetebølgen pågår ennå
            else:
                c += 1               # Hvis dagens, forrige og neste dags temperatur er over 25, teller vi videre
        else:
            c = 1                   # Hvis ikke, resetter vi telleren 


varmebolge(maxDaily)
# Kaller på funksjonen