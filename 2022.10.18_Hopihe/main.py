from asyncio.windows_events import NULL
from cmath import nan
from pickle import FALSE


def BekerFajlNev():
    try:
        f = open(beker, "r", encoding="utf-8")
        lista = []
        for sor in f:
            lista.append(sor.replace("\n", ""))
        return lista
    except:
        if beker != "":
            print("A fájl megnyitása sikertelen!")
        return None

def CheckSorOszlop():
    sorDb = 0
    for sor in sorok:
        if "*" in sor:
            sorDb+=1
    if sorDb % 2 == 1 and len(sorok[0]) % 2 == 1 and sorDb==len(sorok[0]):
        return True
    return False

def CheckSorAtlo():
    #KözépsőSor
    for kar in sorok[int(len(sorok)/2)]:
        if kar != "*":
            return False
    for sor in sorok:
        if sor[int(len(sor)/2)] != "*":
            return False
    index = 0
    for sor in sorok:
        if sor[index] != "*":
            return False
        if sor[len(sor)-1-index] != "*":
            return False
        index+=1
    return True
    
def KarakterekSzama():
    ossz = 0
    szokozDb = 0
    for sor in sorok:
        for betu in sor:
            ossz+=1
            if betu == " ":
                szokozDb+=1
    if szokozDb / ossz * 100 >= 30:
        return True
    return False

def CheckSzimmetria():
    kozIndex = int(len(sorok[0]) / 2)
    for sor in sorok:
        for i in range(0, kozIndex+1):
            if sor[kozIndex-i] != sor[kozIndex+i]:
                return False
    for i in range(len(sorok)//2):
        if sorok[kozIndex+i] != sorok[kozIndex-i]:
            return False
    return True


#Főprogram
beker = "a"
while beker != "":
    beker = input("Adja meg a fájl nevét: ")
    sorok = BekerFajlNev()
    if sorok != None:
        if CheckSorOszlop() and CheckSorAtlo() and KarakterekSzama() and CheckSzimmetria():
            print("Az alakzat Hópihe!")
        else:
            print("Az alakzat NEM hópihe!")