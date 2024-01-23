print("1.feladat: LNKO")
a: int= int(input("a="))
b: int= int(input("b="))
print(f"LNKO({a},{b}) = ", end="")
while a!= b:
    if a>b:
        a = a-b
    else:
        b = b-a
print(a)