from megoldas import *

m = Megoldas()
m.FajlOlvas(m.Karakterek, "bank.txt")
print(f"5.feladat: Karakterek száma: {m.GetHossz()}")
kar = m.GetKar()
keresett = m.Keres(kar)
print("7.feladat:")
if keresett != None:
    keresett.MatrixKiir()
else:
    print("Nincs ilyen karakter a bankban!")
m.FajlOlvas(m.Dekodolando, "dekodol.txt")
print(f"9.feladat: Dekódolás:\n{m.Dekodol()}")