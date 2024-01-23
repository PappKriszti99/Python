class Eredmeny:
    def __init__(self, sor):
        adatok = sor.strip().split(';')
        self.Nev = adatok[0]
        self.Rajtszam = int(adatok[1])
        self.Kategoria = adatok[2]
        self.Ido = adatok[3]
        self.Teljesitett = int(adatok[4])