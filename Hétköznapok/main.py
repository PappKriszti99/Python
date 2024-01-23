def maganhangzo(nap)->int:
    db=0
    for k in nap:
        if k in "aáeéiíoóöőuúüű":
            db+=1
    return db


print("2.feladat:Hetkoznapok")

lista=["hétfő" , "kedd", "szerda", "csütörtök", "péntek"]
mgh=0
for i in range(1, len(lista)):
    if maganhangzo(lista[i]) > maganhangzo(lista[mgh]):
        mgh= i
print(f"A legtöbb magánhangzó a {lista[mgh]}-ben van")