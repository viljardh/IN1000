# Oblig 2 Oppg 1.1 og 1.2
# Dette prorammet tar navn og sted som input
# fra bruker og printer ut brukerens navn
# og hvor de sier de kommer fra. 

def utskrift():
    # Definerer en funksjon vi kan kalle på
    
    navn = input('Skriv inn et navn: ')
    sted = input('Hvor kommer du fra? ')
    # Henter navn og sted som input, tilegner de
    # som strenger til variable
    
    print(f'Hei {navn}! Du er fra {sted}.')
    # Printer en liten hilsen med navn og hvor bruker
    # sier de er fra.

utskrift()
utskrift()
utskrift()
# Kaller funksjonen tre ganger slik at alt går på rekke og rad