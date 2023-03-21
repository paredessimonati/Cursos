def main():
    food = get("order")


def get(items):
    order = 0
    #dictionary
    d = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # doing a while loop
    while True:
        try:

            #trying again to make as few lines as possible in try 
            order += d[(input("Item: ")).lower().title()]
            print(f"${order:.2f}")
        except KeyError:
            pass
        except EOFError:
            print("")
            return order


main()


