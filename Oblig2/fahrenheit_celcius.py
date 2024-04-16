# Oppgave 2
# Dette programmet tar en temperatur i fahrenheit som
# input, konverterer det til celcius og gir som output

tempf = input('Skriv en temperatur i fahrenheit:\n')
tempf = float(tempf)
# Spør om temperatur i F som input, tilegner en variabel
# og konverterer den fra string til float

print(f'Temperaturen er {tempf:.2f} grader fahrenheit')
# Printer ut temperaturen i F med to desimaler
# (Synes det ser renere ut)

tempc = (tempf-32)*(5/9)
# Foretar konverteringen og tilegner ny variabel

print(f'Temperaturen er {tempc:.2f} grader celsius')
# Printer den konverterte temperaturen i C
# Formatert til å ha to desimaltall