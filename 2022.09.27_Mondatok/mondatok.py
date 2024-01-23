mondat = "b"

while mondat != "":
    mondat = input("Adjon meg egy mondatot: ")
    szavak = mondat.strip().split()
    for i in range(0, len(szavak)):
        print(f"{szavak[len(szavak)-i-1]} ", end="")