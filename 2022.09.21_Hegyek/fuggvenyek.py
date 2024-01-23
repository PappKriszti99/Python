def GetLegmagasabb(magassagok):
    return magassagok.index(max(magassagok))

def GetMasodik(magassagok, legmagasabb):
    max = magassagok[0]
    for magassag in magassagok:
        if max < magassag and magassag != legmagasabb:
            max = magassag
    return magassagok.index(max)

def AtlagSzamol(magassagok):
    ossz = 0
    db = 0
    for szam in magassagok:
        if szam > 850:
            ossz += szam
            db+=1
    return round(ossz/db, 2)

def GetNevUgyanaz(nevek):
    db = 0
    for nev in nevek:
        for betu in nev:
            if betu.isnumeric():
                db+=1
                break
    return db