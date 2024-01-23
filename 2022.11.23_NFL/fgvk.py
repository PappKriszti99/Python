from Jatekos import *

def FajlOlvas(jatekosok):
    f = open("NFL_iranyitok.txt", "r", encoding="utf-8")
    for sor in f:
        jatekosok.append(Jatekos(sor))
    f.close()

def GetMutato(jatekosok):
    print("7. feladat: Legjobb irányítók:")
    for jatekos in jatekosok:
        if jatekos.IranyitoMutato >= 100 and jatekos.Meter >= 4000:
            print(f"\t{jatekos.FormazottNev()} (Irányító mutató: {jatekos.IranyitoMutato}, Passzok: {jatekos.Meter:.0f}m)")

def FajlIr(jatekosok):
    hibaBeker = input("8. feladat: Eladott labdák száma: ")
    hibasJatekosok = []
    for jatekos in jatekosok:
        if jatekos.EladottLabdak > int(hibaBeker):
            hibasJatekosok.append(jatekos.Nev)
    hibasJatekosok.sort()
    f = open("legtobbeladott.txt", "w", encoding="utf-8")
    for jatekos in hibasJatekosok:
        f.write(f"{jatekos}\n")
    f.close()

def GetLegtobbTouchD(jatekosok):
    max = jatekosok[0]
    for jatekos in jatekosok:
        if max.PasszTouchD < jatekos.PasszTouchD:
            max = jatekos
    print("9. feladat: A legtöbb TD-t szerző játékos:")
    print(f"\tNeve: {max.Nev}\n\tTD-k száma: {max.PasszTouchD}\n\tEladott labdák száma: {max.EladottLabdak}")

def GetEgyetemek(jatekosok):
    stat = {}
    for jatekos in jatekosok:
        if jatekos.Egyetem in stat.keys():
            stat[jatekos.Egyetem] += 1
        else:
            stat[jatekos.Egyetem] = 1
    print("10. feladat: Legsikeresebb egyetemek:")
    for key, value in stat.items():
        if value > 1:
            print(f"\t{key} - {value}")