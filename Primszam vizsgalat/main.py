import random

print("2.feladat: Prímszám vizsgálata")

def ez_prim(szam):
    if szam < 2:
        return False
    for i in range (2, int(szam**0.5) + 1):
        if szam % i == 0:
            return False
    return True

lista = [random.randint(10,99) for _ in range(10)]
print("Generált lista:", lista)

talalt_prim = False
for szam in lista:
    if ez_prim(szam):
        print(f"Van prímszám a listában: {szam}")
        talalt_prim = True
        break

if not talalt_prim:
    print("Nincs prímszám a listában.")