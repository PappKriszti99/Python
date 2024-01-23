from re import I


def orszagVanE(orszagLista):
    for orszag in orszagLista:
        if "ország" in orszag:
            print(f"\t{orszag}")

def legnagyobbKeres(teruletLista, maxKeres):
    index = 0
    szorzat = 1 if maxKeres else -1
    max = teruletLista[index]
    for i in range(len(teruletLista)):
        if max < teruletLista[i] * szorzat:
            max = teruletLista[i]
            index = i
    return index

def legkisebbKeres(teruletLista):
    index = 0
    min = teruletLista[index]
    for i in range(len(teruletLista)):
        if min > teruletLista[i]:
            min = teruletLista[i]
            index = i
    return index

def NegyzazEzerFelett(orszagLista, teruletLista):
    for i in range(len(teruletLista)):
        if teruletLista[i] > 400000:
            print(f"\t{orszagLista[i]} : {teruletLista[i]}")
    