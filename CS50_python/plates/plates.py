def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # starting a string to keep track of digits
    numbers = ""

    # checking length of the plate
    if not 2 <= len(s) <= 6:
        return 0

    # looping through characters
    for i, c in enumerate(s):
        if c in (",. "):
            return 0

        # if character is digit, add digit to "numbers"
        elif c.isdigit():
            numbers += c

            # slicing the string to check if there are letters after any number
            if not s[i:].isdecimal():
                return 0

    # checking if the first number is a 0
    if numbers.startswith("0"):
        return 0

    # hoping i didnt miss any checks, returns plate as valid
    return 1


if __name__ == "__main__":
    main()
