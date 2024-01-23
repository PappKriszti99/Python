# használandó osztály importja:
from épület import épület


def beolvas(forrás: str) -> list[épület]:
    épületek: list[épület] = []
    # állomány  beolvasása
    # with és az open egy előkészítés az állomány olvasását
    # épült sor létrehoz egy osztálypéldányt
    with open(forrás, "r", encoding="UTF-8") as file:
        for sor in file.read().splitlines()[1:]:
            épületek.append(épület(sor))
    return épületek


def emeltek_összege(éppületek: list[épület]) -> int:
    összeg: int = 0
    for épület in éppületek:
        összeg += épület.emelet
    return összeg


def legmagasabb_épület(épületek: list[épület]) -> épület:
    legmagasabb: épület = épületek[0]
    for épület in épületek[1:]:
        if épület.magasság > legmagasabb.magasság:
            legmagasabb = épület
    return legmagasabb


def épület_str(épület: épület) -> str:
    vissza: str = ""
    vissza += f"\tnév: {épület.név}\n"
    vissza += f"\tváros: {épület.város}\n"
    vissza += f"\tország: {épület.ország}\n"
    vissza += f"\tmagasság: {épület.magasság}m\n"
    vissza += f"\temelet: {épület.emelet}\n"
    vissza += f"\tépült: {épület.épült}\n"
    return vissza

def van_olasz(épületek:list[épület])-> bool:
    van:bool=False
    for é in épületek:
        if é.ország=="Olaszország":
            van=True
            break
    return van

def épületek_száma(épületek:list[épület],határ_láb:float)->int:
    darab:int=0
    for a in épületek:
        if a.magasság_láb> határ_láb:
            darab+=1
    return darab



def stat_összeállit(épületek:list[épület])->dict[str, int]:
    stat: dict[str,int]={}
    for e in épületek:
        if e.ország in stat:
            stat[e.ország]+=1
        else:
            stat[e.ország]=1
    return stat        

def stat_str(stat:dict[str,int]) -> str:
    vissza:str=""
    for k, v in stat.items():
        vissza+=f"{k} - {v} db\n"
    return vissza    













def main() -> None:
    # 2. feladat
    épületek: list[épület] = beolvas("legmagasabb.txt")
    print(f"3. feladat: épületek száma: {len(épületek)} db")
    print(f"4. feladat: emeletek összege: {emeltek_összege(épületek)}")
    print("5. feladat: A legmagasabb épület adatai:")
    legmagasabb: épület = legmagasabb_épület(épületek)
    print(épület_str(legmagasabb))
    print(f"6. feladat:{"van"if van_olasz(épületek) else "Nincs" } Olasz épület az adatok között! ")
    print(f"7.feladat:  666 lábnál magasabb épületek száma : {épületek_száma(épületek, 666)} ")
    print(f"8. feladat: Országo statisztika")
    print(stat_str(stat_összeállit(épületek)))






if __name__ == "__main__":
    main()
