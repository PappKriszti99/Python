def main() -> None:
    pass  # Kezd a kódolást itt!


# többágú elágazás if-elif--else
print("Osztály jegyei!")
jegy: int = int(input("Kérem az osztályzatot"))
if jegy == 1:
    print("elégtelen")
elif jegy == 2:
    print("elégséges")
elif jegy == 3:
    print("közepes")
elif jegy == 4:
    print("jó")
elif jegy == 5:
    print("jeles")
else:
    print("ez nem érdemjegy")


if __name__ == "__main__":
    main()
