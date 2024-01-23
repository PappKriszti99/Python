def nagybetu(szöveg):
    db = 0
    for betű in szöveg:
        if betű.isupper():
            db += 1
    return db


def angolbetű(szöveg):
    a = 0
    for betű in szöveg:
        if betű >= "A" and betű <= "Z":
            a += 1
    return a


mondat = []
inputkifej = ""
while inputkifej != "exit":
    inputkifej = input(" kérem a kifejezést:")
    if inputkifej != "exit":
        mondat.append(inputkifej)
for i in mondat:
    print(f"{i} Nagybetűk száma= {nagybetu(i)}")
