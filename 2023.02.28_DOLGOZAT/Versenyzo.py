class Versenyzo:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.Nev = adatok[0]
        self.Kategoria = adatok[1]
        self.Egyesulet = adatok[2]
        self.Pontok = []
        for i in range(3,len(adatok)):
            self.Pontok.append(int(adatok[i]))

    def PontSzamit(self):
        ossz = 0
        self.Pontok.sort()
        if self.Pontok[0] > 0:
            ossz += 10
        if self.Pontok[1] > 0:
            ossz += 10
        for i in range(2, len(self.Pontok)):
            ossz += self.Pontok[i]
        return ossz