def testtomeg_index_szamitas(magasag, testsuly):
    try:
        # Magasság méterben
        magasag_meter = magasag / 100
        # BMI kiszámítása
        bmi = testsuly / (magasag_meter**2)
        return bmi
    except ZeroDivisionError:
        return "A magasság nem lehet nulla!"
    except Exception as e:
        return f"Hiba történt: {str(e)}"


def bmi_ertekezes(bmi):
    if bmi < 16:
        return "Súlyos soványság"
    elif 16 <= bmi < 17:
        return "Mérsékelt soványság"
    elif 17 <= bmi < 18.5:
        return "Enyhe soványság"
    elif 18.5 <= bmi < 24.9:
        return "Normál testsúly"
    elif 25 <= bmi < 29.9:
        return "Túlsúlyos"
    elif 30 <= bmi < 34.9:
        return "I. fokú elhízás"
    elif 35 <= bmi < 39.9:
        return "II. fokú elhízás"
    else:
        return "Súlyos (III. fokú) elhízás"


if __name__ == "__main__":
    magasag = float(input("Kérlek, add meg a magasságod centiméterben: "))
    testsuly = float(input("Kérlek, add meg a testsúlyod kilogrammban: "))

    bmi = testtomeg_index_szamitas(magasag, testsuly)
    if type(bmi) == float:
        print(f"A BMI értéked: {bmi:.2f}")
        print(f"BMI értékelés: {bmi_ertekezes(bmi)}")
    else:
        print(bmi)
