def heronkeplet(a,b,c):
    s=(a+b+c)/2
    terulet=(s*(s-a)*(s-b)*(s-c))**0.5
    return terulet

print("1.feladat: Hérón")
print("Kérem a háromszög oldalait")
a= float(input("a="))
b= float(input("b="))
c= float(input("c="))

kerulet: float = a + b + c
terulet: float = heronkeplet(a,b,c)

print(f"Kerület:{kerulet}")
print(f"Terület:{terulet}")