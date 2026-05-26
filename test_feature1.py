from feature1 import nehezsegiszintekhatasa

def test_easy_difficulty():
    state = {}
    nehezsegiszintekhatasa(state, "easy")

    assert state["gather_multiplier"] == 1.2
    assert state["attack_multiplier"] == 0.8

def test_medium_difficulty():
    state = {}
    nehezsegiszintekhatasa(state, "medium")

    assert state["gather_multiplier"] == 1.0
    assert state["attack_multiplier"] == 1.1

def test_hard_difficulty():
    state = {}
    nehezsegiszintekhatasa(state, "hard")
    assert state["gather_multiplier"] == 0.7
    assert state["attack_multiplier"] == 1.4