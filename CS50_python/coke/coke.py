def main():
    cash = int(input("Insert Coin: "))
    cash = check(cash)
    while cash < 50:
        print(f"Amount Due: {50 - cash}")
        due = int(input("Insert Coin: "))
        due = check(due)
        cash += due
    if cash > 50:
        print(f"Change Owed: {cash - 50}")
    elif cash == 50:
        print("Change Owed: 0")


def check(coins):
    if coins == 25 or coins == 10 or coins == 5:
        return(coins)
    else:
        return 0


if __name__ == "__main__":
    main()