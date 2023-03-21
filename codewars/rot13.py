def rot13(message):
    code = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                case = 65
            else:
                case = 97
            code += chr(case + ((ord(letter) - case + 13) % 26))
        else:
            code += letter
    return code










alala = "aA bB zZ 1234 *!?%"


print(rot13(alala))