# Oppg 3

# Denne klasen tar for seg en enkel simulering av en hund. 
# Den har en alder og vekt, og kan trimmes og fores sånn at 
# kan gå opp og ned i vekt. 

# 3.1
class Hund: # Starter med å definereklassen

    def __init__(self, alder, vekt): # Konstruerer med variablene vi tar som parametre
        self._alder = alder          # Lager instansvariable av parametrene
        self._vekt = vekt
        self._metthet = 10           # Og starter med at bikkja har en metthet på 10

# 3.3
    def hent_alder(self):    # Definerer en instansmetode som returnerer
        return self._alder   # alderen på hunden

    def hent_vekt(self):     # Definerer en instansmetode som returnerer
        return self._vekt    # hundens vekt

# 3.4
    def spring(self):        # Definerer en instansmetode som lar den trimme litt
        self._metthet -= 1   # Trim vil redusere metthetsverdien, og hvis den er 
        if self._metthet < 5:# redusert nok vil hunden også gå ned 1 verdi i vekt. 
            self._vekt -= 1

# 3.5    
    def spis(self, mengd):    # Definerer en instansmetode som lar oss mate hunden
        self._metthet += mengd# Tar matmengde som parameter som øker mettheten
        if self._metthet > 7: # Og hvis hunden er over et visst metthetsnivå
            self._vekt += 1   # vil den gå ett hakk op i vekt. 

        
