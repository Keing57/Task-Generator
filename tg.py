import random

def math_task():
    score = 0
    rounds = 3
    for _ in range(rounds):
        print("Valassz nehezseget:")
        print("1. Konnyu (osszeadas)")
        print("2. Kozep (szorzas)")
        print("3. Nehez (egyszeru egyenlet)")
        szint = input("Nehezseg (1-3): ")
        
        if szint == "1":
            szam1 = random.randint(1, 20)
            szam2 = random.randint(1, 20)
            bekert = input(f"Mennyi {szam1} + {szam2}? ")
            if int(bekert) == szam1 + szam2:
                print("Ez az, helyes valasz!")
                score += 1
            else:
                print("Nem jo, ezt meg kell meg gyakorolni.")
        elif szint == "2":
            szam1 = random.randint(2, 10)
            szam2 = random.randint(2, 10)
            bekert = input(f"Mennyi {szam1} * {szam2}? ")
            if int(bekert) == szam1 * szam2:
                print("Ez az, helyes valasz!")
                score += 1
            else:
                print("Nem jo, ezt meg kell meg gyakorolni.")
        elif szint == "3":
            x = random.randint(1, 10)
            a = random.randint(2, 5)
            b = random.randint(1, 10)
            c = a * x + b
            bekert = input(f"Mennyi x erteke? {a}*x + {b} = {c} ")
            if int(bekert) == x:
                print("Ez az, helyes valasz!")
                score += 1
            else:
                print(f"Nem jo, a helyes x: {x}")
        else:
            print("Ilyen nehezseg nincs.")
    print(f"A jatek veget ert! A pontszamod: {score}/{rounds}")

def info_task():
    score = 0
    rounds = 3
    kerdesek = [
        ("Hany bit egy byte?", "8"),
        ("Mi a kozponti feldolgozo egyseg roviditese?", "cpu"),
        ("Mennyi a decimalis 2-es szam binaris alakja?", "10"),
        ("Melyik logikai kapu ad hamis kimenetet csak akkor, ha mindket bemenete igaz (VAGY/ES/NAND)?", "nand")
    ]
    for _ in range(rounds):
        k = random.choice(kerdesek)
        bekert = input(f"Informatika kerdes: {k[0]} ")
        if bekert.strip().lower() == k[1]:
            print("Tokeletes, ugyes vagy!")
            score += 1
        else:
            print("Nem talalt, a helyes valasz: " + k[1])
    print(f"Az info kor veget ert! Pontszam: {score}/{rounds}")

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