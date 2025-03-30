
def display_intro():
    """Display the introduction of the game"""
    print("=" * 60)
    print("Welcome to the Magical Forest Adventure")
    print("=" * 60)
    print("You find yourself at the edge of a mysterious forest.")
    print("Your goal is to find the hidden treasure and return safely.")
    print("Along the way, you'll need to make choices and overcome challenges.")
    print("=" * 60)


def get_player_name():
    """Get player name and return it"""
    name = input("What is your name, brave adventurer? ")
    return name


def make_choice(options):
    """display options and get user chioce"""
    print("\nWhat would you like to do?")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("\nEnter the number of your choice. "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("Please enter a valid number")


def play_game():
    """Main function to start the game"""
    display_intro()
    player_name = get_player_name()

    inventory = []

    treasure_found = forest_path(inventory, player_name)
    # Game conclusion
    print("\n" + "=" * 60)
    print(f"ADVENTURE COMPLETE!")
    print("=" * 60)
    if treasure_found:
        print(f"Welldone {player_name}! You have successfully completed the quest.")
    else:
        print(f"Better luck next time {player_name}! Why not try again with different options.")

    print("\nYour final inventroy contained:")
    if inventory:
        for item in inventory:
            print(item)
    else:
        print("Nothing, your pockets are empty.")

    print("Thank you for playing the Magical Forest Adventure.")
    print("=" * 60)




def forest_path(inventory, player_name):
    """Forst path section of the game"""
    print("\nYou enter the dense forest. The path splits in three directions.")

    options = ["Take the narrow path on the left",
               "Take the wide path in the middle",
               "Take the overgrown path on the right"]

    choice = make_choice(options)

    if choice == 1:
        print("\nYou squeeze through the narrow path...")
        print("You discover a small, hidden cave!")
        options = ["Enter the cave", "Continue on the path"]

        choice = make_choice(options)
        if choice == 1:
            print("\nInside the cave, you find a rusty old key!")
            inventory.append("rusty key")
            print(f"Added 'rusty key' to your inventory.")
            print("You exit the cave and continue your journey.")
            return river_crossing(inventory, player_name)
        elif choice == 2:
            print("\nYou decide not to enter the cave and continue on the path.")
            return river_crossing(inventory, player_name)

    elif choice == 2:
        print("\nYou follow the wide path...")
        print("Suddenly, you encounter a friendly forest elf!")
        print(f"'Greetings, {player_name}!' says the elf.")
        print("'Take this magical amulet. It will protect you on your journey.'")
        inventory.append("magical amulet")
        print(f"Added 'magical amulet' to your inventory.")
        return river_crossing(inventory, player_name)

    elif choice == 3:
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


def river_crossing(inventory, player_name):
    """Handles the river corssing section of the game"""
    print("\nAfter walking for some time, you reach a wide river blocking your path.")

    options = ["Look for a bridge",
               "Try to swim across",
               "Search for another way"]

    choice = make_choice(options)

    match choice:
        case 1:
            print("\nYou walk along the riverbank and find an old wooden bridge!")
            print("It looks rickety, but it should hold your weight.")
            print("You carefully cross the bridge to the other side.")
        case 2:
            print("\nYou prepare to swim across the river...")

            if "magical amulet" in inventory:
                print("As you touch the water, your magical amulet glows.")
                print("Suddenly, you can walk on water! You cross the river easily.")
            else:
                print("The current is stronger than you expected!")
                print("You struggle, but manage to reach the other side, completely soaked.")
        case 3:
            print("\nYou search along the riverbank for another way...")
            print("You discover a small rowboat hidden among the reeds!")
            print("You use the boat to cross the river safely.")
            inventory.append("rowboat")
            print(f"Added 'rowboat' to your inventory.")

    return treasure_room(inventory, player_name)


def treasure_room(inventory, player_name):
    """Handle the treasure room section of the game"""
    print("\nBeyond the river, you find an ancient stone structure.")
    print("It appears to be a temple of some kind.")
    print("At the entrance, there's a large wooden door with a rusty keyhole.")

    if "rusty key" in inventory:
        print("\nYou remember the rusty key you found earlier.")
        print("You insert the key into the lock, and it fits perfectly!")
        print("The door creaks open, revealing a chamber filled with golden treasure!")
        print(f"Congratulations, {player_name}! You've found the hidden treasure!")
        return True

    options = ["Search around the temple",
               "Try to break the door",
               "Return to the forest to look for a key"]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou search around the temple...")
        print("After some time, you find a small opening in the back wall.")
        print("It's just big enough for you to squeeze through.")
        print("Inside, you find the treasure chamber!")
        print(f"Congratulations, {player_name}! You've found the hidden treasure!")
        return True

    elif choice == 2:
        print("\nYou try to break down the door...")
        print("But it's too sturdy, and you only hurt your shoulder.")
        print("It seems impossible to enter without a key.")
        print(f"Sorry, {player_name}. You were close, but couldn't get the treasure.")
        return False

    else:  # choice#3
        print("\nYou decide to return to the forest to look for a key.")
        print("But as you turn around, you see a dark figure blocking your path.")
        print("It's the forest guardian! He demands to know your purpose.")

        options = ["Tell the truth about seeking treasure",
                   "Make up a story",
                   "Offer something from your inventory"]

        choice = make_choice(options)

        if choice == 1:
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

        elif choice == 2:
            print("\nYou make up a story about being lost in the forest.")
            print("The guardian frowns. 'I sense deception in your words.'")
            print("He vanishes, leaving you alone at the temple entrance.")
            print("With no way to open the door, you must leave empty-handed.")
            print(f"Sorry, {player_name}. You were close, but couldn't get the treasure.")
            return False

        elif choice == 3:
            if len(inventory) > 0:
                choice = make_choice(inventory)
                offered_item = inventory[choice-1]
                if offered_item == "magical amulet":
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
                else:
                    print("The guardian shakes his head.")
                    print("'This is not what I seek,' he says, returning your offering.")
                    print("He disappears into the forest, leaving you alone.")
                    print(f"Sorry, {player_name}. You were close, but couldn't get the treasure.")
                    return False
            else:
                print("\nYou don't have anything to offer the guardian.")
                print("He shakes his head disapprovingly and vanishes.")
                print("With no way to open the door, you must leave empty-handed.")
                print(f"Sorry, {player_name}. You were close, but couldn't get the treasure.")
                return False





if __name__ == "__main__":
    play_game()











