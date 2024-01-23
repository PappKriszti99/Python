from re import I


kapottSzam = input("Kérem adjon meg egy 2-es számrendszerbeli számot: ")
ujSzam = 0
index = 0
for i in range(len(kapottSzam)-1, 0-1, -1):
    ujSzam += int(kapottSzam[i]) * pow(2, index)
    index += 1
print(f"A 10-es számrendszerbeli szám: {ujSzam}")