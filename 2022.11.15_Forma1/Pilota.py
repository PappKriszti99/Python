class Pilota:
    def __init__(self, sor):
        adatok = sor.strip().split(';')
        self.Nev = adatok[0]
        self.SzulDatum =  adatok[1]
        self.Nemzetiseg = adatok[2]
        self.Rajtszam = adatok[3]