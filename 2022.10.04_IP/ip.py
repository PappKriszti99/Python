def CheckIp():
    reszek = ip.split(".")
    if len(reszek) == 4:
        for resz in reszek:
            if resz.isnumeric():
                if int(resz) < 0 or int(resz) > 255:
                    return False
            else:
                return False
        return True
    return False

ip = input("Adjon meg egy IP címet: ")
if CheckIp():
    print("Az IP cím VALID!")
else:
    print("Az IP cím HIBÁS!")