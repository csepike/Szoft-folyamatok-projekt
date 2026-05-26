# -*- coding: utf-8 -*-
import random
from feature1 import nehezsegiszintek, nehezsegiszintekhatasa
from feature2 import nappalaiesemenyesely

# Ez a program egy egyszerű, konzolos fantasy bázisvédelmi játék.

GAME_DAYS = 10

UPGRADES = [
    {
        "key": "keen_traps",
        "name": "Éles csapdák",
        "description": "A csapdák nagyobb védelmet adnak bestiák és portyázók ellen.",
    },
    {
        "key": "reinforced_gate",
        "name": "Megerősített kapu",
        "description": "A barikádok nagyobb védelmet adnak ostromok ellen.",
    },
    {
        "key": "masonry",
        "name": "Kőfalazás",
        "description": "A torony javítása több életerőt állít vissza.",
    },
    {
        "key": "hunter_team",
        "name": "Vadászcsapat",
        "description": "A vadászat során több élelem gyűjthető.",
    },
    {
        "key": "herbal_lore",
        "name": "Füvész szerszám",
        "description": "A gyógynövénygyűjtés hatékonyabb, és a főzet olcsóbb.",
    },
    {
        "key": "field_medic",
        "name": "Tábori gyógyító",
        "description": "A pihenés és a gyógyital több HP-t ad vissza.",
    },
    {
        "key": "watchfire",
        "name": "Jelzőtűz",
        "description": "Pontosabb éjszakai előrejelzés, és a felderítés védelmi bónuszt ad.",
    },
    {
        "key": "veteran_commander",
        "name": "Veterán parancsnok",
        "description": "Minden éjszakai védelmi taktika erősebb lesz.",
    },
]

NIGHT_TEMPLATES = {
    1: {"beasts": 5, "raiders": 0, "siege": 0},
    2: {"beasts": 0, "raiders": 6, "siege": 0},
    3: {"beasts": 0, "raiders": 0, "siege": 7},
    4: {"beasts": 6, "raiders": 3, "siege": 0},
    5: {"beasts": 2, "raiders": 7, "siege": 2},
    6: {"beasts": 0, "raiders": 4, "siege": 9},
    7: {"beasts": 5, "raiders": 5, "siege": 4},
    8: {"beasts": 3, "raiders": 8, "siege": 6},
    9: {"beasts": 7, "raiders": 5, "siege": 8},
    10: {"beasts": 8, "raiders": 8, "siege": 10},
}

STANCE_DATA = {
    "hold_gate": {
        "name": "Kaput tartani",
        "beasts": 0,
        "raiders": 1,
        "siege": 4,
        "description": "Főleg ostromlók ellen erős. Bestiák ellen alig segít.",
    },
    "ranged_defense": {
        "name": "A falakról védekezni",
        "beasts": 2,
        "raiders": 2,
        "siege": 1,
        "description": "Kiegyensúlyozott választás. Bestiák és portyázók ellen jó.",
    },
    "sortie": {
        "name": "Kirohanni",
        "beasts": 3,
        "raiders": 4,
        "siege": 0,
        "description": "Nagyon erős bestiák és portyázók ellen, de a hős nagyobb kockázatot vállal.",
    },
    "defend_supplies": {
        "name": "Készleteket védeni",
        "beasts": 1,
        "raiders": 3,
        "siege": 0,
        "description": "Portyázók ellen hasznos, és csökkenti a lopást.",
    },
    "retreat": {
        "name": "Visszavonulni a toronyba",
        "beasts": 0,
        "raiders": 0,
        "siege": 1,
        "description": "A hőst óvja, de a torony több kárt szenvedhet.",
    },
}

