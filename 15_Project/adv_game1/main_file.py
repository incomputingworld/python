from utility import get_player_name, display_intro
from forest import forest_path


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


if __name__ == "__main__":
    play_game()
