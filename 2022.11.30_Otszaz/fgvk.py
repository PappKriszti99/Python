from Vasarlas import *

def FajlOlvas(vasarlasok):
    f = open("penztar.txt", "r", encoding="utf-8")
    termekek = []
    for sor in f:
        stripped = sor.strip()
        if stripped == "F":
            egyVasarlas = Vasarlas()
            egyVasarlas.TermekAdd(termekek)
            vasarlasok.append(egyVasarlas)
            termekek = []
        else:
            termekek.append(stripped)
    f.close()

def Beker():
    sorszam = int(input("\tAdja meg egy vásárlás sorszámát: "))
    arucikk = input("\tAdja meg egy árucikk nevét: ")
    db = int(input("\tAdja meg a vásárolt darabszámot: "))
    return sorszam, arucikk, db

def ElsoUtolsoKeres(vasarlasok ,termeknev):
    elso = -1
    utolso = -1
    db = 0
    for i in range(len(vasarlasok)):
        if termeknev in vasarlasok[i].GetTermekek():
            db+=1
            if elso == -1:
                elso = i+1
            utolso = i+1
    print("5.feladat:")
    print(f"\tAz első vásárlás sorszáma: {elso}")
    print(f"\tAz utolsó vásárlás sorszáma: {utolso}")       
    print(f"\t{db} vásárlás során vettek belőle.")

def OsszSzamol(db):
    ossz = 0
    for i in range(0,db):
        if i < 3:
            ossz += 500-(50*i)
        else:
            ossz += 400
    return ossz

def VasarlasDb(vasarlasok, sorszam):
    stat = {}
    kosar = vasarlasok[sorszam-1].GetTermekek()
    for termek in kosar:
        if termek in stat.keys():
            stat[termek]+=1
        else:
            stat[termek]=1
    return stat

def GetDicKt(stat):
    print("7.feladat")
    for key, value in stat.items():
        print(f"\t{value} {key}")

def OsszegekSzamol(vasarlasok):
    f = open("osszeg.txt", "w", encoding="utf-8")
    for i in range(len(vasarlasok)):
        osszeg = 0
        dickionary = VasarlasDb(vasarlasok, i+1)
        for key, value in dickionary.items():
            osszeg += OsszSzamol(value)
        f.write(f"{i+1}. {osszeg}\n")
    f.close()