DAY_ACTION_TEXT = {
    "1": "Fa gyűjtése: 3-5 fa. Csapdákhoz és javításhoz fontos.",
    "2": "Kő gyűjtése: 2-4 kő. Javításhoz és barikádokhoz kell.",
    "3": "Vadászat és élelemkeresés: 2-4 élelem. Hosszú távon létfontosságú.",
    "4": "Gyógynövény gyűjtése: 1-3 gyógynövény. Főzetekhez kell.",
    "5": "Torony javítása: -2 fa, -1 kő, +5 torony HP. Kőfalazással még jobb.",
    "6": "Csapda készítése: -2 fa, +1 csapda. Bestiák és kisebb portyák ellen jó.",
    "7": "Barikád építése: -1 fa, -2 kő, +1 barikád. Ostromlók ellen erős.",
    "8": "Gyógyital főzése: gyógynövényből készülő egyszer használható gyógyítás.",
    "9": "Pihenés: +4 HP. Tábori gyógyítóval még erősebb.",
    "10": "Felderítés: pontosabb képet ad az éjszakai támadásról. Jelzőtűzzel bónuszt is ad.",
    "11": "Fejlesztések megtekintése: megmutatja a már megszerzett bónuszokat.",
}
def create_game_state():
    upgrades = {}
    for upgrade in UPGRADES:
        upgrades[upgrade["key"]] = False

    state = {
        "day": 1,
        "player_hp": 20,
        "player_max_hp": 20,
        "tower_hp": 22,
        "tower_max_hp": 22,
        "wood": 5,
        "stone": 4,
        "food": 5,
        "herbs": 1,
        "traps": 1,
        "barricades": 0,
        "potions": 0,
        "signal_horn": 1,
        "upgrades": upgrades,
        "current_attack": None,
        "scouted_today": False,
        "scout_defense_bonus": 0,
    }
    return state


def print_separator():
    print("-" * 60)


def print_intro():
    print_separator()
    print("A HATÁRTORONY TÍZ ÉJSZAKÁJA")
    print_separator()
    print("Fantasy bázisvédelmi játék konzolra.")
    print("Cél: éld túl a 10. éjszakát, amíg megérkezik a felmentősereg.")
    print()
    print("Minden nap 2 akciód van.")
    print("Éjszaka a közeledő fenyegetés ellen kell védekezned.")
    print("A jó döntések fontosak, de kis mértékben a szerencse is szerepet kap.")
    print()
    print("Támadásfajták:")
    print("- Bestiák: a hőst veszélyeztetik, a csapdák jók ellenük.")
    print("- Portyázók: sebezhetnek, és készleteket is lophatnak.")
    print("- Ostromlók: főleg a tornyot rombolják, a barikádok és a kapu védelme jó ellenük.")
    print()
    print("Tipp: ne csak egyféle nyersanyagot gyűjts. A hosszabb játékban")
    print("élelemre, javításra és célzott védelemre is szükséged lesz.")
    print_separator()


def print_status(state):
    print_separator()
    print("Nap:", state["day"], "/", GAME_DAYS)
    print("Hős HP:", state["player_hp"], "/", state["player_max_hp"])
    print("Torony HP:", state["tower_hp"], "/", state["tower_max_hp"])
    print("Fa:", state["wood"], "| Kő:", state["stone"], "| Élelem:", state["food"], "| Gyógynövény:", state["herbs"])
    print("Csapdák:", state["traps"], "| Barikádok:", state["barricades"], "| Gyógyitalok:", state["potions"])
    print("Jelkürt:", state["signal_horn"])
    print_separator()


def print_upgrades(state):
    owned_any = False
    print("Fejlesztések:")
    for upgrade in UPGRADES:
        if state["upgrades"][upgrade["key"]]:
            owned_any = True
            print("-", upgrade["name"], "-", upgrade["description"])
    if not owned_any:
        print("- Nincs még fejlesztés.")
    print_separator()


