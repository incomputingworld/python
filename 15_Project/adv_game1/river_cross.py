from utility import make_choice
from treasure import treasure_room


def river_crossing(inventory, player_name):
    """Handles the river corssing section of the game"""
    print("\nAfter walking for some time, you reach a wide river blocking your path.")

    options = ["Look for a bridge",
               "Try to swim across",
               "Search for another way"]

    choice = make_choice(options)
    match choice:
        case 1:
            river_ch_1()
        case 2:
            river_ch_2(inventory)
        case 3:
            river_ch_3(inventory)
    return treasure_room(inventory, player_name)


def river_ch_1():
    print("\nYou walk along the riverbank and find an old wooden bridge!")
    print("It looks rickety, but it should hold your weight.")
    print("You carefully cross the bridge to the other side.")


def river_ch_2(inventory):
    print("\nYou prepare to swim across the river...")

    if "magical amulet" in inventory:
        print("As you touch the water, your magical amulet glows.")
        print("Suddenly, you can walk on water! You cross the river easily.")
    else:
        print("The current is stronger than you expected!")
        print("You struggle, but manage to reach the other side, completely soaked.")


def river_ch_3(inventory):
    print("\nYou search along the riverbank for another way...")
    print("You discover a small rowboat hidden among the reeds!")
    print("You use the boat to cross the river safely.")
    inventory.append("rowboat")
    print(f"Added 'rowboat' to your inventory.")