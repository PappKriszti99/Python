from Epulet import *
from Fgvk import *

epuletek = []
FileOlvas(epuletek)
print(f"3.2 feladat: Épületek száma: {len(epuletek)} db")
print(f"3.3 feladat: Emeletek összege: {GetOsszEmelet(epuletek)}")
legEpulet = LegmagasabbKeres(epuletek)
print(f"3.4 feladat: A legmagasabb épület adatai")
print(f"\tNév: {legEpulet.Nev}\n\tVáros: {legEpulet.Varos}\n\tOrszág: {legEpulet.Orszag}\n\tMagasság: {legEpulet.Magassag} m\n\tEmeletek száma: {legEpulet.Emelet}\n\tÉpítés éve: {legEpulet.Ev}")
print(f"3.5 Feladat: {OlaszKeres(epuletek)} olasz épület az adatok között!")