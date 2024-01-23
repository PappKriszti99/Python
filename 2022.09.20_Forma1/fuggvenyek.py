import random

def IdoGeneral(lista):
    for i in range(20):
        egesz = random.randint(70,75)
        tort = random.randint(0,999)
        lista.append(float(f"{egesz}.{tort}"))

def LeggyorsabbKeres(lista):
    min = lista[0]
    for szam in lista:
        if min > szam:
            min = szam
    return min

def LeglassabbKeres(lista):
    max = lista[0]
    for szam in lista:
        if max < szam:
            max = szam
    return max

def IdoAlakit(lista):
    for ido in lista:
        darabok = str(ido).strip().split('.')
        percStr = int(darabok[0]) / 60
        mpStr = str(int(darabok[0])-(int(percStr)*60))
        tizedes = darabok[1]
        if len(mpStr) == 1:
            mpStr = f"0{mpStr}"
        if len(tizedes) == 1:
            tizedes = f"00{tizedes}"
        elif len(tizedes) == 2:
            tizedes = f"0{tizedes}"
        print(f"\t{ido} -> 0{round(percStr)}:{mpStr}:{tizedes}")
        
