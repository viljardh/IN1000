# Oppgave 2: Beslutninger
# Programmet gjør en kjapp if-test som sjekker hvorvidt bruker svarer
# "ja" eller "nei" på et enkelt spørsmål. Tar dessverre ikke hensyn til
# stor forbokstav.

beslutning = input('Vil du ha en brus, ja eller nei?\n')
# Stiller spørsmål og lagrer svaret som streng i en variabel

if beslutning == "ja":          # Tester om svaret er "ja"
    print('Her har du en brus!')# og printer i så fall dette

elif beslutning == "nei":       # Hvis svaret er "nei" printer
    print('Den er grei.')       # den dette heller

else:                           # Hvis det lagres noe annet enn ja eller nei
    print('Den forstod jeg ikke helt.')