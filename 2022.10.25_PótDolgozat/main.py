varosok = ["Bangkok", "Bengaluru", "Bogotá", "Buenos Aires", "Chicago", "Csangcsou", "Csengcsou", "Csengtu", "Csennai", "Csinan", "Csingtao", "Csungking", "Dakka", "Delhi", "Hangcsou", "Harbin", "Hszian", "Isztambul", "Jakarta", "Johannesburg", "Kairó", "Kanton", "Karacsi", "Kinshasa", "Kolkata", "Lagos", "Lahor", "Lima", "London", "Los Angeles", "Manila", "Mexikóváros", "Milánó", "Moszkva", "Mumbai", "Nagoja", "Nanking", "New York", "Oszaka", "Párizs", "Peking", "Rio de Janeiro", "Ruhr-vidék", "San Francisco", "Sanghaj", "Santou", "S?o Paulo", "Sencsen", "Surabaya", "Szöul", "Teherán", "Tiencsin", "Tokió", "Vuhan", "Washington"]
orszagok = ["Thaiföld", "India", "Kolumbia", "Argentína", "Egyesült Államok", "Kína", "Kína", "Kína", "India", "Kína", "Kína", "Kína", "Banglades", "India", "Kína", "Kína", "Kína", "Törökország", "Indonézia", "Dél-Afrika", "Egyiptom", "Kína", "Pakisztán", "Kongói Dem. Közt.", "India", "Nigéria", "Pakisztán", "Peru", "Egyesült Királyság", "Egyesült Államok", "Fülöp-szigetek", "Mexikó", "Olaszország", "Oroszország", "India", "Japán", "Kína", "Egyesült Államok", "Japán", "Franciaország", "Kína", "Brazília", "Németország", "Egyesült Államok", "Kína", "Kína", "Brazília", "Kína", "Indonézia", "Dél-Korea", "Irán", "Kína", "Japán", "Kína", "Egyesült Államok"]
lakossag = [5696409, 8443675, 7150000, 3063728, 2722389, 3570000, 7005000, 11050000, 8696000, 3250000, 5775000, 7990000, 8906039, 12800000, 9468000, 5015000, 5740000, 11343220, 10348348, 4434827, 9293612, 13080500, 14910352, 7855000, 4496694, 7937932, 10665000, 8380300, 8908081, 3976322, 1780148, 8851080, 1351562, 12500123, 12442373, 2325918, 6320000, 8398748, 2740202, 2187526, 15380000, 6520266, 10125998, 805235, 23390000, 5319028, 12106920, 11908400, 4975000, 9806538, 8846782, 12491300, 13942856, 11895000, 672228]

def TizmillioFelett():
    db = 0
    for szam in lakossag:
        if szam > 10000000:
            db+=1
    print(f"3.Feladat: Legalább 10 milliós városok száma: {db}.")

def MaxKeres():
    index = 0
    max = lakossag[index]
    for i in range(len(lakossag)):
        if max < lakossag[i]:
            max = lakossag[i]
            index = i
    print(f"4.Feladat: Legnépesebb város:\n\tNeve: {varosok[index]}\n\tOrszág: {orszagok[index]}\n\tLakosság: {lakossag[index]} fő")

def KinaSzamol():
    ossz = 0
    db = 0
    for i in range(len(lakossag)):
        if orszagok[i] == "Kína":
            ossz += lakossag[i]
            db+=1
    print(f"5.Feladat: A {db} legnagyobb kínai város összlakossága: {ossz}")

def BekerKeres():
    orszagnev = input("6.Feladat: Kérem az ország nevét: ")
    if orszagnev in orszagok:
        print(f"\t{orszagnev}i város szerepel a listában.")
    else:
        print(f"\t{orszagnev}i város nem szerepel a listában.")

def GetAtlag():
    ossz = 0
    db = 0
    for i in range(len(orszagok)):
        if orszagok[i] == "India":
            ossz += lakossag[i]
            db += 1
    print(f"7.Feladat: Indiai városok lakosságának átlaga: {ossz/db:.0f} fő")

def StatKeszit():
    stat = {}
    for orszag in orszagok:
        if orszag in stat.keys():
            #benne van
            stat[orszag]+=1
        else:
            #nincs benne
            stat[orszag]=1
    db=1
    print("+1. Feladat:")
    while len(stat) != 0:
        max = 0
        maxKulcs = ""
        for kulcs, ertek in stat.items():
            if ertek > max:
                max = ertek
                maxKulcs = kulcs
        print(f"\t {db}. {maxKulcs} - {max}")
        stat.pop(maxKulcs)
        db+=1


print(f"2.Feladat: A városok száma: {len(varosok)}")
TizmillioFelett()
MaxKeres()
GetAtlag()
StatKeszit()

