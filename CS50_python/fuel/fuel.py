def main():
    fuel = get("percentage")

    # if x > y, goes back to the get funct
    if fuel > 100:
        get("percentage")
    # edge cases, literally
    elif fuel >= 99:
        print("F")
    elif fuel <= 1:
        print("E")
    else:
        print(f"{fuel}%")


def get(x):

    # doing a while loop
    while True:
        try:
            # tried to get all in one line but couldnt figure out how
            x, y = input("enter x/y ").split("/")
            return round((int(x) / int(y)) * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()