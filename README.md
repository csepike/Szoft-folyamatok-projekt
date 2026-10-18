# The 10 Nights of the Border Tower

A console-based tower defence / survival game written in Python. Over 10 days and nights the player defends a border tower: by day they gather resources and prepare, by night they have to withstand different kinds of attacks.

University project for the *Software Processes* course (University of Szeged, BSc in Computer Science).

## Game overview

- **10 days, 10 nights.** The game ends if the player's HP or the tower's HP reaches zero. Surviving the 10th night wins the game.
- **Day phase:** 2 actions per day – gather wood, stone, food and herbs, repair the tower, build traps and barricades, brew potions, rest or scout.
- **Night phase:** use a tool (signal horn, potion), then choose a combat stance. There are three attack types: beasts, raiders and sieges.
- **Upgrades:** after each night the player picks one upgrade from a randomly offered selection.

## My contribution

The base game was chosen as part of the course. I implemented the two features below and their tests on my own.

### 1. Difficulty levels (`feature1.py`)

At the start of the game the player chooses one of three levels: **easy, medium or hard**. The choice sets the starting values and multipliers:

| | Easy | Medium | Hard |
|---|---|---|---|
| Attack strength | ×0.8 | ×1.1 | ×1.4 |
| Gathering efficiency | ×1.2 | ×1.0 | ×0.7 |
| Starting HP (player / tower) | 25 / 25 | 20 / 22 | 16 / 18 |
| Starting wood and stone | 7-7 | 4-4 | 2-2 |
| Starting food | 6 | 4 | 2 |
| Single-use items | more | fewer | none |

### 2. Random daytime events (`feature2.py`)

At the start of each day there is a 30% chance that something happens, with at most one event per day. There are six different events:

- finding abandoned supplies,
- a guard gets injured (HP decreases),
- a storm (gathering efficiency drops),
- spoiled food,
- a traveller arrives (defence bonus for the next night),
- a scout party returns (HP increases, food decreases, defence bonus).

### 3. Tests (`test_feature1.py`, `test_feature2.py`)

The features come with `pytest` tests. For example, they check that each difficulty level sets the correct multipliers, and that daytime events never raise errors or leave the food supply negative.

## Running the game

Requirements: Python 3.

```bash
python border_tower_game.py
```

The game is controlled by typing numbers. At the end you can start a new game.

### Running the tests

```bash
pip install pytest
pytest
```

## Author:
Cséplő Bálint Gábor – [github.com/csepike](https://github.com/csepike)
