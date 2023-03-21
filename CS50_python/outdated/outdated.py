months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        date = input("Date: ").strip().lower().title()

        # Im looking for a comma here, is not elegant but works
        # for this specific problem
        if date[-6] == ",":
            month, day, year = date.split()
            month = months.index(month) + 1
            day = day.removesuffix(",")
        else:
            month, day, year = date.split("/")

        # if days or months are outside of parameters, start loop again
        if int(day) > 31 or int(month) > 12:
            continue
        day = int(day)
        month = int(month)
        print(f"{year}-{month:02}-{day:02}")
        break

    # exceptions...
    except ZeroDivisionError:
        print("I dont know how we got here honestly...")
        break
    except ValueError:
        pass
    except EOFError:
        print("(ノಠ益ಠ)ノ彡┻━┻")
        break
    except IndexError:
        pass
