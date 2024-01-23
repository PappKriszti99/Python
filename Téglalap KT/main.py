def main() -> None:
    # "ez egy string literal"
    # print()-> függvény
    print("Téglalap kerülete és területe")
    print("Kérem a téglalap oldalait!")
    a: int = int(input("a= "))
    b: int = int(input("b= "))
    # számítás
    terület: int = a * b
    kerület: int = 2 * (a + b)

    # eredmények kíirása "f"string-el
    print(f"terület={terület}")
    print(f"kerület={kerület}")


if __name__ == "__main__":
    main()
