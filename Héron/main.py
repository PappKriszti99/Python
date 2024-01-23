import math


def háromszög(oldalak: list[int]) -> bool:
    a: int = oldalak[0]
    b: int = oldalak[1]
    c: int = oldalak[2]
    return a + b > c and a + c > b and b + c > a


def háromszög_kerület(oldalak: list[int]) -> int:
    a: int = oldalak[0]
    b: int = oldalak[1]
    c: int = oldalak[2]
    return a + b + c


def háromszög_terület(oldalak: list[int]) -> float:
    a: int = oldalak[0]
    b: int = oldalak[1]
    c: int = oldalak[2]
    s: float = háromszög_kerület(oldalak) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def ker_ter(oldalak: list[int]) -> None:
    k: int = háromszög_kerület(oldalak)
    t: float = háromszög_terület(oldalak)
    print(f"k={k}")
    print(f"t={t}")


def oldal_bekérése() -> list[int]:
    oldalak: list[int] = []
    oldalak.append(int(input("a=")))
    oldalak.append(int(input("b=")))
    oldalak.append(int(input("c=")))
    return oldalak


def eredmények(oldalak: list[int]) -> None:
    if háromszög(oldalak):
        ker_ter(oldalak)
    else:
        print("a háromszög nem szerkesztehető")


def main() -> None:
    oldalak: list[int] = oldal_bekérése()
    eredmények(oldalak)


if __name__ == "__main__":
    main()
