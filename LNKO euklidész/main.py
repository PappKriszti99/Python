def main() -> None:
    pass  # Kezd a kódolást itt!


print("LNKO Euklideszi algoritmus!")
a: int = int(input("a= "))
b: int = int(input("b= "))
m: int = -1
while m != 0:
    m = a % b
    a = b
    b = m


print(f"LNKO ={a} ")
#print(f"LNKO ={a} ") hibás itt már mindig 0



if __name__ == "__main__":

    main()
