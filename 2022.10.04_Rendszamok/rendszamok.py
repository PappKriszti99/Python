import random

rendszamok = []

def RegiGeneral():
    rendszam = ""
    for i in range(0,3):
        rendszam += chr(random.randint(ord("A"), ord("Z")))
    rendszam += "-"
    for i in range(0,3):
        rendszam += str(random.randint(0,9))
    return rendszam
    
def UjGeneral():
    rendszam = ""
    for i in range(0,2):
        for j in range(0, 2):
            rendszam += chr(random.randint(ord("A"), ord("Z")))
        rendszam += "-"
    for i in range(0,3):
        rendszam += str(random.randint(0,9))
    return rendszam

while len(rendszamok) < 1000:
    if random.randint(0,1) == 0:
        rendszam = RegiGeneral()
    else:
        rendszam = UjGeneral()
    if rendszam not in rendszamok:
        rendszamok.append(rendszam)
    else:
        print("Már szerepelt ez a rendszám")

print(rendszamok)