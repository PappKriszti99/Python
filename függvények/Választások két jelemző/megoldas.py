from jelölt import jelölet


class megoldas:
    _jelöltek: list[jelölet] = []

    @property
    def jelöltek_száma(self) -> int:
        return len(self._jelöltek)

    @property
    def megjelntek(self) -> int:
        összes: int = 0
        for e in self._jelöltek:
            összes += e.szavazat
        return összes

    @property
    def megjelnteksz(self) -> str:
        arány: float = self.megjelntek / 12345
        százalék: float = arány * 100
        return f"{round(százalék, 2)} % "

    @property
    def legtöbbsz(self) -> int:
        leg: int = self._jelöltek[0].szavazat
        for e in self._jelöltek[1:]:
            if e.szavazat > leg:
                leg = e.szavazat
        return leg

    @property
    def nyertes(self) -> str:
        vissza: str = ""
        legt: int = self.legtöbbsz
        for e in self._jelöltek:
            if e.szavazat == legt:
                vissza += f"\t {e.név} {e.pártnév2}\n"
        return vissza

    def __init__(self, állomány_neve: str) -> None:
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for adatsor in file.read().splitlines():
                self._jelöltek.append(jelölet(adatsor))

    def jelölt_ker(self, nev: str) -> int:
        for e in self._jelöltek:
            if e.név == nev:
                return e.szavazat
        return -1

    def jelölt_kera(self, név: str) -> str:
        szavazat_db: int = self.jelölt_ker(név)
        if szavazat_db != 1:
            return f"{név} {szavazat_db}"
        else:
            return "A kerestt képviselő nem található"