def print_day_action_help():
    print_separator()
    print("Nappali akciók röviden:")
    print("1.", DAY_ACTION_TEXT["1"])
    print("2.", DAY_ACTION_TEXT["2"])
    print("3.", DAY_ACTION_TEXT["3"])
    print("4.", DAY_ACTION_TEXT["4"])
    print("5.", DAY_ACTION_TEXT["5"])
    print("6.", DAY_ACTION_TEXT["6"])
    print("7.", DAY_ACTION_TEXT["7"])
    print("8.", DAY_ACTION_TEXT["8"])
    print("9.", DAY_ACTION_TEXT["9"])
    print("10.", DAY_ACTION_TEXT["10"])
    print_separator()


def print_night_stance_help():
    print_separator()
    print("Éjszakai taktikák röviden:")
    print("- Kaput tartani: főleg ostromlók ellen erős.")
    print("- A falakról védekezni: kiegyensúlyozott, általánosan jó.")
    print("- Kirohanni: bestiák és portyázók ellen erős, de veszélyes.")
    print("- Készleteket védeni: portyázók és lopás ellen jó.")
    print("- Visszavonulni a toronyba: a hőst védi, de a torony sérülhet.")
    print_separator()


def clamp_hp(state):
    if state["player_hp"] > state["player_max_hp"]:
        state["player_hp"] = state["player_max_hp"]
    if state["tower_hp"] > state["tower_max_hp"]:
        state["tower_hp"] = state["tower_max_hp"]

def get_random_attack_for_day(day, state):
    base = NIGHT_TEMPLATES[day]
    attack = {"beasts": 0, "raiders": 0, "siege": 0}

    for key in attack: #szia
        attack[key] = int(attack[key] * state["attack_multiplier"])


    for key in attack:
        attack[key] = base[key]
        if base[key] > 0:
            attack[key] = attack[key] + random.randint(0, 1)

    if day >= 5:
        strongest_key = find_strongest_attack_key(attack)
        attack[strongest_key] = attack[strongest_key] + random.randint(0, 1)

    if day >= 8:
        strongest_key = find_strongest_attack_key(attack)
        attack[strongest_key] = attack[strongest_key] + 1

    return attack


def find_strongest_attack_key(attack):
    strongest_key = "beasts"
    strongest_value = attack["beasts"]

    if attack["raiders"] > strongest_value:
        strongest_key = "raiders"
        strongest_value = attack["raiders"]

    if attack["siege"] > strongest_value:
        strongest_key = "siege"
        strongest_value = attack["siege"]

    return strongest_key


def describe_attack_vague(attack):
    strongest = find_strongest_attack_key(attack)

    if strongest == "beasts":
        return "Vonyítás és morgás hallatszik az erdőből. Bestiák közelednek."

    if strongest == "raiders":
        return "Füstöt és mozgó fényeket látsz a távolban. Portyázók készülnek."

    return "Dobpergés és nehéz lépések hallatszanak. Ostromlók gyülekeznek."


def describe_attack_exact(attack):
    parts = []

    if attack["beasts"] > 0:
        parts.append("bestiák ereje: " + str(attack["beasts"]))

    if attack["raiders"] > 0:
        parts.append("portyázók ereje: " + str(attack["raiders"]))

    if attack["siege"] > 0:
        parts.append("ostromlók ereje: " + str(attack["siege"]))

    if len(parts) == 0:
        return "Nyugodt éjszaka ígérkezik."

    text = "Várható éjszakai fenyegetés: "
    index = 0

    while index < len(parts):
        if index > 0:
            text = text + ", "
        text = text + parts[index]
        index = index + 1

    return text


def show_day_forecast(state):
    attack = state["current_attack"]
    print("Mai előrejelzés:")
    print(describe_attack_vague(attack))

    if state["upgrades"]["watchfire"]:
        print(describe_attack_exact(attack))

    print_separator()


def choose_menu_option(title, options):
    print(title)

    number = 1
    while number <= len(options):
        print(str(number) + ".", options[number - 1][1])
        number = number + 1

    while True:
        choice = input("Válassz egy lehetőséget: ").strip()

        if choice.isdigit():
            index = int(choice) - 1
            if index >= 0 and index < len(options):
                return options[index][0]

        print("Érvénytelen válasz. Próbáld újra.")
