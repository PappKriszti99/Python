from Versenyzo import *

class Megoldas:
    versenyzok = []
    def __init__(self):
        self.FajlOlvas()

    def FajlOlvas(self):
        f = open("fob2016.txt", "r", encoding="utf-8")
        for sor in f:
            self.versenyzok.append(Versenyzo(sor))
        f.close()

    def GetIndulok(self):
        return len(self.versenyzok)

    def GetNokAranya(self):
        noDb = 0
        for versenyzo in self.versenyzok:
            if versenyzo.Kategoria == "Noi":
                noDb+=1
        return round(noDb / len(self.versenyzok)*100,2)

    def GetNoGyoztes(self):
        max = 0
        maxVersenyzo = None
        for versenyzo in self.versenyzok:
            if versenyzo.Kategoria == 'Noi':
                osszPont = versenyzo.PontSzamit()
                if max < osszPont:
                    max = osszPont
                    maxVersenyzo = versenyzo
        return maxVersenyzo

    def FajlIr(self):
        f = open("osszpontFF.txt", "w", encoding="utf-8")
        for versenyzo in self.versenyzok:
            if "ferfi" in versenyzo.Kategoria:
                f.write(f"{versenyzo.Nev};{versenyzo.PontSzamit()}\n")
        f.close()

    def StatKeszti(self):
        stat = {}
        for versenyzo in self.versenyzok:
            if versenyzo.Egyesulet != "n.a.":
                if versenyzo.Egyesulet in stat.keys():
                    stat[versenyzo.Egyesulet]+=1
                else:
                    stat[versenyzo.Egyesulet] = 1
        return stat