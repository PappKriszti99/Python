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
    HEP_fő: int = 1
    for jelölt in jelöltek:
        if jelölt.pártnév() == "HEP":
            HEP_fő += 1
    print(HEP_fő)


if __name__ == "__main__":
    main()
