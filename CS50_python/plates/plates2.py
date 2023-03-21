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

# --------------version 2 -------------


def is_valid(s):
    numbers = ""
    if not 2 <= len(s) <= 6:
        return 0
    for i, c in enumerate(s):
        if c in (",. "):
            return 0
        elif c.isdigit():
            numbers += c
            if not s[i:].isdecimal():
                return 0
    if numbers.startswith("0"):
        return 0
    elif s.isalnum() and s[-1].isalpha():
        return 0
    return 1


# --------------version 1 -------------

def is_valid(s):
    for c in s:
        if c in (",. "):
            return 0
    if 2 <= len(s) <= 6:
        if s.isalpha():
            return 1
        if s.isalnum():
            numbers = ""
            for i, c in enumerate(s):
                if c.isdigit():
                    numbers += c
                if not s[i:].isdecimal():
                    return 0
            if numbers.startswith("0"):
                return 0
            if s[-1].isalpha():
                return 0
        return 1
    return 0
