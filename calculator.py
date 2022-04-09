print("1.GAMRAVLEBA")
print("2.GAYOFA")
print("3.MIMATEBA")
print("4.GAMOKLEBA")

archevani = input("airchie sasurveli moqmedeba: ")

pirveli = int(input("dawere pirveli cifri/ricxvi: "))
meore = int(input("dawere meore cifri/ricxvi: "))

if archevani == "1":
    print(pirveli*meore)
elif archevani == "2":
    if meore == 0:
        print("SHE TAVXEDO 0ZE VER GAYOF")
    else:
        print(pirveli/meore)
elif archevani == "3":
    print(pirveli+meore)
elif archevani == "4":
    print(pirveli-meore)
else:
    print("REEBI GIWERIA SHE TAVXEDO")