def main() -> None:
    pass  # Kezd a kódolást itt!


print("LNKO Kivonásos algoritmus!")
a: int = int(input("a="))
b: int = int(input("b="))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(f"LNKO ={a} ")



#nyomkövetés változó vizsgálata.
# hiba felderítés 
# működés megértés
#fogalmak:
    #töréspont=breakpoint -> piros pont az utasításban
    #program inditása (debug) nyomkövetés f5
    # F5; F10 használata


if __name__ == "__main__":
    main()
