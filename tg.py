import random

def math_task():
    print("Valassz nehezseget:")
    print("1. Konnyu (osszeadas)")
    print("2. Kozep (szorzas)")
    print("3. Nehez (gyokszamitas)")
    szint = input("Nehezseg (1-3): ")
    
    if szint == "1":
        szam1 = random.randint(1, 20)
        szam2 = random.randint(1, 20)
        bekert = input(f"Mennyi {szam1} + {szam2}? ")
        if int(bekert) == szam1 + szam2:
            print("Ez az, helyes valasz!")
        else:
            print("Nem jo, ezt meg kell meg gyakorolni.")
    elif szint == "2":
        szam1 = random.randint(2, 10)
        szam2 = random.randint(2, 10)
        bekert = input(f"Mennyi {szam1} * {szam2}? ")
        if int(bekert) == szam1 * szam2:
            print("Ez az, helyes valasz!")
        else:
            print("Nem jo, ezt meg kell meg gyakorolni.")
    elif szint == "3":
        szam1 = random.randint(1, 100)
        eredmeny = int(szam1 ** 0.5)
        bekert = input(f"Mennyi a gyoke ennek: {szam1} (kerekits egeszre)? ")
        if int(bekert) == eredmeny:
            print("Ez az, helyes valasz!")
        else:
            print(f"Nem jo, a helyes egesz gyok: {eredmeny}")
    else:
        print("Ilyen nehezseg nincs.")

def info_task():
    kerdesek = [
        ("Hany bit egy byte?", "8"),
        ("Mi a kozponti feldolgozo egyseg roviditese?", "cpu")
    ]
    k = random.choice(kerdesek)
    bekert = input(f"Informatika kerdes: {k[0]} ")
    if bekert.strip().lower() == k[1]:
        print("Tokeletes, ugyes vagy!")
    else:
        print("Nem talalt, a helyes valasz: " + k[1])

def main():
    print("Feladatgeneralor elinditva...")
    print("1. Matek")
    print("2. Info")
    valasztas = input("Valassz egy modot (1 vagy 2): ")
    
    if valasztas == "1":
        math_task()
    elif valasztas == "2":
        info_task()
    else:
        print("Ilyen opcio nincsen.")

if __name__ == "__main__":
    main()