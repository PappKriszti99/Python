import random

nevek = [
    "Markó Milán",
    "Sándor Ajsa",
    "Zsoldos Donát",
    "Ress Dominik",
    "Molnár Bálint",
    "Varga Vendel",
    "Panyik Krisztián",
    "Marquetant Zalán",
    "Nemes Balázs",
    "Márton Kristóf",
    "Moldován András",
    "Szabó Domonkos",
    "Törös Gergő",
    "Tédi Bálint",
    "Vörös Bence",
    "Podlipnik Ádám"]

def sorsolas():
    index = random.randint(0, len(nevek)-1)
    print(f"A mai szerencsés nyertes: {nevek[index]}")
    nevek.remove(nevek[index])

next = 'i'
while next == 'i' and len(nevek) > 0:
    sorsolas()
    next = input("Következő sorsolás (i/n): ")