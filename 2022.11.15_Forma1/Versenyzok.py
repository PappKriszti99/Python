from fgvk import *

pilotak = []
FajlOlvas(pilotak)
print(f"3. feladat: {len(pilotak)}")
print(f"4. feladat: {pilotak[-1].Nev}")
print("5. feladat:")
GetTizenkilenc(pilotak)
print(f"6. feladat: {GetLegkisebb(pilotak)}")
print("7. feladat: ", end="")
GetDuplaRajtszam(pilotak)