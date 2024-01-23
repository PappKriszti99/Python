# str szöveg
# bool logika
# float tört
# int egész
# list lista
def maxszama(lista):
    maxe = lista[0]
    for i in lista[1:]:
        if i > maxe:
            maxe = i
    return maxe


szamok = []
adat = -1  # a 0 fogja jelezni a kilépést
while adat != 0:
    adat = int(input(" szám= "))
    if adat != 0:
        szamok.append(adat)
print(f"a legnagyobb szám a listában= {maxszama(szamok)}")
