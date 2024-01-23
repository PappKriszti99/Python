class repulo:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.Tipus=adatok[0]
        self.Ev= int(adatok[1])
        self.Utas=adatok[2]
        self.Szemelyzet=[3]
        self.Sebesseg=int(adatok[4])
        self.Felszallotomeg= int(adatok[5])
        self.Fesztav=float(adatok[6] .replace(",","."))
    
    def getmaxutas(self):
        if "-" in self.Utas:
            darabok= self.Utas.split("-")
            return int(darabok[1])
        return int(self.Utas)
    
    def getmaxszemelyzet(self):
        if "-" in self.Szemelyzet: 
            darabok= self.Szemelyzet.split("-")
            return int(darabok[1])
        return str(self.Szemelyzet)

    
    



