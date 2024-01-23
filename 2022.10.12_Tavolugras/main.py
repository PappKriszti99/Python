# '''
#     1. Kérje be egy versenyző nevét -> indult-e ?
#     2. Legnagyobb ugrás -> hány méter
#     3. Kérjünk be egy távolságot -> hányan ugrattak ennél többet
#     4. Legjobb ugrások átlaga
#     0. Utolsó pillatban újabb versenyző nevezett -> 
#             Kérjük be a nevét, országát, 3 ugrás eredményét -> tároljuk el a listába
#             a legjobb ugrását nekünk kell kiszámolni.
# '''

def FajlBeolvas():
    try:
        f = open("adatok.csv", "r", encoding="utf-8")
        f.readline()
        for sor in f:
            versenyzok.append(sor)
    except:
        print("A fájlt nem sikerült beolvasni!")

def BekerKeres():
    beker = input("1.Feladat: Adja meg egy versenyző nevét: ")
    for sor in versenyzok:
        adatok = sor.strip().split(";")
        if beker == adatok[1]:
            print(f"\t{beker} versenyző indult a versenyen!")
            return True
    print("\tNem indult ilyen nevű versenyző!")
    return False

def LegnagyobbKeres():
    max = 0
    for sor in versenyzok:
        szam = StringToFloat(sor, 6)
        if szam > max:
            max = szam
    return max

def BekerNagyobb():
    db = 0
    beker = float(input("3.Feladat: Adjon meg egy távolságot: "))
    for sor in versenyzok:
        szam = StringToFloat(sor, 6)
        if szam > beker:
            db+=1
    print(f"{beker}m-nél nagyobbat ugrott {db} versenyző")

def StringToFloat(adat, hanyadik):
    adatok = adat.strip().split(";")
    eredmeny = adatok[hanyadik].replace(",", ".")
    try:
        szam = float(eredmeny)
        return szam
    except:
        return 0

def AtlagSzamol():
    ossz = 0
    for versenyzo in versenyzok:
        ossz += StringToFloat(versenyzo, 6)
    print(f"4.Feladat: A legnagyobb ugrások átlaga: {ossz/len(versenyzok):.4f}")

def Beker():
    nev = input("Adja meg a versenyző nevét: ")
    orszag = input("Adja meg a versenyző országát: ")
    ugrasok = []
    max = 0
    for i in range(0,3):
        ugras = input(f"Adja meg az {i+1}. ugrás eredményét: ")
        ugrasok.append(ugras)
        if ugras != "×" and float(ugras) > max:
            max = float(ugras)
    sor = f"{len(versenyzok)+1}.;{nev};{orszag};{ugrasok[0].replace('.', ',')};{ugrasok[1].replace('.', ',')};{ugrasok[2].replace('.', ',')};{max};\n"
    versenyzok.append(sor)
    f = open("adatok.csv", "a", encoding="utf-8")
    f.write(sor)
    f.close()  

versenyzok = []
FajlBeolvas()
print(versenyzok)
BekerKeres()
print(f"2.Feladat: A legnagyobb ugrás: {LegnagyobbKeres()}")
BekerNagyobb()
AtlagSzamol()
Beker()