# Oppgave 4

# Dette programmet sender all informasjonen klassen Verden trenger 
# for å skape en liten verden til et sett tilfeldig genererte celler
# og lar oss gå fremover i generasjonene så lenge brukeren ønsker. 
# Dette er et lite ASCII Game of Life, dog litt redusert. 

from verden import Verden

def hovedprogram(): # Setter sirkuset i gang

    inp = input('Hvor stort brett vil du ha? \nFormat: [tall]x[tall] f.eks 100x100\n')
    inp = inp.split('x')                # Tar brettstørrelse som input, gitt format
    v = Verden(int(inp[1]), int(inp[0]))# Og lager en verden deretter. 
    v.tegn()                            # Printer ut første (0-te) generasjon
    
    x = True            # Initialverdi, lager en enkel menyloop
    while x:            # Mens bruker vil fortsette
        x = input('Press Enter for å fortsette, eller q for å avslutte\n')
        v.oppdatering() # Hvis bruker vil fortsette, skyver vi verden en generasjon videre
        v.tegn()        # Og tegner den slik at brukeren får se
        if x != 'q':    # Enklest - Så lenge bruker ikke vil avslutte, fortsetter vi
            x = True    # Dette tillater å bare trykke enter for å iterere. 
        else:           # Ellers
            x = False   # Avslutter vi
            
# starte hovedprogrammet
hovedprogram()