def gather_wood(state): #szia
    amount = random.randint(3, 5) * state["gather_multiplier"]
    state["wood"] = state["wood"] + amount
    print("Sikerült", amount, "faanyagot gyűjtened.")


def gather_stone(state):
    amount = random.randint(2, 4) * state["gather_multiplier"]
    state["stone"] = state["stone"] + amount
    print("Sikerült", amount, "követ gyűjtened.")


def gather_food(state):
    amount = random.randint(2, 4) * state["gather_multiplier"]
    if state["upgrades"]["hunter_team"]:
        amount = amount + 1
    state["food"] = state["food"] + amount
    print("Sikerült", amount, "élelmet szerezni.")


def gather_herbs(state):
    amount = random.randint(1, 3) * state["gather_multiplier"]
    if state["upgrades"]["herbal_lore"]:
        amount = amount + 1
    state["herbs"] = state["herbs"] + amount
    print("Sikerült", amount, "gyógynövényt gyűjtened.")


def repair_tower(state):
    if state["wood"] < 2 or state["stone"] < 1:
        print("Nincs elég fa vagy kő a javításhoz.")
        return False

    heal = 5
    if state["upgrades"]["masonry"]:
        heal = heal + 2

    state["wood"] = state["wood"] - 2
    state["stone"] = state["stone"] - 1
    state["tower_hp"] = state["tower_hp"] + heal
    clamp_hp(state)

    print("A torony", heal, "HP-t gyógyult.")
    return True


def build_trap(state):
    if state["wood"] < 2:
        print("Nincs elég fa csapda készítéséhez.")
        return False

    state["wood"] = state["wood"] - 2
    state["traps"] = state["traps"] + 1
    print("Egy új csapdát készítettél.")
    return True


def build_barricade(state):
    if state["wood"] < 1 or state["stone"] < 2:
        print("Nincs elég nyersanyag barikádhoz.")
        return False

    state["wood"] = state["wood"] - 1
    state["stone"] = state["stone"] - 2
    state["barricades"] = state["barricades"] + 1
    print("Egy új barikádot építettetek.")
    return True


def brew_potion(state):
    herb_cost = 2
    if state["upgrades"]["herbal_lore"]:
        herb_cost = 1

    if state["herbs"] < herb_cost:
        print("Nincs elég gyógynövény a gyógyitalhoz.")
        return False

    state["herbs"] = state["herbs"] - herb_cost
    state["potions"] = state["potions"] + 1
    print("Egy új gyógyital készült.")
    return True


def rest_player(state):
    heal = 4
    if state["upgrades"]["field_medic"]:
        heal = heal + 2

    state["player_hp"] = state["player_hp"] + heal
    clamp_hp(state)
    print("Pihenés után", heal, "HP-t gyógyultál.")


def scout_area(state):
    if state["scouted_today"]:
        print("Ma már felderítetted a környéket.")
        return False

    state["scouted_today"] = True

    if state["upgrades"]["watchfire"]:
        state["scout_defense_bonus"] = 1

    print(describe_attack_exact(state["current_attack"]))

    if state["upgrades"]["watchfire"]:
        print("A jelzőtűz és a felderítés miatt ma éjszaka +1 védelmi bónuszt kapsz.")

    return True
def print_day_actions_menu():
    print("Választható akciók:")
    print("1. Fa gyűjtése - 3-5 fa")
    print("2. Kő gyűjtése - 2-4 kő")
    print("3. Vadászat és élelemkeresés - 2-4 élelem")
    print("4. Gyógynövény gyűjtése - 1-3 gyógynövény")
    print("5. Torony javítása - 2 fa + 1 kő felhasználása")
    print("6. Csapda készítése - 2 fa felhasználása")
    print("7. Barikád építése - 1 fa + 2 kő felhasználása")
    print("8. Gyógyital főzése - gyógynövényből")
    print("9. Pihenés - HP visszatöltése")
    print("10. Felderítés - pontosabb éjszakai információ")
    print("11. Fejlesztések megtekintése")
    print("12. Akciók részletes leírása")


