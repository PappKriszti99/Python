import math


def tökéletes(y: int) -> bool:
    osztók_összege: int = 0
    ig: int = int(y / 2) if y % 2 == 0 else int(math.sqrt(y))
    for vizsgált_osztó in range(1, ig + 1):
        if y % vizsgált_osztó == 0:
            osztók_összege += vizsgált_osztó
    return y == osztók_összege


# 1. verzió
def main() -> None:
    print("2. feladat: tökéletes számok")
    print("kérek két természetes számot")
    tól: int = int(input("tól = "))
    ig: int = int(input("ig="))
    print(f"tökéletes számok{tól} és {ig} között join.nal :")
    tökéletes_számok: list[int] = []
    for szám in range(tól, ig + 1):
        if tökéletes(szám):
            tökéletes_számok.append(szám)
    if len(tökéletes_számok) != 0:
        # print(";".join(map(str, tökéletes_számok)))
        # for tsz in tökéletes_számok:
        # print(f"{tsz};", end="\n")
        print(*tökéletes_számok, sep=";")
    else:
        print("A megadott tartományban nincs tökéletes szám!")

    # 2. verzió

    print(f"tökéletes számok{tól} és {ig} között:")
    tökéletes_számok2: list[str] = []
    for szám in range(tól, ig + 1):
        if tökéletes(szám):
            tökéletes_számok2.append(str(szám))
    if len(tökéletes_számok2) != 0:
        # print(";".join(map(str, tökéletes_számok)))
        # for tsz in tökéletes_számok:
        # print(f"{tsz};", end="\n")
        print(*tökéletes_számok2, sep=";")
    else:
        print("A megadott tartományban nincs tökéletes szám!")

    # 3. verzió (csak kiírás)
    if len(tökéletes_számok) != 0:
        for sz in tökéletes_számok[:-1]:
            print(f"{sz};", end="")
        print(tökéletes_számok[-1])
    else:
        print("A megadott tartományban nincs tökéletes szám!")


if __name__ == "__main__":
    main()
