def Beker():
    a = b = c = -1
    while a < 0 or a > 24:
        a = int(input("Adja meg az órákat: "))
    while b < 0 or b > 59:
        b = int(input("Adja meg a perceket: "))
    while c < 0 or c > 59:
        c = int(input("Adja meg a másodperceket: "))
    return (a*60*60) + (b *60) + c
print(Beker())
