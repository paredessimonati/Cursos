def main():
    fuel = convert(input("x/y: "))
    tank = gauge(fuel)
    print(tank)


def convert(string_to_ints):
    while True:
        try:
            x, y = string_to_ints.split("/")
            return round((int(x) / int(y)) * 100)
        except ValueError:
            raise
        except ZeroDivisionError:
            raise


def gauge(x):
    if x >= 99:
        return "F"
    elif x <= 1:
        return "E"
    else:
        return f"{x}%"


if __name__ == "__main__":
    main()
