import sys

import os
import text
from game_logic import main_loop
from player import Player


DEBUG_MODE = 0  # skips intro and stuff


def main():
    # Set difficulty (damage received)
    difficulty = 0

    # Set probability of the enemy spawning in the current room.
    enemy_spawning = 80

    if DEBUG_MODE == 0:
        # clear the screen
        os.system("cls" if os.name == "nt" else "clear")
        print(text.castle)
        text.title("PYTHONIC ADVENTURE")
        # Create a Player
        player = Player()
        player_name = input("Please enter your name:")
    else:
        player = Player()
    os.system("cls" if os.name == "nt" else "clear")
    # player.name = input(...TODO...)

    # add some story

    # Start the game
    # Counter for how many rooms the player cleared.
    room_counter = 0
    game_variables = {
        "difficulty": difficulty,
        "enemy_spawning": enemy_spawning,
        "player": player,
        "room_counter": room_counter,
    }
    death = main_loop(game_variables)
    if death == True:
        os.system("cls" if os.name == "nt" else "clear")
        print(text.castle)
        text.death("GAME OVER")
    sys.exit()


if __name__ == "__main__":
    main()
