from Epulet import *

def FileOlvas(epuletek):
    f = open("legmagasabb.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        epuletek.append(Epulet(sor))
    f.close()

def GetOsszEmelet(epuletek):
    ossz = 0
    for epulet in epuletek:
        ossz += epulet.Emelet
    return ossz

def LegmagasabbKeres(epuletek):
    maxEpulet = epuletek[0]
    for epulet in epuletek:
        if epulet.Magassag > maxEpulet.Magassag:
            maxEpulet = epulet
    return maxEpulet

def OlaszKeres(epuletek):
    for epulet in epuletek:
        if epulet.Orszag == "Olaszország":
            return "Van"
    return "Nincs"