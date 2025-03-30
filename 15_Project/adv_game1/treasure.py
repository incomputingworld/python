from utility import make_choice


def treasure_room(inventory, player_name):
    """Handle the treasure room section of the game"""
    treasure_room_desc()
    rusty_key = check_rusty_key_in_inventory(inventory, player_name)
    if rusty_key:
        return rusty_key

    options = ["Search around the temple",
               "Try to break the door",
               "Return to the forest to look for a key"]
    choice = make_choice(options)
    if choice == 1:
        return tresure_ch_1(player_name)
    elif choice == 2:
        return tresure_ch_2(player_name)
    else:  # choice#3
        return treasure_ch_3(inventory, player_name)


def treasure_room_desc():
    print("\nBeyond the river, you find an ancient stone structure.")
    print("It appears to be a temple of some kind.")
    print("At the entrance, there's a large wooden door with a rusty keyhole.")


def check_rusty_key_in_inventory(inventory, player_name):
    if "rusty key" in inventory:
        print("\nYou remember the rusty key you found earlier.")
        print("You insert the key into the lock, and it fits perfectly!")
        print("The door creaks open, revealing a chamber filled with golden treasure!")
        print(f"Congratulations, {player_name}! You've found the hidden treasure!")
        return True
    return False


def tresure_ch_1(player_name):
    print("\nYou search around the temple...")
    print("After some time, you find a small opening in the back wall.")
    print("It's just big enough for you to squeeze through.")
    print("Inside, you find the treasure chamber!")
    print(f"Congratulations, {player_name}! You've found the hidden treasure!")
    return True


def tresure_ch_2(player_name):
    print("\nYou try to break down the door...")
    print("But it's too sturdy, and you only hurt your shoulder.")
    print("It seems impossible to enter without a key.")
    print(f"Sorry, {player_name}. You were close, but couldn't get the treasure.")
    return False


def treasure_ch_3(inventory, player_name):
    tresure_ch_3_desc()

    options = ["Tell the truth about seeking treasure",
               "Make up a story",
               "Offer something from your inventory"]

    choice = make_choice(options)

    if choice == 1:
        return guardian_ch_1(inventory, player_name)
    elif choice == 2:
        return guardian_ch_2(player_name)
    elif choice == 3:
        if len(inventory) == 0:
            return no_inventory_lose_game(player_name)

        print("\nYou offer the guardian something from your inventory:")
        choice = make_choice(inventory)
        offered_item = inventory[choice - 1]

        if offered_item == "magical amulet":
            return amulet_offered_win_game(inventory, player_name)
        else:
            return no_amulet_lose_game(player_name)



def tresure_ch_3_desc():
    print("\nYou decide to return to the forest to look for a key.")
    print("But as you turn around, you see a dark figure blocking your path.")
    print("It's the forest guardian! He demands to know your purpose.")


def guardian_ch_1(inventory, player_name):
    print("\nYou explain honestly that you're seeking the temple's treasure.")
    print("The guardian appreciates your honesty.")
    print("'The treasure belongs to those who speak truth,' he says.")
    print("He hands you an ancient key and disappears into the forest.")

    inventory.append("ancient key")
    print(f"Added 'ancient key' to your inventory.")

    print("\nYou return to the temple door and use the ancient key.")
    print("The door opens, revealing the treasure chamber!")
    print(f"Congratulations, {player_name}! You've found the hidden treasure!")
    return True


def guardian_ch_2(player_name):
    print("\nYou make up a story about being lost in the forest.")
    print("The guardian frowns. 'I sense deception in your words.'")
    print("He vanishes, leaving you alone at the temple entrance.")
    print("With no way to open the door, you must leave empty-handed.")
    print(f"Sorry, {player_name}. You were close, but couldn't get the treasure.")
    return False


def no_inventory_lose_game(player_name):
    print("\nYou don't have anything to offer the guardian.")
    print("He shakes his head disapprovingly and vanishes.")
    print("With no way to open the door, you must leave empty-handed.")
    print(f"Sorry, {player_name}. You were close, but couldn't get the treasure.")
    return False


def amulet_offered_win_game(inventory, player_name):
    print("The guardian is impressed by your sacrifice.")
    print("'The amulet is a powerful gift,' he says.")
    print("He hands you a golden key in exchange and disappears.")

    inventory.remove("magical amulet")
    inventory.append("golden key")
    print(f"Removed 'magical amulet' from your inventory.")
    print(f"Added 'golden key' to your inventory.")

    print("\nYou use the golden key to open the temple door.")
    print("Inside, you find the treasure chamber!")
    print(f"Congratulations, {player_name}! You've found the hidden treasure!")
    return True


def no_amulet_lose_game(player_name):
    print("The guardian shakes his head.")
    print("'This is not what I seek,' he says, returning your offering.")
    print("He disappears into the forest, leaving you alone.")
    print(f"Sorry, {player_name}. You were close, but couldn't get the treasure.")
    return False
