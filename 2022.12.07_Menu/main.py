from data import FajlOlvas
from menu import menu
from fgvk import *

FajlOlvas()
menupontok = ["Tanuló keresése", "Minden tanuló listázása", "Új tanuló rögzítése", "Tanuló adatainak módosítása", "Tanuló törlése"]
valasztas = menu(menupontok)
while valasztas != 0:
    if valasztas == 1:
        VizsgazoKeres()
    elif valasztas == 2:
        ListOsszes()
    elif valasztas == 3:
        UjNber()
    elif valasztas == 4:
        MODOSit()
    elif valasztas == 5:
        TanuloTorol()
    valasztas = menu(menupontok)
FajlIr()