from multiprocessing.sharedctypes import Value


beker = "a"

def betuSzamol():
    betuk = {}
    for betu in beker:
        if betu.isalpha():
            if betu in betuk.keys():
                betuk[betu]+=1
            else:
                betuk[betu] = 1
    print("Betűk száma: ")
    for key, value in betuk.items():
        print(f"\t{key}: {value}")

#főprogram
while beker != "":
    beker = input("Adjon meg egy mondatot: ").upper()
    betuSzamol()