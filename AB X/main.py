def main() -> None:
    pass  # Kezd a kódolást itt!


print("Szám abszolút értéke")
x: int = int(input("x = "))
if x < 0:
    # igaz ág vagy igaz blokk
    x = x * -1

print(f"|x|={x}")


if __name__ == "__main__":
    main()