def perform_day_action(state):
    while True:
        print_status(state)
        show_day_forecast(state)
        print_day_actions_menu()

        choice = input("Válassz akciót: ").strip()
        print_separator()

        if choice == "1":
            gather_wood(state)
            return
        if choice == "2":
            gather_stone(state)
            return
        if choice == "3":
            gather_food(state)
            return
        if choice == "4":
            gather_herbs(state)
            return
        if choice == "5":
            if repair_tower(state):
                return
        elif choice == "6":
            if build_trap(state):
                return
        elif choice == "7":
            if build_barricade(state):
                return
        elif choice == "8":
            if brew_potion(state):
                return
        elif choice == "9":
            rest_player(state)
            return
        elif choice == "10":
            if scout_area(state):
                return
        elif choice == "11":
            print_upgrades(state)
        elif choice == "12":
            print_day_action_help()
        else:
            print("Érvénytelen válasz.")


def daily_food_phase(state):
    print_separator()
    print("Esti ellátás:")

    if state["food"] > 0:
        state["food"] = state["food"] - 1
        print("Elfogyasztottatok 1 élelmet.")
    else:
        state["player_hp"] = state["player_hp"] - 2
        print("Nincs elég élelem! A hős 2 HP-t veszít az éhezés miatt.")

    print_separator()


def choose_night_tool(state):
    while True:
        print("Éjszakai előkészületek:")
        print("0. Nem használok külön eszközt")

        if state["signal_horn"] > 0:
            print("1. Jelkürtöt fújni - a legerősebb támadásösszetevő 3-mal csökken")

        if state["potions"] > 0 and state["player_hp"] < state["player_max_hp"]:
            print("2. Gyógyitalt inni - HP visszatöltése")

        print("3. Eszközök rövid leírása")

        choice = input("Választás: ").strip()

        if choice == "0":
            return
        if choice == "1" and state["signal_horn"] > 0:
            use_signal_horn(state)
            return
        if choice == "2" and state["potions"] > 0 and state["player_hp"] < state["player_max_hp"]:
            drink_potion(state)
            return
        if choice == "3":
            print_separator()
            print("Jelkürt: egyszer használható vészmegoldás, amely a legerősebb")
            print("fenyegetés erejét csökkenti 3-mal.")
            print("Gyógyital: azonnal gyógyít az éjszaka előtt.")
            print_separator()
        else:
            print("Érvénytelen válasz.")
def use_signal_horn(state):
    attack = state["current_attack"]
    strongest = find_strongest_attack_key(attack)

    reduced = 3
    if attack[strongest] < reduced:
        reduced = attack[strongest]

    attack[strongest] = attack[strongest] - reduced
    state["signal_horn"] = state["signal_horn"] - 1

    name_text = ""
    if strongest == "beasts":
        name_text = "bestiák"
    elif strongest == "raiders":
        name_text = "portyázók"
    else:
        name_text = "ostromlók"

    print("A jelkürt hangja megzavarta az ellenséget. A", name_text, "fenyegetése", reduced, "ponttal csökkent.")


def drink_potion(state):
    heal = 6
    if state["upgrades"]["field_medic"]:
        heal = heal + 2

    state["potions"] = state["potions"] - 1
    state["player_hp"] = state["player_hp"] + heal
    clamp_hp(state)

    print("Megittál egy gyógyitalt. Visszanyertél", heal, "HP-t.")


