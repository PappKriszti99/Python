print("1.feladat: Téglalap terület és kerület számítás")
a: float = float(input("a="))
b: float = float(input("b="))
terulet: float = a * b
kerulet: float = 2 * (a + b)
print(f"T={terulet}")
print(f"K={kerulet}")