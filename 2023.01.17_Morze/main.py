from megoldas import *

m = Megoldas()
m.AbcOlvas()
m.MorzeOlvas()
print(f"3.feladat: A morze abc {m.GetAbcHossz()} db karakter kódját tartalmazza.")
beker = input(f"4.feladat: Kérek egy karaktert: ").upper()
keresett = m.GetChar(beker)
if keresett != "":
    print(f"\tA {beker} karakter morze kódja: {keresett}")
else:
    print("\tNem található a kódtárban ilyen karakter!")
print(f"7.feladat: Az első idézet szerzője: {m.ElsoFordit()}")
print(f"8.feladat: A leghosszabb idézet szerzője és az idézet: {m.LeghosszabbKeres()}")
idezetek = m.GetArisztotelesz()
print(f"9.feladat: Arisztotelész idézetei:")
for idezet in idezetek:
    print(f"\t- {idezet}")
m.FajlIr()