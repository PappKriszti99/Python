from re import I


def getOsszKm(kilometerek):
    ossz = 0
    for km in kilometerek:
        ossz += km
    return ossz

def getMax(kilometerek, maxIndex):
    index = 0
    max = kilometerek[index]
    for i in range(len(kilometerek)):
        if max < kilometerek[i] and maxIndex != i:
            max = kilometerek[i]
            index = i
    return index


