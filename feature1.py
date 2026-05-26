#II. Nehézségi szintek
#Valósíts meg legalább három nehézségi szintet:
#könnyű done
#közepes done
#nehéz done gl hf for this

def nehezsegiszintek():
    print("Válassz nehézségi szintet:")
    print("1. Könnyű")
    print("2. Közepes")
    print("3. Nehéz")
    while True:
        valaszt = input("Választás: ")
        if valaszt == "1":
            return "easy"
        elif valaszt == "2":
            return "medium"
        elif valaszt == "3":
            return "hard"
        else:
            print("Érvénytelen választás.")

#A nehézség legalább az alábbiakra hasson:
#kezdő nyersanyagok done
#maximális HP-értékek done
#az éjszakai támadások ereje done
#a nappali gyűjtés hatékonysága done
#az egyszer használható eszközök száma done

def nehezsegiszintekhatasa(state, nehezseg):
    if nehezseg == "easy":
        state["attack_multiplier"] = 0.8
        state["gather_multiplier"] = 1.2
        state["player_hp"] = 25
        state["player_max_hp"] = 25
        state["tower_hp"] = 25
        state["tower_max_hp"] = 25
        state["wood"] = 7
        state["stone"] = 7
        state["food"] = 6
        state["herbs"] = 3
        state["traps"] = 3
        state["barricades"] = 2
        state["potions"] = 2
        state["signal_horn"] = 2

    elif nehezseg == "medium":
        state["attack_multiplier"] = 1.1
        state["gather_multiplier"] = 1
        state["player_hp"] = 20
        state["player_max_hp"] = 20
        state["tower_hp"] = 22
        state["tower_max_hp"] = 22
        state["wood"] = 4
        state["stone"] = 4
        state["food"] = 4
        state["herbs"] = 1
        state["traps"] = 1
        state["barricades"] = 1
        state["potions"] = 1
        state["signal_horn"] = 1

    elif nehezseg == "hard":
        print("Gl hf brother")
        state["attack_multiplier"] = 1.4
        state["gather_multiplier"] = 0.7
        state["player_hp"] = 16
        state["player_max_hp"] = 18
        state["tower_hp"] = 18
        state["tower_max_hp"] = 20
        state["wood"] = 2
        state["stone"] = 2
        state["food"] = 2
        state["herbs"] = 0
        state["traps"] = 0
        state["barricades"] = 0
        state["potions"] = 0
        state["signal_horn"] = 0
