import sys

import attr
import os
import random
import text
from enemy import Enemy
from room import Room


def main_loop(var) -> bool:
    """
    Main loop of the game

    Gets passed a dictionary of variables from main().
    At the end room_counter increases by one.
    """
    # unpacking variables
    difficulty, enemy_spawning, player, room_counter = var.values()

    # Starting main loop
    while player.hp > 0:
        # Create a room

        room = Room()
        room.new_room()
        seed = room.seed

        # Room enemy
        # Even though an enemy instance is created for every room
        # i dont want an enemy in every single one, 90% of the time i do.
        enemy = Enemy(room.current_room)
        enemy_name = enemy.name
        enemy.is_visible(seed, enemy_spawning)
        enemy_spawn = enemy.visible

        ...

        # Room description
        room_description = room.describe_room(room_counter, enemy_spawn)
        command(player, room_description, custom_menu=text.fight_menu)
        input()
        # Describe enemy if visible
        os.system("cls" if os.name == "nt" else "clear")
        enemy_description = ""
        if enemy.visible:
            enemy_description = enemy.description(seed, difficulty, room)

            # If enemy is aggro, automatic fight
            if enemy.aggro:
                enemy_description += text.bold(attr.enemies[enemy_name]["attacks"])
                command(player, enemy_description, custom_menu=text.fight_menu)
                # text.format(enemy_description, "double")
                # text.super_line()
                input()
                os.system("cls" if os.name == "nt" else "clear")
                room_description = fight_loop(
                    player, enemy, difficulty, room_description
                )

            # If not aggro, description of enemy with no_attack variable.
            else:
                enemy_description += attr.enemies[enemy_name]["no_attack"]
                command(player, enemy_description, custom_menu=text.fight_menu)
                # text.format(enemy_description, "double")
                # text.super_line()
                input()
                os.system("cls" if os.name == "nt" else "clear")
        else:
            room_description += room.current_room["no_enemy"]

        # Room investigation
        # Set flags for room search 1 or 0, might remove later
        search_flag = 0
        if player._hp <= 0:
            return True
        # Temp description so it doesnt overwrite the others while it loops
        # through the while loop.
        buffer = room_description
        while True:
            # Checking for commands imputs

            command(player, buffer)
            action = input("Type command: ")
            if action in ("room", "r"):
                buffer = room_description
                continue
                # command(player, room_description)
            # Searches the room
            if action in ("search", "s"):
                search_description = room.room_search()
                buffer = search_description
                # command(player, search_description)
                search_flag = 1
                continue

            # If search flag is 0, player gets prompted to search instead.
            if action in ("open", "o"):
                if search_first(search_flag, player):
                    continue

                loot = room.room_loot()
                loot_item = attr.loot[room.current_room["loot"]]["description"]
                if loot == "":
                    string = "You didnt find anything, try the next room."
                    buffer = string
                    continue
                while True:
                    try:
                        string = f"Do you want to open the {loot[0]}?"
                        loot_choice = command(player, string, text.yes_no)
                        loot_choice = input("Type command: ")
                        buffer = room_description
                        if loot_choice == "y":
                            string = f"You receive {loot_item}"
                            command(player, string, custom_menu=text.fight_menu)
                            input()
                            room.seed = room.seed[:2] + "00" + room.seed[4:]
                            break

                            # item_buff = ...
                            """Might add buffs from items later"""

                        elif loot_choice in ("no", "n"):
                            string = "Better safe than sorry."
                            command(player, string, custom_menu=text.fight_menu)
                            input()
                            break
                        else:
                            raise ValueError("Invalid Input")
                    except ValueError:
                        search_flag += 1
                        if search_flag == 3:
                            you_better_collaborate(player, 2)
                        if search_flag == 4:
                            you_better_collaborate(player, 3)
                        if search_flag == 5:
                            you_better_collaborate(player, 4)
                            return True
                        if search_flag == 15:
                            sys.exit("come on....")

            if action in ("drink", "d"):
                if search_first(search_flag, player):
                    continue

                potion = room.room_potion()

                # potion_item = ...
                """Emtpy for now, might add different potions later"""

                if potion == "":
                    string = "You didnt find any potions, try the next room."
                    buffer = string
                    continue
                while True:
                    try:
                        string = "Do you want to drink the potion?"
                        loot_choice = command(player, string, text.yes_no)
                        loot_choice = input("Type command: ")
                        buffer = room_description
                        if loot_choice in ("y", "yes"):
                            player.damage_received(-100)
                            string = "You receive a sudden rush of energy."
                            command(player, string, custom_menu=text.fight_menu)
                            input()
                            room.seed = room.seed[:4] + "00" + room.seed[6:]
                            # if implemented, different potions could be good or bad
                            break

                        elif loot_choice in ("n", "no"):
                            string = "Better safe than sorry."
                            command(player, string, custom_menu=text.fight_menu)
                            input()
                            break
                        else:
                            raise ValueError("Invalid Input")
                    except ValueError:
                        search_flag += 1
                        if search_flag == 3:
                            you_better_collaborate(player, 2)
                        if search_flag == 4:
                            you_better_collaborate(player, 3)
                        if search_flag == 5:
                            you_better_collaborate(player, 4)
                            return True
                        if search_flag == 15:
                            sys.exit("come on....")

            if action in ("attack", "a"):
                if enemy.visible and enemy.alive:
                    string = f"Are you sure you want to attack a {enemy_name}?"
                    command(player, string, text.yes_no)
                    attack_choice = input("Type command: ")
                    if attack_choice in ("yes" or "y"):
                        room_description = fight_loop(
                            player, enemy, difficulty, room_description
                        )
                    else:
                        continue
                else:
                    string = "There's no one worth attacking."
                    command(player, string, custom_menu=text.fight_menu)
                    input()
            if action in ("exit", "e"):
                if search_first(search_flag, player):
                    continue
                exits = room.current_room["exits"]
                while True:
                    try:
                        command(player, exits, custom_function=text.print_exit)
                        choice = input("Which door number do you choose? ")
                        if choice == "1" or choice == "2" or choice == "3":
                            break
                        else:
                            raise ValueError("Invalid Input")
                    except ValueError:
                        search_flag += 1
                        if search_flag == 3:
                            you_better_collaborate(player, 2)
                        if search_flag == 4:
                            you_better_collaborate(player, 3)
                        if search_flag == 5:
                            you_better_collaborate(player, 4)
                            return True
                        if search_flag == 15:
                            sys.exit("come on....")

                break
        os.system("cls" if os.name == "nt" else "clear")
        room_counter += 1
        continue


