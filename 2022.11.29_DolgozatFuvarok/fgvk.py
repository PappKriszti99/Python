from fuvar import *
import operator

def FajlOlvas(fuvarok):
    f = open("fuvar.csv", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        fuvarok.append(Fuvar(sor))
    f.close()

def FuvarKeres(fuvarok):
    db = 0
    ossz = 0
    for fuvar in fuvarok:
        if fuvar.ID == 6185:
            db+=1
            ossz+=fuvar.Viteldij + fuvar.Borravalo
    return db, ossz

def FizmodStat(fuvarok):
    stat = {}
    for fuvar in fuvarok:
        if fuvar.Fizmod in stat.keys():
            stat[fuvar.Fizmod]+=1
        else:
            stat[fuvar.Fizmod]=1
    print("5.feladat:")
    for key, value in stat.items():
        print(f"\t{key}: {value} fuvar")

def GetOsszKm(fuvarok):
    ossz = 0
    for fuvar in fuvarok:
        ossz += fuvar.Tavolsag
    return ossz*1.6

def GetLeghosszabb(fuvarok):
    maxFuvar = fuvarok[0]
    for fuvar in fuvarok:
        if maxFuvar.Idotartam < fuvar.Idotartam:
            maxFuvar = fuvar
    print("7.feladat: Leghosszabb fuvar:")
    print(f"\tFuvar hossza: {maxFuvar.Idotartam} másodperc\n\tTaxi azonosítója: {maxFuvar.ID}\n\tMegtett távolság: {maxFuvar.Tavolsag} mérföld\n\tViteldij: {maxFuvar.Viteldij}$")

def FajlIr(fuvarok):
    f = open("hibak.txt", "w", encoding="utf-8")
    hibasak = []
    for fuvar in fuvarok:
        if fuvar.Idotartam > 0 and fuvar.Viteldij > 0 and fuvar.Tavolsag == 0:
            hibasak.append(fuvar)
    rendezett = sorted(hibasak, key=operator.attrgetter('Indulas'))
    for fuvar in rendezett:
        f.write(f"{fuvar.ID};{fuvar.Indulas};{fuvar.Idotartam};{fuvar.Tavolsag};{fuvar.Viteldij};{fuvar.Borravalo};{fuvar.Fizmod}\n")
    f.close()