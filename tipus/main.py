def nagybetu(szöveg):
    vissza = ""
    for betu in szöveg:
        vissza += betu.capitalize()
    return vissza
def kisnagy(szöveg):
    return szöveg.capitalize()    


def main() -> None:
    pass  # Kezd a kódolást itt!
    print(nagybetu("Almafa ága"))
    print(kisnagy("ASD ASD ASD"))


if __name__ == "__main__":
    main()
