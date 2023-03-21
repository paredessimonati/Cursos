def main():
    d = get("items")

    # iterating in the dictionary printing the number of items d[i]
    # and the items i
    for i in sorted(d):
        print(d[i], i)


def get(everything):
    #dictionary
    d = {}

    #trying another way
    try:
        while True:
            item = input("").upper()
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
    except EOFError:
        print("")
        return d


main()
