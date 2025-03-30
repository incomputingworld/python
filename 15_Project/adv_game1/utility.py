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


if __name__ == "__main__":
    pass  # Write test code here for this module.
