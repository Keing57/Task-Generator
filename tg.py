import random

class ProblemGenerator:
    def __init__(self):
        self.filename = "eredmenyek.txt"

    def save_result(self, name, mode, score, rounds):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{name};{mode};{score};{rounds}\n")

    def show_results(self):
        print("\n--- EDDIGI EREDMENYEK ---")
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if not lines:
                    print("Meg nincsenek mentesek.")
                else:
                    for line in lines:
                        parts = line.strip().split(";")
                        if len(parts) == 4:
                            print(f"Nev: {parts[0]} | Mod: {parts[1]} | Eredmeny: {parts[2]}/{parts[3]}")
                        else:
                            print(line.strip())
        except FileNotFoundError:
            print("Meg nincs eredmenyek fajl.")
        print("-------------------------")

    def show_leaderboard(self):
        print("\n--- TOP DICSOSÉGTÁBLA ---")
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if not lines:
                    print("Még nincsenek adatok a ranglistához.")
                    print("-------------------------")
                    return
                
                entries = []
                for line in lines:
                    parts = line.strip().split(";")
                    if len(parts) == 4:
                        name, mode, score, rounds = parts
                        entries.append((name, mode, int(score), int(rounds)))
                
                entries.sort(key=lambda x: x[2], reverse=True)
                
                for i, entry in enumerate(entries[:5], 1):
                    print(f"{i}. {entry[0]} ({entry[1]}) - Pont: {entry[2]}/{entry[3]}")
        except FileNotFoundError:
            print("Meg nincs eredmenyek fajl.")
        print("-------------------------")

    def show_statistics(self):
        print("\n--- STATISZTIKA ---")
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if not lines:
                    print("Még nincsenek adatok a statisztikához.")
                    print("-------------------")
                    return
                
                total_games = len(lines)
                total_score = 0
                total_rounds = 0
                
                for line in lines:
                    parts = line.strip().split(";")
                    if len(parts) == 4:
                        total_score += int(parts[2])
                        total_rounds += int(parts[3])
                        
                avg_percentage = (total_score / total_rounds) * 100 if total_rounds > 0 else 0
                print(f"Összes lejátszott kör: {total_games}")
                print(f"Összes elért pont: {total_score}/{total_rounds}")
                print(f"Átlagos teljesítmény: {avg_percentage:.1f}%")
        except FileNotFoundError:
            print("Meg nincs eredmenyek fajl.")
        print("-------------------")

    def clear_results(self):
        open(self.filename, "w", encoding="utf-8").close()
        print("Eredmenyek torolve!")

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def math_task(self, name):
        score = 0
        rounds = 3
        for _ in range(rounds):
            print("Valassz nehezseget:")
            print("1. Konnyu (osszeadas)")
            print("2. Kozep (szorzas)")
            print("3. Nehez (egyszeru egyenlet)")
            print("4. Profi (hatvanyozas)")
            print("5. Mester (szazalekszamitas)")
            print("6. Mesterelmok (prim-e szam)")
            szint = input("Nehezseg (1-6): ")
            
            if szint == "1":
                szam1 = random.randint(1, 20)
                szam2 = random.randint(1, 20)
                bekert = input(f"Mennyi {szam1} + {szam2}? ")
                try:
                    if int(bekert) == szam1 + szam2:
                        print("Ez az, helyes valasz!")
                        score += 1
                    else:
                        print("Nem jo, ezt meg kell meg gyakorolni.")
                except ValueError:
                    print("Ez nem is szam volt!")
            elif szint == "2":
                szam1 = random.randint(2, 10)
                szam2 = random.randint(2, 10)
                bekert = input(f"Mennyi {szam1} * {szam2}? ")
                try:
                    if int(bekert) == szam1 * szam2:
                        print("Ez az, helyes valasz!")
                        score += 1
                    else:
                        print("Nem jo, ezt meg kell meg gyakorolni.")
                except ValueError:
                    print("Ez nem is szam volt!")
            elif szint == "3":
                x = random.randint(1, 10)
                a = random.randint(2, 5)
                b = random.randint(1, 10)
                c = a * x + b
                bekert = input(f"Mennyi x erteke? {a}*x + {b} = {c} ")
                try:
                    if int(bekert) == x:
                        print("Ez az, helyes valasz!")
                        score += 1
                    else:
                        print(f"Nem jo, a helyes x: {x}")
                except ValueError:
                    print("Ez nem is szam volt!")
            elif szint == "4":
                alap = random.randint(2, 5)
                kitevo = random.randint(2, 4)
                eredmeny = alap ** kitevo
                bekert = input(f"Mennyi {alap} a(z) {kitevo}. hatvanya? ")
                try:
                    if int(bekert) == eredmeny:
                        print("Ez az, helyes valasz!")
                        score += 1
                    else:
                        print(f"Nem jo, a helyes valasz: {eredmeny}")
                except ValueError:
                    print("Ez nem is szam volt!")
            elif szint == "5":
                alap_szam = random.choice([50, 100, 200, 300, 400, 500])
                szazalek = random.choice([10, 20, 25, 50])
                eredmeny = int(alap_szam * szazalek / 100)
                bekert = input(f"Mennyi {szazalek}%-a ennek: {alap_szam}? ")
                try:
                    if int(bekert) == eredmeny:
                        print("Ez az, helyes valasz!")
                        score += 1
                    else:
                        print(f"Nem jo, a helyes valasz: {eredmeny}")
                except ValueError:
                    print("Ez nem is szam volt!")
            elif szint == "6":
                szam = random.randint(2, 50)
                helyes = "igen" if self.is_prime(szam) else "nem"
                bekert = input(f"Primszam-e a(z) {szam}? (igen/nem): ")
                if bekert.strip().lower() == helyes:
                    print("Ez az, helyes valasz!")
                    score += 1
                else:
                    print(f"Nem jo, a helyes valasz: {helyes}")
            else:
                print("Ilyen nehezseg nincs.")
        print(f"A jatek veget ert! A pontszamod: {score}/{rounds}")
        self.save_result(name, "Matek", score, rounds)

    def info_task(self, name):
        score = 0
        rounds = 3
        print("Valassz infotematikat:")
        print("1. Hardver es Adatmennyiseg")
        print("2. Logika es Binaris")
        print("3. Programozas es Halozatok")
        tema = input("Tema (1-3): ")
        
        if tema == "1":
            kerdesek = [
                ("Hany bit egy byte?", "8"),
                ("Mi a kozponti feldolgozo egyseg roviditese?", "cpu"),
                ("Hany bajt egy kilobajt a Szamitastechnikaban (1024 vagy 000)?", "1024")
            ]
        elif tema == "2":
            kerdesek = [
                ("Mennyi a decimalis 2-es szam binaris alakja?", "10"),
                ("Melyik logikai kapu ad hamis kimenetet csak akkor, ha mindket bemenete igaz (VAGY/ES/NAND)?", "nand")
            ]
        elif tema == "3":
            kerdesek = [
                ("Milyen programozasi szerkezet hajt vegre utasitas-sorozatot ismetelten (feltetel alapjan)?", "ciklus"),
                ("Mi a neve annak a programozasi elemnek, ami adatokat tarol es nevet kap a memoriaban?", "valtozo"),
                ("Milyen eszkoz kot ossze kulonbozo halozatokat (pl. az otthoni halozatot az internettel)?", "router"),
                ("Mi a helyi halozatok roviditese (angol betuwo)?", "lan")
            ]
        else:
            print("Nincs ilyen tema, kapkodsz az alapbol...")
            kerdesek = [("Hany bit egy byte?", "8")]

        for _ in range(rounds):
            if not kerdesek:
                break
            k = random.choice(kerdesek)
            bekert = input(f"Informatika kerdes: {k[0]} ")
            if bekert.strip().lower() == k[1]:
                print("Tokeletes, ugyes vagy!")
                score += 1
            else:
                print("Nem talalt, a helyes valasz: " + k[1])
        print(f"Az info kor veget ert! Pontszam: {score}/{rounds}")
        self.save_result(name, "Info", score, rounds)

    def run(self):
        print("Feladatgeneralor elinditva...")
        name = input("Add meg a nevedet, kerlek: ")
        while True:
            print(f"\nUdv, {name}! Valassz modot:")
            print("1. Matek")
            print("2. Info")
            print("3. Eredmenyek megtekintese")
            print("4. Top Ranglista")
            print("5. Statisztika")
            print("6. Eredmenyek torlese")
            print("7. Kilepes")
            valasztas = input("Valassz egy opciot (1-7): ")
            
            if valasztas == "1":
                self.math_task(name)
            elif valasztas == "2":
                self.info_task(name)
            elif valasztas == "3":
                self.show_results()
            elif valasztas == "4":
                self.show_leaderboard()
            elif valasztas == "5":
                self.show_statistics()
            elif valasztas == "6":
                self.clear_results()
            elif valasztas == "7":
                print("Viszlat!")
                break
            else:
                print("Ilyen opcio nincsen.")

def main():
    app = ProblemGenerator()
    app.run()

if __name__ == "__main__":
    main()