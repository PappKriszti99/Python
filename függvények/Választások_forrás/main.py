from jelölt import jelölet


def main() -> None:
    pass  # Kezd a kódolást itt!
    # 1. feladat: beolvasás
    jelöltek: list[jelölet] = []
    with open("szavazatok.txt", "r", encoding="UTF 8") as file:
        for sor in file.read().splitlines():
            jelöltek.append(jelölet(sor))
    print(f"2. feladat: A helyhatósági választáson {len(jelöltek)} képviselő indult.")
    # példa
    # HEP_fő: int = 1
    # for jelölt in jelöltek:
    # if jelölt.pártnév() == "HEP":
    # HEP_fő += 1
    # print(HEP_fő)
    keresztnev: str = input("3. feladat: kérem a nevet: ")
    van: bool = False
    for e in jelöltek:
        if e.név() == keresztnev:
            print(f"{keresztnev} {e.szavazat()} szavazatott kapott")
            van = True
            break
    if van is False:
        print(f"Nincs ilyen párt jelölt")
    # 4.feladat
    megjelent: int = 0
    for e in jelöltek:
        megjelent += e.szavazat()
    print(
        f"A választáson {megjelent} állaporgár a jogusltak {round( megjelent/ 12345 *100, 2)}% vett részt"
    )
    # 5. feladat
    stat: dict[str, int] = {}
    for e in jelöltek:
        if e.párt_nev() in stat:
            régi: int = stat[e.párt_nev()]
            stat[e.párt_nev()] = régi + e.szavazat()
        else:
            stat[e.párt_nev()] = e.szavazat()
    for kulcs, ertek in stat.items():
        print(f"\t {kulcs}= {round (ertek/ megjelent*100 , 2)}%")


if __name__ == "__main__":
    main()
