from datetime import date
import inflect
import sys


def main():
    # prompt user for date of birth YYYY-MM-DD
    date_of_birth = input("Date of birth: ").strip()
    # get minutes
    minute = minutes(date_of_birth)
    # get "song"
    song = convert(minute)
    # print how old they are in minutes, rounded, in words without ands
    print((f"{song} minutes").capitalize())


def minutes(s):
    try:
        year, month, day = s.split("-")
    except ValueError:
        sys.exit("Incorrect date format")
    date_of_birth = date(int(year), int(month), int(day))
    date_today = date.today()
    date_delta = date_today - date_of_birth
    return int(date_delta.total_seconds() / 60)


def convert(s):
    p = inflect.engine()
    return p.number_to_words(str(s), andword="")


if __name__ == "__main__":
    main()
