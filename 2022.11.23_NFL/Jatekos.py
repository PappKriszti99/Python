class Jatekos:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.Nev = adatok[0]
        self.Yard = int(adatok[1])
        self.PasszKiserlet = int(adatok[2])
        self.PasszSikeres = int(adatok[3])
        self.PasszTouchD = int(adatok[4])
        self.EladottLabdak = int(adatok[5])
        self.IranyitoMutato = float(adatok[6].replace(",", "."))
        self.Egyetem = adatok[7]
        self.Meter = round(self.Yard * 0.9144, 0)

    def FormazottNev(self):
        nevDb = self.Nev.split()
        javitott = ""
        for i in range(len(nevDb)):
            if i == len(nevDb)-1:
                javitott += f"{nevDb[i].upper()} "
            else:
                javitott += f"{nevDb[i]} "
        return javitott.strip()

