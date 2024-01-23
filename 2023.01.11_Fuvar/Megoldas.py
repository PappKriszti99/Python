from Fuvar import *

class Megoldas:
    def __init__(self):
        self.fuvarok = []

    def FajlOlvas(self):
        f = open("tavok.txt", "r", encoding="utf-8")
        for sor in f:
            self.fuvarok.append(Fuvar(sor))
        f.close()

    def ElsoKeres(self):
        min = self.fuvarok[0].Nap
        elsoNapok = []
        for fuvar in self.fuvarok:
            if min > fuvar.Nap:
                min = fuvar.Nap
        for fuvar in self.fuvarok:
            if fuvar.Nap == min:
                elsoNapok.append(fuvar)
        for fuvar in elsoNapok:
            if fuvar.Sorszam == 1:
                return fuvar.Tav

    def UtolsoKeres(self):
        max = self.fuvarok[0].Nap
        utolsoNapok = []
        for fuvar in self.fuvarok:
            if max < fuvar.Nap:
                max = fuvar.Nap
        for fuvar in self.fuvarok:
            if fuvar.Nap == max:
                utolsoNapok.append(fuvar)
        maxFuvar = utolsoNapok[0]
        for fuvar in utolsoNapok:
            if maxFuvar.Sorszam < fuvar.Sorszam:
                maxFuvar = fuvar
        return maxFuvar.Tav

    def NapKeres(self):
        dolgozottNap = []
        nemDolgozott = []
        for fuvar in self.fuvarok:
            if fuvar.Nap not in dolgozottNap:
                dolgozottNap.append(fuvar.Nap)
        for i in range(1,8):
            if i not in dolgozottNap:
                nemDolgozott.append(i)
        return nemDolgozott

    def GetHetNapja(self, sorszam):
        hetNapjai = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
        return hetNapjai[sorszam-1]

    def GetLegtobbFuvar(self):
        legnagyobbFuvar = max(self.fuvarok, key=lambda x : x.Sorszam)
        return legnagyobbFuvar

    def GetStat(self):
        stat = {}
        for i in range(1,8):
            stat[i] = 0
        for fuvar in self.fuvarok:
            stat[fuvar.Nap] += fuvar.Tav
        return stat

        