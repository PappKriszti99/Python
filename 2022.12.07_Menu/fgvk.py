from data import vizsgazok
from vizsgazo import *
from menu import menu
import os

def VizsgazoKeres():
    nev = input("Keresés: Adja meg a nevet: ")
    volt = False
    for vizsgazo in vizsgazok:
        if nev.lower() in vizsgazo.Nev.lower():
            print(f"Név: {vizsgazo.Nev}\tVizsgatípus: {vizsgazo.VizsgaTipus}\tIdő: {vizsgazo.Ido}\tEredmény: {vizsgazo.Eredmeny}" )
            volt = True
    if(not volt):
        print("Nem volt a keresésnek megfelelő vizsgázó!")
    input("\nTovább: Enter")

def ListOsszes():
    for vizsgazo in vizsgazok:
        print(f"Név: {vizsgazo.Nev}\tVizsgatípus: {vizsgazo.VizsgaTipus}\tIdő: {vizsgazo.Ido}\tEredmény: {vizsgazo.Eredmeny}" )
    input("\nTovább: Enter")

def UjNber():
    name = input("Új tanuló neve: ")
    tipus = TipusBeker()
    ido = IdoBeker()
    eredmeny = EredmenyBeker()
    ujVizsgazo = Vizsgazo(f"{name};{tipus};{ido};{eredmeny}")
    vizsgazok.append(ujVizsgazo)

def TipusBeker():
    vizsgatipus = ['Alapismeretek', 'Word', 'Excel', 'Powerpoint', 'Access', 'On-line', 'Webszerkesztés']
    for i in range(len(vizsgatipus)):
        print(f"{i+1}. {vizsgatipus[i]}")
    valasztas = "ab"
    while '0' > valasztas or '7' < valasztas:
        valasztas = input("Adja meg a típus számát [1-7]: ")
    return vizsgatipus[int(valasztas)-1]

def IdoBeker():
    idoklista = []
    while True:
        idoklista = input('ido (mm:ss):  ').strip().split(':')
        if len(idoklista) == 2 and str(idoklista[0]).isnumeric() == True and str(idoklista[1]).isnumeric() == True and int(idoklista[0]) < 45 and int(idoklista[1]) < 60 and int(idoklista[0]) >= 0 and int(idoklista[1]) >= 0:
            break
    return f"{idoklista[0]}:{idoklista[1]}"

def EredmenyBeker():
    while True:
        eredmeny = input("Adja meg az eredményt:")
        if eredmeny.isnumeric() and int(eredmeny) >= 0 and int(eredmeny) <= 100:
            break
    return eredmeny

def MODOSit():
    menupontok = ["Név", "Vizsgatípus", "Idő", "Eredmény"]
    nev = input("Adja meg egy vizsgázó nevét: ")
    for vizsgazo in vizsgazok:
        if vizsgazo.Nev == nev:
            print("Válasszon módosítandó adatot:")
            valasztas = menu(menupontok)
            while valasztas != 0:
                if valasztas == 1:
                    vizsgazo.Nev = input("Adja meg az új nevet: ")
                elif valasztas == 2:
                    vizsgazo.VizsgaTipus = TipusBeker()
                elif valasztas == 3:
                    vizsgazo.Ido = IdoBeker()
                elif valasztas == 4:
                    vizsgazo.Eredmeny = EredmenyBeker()
                valasztas = menu(menupontok)
            break
    else:
        print("Nem található a megadott névnek megfelelő vizsgázó!")
    
def TanuloTorol():
    nev = input("Adja meg a törlendő tanuló nevét: ")
    for vizsgazo in vizsgazok:
        if vizsgazo.Nev == nev:
            vizsgazok.remove(vizsgazo)
            break
    else:
        print("Nem található a megadott névnek megfelelő vizsgázó!")

def FajlIr():
    f = open("vizsgazok.txt", "w", encoding="utf-8")
    for vizsgazo in vizsgazok:
        f.write(f"{vizsgazo.Nev};{vizsgazo.VizsgaTipus};{vizsgazo.Ido.strftime('%M:%S')};{vizsgazo.Eredmeny}\n")
    f.close()




