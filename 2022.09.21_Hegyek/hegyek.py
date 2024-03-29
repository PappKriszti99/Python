from fuggvenyek import *

hegyek = ["Ágasvár", "Bálvány", "Büszkés-hegy", "Cserepes-kő", "Csikorgó", "Csóványos", "Darázs-hegy", "Esztea-fő", "Fekete-Sár-bérc", "Felső-Borovnyák (2)",
	  "Felső-Borovnyák (1)", "Fodor-hegy", "Füstös-kő-bérc", "Galya-tető", "Galya-vár", "Gergely-hegy", "Győr-hegy", "Hangyás-bérc (1)", "Hangyás-bérc (2)",
 	  "Hármas-határ-hegy", "Három-kő", "Hegyes-kő", "Hermanház-tető", "Hidas-bérc", "Hosszú-bérc", "Huta-bérc", "Írott-kő", "Ispán-hegy", "Istállós-kő", "Kékes",
 	  "Kerek-hegy", "Kerek-hegy", "Kerek-réti-fő", "Kis-Átal-kő", "Kis-kő", "Kis-kő-hát", "Kis-Sár-bérc", "Kis-Sas-kő", "Kis-tanya", "Kis-Virágos-hegy", "Korom-bérc",
	  "Kőris-hegy", "Kőrös-bérc", "Köves-orom", "Közép-bérc (1)", "Közép-bérc (2)", "Kukocsó-hegy", "Kút-hegy", "Küllő-hegy", "Leány-hegy", "Legyendi-galya", "Magos-fa",
	  "Messzelátó", "Mogyorós-orom", "Muzsla", "Nagy-Átal-kő", "Nagy-Csipkés-tető", "Nagy-Csipkés-tető (3)", "Nagy-Dél (1)", "Nagy-Dél (2)", "Nagy-Dél (3)", "Nagy-Hárs",
 	  "Nagy-Hideg-hegy", "Nagy-Inóc", "Nagy-Kopasz", "Nagy-kő-hát (1)", "Nagy-kő-hát (2)", "Nagy-Kőris", "Nagy-Milic", "Nyárju-hegy (1)", "Nyárju-hegy (2)", "Nyesett-vár",
 	  "Őr-kő (2)", "Őr-kő (1)", "Pes-kő", "Péter hegyese", "Piszkés-tető", "Pogányvár", "Remete-hegy", "Sándor-hegy", "Sas-kő", "Semmi-bérc", "Som-tető", "Szilvási-kő",
	  "Tányéros-töbör", "Tar-kő", "Teréz-hegy", "Tót-hegyes", "Tölgyes-bérc", "Vadkert-tető", "Vargai-Kurta-bérc (1)", "Vargai-Kurta-bérc (2)", "Varsa-tető", "Veres-Sár-bérc",
	  "Virágos-sár (2)", "Virágos-Sár-hegy", "Zsérci-Nagy-Dél (1)", "Zsérci-Nagy-Dél (2)", "Zsérci-Nagy-Dél (3)", "Zsérci-Nagy-Dél (4)"]

magassagok = [789, 956, 952, 823, 778, 938, 834, 797, 930, 932, 945, 931, 912, 964, 837, 783, 831, 863, 854, 795, 904, 792, 884, 971,
	          820, 920, 882, 912, 958, 1014, 827, 790, 880, 787, 787, 939, 925, 830, 916, 868, 825, 944, 956, 787, 807, 804, 941, 878,
              899, 892, 936, 916, 855, 838, 806, 823, 869, 843, 821, 799, 787, 840, 864, 826, 903, 946, 936, 822, 895, 889, 885, 813,
              855, 880, 857, 960, 944, 823, 894, 870, 898, 906, 783, 961, 958, 950, 792, 814, 799, 834, 821, 819, 871, 912, 950, 955,
              879, 877, 859, 850]

maxIndex = GetLegmagasabb(magassagok)
print(f"A legmagasabb hegy: {hegyek[maxIndex]} \tMagassága: {magassagok[maxIndex]} m")
masodikIndex = GetMasodik(magassagok, magassagok[maxIndex])
print(f"A második legmagasabb hegy: {hegyek[masodikIndex]} \tMagassága: {magassagok[masodikIndex]} m")
print(f"A két hegy közti magasság különbség: {magassagok[maxIndex]-magassagok[masodikIndex]} m")
print(f"A 850m-nél magasabb hegyek átlaga: {AtlagSzamol(magassagok)} m")
print(f"Hegyek, amik többször szerepelnek: {GetNevUgyanaz(hegyek)}")