def main() -> None:
    pass  # Kezd a kódolást itt!


import random

# python lista létrehozása (tömb nincs de hasonló adatszerkezet a lista)
# lista= tömb= vektor
# lista: egy összetett adatszerkezet, több érték adattárolására alkalmas
# lista létrehozása:


számok: list[int] = [3, 8, 5, 10, 4, 6]
print(számok)
print(f"a számok első eleme: {számok[0]}")
print(f"a számok első eleme: {számok[len(számok)-1]}")
# összegzés
# lista bejárása (cv az index veszi fel)
# megszámlás tétele
# az 5 nél nagyobb számok darabszáma
ötnél_nagyobb: int = 0
for szam in számok:
    if szam > 5:
        ötnél_nagyobb = ötnél_nagyobb + 1
print(f"5-nél nagyobb számok darabszáma: {ötnél_nagyobb}")
összeg: int = 0
for szam in számok:
    összeg = összeg + szam
print(f"számok összege:{összeg}")
print(f"számok lista elemszáma:{len(számok)}")
# hivetkozás a lista elemeire
# még mindig összegzés
# páros számok összege
összeg_páros: int = 0
for i in range(0, len(számok)):
    if számok[i] % 2 == 0:
        összeg_páros = összeg_páros + számok[i]
print(f"párosszámok összege:{összeg_páros}")
# eldöntés tétele: a számok listában van-e páros szám?
# a keresést ne folytassa, ha a választ meg tudja adni!

vanpáros: bool = False  # azt feltételezük, hogy nincs páros
for szam in számok:
    if szam % 2 == 0:
        vanpáros = True
        break  # befejezem a további keresést
if vanpáros:
    print("van páros szám a listában")
else:
    print("nincs páros szám a listában")
# fenti két ágú elágazás kiváltásaű
print(f" {'van' if vanpáros else 'Nincs'} páros szám a lsitában ")
# szélső érték keresése
# legnagyobb szám a listában
# a lsita bejárása az első elem elhagyásával
legna: int = számok[0]
for szam in számok[1:]:
    if szam > legna:
        legna = szam
print(f"A legnagyobb szám a listában:{legna}")
# legkisebb páros szám a lsitában
# union type: int| None -> vagy int vagy none tipusú lehet
# itt a none érték azt fogja jelenteni hogy nincs páros szám a listában
legkis: int | None = None
for szam in számok:
    if szam % 2 == 0:
        if legkis is None:
            legkis = szam
        else:
            if szam < legkis:
                legkis = szam
if legkis is None:
    print("nincs páros szám a listában")
else:
    print(f"a legkisebb páros szám:{legkis}")

# feladat: tölsünk fel egy listát véletszerű kétjegyű számokkal (10-99)
# A lista elem száma 10 legyen
vszámok: list[int] = []
while len(vszámok) < 10:
    vszámok.append(random.randint(10, 99))
print(f"a 10 darab véletlen szám:{vszámok}")


vszámok2: list[int] = []
for _ in range(10):
    vszámok2.append(random.randint(10, 99))
print(f"a 10 darab véletlen szám:{vszámok}")

# lottó számok szombatra:
lottó: list[int] = []
while len(lottó) < 5:
    sorsoltszám: int = random.randint(1, 90)
    if sorsoltszám not in lottó:
        lottó.append(sorsoltszám)


print(f"a lottó számok:{lottó}")

if __name__ == "__main__":
    main()
