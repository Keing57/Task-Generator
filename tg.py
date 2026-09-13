import random

def math_task():
    szam1 = random.randint(1, 20)
    szam2 = random.randint(1, 20)
    bekert = input(f"Mennyi {szam1} + {szam2}? ")
    if int(bekert) == szam1 + szam2:
        print("Ez az, helyes valasz!")
    else:
        print("Nem jo, ezt meg kell meg gyakorolni.")

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