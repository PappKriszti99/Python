class Fuvar:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.ID = int(adatok[0])
        self.Indulas = adatok[1]
        self.Idotartam = int(adatok[2])
        self.Tavolsag = float(adatok[3].replace(",", "."))
        self.Viteldij = float(adatok[4].replace(",", "."))
        self.Borravalo = float(adatok[5].replace(",", "."))
        self.Fizmod = adatok[6]