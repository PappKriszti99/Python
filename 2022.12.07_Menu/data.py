from vizsgazo import *

vizsgazok = []

def FajlOlvas():
    f = open("vizsgazok.txt", "r", encoding="UTF-8")
    for sor in f:
        vizsgazok.append(Vizsgazo(sor))
    f.close()