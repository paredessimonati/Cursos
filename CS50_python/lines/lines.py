import sys


def main():
    count = 0
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-2:] != "py":
        sys.exit("Not a Python file")
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    for line in lines:
        # line = line.strip()
        if line.isspace():
            continue
        if line.strip().startswith("#"):
            continue
        count += 1
    print(count)


if __name__ == "__main__":
    main()
