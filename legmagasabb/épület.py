class épület:
    # adattagok
    # név;város;ország;magasság;emelet;épült
    név: str
    város: str
    ország: str
    magasság: float
    emelet: int
    épült: int

    # jellemző(valójában metódus, de adattagnak látszik)
    @property
    def magasság_láb(self) -> float:
        return self.magasság * 3.280839895

    # kódtagok
    # speciális függvény-> metódus: kostruktor
    # self-> metódusa kötelező paramétere
    # None->a konstruktor nem tér vissza
    # kostruktor szerepe: osztálypéldány(objektum) felkészítése a használatra(inicializálása)
    # szöveges tipusu segéd változó

    def __init__(self, sor: str) -> None:
        név, város, ország, magasság, emelet, épült = sor.split(";")
        self.név = név
        self.város = város
        self.ország = ország
        self.magasság = float(magasság.replace(",", "."))  # lecseréli a "," pontra
        self.emelet = int(emelet)
        self.épült = int(épült)
