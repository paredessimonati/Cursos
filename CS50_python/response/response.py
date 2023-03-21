from validator_collection import validators, errors


def main():
    print(validation(input("Text: ")))


def validation(s):
    try:
        email_address = validators.email(s)
        return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
