import re
import textwrap
import time
import sys


# i went to the internet and found THIS:
class color:
    reset = "\033[0m"
    bold = "\033[01m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    orange = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[36m"
    lightgrey = "\033[37m"
    darkgrey = "\033[90m"
    lightred = "\033[91m"
    lightgreen = "\033[92m"
    yellow = "\033[93m"
    lightblue = "\033[94m"
    pink = "\033[95m"
    lightcyan = "\033[96m"


# controls time delay in seconds, 0 is fastest
TEXTSPEED = 0.06


# Lines to make things clearer
line = "-" * 80

enter = "-" * 28 + "Press Enter to Continue" + "-" * 29


# this i did myself though
def format(text, jump="no_jump"):
    linebreak = ""
    if jump == "jump":
        linebreak = "\n"
    if jump == "double":
        linebreak = "\n\n"
    split_text = re.split("(?<=\.\s)", text)
    # print("\n" * (6 - len(split_text)))
    for string in split_text:
        time.sleep(TEXTSPEED)
        if len(string) > 80:
            print(f"{textwrap.fill(string, 60)}{linebreak}")
        else:
            print(f"{(string)}{linebreak}")
    print("\033[99B")
    print("\033[3A")


def print_exit(text):
    for number, letter in enumerate(text, 1):
        time.sleep(TEXTSPEED)
        print(number, letter)


def menu() -> str:
    """Prints the command menu at the bottom of the terminal"""
    menu = "\033[99B\033[4AWhat would you like to do?\nCommands: Room, Search, Attack, Open, Drink, Exit"
    return menu


def fight_menu() -> str:
    """Prints the simple fight menu at the bottom of the terminal"""
    menu = f"\033[99B\033[4A\n\n{enter}"
    return menu


def yes_no(text=""):
    print(text)
    print(f"\n{color.green}", end="")
    print("Yes", color.red, "No", color.reset)


def red(string) -> str:
    """Returns red string"""
    string = color.red + str(string) + color.reset
    return string


def green(string) -> str:
    """Returns green string"""
    string = color.green + str(string) + color.reset
    return string


def bold(string) -> str:
    """Returns bold string"""
    string = color.bold + str(string) + color.reset
    return string


# if no parameter is sent, it will default to that message
def super_line(text="Press Enter to Continue"):
    print()
    print(line)

    # If the passed variable isnt text it should be the health, so:
    if isinstance(text, int):
        text = f"Health = {str(text)}"

    if len(text) % 2 == 1:
        dashes = int((77 - len(text)) / 2)
        print(("-" * (dashes + 1)), text, "-" * dashes)
    else:
        dashes = int((78 - len(text)) / 2)
        print("-" * dashes, text, "-" * dashes)
    print(line)


# Art (https://www.asciiart.eu/)
castle = """                                                |>>>
                                                |
                                            _  _|_   _
                                           |;|_|;|__|;|
                                           \ \.    .  /
                                            \ \:  .  /
                                             | |:   |
                                             | |:.  |
                                             | |:  .|
                                             | |:   |       \,/
                                             | |: , |            /`\ 
                                             | |:   |
                                             | |: . |
              __                            _| |_   |
     ____--`~    '--~~__            __ ----~    ~`---,              ___
-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~

"""


# with a little help from stack overflow...
# ANSI codes from (https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)


def title(letters):
    print("\033[K", end="")
    print("\033[12F", end="")
    print(f'{" " * 25}', end="")
    for letter in letters:
        print(letter, end="", flush=True)
        time.sleep(TEXTSPEED)
    print("\033[26C", end="")
    print("\033[3B", end="")
    for letter in "caaak":
        print(letter, end="", flush=True)
        time.sleep(TEXTSPEED / 2)
    print("")
    print("\033[12B", end="")
    print("\033[K", end="")


def death(letters):
    print("\033[K", end="")
    print("\033[12F", end="")
    print(f'{" " * 25}', end="")
    for letter in letters:
        print(letter, end="", flush=True)
        time.sleep(TEXTSPEED)
    print("\033[33C", end="")
    print("\033[3B", end="")
    for letter in "lol...":
        print(letter, end="", flush=True)
        time.sleep(TEXTSPEED / 2)
    print("")
    print("\033[12B", end="")
    print("\033[K", end="")
