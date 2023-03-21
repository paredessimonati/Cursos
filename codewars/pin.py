def get_numbers(x):
    digits = {
        0: ['0', '8'],
        1: ['1', '2', '4'],
        2: ['1', '2', '3', '5'],
        3: ['2', '3', '6'],
        4: ['1', '4', '5', '7'],
        5: ['2', '4', '5', '6', '8'],
        6: ['3', '5', '6', '9'],
        7: ['4', '7', '8'],
        8: ['5', '7', '8', '9', '0'],
        9: ['6', '8', '9'],
    }

    return digits[x]


def get_pins_helper(observed, current_pin, valid_pins):
    if not observed:
        valid_pins.append(current_pin)
        return

    digit = observed[0]
    for replacement in get_numbers(int(digit)):
        next_pin = current_pin + replacement
        get_pins_helper(observed[1:], next_pin, valid_pins)


def get_pins(observed):
    valid_pins = []
    get_pins_helper(observed, '', valid_pins)
    return valid_pins


print(get_pins("86592821"))