def choose_night_stance():
    while True:
        print("Válassz éjszakai taktikádat:")
        print("1. Kaput tartani - főleg ostromlók ellen erős")
        print("2. A falakról védekezni - kiegyensúlyozott választás")
        print("3. Kirohanni - bestiák és portyázók ellen erős, de veszélyes")
        print("4. Készleteket védeni - portyázók és lopás ellen jó")
        print("5. Visszavonulni a toronyba - a hőst védi")
        print("6. Taktikák részletes leírása")

        choice = input("Válassz egy lehetőséget: ").strip()

        if choice == "1":
            return "hold_gate"
        if choice == "2":
            return "ranged_defense"
        if choice == "3":
            return "sortie"
        if choice == "4":
            return "defend_supplies"
        if choice == "5":
            return "retreat"
        if choice == "6":
            print_night_stance_help()
        else:
            print("Érvénytelen válasz. Próbáld újra.")


def get_general_defense_bonus(state):
    bonus = 0

    if state["upgrades"]["veteran_commander"]:
        bonus = bonus + 1

    if state["scout_defense_bonus"] > 0:
        bonus = bonus + state["scout_defense_bonus"]

    return bonus


def apply_stance_modifiers(stance_key, player_damage, tower_damage, theft_points):
    if stance_key == "sortie":
        player_damage = player_damage + 1
    elif stance_key == "retreat":
        if player_damage > 0:
            player_damage = player_damage - 1
        tower_damage = tower_damage + 1
    elif stance_key == "defend_supplies":
        if theft_points > 0:
            theft_points = theft_points - 2
            if theft_points < 0:
                theft_points = 0

    return player_damage, tower_damage, theft_points
def resolve_beasts(state, stance_key, report_lines):
    strength = state["current_attack"]["beasts"]
    if strength <= 0:
        return

    general_bonus = get_general_defense_bonus(state)
    stance_defense = STANCE_DATA[stance_key]["beasts"]

    trap_power = 2
    if state["upgrades"]["keen_traps"]:
        trap_power = trap_power + 1

    traps_used = 0
    trap_defense = 0

    while traps_used < state["traps"] and traps_used < 2 and trap_defense < strength:
        trap_defense = trap_defense + trap_power
        traps_used = traps_used + 1

    state["traps"] = state["traps"] - traps_used

    remaining = strength - trap_defense - stance_defense - general_bonus
    if remaining < 0:
        remaining = 0

    player_damage = (remaining + 1) // 2
    tower_damage = remaining // 2
    theft_points = 0

    player_damage, tower_damage, theft_points = apply_stance_modifiers(
        stance_key, player_damage, tower_damage, theft_points
    )

    state["player_hp"] = state["player_hp"] - player_damage
    state["tower_hp"] = state["tower_hp"] - tower_damage

    text = "Bestiák támadtak (erő: " + str(strength) + ")"
    text = text + ", csapdák felhasználva: " + str(traps_used)
    text = text + ", kapott kár: hős " + str(player_damage) + ", torony " + str(tower_damage)

    report_lines.append(text)


def resolve_raiders(state, stance_key, report_lines):
    strength = state["current_attack"]["raiders"]
    if strength <= 0:
        return

    general_bonus = get_general_defense_bonus(state)
    stance_defense = STANCE_DATA[stance_key]["raiders"]

    trap_power = 1
    if state["upgrades"]["keen_traps"]:
        trap_power = trap_power + 1

    traps_used = 0
    trap_defense = 0

    while traps_used < state["traps"] and traps_used < 1 and trap_defense < strength:
        trap_defense = trap_defense + trap_power
        traps_used = traps_used + 1

    state["traps"] = state["traps"] - traps_used

    remaining = strength - trap_defense - stance_defense - general_bonus
    if remaining < 0:
        remaining = 0

    tower_damage = remaining // 3
    player_damage = remaining // 3
    theft_points = remaining - tower_damage - player_damage

    player_damage, tower_damage, theft_points = apply_stance_modifiers(
        stance_key, player_damage, tower_damage, theft_points
    )

    state["player_hp"] = state["player_hp"] - player_damage
    state["tower_hp"] = state["tower_hp"] - tower_damage

    stolen_text = steal_resources(state, theft_points)

    text = "Portyázók támadtak (erő: " + str(strength) + ")"
    text = text + ", csapdák felhasználva: " + str(traps_used)
    text = text + ", kapott kár: hős " + str(player_damage) + ", torony " + str(tower_damage)

    if stolen_text != "":
        text = text + ", " + stolen_text

    report_lines.append(text)


