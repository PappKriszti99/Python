import math


def összead(a: int, b: int) -> int:
    return a + b


def háromszög(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a


def háromszög_kerület(a: int, b: int, c: int) -> int:
    return a + b + c


def háromszög_terület(a: int, b: int, c: int) -> float:
    s: float = háromszög_kerület(a, b, c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def ker_ter(a: int, b: int, c: int) -> None:
    k: int = háromszög_kerület(a, b, c)
    t: float = háromszög_terület(a, b, c)
    print(f"k={k}")
    print(f"t={t}")


# a fűgvény fej azzal kell kezdődnie
# azonosító mint az összead
# kell paraméter
# egy utasítás a végén.
# meg kell viszatérítési érték a -> után.
# return után az a+b kifejezés a visszatérítési értékét határozza meg


def main() -> None:
    # a fggvény hívása(visszatérési érték elveszik):
    összead(3, 4)
    print(f"3+4 összege={összead(3, 4)}")
    # 3 és a 4 literál a fg. aktuális paraméterei)
    print(f"3,4,5 háromszög szerk: {háromszög(3,4,5)}")
    print("háromszög megszerkeszthetősége, kerülete, területe:")
    oldal_a: int = int(input("a="))
    oldal_b: int = int(input("b="))
    oldal_c: int = int(input("c="))
    if háromszög(oldal_a, oldal_b, oldal_c):
        # kerület terület számítás
        ker_ter(oldal_a, oldal_b, oldal_c)
    else:
        print("a háromszög nem szerkeszthető!")


if __name__ == "__main__":
    main()
