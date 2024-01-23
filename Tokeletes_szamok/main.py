import math


def tökéletes(y: int) -> bool:
    osztók_összege: int = 0
    ig: int = int(y / 2) if y % 2 == 0 else int(math.sqrt(y))
    for vizsgált_osztó in range(1, ig + 1):
        if y % vizsgált_osztó == 0:
            osztók_összege += vizsgált_osztó
    return y == osztók_összege


print("2.feladat: Tökéletes számok")
print("Kérek két természetes számot:")
tól: int = int(input("tól = "))
ig: int = int(input("ig = "))
print(f"Tökéletes számok{tól} és {ig} között:")
tökéletes_számok: list[str] = []
for szám in range(tól, ig + 1):
    if tökéletes(szám):
        tökéletes_számok.append(str(szám))
if len(tökéletes_számok) !=0:
    print(*tökéletes_számok, sep=";")
else:
    print("A megadott tartományban nincs tökéletes szám!")