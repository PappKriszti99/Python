import random



def halmaz(szamok) -> bool:
    list=[]
    for e in szamok:
        if e not in list:
            list.append(e)
    return len(szamok)==len(list)


print("2.feladat: Halmaz-e?")
for i in range(1,11):
    lista=[]
    for i in range(5):
        lista.append(random.randint(0,9))
    print(f"{i:2}, {lista} halmaznak {"" if halmaz(lista)else"nem"} tekinthető")