from Megoldas import *

megoldas = Megoldas()

megoldas.FajlOlvas()
print(f"2.feladat:\n\tAz első fuvar hossza: {megoldas.ElsoKeres()} km")
print(f"3.feladat:\n\tAz utolsó fuvar hossza: {megoldas.UtolsoKeres()} km")
print(f"4.feladat: A futár az alábbi napokon nem dolgozott:")
for nap in megoldas.NapKeres():
    print(f"\t{nap}. nap - {megoldas.GetHetNapja(nap)}")
legtobbFuvar = megoldas.GetLegtobbFuvar()
print(f"6.feladat:\n\tA legtöbb fuvar a hét {legtobbFuvar.Nap}. napján volt: {legtobbFuvar.Sorszam} db")
stat = megoldas.GetStat()
print(f"6.feladat: Az egyes napokon tekert kilóméterek:")
for key, value in stat.items():
    print(f"\t{key}. nap: {value} km")