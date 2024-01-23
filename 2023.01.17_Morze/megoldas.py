from Idezet import *

class Megoldas:
    def __init__(self):
        self.Abc = {}
        self.Szovegek = []

    def AbcOlvas(self):
        f = open("morzeabc.txt", "r", encoding="utf-8")
        f.readline()
        for sor in f:
            adatok = sor.strip().split("\t")
            self.Abc[adatok[0]] = adatok[1]
        f.close()

    def MorzeOlvas(self):
        f = open("morze.txt", "r", encoding="utf-8")
        for sor in f:
            self.Szovegek.append(Idezet(sor))
        f.close()

    def GetAbcHossz(self):
        return len(self.Abc)

    def GetChar(self, beker):
        if beker in self.Abc.keys():
            return self.Abc[beker]
        return ""

    def Morze2Szoveg(self, szoveg):
        eredmeny = ""
        szavak = szoveg.split("       ")
        for szo in szavak:
            index = 0
            karakterek = szo.split("   ")
            for kar in karakterek:
                for key, value in self.Abc.items():
                    if value == kar:
                        eredmeny += key
            eredmeny += " "
        return eredmeny[:-1]

    def ElsoFordit(self):
        return self.Morze2Szoveg(self.Szovegek[0].Szerzo)

    def LeghosszabbKeres(self):
        maxSzoveg = self.Morze2Szoveg(self.Szovegek[0].IdezettSzoveg)
        idezo = self.Szovegek[0].Szerzo
        for szoveg in self.Szovegek:
            leforditott = self.Morze2Szoveg(szoveg.IdezettSzoveg)
            if len(maxSzoveg) < len(leforditott):
                maxSzoveg = leforditott
                idezo = szoveg.Szerzo
        return f"{self.Morze2Szoveg(idezo)}: {maxSzoveg}"

    def GetArisztotelesz(self):
        idezetek = []
        for szoveg in self.Szovegek:
            if self.Morze2Szoveg(szoveg.Szerzo) == "ARISZTOTELÉSZ":
                idezetek.append(self.Morze2Szoveg(szoveg.IdezettSzoveg))
        return idezetek

    def FajlIr(self):
        f = open("forditas.txt", "w", encoding="utf-8")
        for szoveg in self.Szovegek:
            f.write(f"{self.Morze2Szoveg(szoveg.Szerzo)}: {self.Morze2Szoveg(szoveg.IdezettSzoveg)}\n")
        f.close()

        
