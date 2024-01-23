class jelölet:
    _kerület: int
    _szavazatok: int
    _vnév: str
    _knév: str
    _pártnév: str

    def pártnév(self) -> str:
        return self._pártnév

    def pártnév2(self) -> str:
        if self.pártnév() == "-":
            return "független"
        else:
            return self.pártnév()

    def név(self) -> str:
        return f"{self._vnév}{self._knév}"
    
    def szavazat(self) -> int:
        return self._szavazatok
    def párt_nev(self) -> str:
        if self.pártnév() == "-":
            return "Független"
        if self.pártnév() == "HEP":
            return "Hús evők pártja"
        if self.pártnév() == "GYEP":
            return "Gyümölcs evők pártja"
        if self.pártnév() == "ZEP":
            return "Zöldség evők pártja"
        if self.pártnév() == "TISZ":
            return "Tejivók pártja"
        return "Hiba!"


    def __init__(self, sor: str) -> None:
        m: list[str] = sor.split(" ")
        self._kerület = int(m[0])
        self._szavazatok = int(m[1])
        self._vnév = m[2]
        self._knév = m[3]
        self._pártnév = m[4]
