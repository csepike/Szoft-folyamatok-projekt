#IV. Véletlen nappali események
# #Valósíts meg nappali eseményeket, amelyek minden nap elején vagy végén kis eséllyel bekövetkezhetnek.
import random

DAY_EVENTS = [
    "elhagy",
    "megseb",
    "vihar",
    "megromlott",
    "utazo",
    "felderito"
]

#Elvárás, hogy legalább 6 különböző esemény legyen, és ezek közül naponta legfeljebb 1 történjen meg. done
def nappalaiesemenyesely(state):
    if random.random() < 0.7: #Ai-t használtam itt
        return
    event = random.choice(DAY_EVENTS)
    nappalaiesemeny(state, event)


# találtok elhagyott készleteket done #megsebesül egy őr (Hős HP csökken) done
# #vihar miatt ma kevesebb fát vagy követ lehet gyűjteni done
# #megromlott élelem (néhány élelem elveszik) done
# #egy utazó pontosan figyelmeztet a következő éjszakára done
# #visszatér egy kisebb csapatnyi felderítő (Hős HP nő, egy élelem elveszik, pontosabb előrejelzés a következő éjszakára) done

def nappalaiesemeny(state, event):
    print("Hoppá történt valami:D")
    state.setdefault("wood", 0)
    state.setdefault("stone", 0)
    state.setdefault("food", 0)
    state.setdefault("player_hp",0)
    state.setdefault("herbs", 0)
    state.setdefault("traps", 0)
    state.setdefault("barricades", 0)
    state.setdefault("potions", 0)
    state.setdefault("signal_horn", 0)
    state.setdefault("scout_defense_bonus", 0)
    state.setdefault("gather_multiplier", 1)

    if event == "elhagy":
        gain = random.randint(1, 3)
        state["food"] += gain
        state["wood"] += gain
        state["stone"] += gain
        state["herbs"] += gain
        state["traps"] += gain
        state["barricades"] += gain
        state["potions"] += gain
        state["signal_horn"] += gain

    elif event == "megseb":
        dmg = random.randint(1, 3)
        state["player_hp"] = max(0, state["player_hp"] - dmg)

    elif event == "vihar":
        state["gather_multiplier"] = 0.4

    elif event == "megromlott":
        kaja = random.randint(1, 3)
        state["food"] = max(0, state["food"] - kaja)

    elif event == "utazo":
        state["scout_defense_bonus"] += 2

    elif event == "felderito":
        state["player_hp"] += 2
        state["food"] = max(0, state["food"] - 1)
        state["scout_defense_bonus"] += 1