def resolve_siege(state, stance_key, report_lines):
    strength = state["current_attack"]["siege"]
    if strength <= 0:
        return

    general_bonus = get_general_defense_bonus(state)
    stance_defense = STANCE_DATA[stance_key]["siege"]

    barricade_power = 2
    if state["upgrades"]["reinforced_gate"]:
        barricade_power = barricade_power + 1

    barricades_used = 0
    barricade_defense = 0

    while barricades_used < state["barricades"] and barricades_used < 2 and barricade_defense < strength:
        barricade_defense = barricade_defense + barricade_power
        barricades_used = barricades_used + 1

    state["barricades"] = state["barricades"] - barricades_used

    remaining = strength - barricade_defense - stance_defense - general_bonus
    if remaining < 0:
        remaining = 0

    tower_damage = remaining
    player_damage = remaining // 4
    theft_points = 0

    player_damage, tower_damage, theft_points = apply_stance_modifiers(
        stance_key, player_damage, tower_damage, theft_points
    )

    state["player_hp"] = state["player_hp"] - player_damage
    state["tower_hp"] = state["tower_hp"] - tower_damage

    text = "Ostrom érkezett (erő: " + str(strength) + ")"
    text = text + ", barikádok felhasználva: " + str(barricades_used)
    text = text + ", kapott kár: hős " + str(player_damage) + ", torony " + str(tower_damage)

    report_lines.append(text)
def steal_resources(state, theft_points):
    if theft_points <= 0:
        return ""

    stolen_food = 0
    stolen_wood = 0
    stolen_stone = 0

    while theft_points > 0:
        if state["food"] > 0:
            state["food"] = state["food"] - 1
            stolen_food = stolen_food + 1
        elif state["wood"] > 0:
            state["wood"] = state["wood"] - 1
            stolen_wood = stolen_wood + 1
        elif state["stone"] > 0:
            state["stone"] = state["stone"] - 1
            stolen_stone = stolen_stone + 1
        else:
            break

        theft_points = theft_points - 1

    parts = []
    if stolen_food > 0:
        parts.append(str(stolen_food) + " élelem")
    if stolen_wood > 0:
        parts.append(str(stolen_wood) + " fa")
    if stolen_stone > 0:
        parts.append(str(stolen_stone) + " kő")

    if len(parts) == 0:
        return "nem tudtak lopni"

    result = "elloptak: "
    index = 0

    while index < len(parts):
        if index > 0:
            result = result + ", "
        result = result + parts[index]
        index = index + 1

    return result


def night_phase(state):
    print_separator()
    print("ÉJSZAKA", state["day"])
    print_separator()

    print(describe_attack_exact(state["current_attack"]))

    choose_night_tool(state)

    print_separator()

    stance_key = choose_night_stance()

    print("Választott taktika:", STANCE_DATA[stance_key]["name"])
    print("Leírás:", STANCE_DATA[stance_key]["description"])
    print_separator()

    report_lines = []

    resolve_beasts(state, stance_key, report_lines)
    resolve_raiders(state, stance_key, report_lines)
    resolve_siege(state, stance_key, report_lines)

    clamp_hp(state)

    print("Az éjszaka eseményei:")

    if len(report_lines) == 0:
        print("A mai éjszaka csendes maradt.")
    else:
        index = 0
        while index < len(report_lines):
            print("-", report_lines[index])
            index = index + 1

    print_separator()
    print("Éjszaka vége.")
    print("Hős HP:", state["player_hp"], "/", state["player_max_hp"])
    print("Torony HP:", state["tower_hp"], "/", state["tower_max_hp"])
    print_separator()


