import random
import sys


# gets results from the other functions and prints
def main():
    level = get_level()
    target = get_random(level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < target:
                print("Too small!")
                continue
            if guess > target:
                print("Too large!")
                continue
            else:
                sys.exit("Just right!")
        except ValueError:
            pass


# gets initial input and catches errors
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
            return level
        except ValueError:
            pass


# gets the most important job done, if input is 1 doesnt
# call the random function and instead just sends the 1 back
def get_random(level):
    if level == 1:
        return 1
    random_number = random.randint(1, level)
    return random_number


main()
