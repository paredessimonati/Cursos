def main():
    hour = input("What time is it? ")

    # calling convert function
    hour = convert(hour)

    # checking if variable fits ranges
    if 7 <= hour <= 8:
        print("breakfast time")
    if 12 <= hour <= 13:
        print("lunch time")
    if 18 <= hour <= 19:
        print("dinner time")

def convert(time):

    # checking if time is am
    if time.endswith("a.m.") == True:
        time = time.removesuffix(" a.m.")
        hours, minutes = time.split(":")

    # checking if time is pm, adding 12 to hours
    elif time.endswith("p.m.") == True:
        time = time.removesuffix( " p.m.")
        hours, minutes = time.split(":")
        hours = int(hours) + 12
    else:
        hours, minutes = time.split(":")

    # finish function
    minutes = int(minutes) / 60
    hours = int(hours)
    time = float(hours + minutes)
    return time


if __name__ == "__main__":
    main()