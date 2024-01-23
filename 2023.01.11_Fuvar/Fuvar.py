class Fuvar:
    def __init__(self, sor):
        adatok = sor.strip().split()
        self.Nap = int(adatok[0])
        self.Sorszam = int(adatok[1])
        self.Tav = int(adatok[2])