def main():
    cash = int(input("Insert Coin: "))
    while True:
        if cash in (25, 10, 5):
            break
        print(f"Invalid Coin: {cash}")
        cash = int(input("Insert Coin: "))

    while cash < 50:
        due = int(input(f"Amount Due: {50 - cash} \nInsert Coin: "))
        while True:
            if due in (25, 10, 5):
                break
            print(f"Invalid Coin: {due}")
            due = int(input("Insert Coin: "))
        cash += due

    if cash > 50:
        print(f"Change Owed: {cash - 50}")
    elif cash == 50:
        print("Change Owed: 0")

if __name__ == "__main__":
    main()
