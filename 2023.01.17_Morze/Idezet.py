class Idezet:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.Szerzo = adatok[0]
        self.IdezettSzoveg = adatok[1]