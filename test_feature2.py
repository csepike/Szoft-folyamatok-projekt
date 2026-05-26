from feature2 import nappalaiesemenyesely
def ensure_state(state): #AI használtam itt
    defaults = {
        "wood": 0,
        "stone": 0,
        "food": 0,
        "herbs": 0,
        "traps": 0,
        "barricades": 0,
        "potions": 0,
        "signal_horn": 0,
        "player_hp": 10,
        "scout_defense_bonus": 0,
        "gather_multiplier": 1.0
    }
    for k, v in defaults.items():
        state.setdefault(k, v)

def test_event_never_crashes(): #AI használtam itt
    state = {"wood": 5, "stone": 5, "food": 5}
    nappalaiesemenyesely(state)
    assert isinstance(state, dict)
def test_no_negative_food():
    state = {"wood": 0, "stone": 0, "food": 0}
    nappalaiesemenyesely(state)
    assert state["food"] >= 0
def test_state_keys_stable():
    state = {"wood": 5, "stone": 5, "food": 5}
    nappalaiesemenyesely(state)
    assert "wood" in state
    assert "stone" in state
    assert "food" in state