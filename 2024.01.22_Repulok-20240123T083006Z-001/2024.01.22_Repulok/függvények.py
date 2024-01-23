from repülő import *
from math import *

repulok=[]

def Fajlolvas():
    f= open("utasszallitok.txt" , "r", encoding="utf-8")
    f.readline()
    for sor in f:
        egyrepulo= repulo(sor)
        repulok.append(egyrepulo)
    f.close()

def Repulokszam():
    return len(repulok)

def Boeingdarabszam():
    db=0
    for repulo in repulok:
        if "Boeing" in repulo.Tipus:
            db+=1
    return db
              
def Legtobbutas():
    maxRepulo= repulok[0]
    for repulo in repulok:
        if repulo.getmaxutas()> maxRepulo.getmaxutas():
            maxRepulo=repulo
    return maxRepulo  

def Fajlirj():
    f= open("utasszallitok_new.txt", "w", encoding="utf-8")
    f.write("típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv\n")
    for repulo in repulok:
        f.write(f"{repulo.Tipus};{repulo.Ev};{repulo.getmaxutas()};{repulo.getmaxszemelyzet()};{repulo.Sebesseg};{round(repulo.Felszallotomeg/1000,0)};{round (repulo.Fesztav*3.2808,0)}\n")
    f.close()



def szamol(q0 ,p0):
    return sqrt(5*((pow(q0/p0+1, 2/7))-1))

def Statkeszit():
    stat= {}
    for repulo in repulok:
        gyarto = repulo.Tipus.split()[0]
        if gyarto in stat.keys():
            stat[gyarto]+=1
        else:
            stat[gyarto] = 1
    return stat            

            





