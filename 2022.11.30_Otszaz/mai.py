from fgvk import *

vasarlasok = []
FajlOlvas(vasarlasok)
print(f"2.feladat:\n\tA fizetések száma: {len(vasarlasok)}")
print(f"3.feladat:\n\tAz első vásárló {len(vasarlasok[0].GetTermekek())} darab árucikket vásárolt.")
bekertAdatok = Beker()
ElsoUtolsoKeres(vasarlasok, bekertAdatok[1])
print(f"6. feladat: {bekertAdatok[2]} darab vételekor fizetendő: {OsszSzamol(bekertAdatok[2])} ft")
GetDicKt(VasarlasDb(vasarlasok, bekertAdatok[0]))
OsszegekSzamol(vasarlasok)