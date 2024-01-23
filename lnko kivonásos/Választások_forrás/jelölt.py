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

    def __init__(self, sor: str) -> None:
        ke, sz, vn, kn, p = sor.split(" ")
        self._kerület = int(ke)
        self._szavazatok = int(sz)
        self._vnév = vn
        self._knév = kn
        self._pártnév = p
