import random
import time

parok = {}
nevek = []

def FajlOlvas():
    f = open("diakok.txt", "r", encoding="utf-8")
    for sor in f:
        nevek.append(sor.strip())
    f.close()

def Sorsol():
    harmadik = random.choice(nevek)
    nevek.remove(harmadik)
    while len(nevek) != 0:
        parElso = random.choice(nevek)
        nevek.remove(parElso)
        parMas = random.choice(nevek)
        nevek.remove(parMas)
        parok[parElso]=parMas
    return harmadik

def Kiir(harmadikSzerencsetlen):
    szam = random.randint(0,7)
    db = 0
    for key, value in parok.items():
        print(f"{db+1}.pár: {key} - {value}", end="")
        if db == szam:  
            print(f"- {harmadikSzerencsetlen}")
        else:
            print()
        time.sleep(2)
        db+=1

FajlOlvas()
harmadik = Sorsol()
Kiir(harmadik)