def command(
    player, middle_text="", custom_function=text.format, custom_menu=text.menu
) -> str:
    """
    Prints a screen of sorts with the health at the top of the terminal,
    text in the middle and commands at the bottom
    """
    os.system("cls" if os.name == "nt" else "clear")
    text.super_line(player.hp)
    print()
    custom_function(middle_text)
    return print(custom_menu())


def fight_loop(player, enemy, difficulty, room_description):
    """
    Fighting loop

    Gets passed the player info, enemy info and the difficulty modifier.

    The difficulty adds a fixed damage value to the attack roll from the enemy.
    Nothing fancy.

    """

    # Combat loop
    while player.hp > 0 and enemy.hp > 0:
        # Player attacks enemy
        player_attack = player.attack + random.randrange(-5, 5)
        enemy_attack = enemy.attack + random.randrange(-5, 5) + (difficulty * 2)

        # Random number gives chance to miss player attack.
        if round(random.random(), 2) < 0.15:
            print(f"You missed the {enemy.name}!")
        else:
            print(
                f"You attack the {enemy.name} for {text.green(player_attack)} damage!"
            )
            enemy._hp -= player_attack

        # Check if enemy is still alive
        if enemy._hp <= 0:
            command(
                player,
                f'{text.bold(attr.enemies[enemy.name]["defeat"])}',
                custom_menu=text.fight_menu,
            )
            input()

            room_description += attr.enemies[enemy.name]["after"]

            os.system("cls" if os.name == "nt" else "clear")
            enemy.alive = False
            return room_description

        # Enemy attacks player
        # Random number gives chance to miss enemy attack.
        if round(random.random(), 2) < 0.2:
            print(f"The {enemy.name} misses you!\n")
        else:
            print(
                f"The {enemy.name} attacks you for {text.red(enemy_attack)} damage!\n"
            )
            player._hp -= enemy_attack

        # Check if player is still alive
        if player._hp <= 0:
            continue

        input("Press Enter to Continue")
        print("\033[999D\033[1A", end="")


def search_first(search_flag, player) -> bool:
    """Tells the player to search first"""
    if search_flag == 0:
        string = "You haven't searched yet, look around first!"
        command(player, string, custom_menu=text.fight_menu)
        input()
        return True
    return False


def you_better_collaborate(player, n):
    if n == 2:
        string = "You hear something."
        command(player, string, custom_menu=text.fight_menu)
        input()
    if n == 3:
        string = "You hear something again.\n\nWhatever it is, is getting closer!"
        command(player, string, custom_menu=text.fight_menu)
        input()
    if n == 4:
        os.system("cls" if os.name == "nt" else "clear")
        for i in range(4):
            print(f"The Shadow attacks you for {text.red(999)} damage!")
            print("The Shadow evades your attack!\n")
            input("Press Enter to Continue\n")
