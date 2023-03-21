def main():
    text = (input("Hello sir ")).lower().strip()
    print(value(text))


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello") == True:
        return 0
    elif greeting.startswith("h") == True:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
