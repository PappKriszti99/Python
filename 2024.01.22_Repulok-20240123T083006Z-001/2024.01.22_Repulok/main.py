from függvények import *


Fajlolvas()
print(f"4. feladat: Adatsorok száma: {len(repulok)}")
print(f"5. feladat: Boeing típusok száma: {Boeingdarabszam()}")
maxRepulo=Legtobbutas()
print(f"6. feladat: A legtöbb utast szállító replőgéptípus: ")
print(f"\tTípus:{maxRepulo.Tipus}")
print(f"\tEv:{maxRepulo.Ev}")
print(f"\tUtasok száma:{maxRepulo.Utas}")
print(f"\tSzemélyzet:{maxRepulo.Szemelyzet}")
print(f"\t Utazósebesség:{maxRepulo.Sebesseg}")
Fajlirj()
q0= float(input("q0="))
p0= float(input("p0="))
eredmeny=szamol(q0,p0)
if eredmeny< 1:
    print(f"Ma={eredmeny}")
else:
    print("Az eredmény nagyobb mint 1!")

dict= Statkeszit()
print("9. feladat")
for key, value in dict.items():
    print(f"\t{key}: {value}: db")

