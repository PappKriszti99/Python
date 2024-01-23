def szavak_megforditasa(mondat):
    for i in range(len(szavak)):
        szavak[i] = szavak[i][::-1]

    forditott_mondat = " ".join(szavak)

    return forditott_mondat


if __name__ == "__main__":
    mondat = input("Kérem, adjon meg egy mondatot: ")
    forditott = szavak_megforditasa(mondat)
    print("A mondat minden szava megfordítva:")
    print(forditott)
