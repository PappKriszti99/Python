from datetime import time

class Vizsgazo:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.Nev = adatok[0]
        self.VizsgaTipus = adatok[1]
        idodb = adatok[2].split(":")
        self.Ido = time(0, int(idodb[0]), int(idodb[1]))
        self.Eredmeny = int(adatok[3])