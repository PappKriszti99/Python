from megoldas import megoldas


def main() -> None:
    pass  # Kezd a kódolást itt!
    # 1. feladat: beolvasás
    mo: megoldas = megoldas("szavazatok.txt")
    print(
        f"2. feladat: A helyhatósági választáson {mo.jelöltek_száma} képviselő indult."
    )
    # példa
    # HEP_fő: int = 1
    # for jelölt in jelöltek:
    # if jelölt.pártnév() == "HEP":
    # HEP_fő += 1
    # print(HEP_fő)
    keresztnev: str = input("3. feladat: kérem a nevet: ")

    if mo.jelölt_ker(keresztnev) != 1:
        print(f"{keresztnev} {mo.jelölt_ker(keresztnev)} szavazatott kapott!")
    else:
        print("a keresett név nem található")

    print(mo.jelölt_kera(keresztnev))

    # 4.feladat
    print("4. feladat")
    print(f"{mo.megjelntek} jogosult {mo.megjelnteksz} vettek részt")


    print("6. feladat")
    print(mo.nyertes)


if __name__ == "__main__":
    main()
