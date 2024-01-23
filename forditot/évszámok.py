from datetime import datetime, timedelta


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def kovetkezo_nap(datum):
    try:
        ev, honap, nap = map(int, datum.split("-"))
        jelenlegi_datum = datetime(ev, honap, nap)

        kovetkezo_datum = jelenlegi_datum + timedelta(days=1)

        if kovetkezo_datum.month != honap or kovetkezo_datum.year != ev:
            if honap == 2 and nap == 28 and leap_year(ev):
                kovetkezo_datum = datetime(ev, 2, 29)
            else:
                kovetkezo_datum = datetime(
                    kovetkezo_datum.year, kovetkezo_datum.month, 1
                )

        return kovetkezo_datum.strftime("%Y-%m-%d")
    except ValueError:
        return "Hibás dátum formátum. Használj éééé-hh-nn formátumot!"


if __name__ == "__main__":
    datum = input("Kérem, adjon meg egy dátumot (éééé-hh-nn formátumban): ")
    kovetkezo = kovetkezo_nap(datum)
    print(f"A naptárban a következő nap: {kovetkezo}")
