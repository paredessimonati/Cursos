import inflect


# inflecting name list
def main():
    names = get()
    p = inflect.engine()
    print(f"Adieu, adieu, to {p.join(names)}")


# getting name list
def get():
    names = []
    try:
        while True:
            names.append((input("Name: ")).capitalize())
    except EOFError:
        print("")
        return names


main()
