from fuggvenyek import *
from fuggvenyek import orszagVanE


orszagok = ['Abházia', 'Afganisztán', 'Algéria', 'Angola', 'Argentína', 'Ausztrália', 'Bolívia', 'Botswana', 'Brazília', 'Burkina Faso', 'Chile', 
	    'Csád', 'Dél-afrikai Köztársaság', 'Dél-Szudán', 'Ecuador', 'Egyesült Királyság', 'Egyiptom', 'Elefántcsontpart', 'Etiópia', 'Európai Unió',
	    'Fehéroroszország', 'Finnország','Franciaország', 'Fülöp-szigetek', 'Gabon', 'Ghána', 'Grönland', 'Guinea', 'Guyana', 'India', 'Indonézia', 
            'Irak', 'Irán', 'Japán', 'Jemen', 'Kamerun', 'Kanada', 'Kazahsztán', 'Kenya', 'Kína', 'Kolumbia', 'Kongói Demokratikus Köztársaság', 'Kongói Köztársaság', 
            'Közép-afrikai Köztársaság', 'Laosz', 'Lengyelország', 'Líbia', 'Madagaszkár', 'Malajzia', 'Mali', 'Marokkó', 'Mauritánia', 'Mexikó', 'Mianmar', 
            'Mongólia', 'Mozambik', 'Namíbia', 'Németország', 'Niger', 'Nigéria', 'Norvégia', 'Nyugat-Szahara', 'Olaszország', 'Omán', 'Oroszország', 'Pakisztán', 
            'Pápua Új-Guinea', 'Paraguay', 'Peru', 'Románia', 'Spanyolország', 'Svédország', 'Szaúd-Arábia', 'Szomália', 'Szudán', 'Tanzánia', 'Thaiföld', 
            'Törökország', 'Türkmenisztán', 'Uganda', 'Új-Zéland', 'Ukrajna', 'USA', 'Üzbegisztán', 'Venezuela', 'Vietnam', 'Zambia', 'Zimbabwe']

teruletek = [8432, 652090, 2381741, 1246700, 2780400, 7692024, 1098581, 582000, 8517877, 274967, 756102, 1284200, 1221037, 619745, 256369, 242900, 1002000, 
             322463, 1104300, 4324782, 207600, 338424, 547030, 300000, 267668, 238533, 2166086, 245857, 214970, 3287263, 1919931, 435244, 1648195, 377930, 
             527968, 475442, 9984670, 2724900, 580367, 9677009, 1141748, 2344858, 342000, 622984, 236800, 312658, 1759540, 587041, 230803, 1240192, 446550, 
             1025520, 1972550, 676578, 1564116, 801590, 824268, 357114, 1267000, 923768, 323782, 266000, 301336, 309500, 17098242, 796095, 462840, 406752, 
             1285216, 238391, 505992, 450295, 2149690, 637657, 1861484, 945087, 513120, 783562, 488100, 241550, 270467, 603500, 9826630, 447400, 912050, 
              331212, 752612, 390757]

print("1.Feladat: Az országok nevei:")
orszagVanE(orszagok)
print(f"2. Feladat: Az országok száma: {len(orszagok)}")
maxIndex = legnagyobbKeres(teruletek, True)
print(f"3. Feladat: A legnagyobb ország: {orszagok[maxIndex]}\tTerülete: {teruletek[maxIndex]}")
minIndex = legnagyobbKeres(teruletek, False)
print(f"4. Feladat: A legkisebb ország: {orszagok[minIndex]}\tTerülete: {teruletek[minIndex]}")
print(f"5.Feladat: A legnagyobb és legkisebb közti különbség: {teruletek[maxIndex]-teruletek[minIndex]}")
print(f"6.Feladat: 400 000 km2 országok:")
NegyzazEzerFelett(orszagok, teruletek)