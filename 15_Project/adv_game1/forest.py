from utility import make_choice
from river_cross import river_crossing


def forest_path(inventory, player_name):
    """Forst path section of the game"""
    print("\nYou enter the dense forest. The path splits in three directions.")

    options = ["Take the narrow path on the left",
               "Take the wide path in the middle",
               "Take the overgrown path on the right"]
    choice = make_choice(options)
    if choice == 1:
        return forest_ch_1(inventory, player_name)
    elif choice == 2:
        return forest_ch_2(inventory, player_name)
    elif choice == 3:
        return forest_ch_3(inventory, player_name)


def forest_ch_1(inventory, player_name):
    print("\nYou squeeze through the narrow path...")
    print("You discover a small, hidden cave!")
    options = ["Enter the cave", "Continue on the path"]

    choice = make_choice(options)
    if choice == 1:
        print("\nInside the cave, you find a rusty old key!")
        inventory.append("rusty key")
        print(f"Added 'rusty key' to your inventory.")
        print("You exit the cave and continue your journey.")
    elif choice == 2:
        print("\nYou decide not to enter the cave and continue on the path.")

    return river_crossing(inventory, player_name)


def forest_ch_2(inventory, player_name):
    print("\nYou follow the wide path...")
    print("Suddenly, you encounter a friendly forest elf!")
    print(f"'Greetings, {player_name}!' says the elf.")
    print("'Take this magical amulet. It will protect you on your journey.'")
    inventory.append("magical amulet")
    print(f"Added 'magical amulet' to your inventory.")
    return river_crossing(inventory, player_name)


def forest_ch_3(inventory, player_name):
    print("\nYou push through the overgrown path...")
    print("Oh no! You've disturbed a nest of angry bees!")
    if "magical amulet" in inventory:
        print("The magical amulet glows and creates a shield around you.")
        print("The bees can't penetrate the shield! You escape safely.")
    else:
        print("You run as fast as you can to escape the bees.")
        print("Unfortunately, you get stung several times before escaping.")
        print("You lose some time recovering from the stings.")

    return river_crossing(inventory, player_name)
