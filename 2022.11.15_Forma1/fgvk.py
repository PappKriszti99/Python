from Pilota import *

def FajlOlvas(pilotak):
    f = open("pilotak.csv", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        egyPilota = Pilota(sor)
        pilotak.append(egyPilota)
    f.close()

def GetTizenkilenc(pilotak):
    for pilota in pilotak:
        datudmDb = pilota.SzulDatum.split(".")
        ev = int(datudmDb[0])
        if ev < 1901:
            print(f"\t{pilota.Nev} ({pilota.SzulDatum})")

def GetLegkisebb(pilotak):
    min = 100
    nemzetiseg = ""
    for pilota in pilotak:
        if pilota.Rajtszam != "" and int(pilota.Rajtszam) < min:
            min = int(pilota.Rajtszam)
            nemzetiseg = pilota.Nemzetiseg
    return nemzetiseg

def GetDuplaRajtszam(pilotak):
    rajtszamok = {}
    for pilota in pilotak:
        if pilota.Rajtszam != "":
            if pilota.Rajtszam in rajtszamok.keys():
                rajtszamok[pilota.Rajtszam] += 1
            else:
                rajtszamok[pilota.Rajtszam] = 1
    for key, value in rajtszamok.items():
        if value > 1:
            print(f"{key}, ", end="")
