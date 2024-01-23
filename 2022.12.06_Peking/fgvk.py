from versenyzo import *
import operator

versenyzok = []

def FajlOlvas():
    f = open("torna.csv", "r", encoding="utf-8")
    fejlec = f.readline()
    for sor in f:
        versenyzok.append(Versenyzo(fejlec, sor))
    f.close()

def GetFoldreszek():
    foldreszek = []
    for versenyzo in versenyzok:
        if versenyzo.Foldresz not in foldreszek:
            foldreszek.append(versenyzo.Foldresz)
    print(f"6.feladat:\nFöldrészek, amelyekről a versenyzők indultak: ", end="")
    kodtabla = "-_aAáÁbBcCdDeEéÉfFgGhHiIíÍjJkKlLmMnNoOóÓöÖőŐpPqQrRsStTuUúÚüÜűŰvVwWxXyYzZ"
    lista = sorted(foldreszek, key= lambda word: [kodtabla.index(c) for c in kodtabla])
    for foldresz in lista:
        print(f"{foldresz}", end=" ")