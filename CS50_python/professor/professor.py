import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        counter = 0
        while True:
            print(f"{x} + {y} = ", end="")
            if counter == 3:
                print(result)
                break
            try:
                if int(input("")) == result:
                    score += 1
                    break
                else:
                    counter += 1
                    print("EEE")
                    continue
            except ValueError:
                print("EEE")
                counter += 1
                continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 3 or level < 1:
                continue
            return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
    else:
        number = random.randint(10 ** (level - 1), 10**level - 1)
    return number


if __name__ == "__main__":
    main()
