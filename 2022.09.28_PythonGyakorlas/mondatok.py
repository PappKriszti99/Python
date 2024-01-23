mondat = "b"
fajtak = ["!", "?", "."]
dbszamok = [0,0,0]

while mondat != "":
    mondat = input("Adjon meg egy mondatot: ")
    if mondat != "":
        szavak = mondat.strip().split()
        for i in range(len(szavak)-1, 0-1, -1):
            print(szavak[i], end=" ")
        print(f"\n{mondat[::-1]}")
        index = fajtak.index(mondat[-1])
        dbszamok[index]+=1
print(fajtak)
print(dbszamok)