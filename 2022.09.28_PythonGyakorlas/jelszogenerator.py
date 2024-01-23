import random

def Beker():
    hossz = ""
    while not hossz.isnumeric():
        hossz = input("Adja meg a jelszó hosszát: ")
        if not hossz.isnumeric():
            print("Nem számot adott meg!")
    return int(hossz)

def JelszoGeneral():
    jelszo = ""
    for i in range(0, karSzam):
        karakter = chr(random.randint(ord("A"), ord("Z")))
        veletlen = random.randint(0,3)
        if veletlen == 0:
            karakter = karakter.lower()
        elif veletlen == 1:
            karakter = str(random.randint(0,9+1))
        jelszo += karakter
    return jelszo

karSzam = Beker()
print(JelszoGeneral())