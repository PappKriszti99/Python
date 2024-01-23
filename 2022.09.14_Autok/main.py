from fuggvenyek import *

autok = ["Honda Accord", "Honda Civic", "Opel Corsa", "Renault Laguna", "Suzuki Ignis", "Ford Focus", "Skoda Fabia", "Honda Jazz", "Suzuki SX4", "Opel Astra",
         "BMW E3", "Ford Puma", "Honda CRV", "Renault Clio", "Suzuki Swift", "Toyota Auris", "Skoda Superb", "Opel Vectra", "Ford Mondeo", "Toyota IQ", "Renault Megane",
         "BMW E320i", "Suzuki Alto", "Ford Kuga", "Honda Legend", "Renault Alpine", "Toyota Avensis", "Skoda Yeti"]

kilometerek = [96352, 76084, 20875, 34258, 29802, 27825, 64809, 17348, 80852, 70337, 10469, 55555, 45234, 98745, 13245, 101245, 
               89845, 21223, 21568, 157852, 122453, 54562, 24564, 70337, 22142, 8452, 6452, 7856, ]

print(f"1. Feladat: Az autók darabszáma: {len(autok)}")
print(f"2. Feladat: Az összes megtett km: {getOsszKm(kilometerek)} km")
maxIndex = getMax(kilometerek, 0)
print(f"3. Feladat: A legtöbb km-et megtevő autó: {autok[maxIndex]} - {kilometerek[maxIndex]} km")
masodikMax = getMax(kilometerek, maxIndex)
print(f"4. Feladat: A 2. legtöbb km-et megtevő autó: {autok[masodikMax]} - {kilometerek[masodikMax]} km")
print(f"5. Feladat: Megtett távolság különbsége: {kilometerek[maxIndex]-kilometerek[masodikMax]} km")
