def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    numbers = ""
    if not 2 <= len(s) <= 6:
        return False
    if not s[:2].isalpha():
        return False
    for i, c in enumerate(s):
        if c in (",. "):
            return False
        elif c.isdigit():
            numbers += c
            if not s[i:].isdecimal():
                return False
    if numbers.startswith("0"):
        return False
    return True


if __name__ == "__main__":
    main()