def is_game_over(state):
    if state["player_hp"] <= 0:
        print("A hős elesett. A torony elveszett.")
        return True

    if state["tower_hp"] <= 0:
        print("A torony összeomlott. A védelmetek megtört.")
        return True

    return False
def get_available_upgrades(state):
    available = []

    for upgrade in UPGRADES:
        if not state["upgrades"][upgrade["key"]]:
            available.append(upgrade)

    return available


def choose_upgrade_candidates(state):
    available = get_available_upgrades(state)

    if len(available) <= 2:
        return available

    pool = []
    index = 0

    while index < len(available):
        pool.append(available[index])
        index = index + 1

    first = random.choice(pool)
    pool.remove(first)
    second = random.choice(pool)

    result = [first, second]
    return result


def offer_upgrade(state):
    candidates = choose_upgrade_candidates(state)

    if len(candidates) == 0:
        return

    print_separator()
    print("Jutalom a túlélésért: válassz egy fejlesztést!")
    print_separator()

    options = []
    index = 0

    while index < len(candidates):
        upgrade = candidates[index]
        label = upgrade["name"] + " - " + upgrade["description"]
        options.append((upgrade["key"], label))
        index = index + 1

    chosen_key = choose_menu_option("Fejlesztési lehetőségek:", options)

    state["upgrades"][chosen_key] = True

    chosen_upgrade = find_upgrade_by_key(chosen_key)

    if chosen_upgrade is not None:
        print("Megszerzett fejlesztés:", chosen_upgrade["name"])

    print_separator()


def find_upgrade_by_key(key):
    for upgrade in UPGRADES:
        if upgrade["key"] == key:
            return upgrade
    return None


def prepare_new_day(state):
    state["scouted_today"] = False
    state["scout_defense_bonus"] = 0
    state["gather_multiplier"] = 1 #szia
    state["current_attack"] = get_random_attack_for_day(state["day"], state)
    nappalaiesemenyesely(state)


def run_day_phase(state):
    print_separator()
    print("NAP", state["day"])
    print_separator()

    action_number = 1

    while action_number <= 2:
        print("Nappali akció", action_number, "/ 2")
        perform_day_action(state)
        print_separator()
        action_number = action_number + 1


def print_victory_message(state):
    print_separator()
    print("GYŐZELEM!")
    print_separator()

    print("Túlélted mind a tíz éjszakát.")
    print("A felmentősereg megjelent a hajnalban.")

    print("Végső állapot:")
    print("Hős HP:", state["player_hp"], "/", state["player_max_hp"])
    print("Torony HP:", state["tower_hp"], "/", state["tower_max_hp"])
    print("Fa:", state["wood"], "| Kő:", state["stone"], "| Élelem:", state["food"], "| Gyógynövény:", state["herbs"])

    print_separator()


def ask_play_again():
    while True:
        answer = input("Szeretnél újra játszani? (i/n): ").strip().lower()

        if answer == "i":
            return True
        if answer == "n":
            return False

        print("Érvénytelen válasz.")


def play_game():
    #szia
    state = create_game_state()

    nehezseg = nehezsegiszintek()
    nehezsegiszintekhatasa(state, nehezseg)

    print_intro()

    while state["day"] <= GAME_DAYS:
        prepare_new_day(state)
        run_day_phase(state)

        daily_food_phase(state)

        if is_game_over(state):
            return

        night_phase(state)

        if is_game_over(state):
            return

        if state["day"] < GAME_DAYS:
            offer_upgrade(state)

        state["day"] = state["day"] + 1

    print_victory_message(state)


def main():
    while True:
        play_game()
        if not ask_play_again():
            print("Köszönjük a játékot!")
            break
        print()


if __name__ == "__main__":
    main()
