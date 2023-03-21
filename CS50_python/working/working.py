import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        v1, v2, v3 = s.split(":")
    except ValueError:
        try:
            v1, v2 = s.split("to")
        except ValueError:
            sys.exit("Value Error", end="")
    try:
        hour = int(v1)
    except ValueError:
        try:
            hour = int(v1[0])
        except ValueError:
            sys.exit("Value Error:")

    # checking for mateches
    if matches := re.search(
        r"(\d{1,2}):?(\d{1,2})? (AM|PM) to (\d{1,2}):?(\d{1,2})? (AM|PM)",
        s,
        re.IGNORECASE,
    ):
        # passing matches to variables to help out with the mess ahead
        hour1, hour2 = int(matches.group(1)), int(matches.group(4))
        try:
            minute1, minute2 = int(matches.group(2)), int(matches.group(5))
        except:
            minute1, minute2 = 0, 0
        med1, med2 = matches.group(3), matches.group(6)

        # honestly this is a mess, maybe i didnt drink enough coffee this morning
        for hours in [hour1, hour2]:
            if not 0 <= hours <= 12:
                raise ValueError
        if hour1 == 12 and med1 == "AM":
            hour1 = 0
        elif hour1 == 12 and med2 == "PM":
            pass
        elif med1 == "PM":
            hour1 += 12
        if hour2 == 12 and med2 == "AM":
            hour2 = 0
        elif hour2 == 12 and med2 == "PM":
            pass
        elif med2 == "PM":
            hour2 += 12
        for minutes in [minute1, minute2]:
            if not 0 <= minutes <= 59:
                raise ValueError
        return f"{hour1:02d}:{minute1:02d} to {hour2:02d}:{minute2:02d}"

    raise ValueError


if __name__ == "__main__":
    main()
