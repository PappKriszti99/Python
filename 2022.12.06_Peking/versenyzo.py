class Versenyzo:
    def __init__(self,fejlec,sor):
        fejlecdb = fejlec.strip().split(";")
        adatok = sor.strip().split(";")
        self.Rajtszam = int(adatok[0])
        self.Nev = adatok[1]
        self.Orsz = adatok[2]
        self.Foldresz = adatok[3]
        self.Eredmenyek = {}
        for i in range(4, len(adatok)):
            self.Eredmenyek[fejlecdb[i]] = float(adatok[i].replace(",", "."))