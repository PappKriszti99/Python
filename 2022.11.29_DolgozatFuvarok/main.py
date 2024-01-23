from fgvk import *

fuvarok = []
FajlOlvas(fuvarok)
print(f"3.feladat: {len(fuvarok)}")
fuvarAdatok = FuvarKeres(fuvarok)
print(f"4.feladat: {fuvarAdatok[0]} fuvar alatt: {fuvarAdatok[1]}$")
FizmodStat(fuvarok)
print(f"6.feladat: {GetOsszKm(fuvarok):.2f} km")
GetLeghosszabb(fuvarok)
FajlIr(fuvarok)