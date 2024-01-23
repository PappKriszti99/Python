print("1.feladat: A háromszög szerkeszthetősége")
print("Kérem a háromszög oldalait!")
a: float = float(input("a="))
b: float = float(input("b="))
c: float = float(input("c="))
if a + b > c and a + c > b and b + c > a:
    print("A háromszög szerkeszthető!")
else:
    print("A háromszög nem szerkeszthető a megadott adatokkal!")