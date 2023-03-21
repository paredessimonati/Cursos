import sys
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    """since tabulate works with "list of lists or another iterable of iterables"
    as per the documentation, im separating the values of the CSV line by line
    and then appending them to a list"""
    list = []
    # string = ""
    for line in lines:
        # string = (line.strip().split(","))
        # list.append(string)
        """and then i figured i could make it all in one line, decided to leave
        the old lines commented out because its easier to understand if i need
        to look back at this solution again"""
        list.append(line.strip().split(","))

    print(tabulate(list, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
