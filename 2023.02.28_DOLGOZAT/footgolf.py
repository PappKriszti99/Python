from megoldas import *

m = Megoldas()
print(f"3.feladat: A versenyzők száma: {m.GetIndulok()}")
print(f"4.feladat: A női versenyzők aránya: {m.GetNokAranya()}%")
gyoztes = m.GetNoGyoztes()
print(f"6.feladat: A bajnok női versenyző:\n\tNév: {gyoztes.Nev}\n\tEgyesület: {gyoztes.Egyesulet}\n\tÖsszpont: {gyoztes.PontSzamit()}")
m.FajlIr()
stat = m.StatKeszti()
print("8.feladat: Egyesület statisztika:")
for key, value in stat.items():
    if value > 2:
        print(f"\t{key} - {value} fő")